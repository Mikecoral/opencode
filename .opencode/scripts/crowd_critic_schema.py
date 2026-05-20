from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any


BREVITY_PATTERN = ("not shown for brevity", "omitted for brevity", "remaining profiles")


@dataclass(frozen=True)
class ValidationCheck:
    name: str
    passed: bool
    detail: str


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def average(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def validation_report(
    *,
    sample_size: int,
    profiles: list[dict[str, Any]],
    assets: list[Path],
    observations: list[dict[str, Any]],
    simulations: list[dict[str, Any]],
) -> dict[str, Any]:
    serialized = json.dumps(
        {
            "profiles": profiles,
            "observations": observations,
            "simulations": simulations,
        },
        ensure_ascii=False,
    ).lower()
    checks = [
        ValidationCheck("profiles_count", len(profiles) == sample_size, f"{len(profiles)}/{sample_size}"),
        ValidationCheck(
            "visual_observation_count",
            len(observations) == len(profiles) * len(assets),
            f"{len(observations)}/{len(profiles) * len(assets)}",
        ),
        ValidationCheck("raw_simulation_count", len(simulations) == len(profiles), f"{len(simulations)}/{len(profiles)}"),
        ValidationCheck(
            "no_brevity_placeholders",
            not any(pattern in serialized for pattern in BREVITY_PATTERN),
            "forbidden abbreviation scan",
        ),
    ]
    return {
        "status": "pass" if all(check.passed for check in checks) else "fail",
        "checks": [{"name": check.name, "pass": check.passed, "detail": check.detail} for check in checks],
    }


def aggregate_simulations(simulations: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "sentiment": dict(Counter(str(item.get("sentiment", "unknown")) for item in simulations)),
        "stance": dict(Counter(str(item.get("stance", "unknown")) for item in simulations)),
        "average_comprehension": round(average([float(item.get("comprehension", 0)) for item in simulations]), 2),
        "average_trust": round(average([float(item.get("trust", 0)) for item in simulations]), 2),
        "average_action_readiness": round(average([float(item.get("action_readiness", 0)) for item in simulations]), 2),
    }


def analysis_markdown(simulations: list[dict[str, Any]], assets: list[Path]) -> str:
    aggregate = aggregate_simulations(simulations)
    lines = [
        "# Crowd Simulation Analysis",
        "",
        "## Setup",
        f"- Profiles: {len(simulations)}",
        "- Assets: " + ", ".join(f"`{asset.name}`" for asset in assets),
        "",
        "## Aggregate Signals",
        f"- Sentiment distribution: {aggregate['sentiment']}",
        f"- Stance distribution: {aggregate['stance']}",
        f"- Average comprehension: {aggregate['average_comprehension']}/10",
        f"- Average trust: {aggregate['average_trust']}/10",
        f"- Average action readiness: {aggregate['average_action_readiness']}/10",
        "",
        "## Profile Comments",
    ]
    for item in simulations:
        segment = item.get("segment", {})
        lines.extend(
            [
                "",
                f"### {item.get('person_id')} - {segment.get('country')}, {segment.get('sex')}, {segment.get('age_band')}",
                f"- Sentiment: {item.get('sentiment')}; stance: {item.get('stance')}; signal: {item.get('designer_signal')}",
                f"- Comment: {item.get('simulated_comment')}",
                f"- Main objection: {item.get('main_objection')}",
                f"- Requested change: {item.get('requested_change')}",
            ]
        )
    return "\n".join(lines) + "\n"
