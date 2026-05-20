from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any, Callable, Iterable


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


def safe_float(value: Any) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def average_scores(simulations: Iterable[dict[str, Any]]) -> dict[str, float]:
    sims = list(simulations)
    keys = ("hierarchy", "type", "contrast", "rhythm", "space")
    result: dict[str, float] = {}
    for key in keys:
        values: list[float] = []
        for sim in sims:
            scores = sim.get("scores")
            if isinstance(scores, dict):
                num = safe_float(scores.get(key))
                if num is not None:
                    values.append(num)
        result[key] = round(average(values), 2)
    return result


def average_field(simulations: Iterable[dict[str, Any]], field: str) -> float:
    values = [num for num in (safe_float(sim.get(field)) for sim in simulations) if num is not None]
    return round(average(values), 2)


def format_distribution(counter: dict[str, int]) -> str:
    items = sorted(counter.items(), key=lambda pair: (-pair[1], pair[0]))
    return ", ".join(f"{key}: {value}" for key, value in items) if items else "—"


def heatmap_table(
    simulations: list[dict[str, Any]],
    *,
    label: str,
    bucket_key: Callable[[dict[str, Any]], str],
    allowed_keys: list[str] | None = None,
) -> str:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for sim in simulations:
        key = bucket_key(sim)
        if allowed_keys is not None and key not in allowed_keys:
            continue
        grouped[key].append(sim)
    ordered = allowed_keys if allowed_keys is not None else sorted(grouped.keys())
    header = f"| {label} | N | Hier | Type | Contr | Rhythm | Space | Compr | Trust | Action |"
    sep = "|---|---|---|---|---|---|---|---|---|---|"
    lines = [header, sep]
    for key in ordered:
        bucket = grouped.get(key, [])
        if not bucket:
            continue
        scores = average_scores(bucket)
        compr = average_field(bucket, "comprehension")
        trust = average_field(bucket, "trust")
        action = average_field(bucket, "action_readiness")
        lines.append(
            f"| {key} | {len(bucket)} | {scores['hierarchy']:.1f} | {scores['type']:.1f} | "
            f"{scores['contrast']:.1f} | {scores['rhythm']:.1f} | {scores['space']:.1f} | "
            f"{compr:.1f} | {trust:.1f} | {action:.1f} |"
        )
    return "\n".join(lines)


def structured_markdown(
    simulations: list[dict[str, Any]],
    observations: list[dict[str, Any]],
    assets: list[Path],
    manifest: dict[str, Any],
    *,
    max_comments_per_bucket: int = 5,
    top_n_freeform: int = 12,
) -> str:
    lines: list[str] = ["# Crowd Critic Structured Data", ""]
    lines.append(
        "Generated deterministically by `crowd_critic_runner.py`. All tables and counts come "
        "directly from `crowd-critic-raw.jsonl` and `crowd-visual-analysis.jsonl`. The aggregation "
        "logic lives in `crowd_critic_schema.structured_markdown`."
    )
    lines.append("")

    # Setup
    lines.append("## Setup")
    lines.append(f"- Sample size: {manifest.get('sample_size')}")
    lines.append(f"- SocioBench domain: `{manifest.get('domain')}`")
    lines.append(f"- Domain selector: `{manifest.get('domain_selector')}`")
    lines.append(f"- Sampling strategy: `{manifest.get('sampling_strategy')}`")
    lines.append(f"- Profiles completed: {len(simulations)}")
    lines.append(f"- Observations recorded: {len(observations)}")
    lines.append(f"- Visual inputs reviewed ({len(assets)}): {', '.join(f'`{asset.name}`' for asset in assets)}")
    lines.append("")
    lines.append("> Limitation: simulated audience critique from demographic profiles, not real user testing.")
    lines.append("")

    # Aggregate signals
    agg = aggregate_simulations(simulations)
    avg_craft = average_scores(simulations)
    designer_signal = dict(Counter(str(sim.get("designer_signal", "unknown")) for sim in simulations))
    lines.append("## Aggregate Signals")
    lines.append("| Signal | Result |")
    lines.append("|--------|--------|")
    lines.append(f"| Sentiment distribution | {format_distribution(agg['sentiment'])} |")
    lines.append(f"| Stance distribution | {format_distribution(agg['stance'])} |")
    lines.append(f"| Designer signal | {format_distribution(designer_signal)} |")
    lines.append(f"| Avg comprehension | {agg['average_comprehension']:.2f}/10 |")
    lines.append(f"| Avg trust | {agg['average_trust']:.2f}/10 |")
    lines.append(f"| Avg action readiness | {agg['average_action_readiness']:.2f}/10 |")
    lines.append(f"| Avg hierarchy | {avg_craft['hierarchy']:.2f}/10 |")
    lines.append(f"| Avg type | {avg_craft['type']:.2f}/10 |")
    lines.append(f"| Avg contrast | {avg_craft['contrast']:.2f}/10 |")
    lines.append(f"| Avg rhythm | {avg_craft['rhythm']:.2f}/10 |")
    lines.append(f"| Avg space | {avg_craft['space']:.2f}/10 |")
    lines.append("")

    # Heatmap by age band
    lines.append("## Score Heatmap by Age Band")
    lines.append(heatmap_table(simulations, label="Age Band", bucket_key=lambda s: str(s.get("segment", {}).get("age_band", "Unknown"))))
    lines.append("")

    # Heatmap by top countries
    country_counter = Counter(str(sim.get("segment", {}).get("country", "Unknown")) for sim in simulations)
    top_countries = [country for country, _ in country_counter.most_common(8)]
    if top_countries:
        lines.append("## Score Heatmap by Country (top 8 by sample count)")
        lines.append(
            heatmap_table(
                simulations,
                label="Country",
                bucket_key=lambda s: str(s.get("segment", {}).get("country", "Unknown")),
                allowed_keys=top_countries,
            )
        )
        lines.append("")

    # Heatmap by sex
    lines.append("## Score Heatmap by Sex")
    lines.append(heatmap_table(simulations, label="Sex", bucket_key=lambda s: str(s.get("segment", {}).get("sex", "Unknown"))))
    lines.append("")

    # Sentiment breakdown by age band
    lines.append("## Sentiment Distribution by Age Band")
    age_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for sim in simulations:
        age_groups[str(sim.get("segment", {}).get("age_band", "Unknown"))].append(sim)
    lines.append("| Age Band | N | Positive | Neutral | Negative |")
    lines.append("|---|---|---|---|---|")
    for age in sorted(age_groups):
        bucket = age_groups[age]
        counts = Counter(str(sim.get("sentiment", "unknown")) for sim in bucket)
        lines.append(
            f"| {age} | {len(bucket)} | {counts.get('positive', 0)} | "
            f"{counts.get('neutral', 0)} | {counts.get('negative', 0)} |"
        )
    lines.append("")

    # Asset mentions
    most_effective = Counter(str(sim.get("most_effective_asset", "")).strip() for sim in simulations if sim.get("most_effective_asset"))
    weakest = Counter(str(sim.get("weakest_asset", "")).strip() for sim in simulations if sim.get("weakest_asset"))
    all_asset_names = {asset.name for asset in assets} | set(most_effective) | set(weakest)
    all_asset_names.discard("")
    lines.append("## Asset Mentions (counted from simulation outputs)")
    lines.append("| Asset | Most Effective | Weakest | Net |")
    lines.append("|-------|----------------|---------|-----|")
    for name in sorted(all_asset_names, key=lambda n: -(most_effective.get(n, 0) - weakest.get(n, 0))):
        eff = most_effective.get(name, 0)
        weak = weakest.get(name, 0)
        net = eff - weak
        lines.append(f"| `{name}` | {eff} | {weak} | {net:+d} |")
    lines.append("")

    # Verbatim main objections (clustered by exact text match)
    objections = Counter(str(sim.get("main_objection", "")).strip() for sim in simulations if sim.get("main_objection"))
    lines.append(f"## Main Objections (verbatim, top {top_n_freeform} by count)")
    if objections:
        for text, count in objections.most_common(top_n_freeform):
            if text:
                lines.append(f"- ({count}×) {text}")
    else:
        lines.append("- (none)")
    lines.append("")

    # Verbatim requested changes
    changes = Counter(str(sim.get("requested_change", "")).strip() for sim in simulations if sim.get("requested_change"))
    lines.append(f"## Requested Changes (verbatim, top {top_n_freeform} by count)")
    if changes:
        for text, count in changes.most_common(top_n_freeform):
            if text:
                lines.append(f"- ({count}×) {text}")
    else:
        lines.append("- (none)")
    lines.append("")

    # Representative comments by sentiment
    by_sentiment: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for sim in simulations:
        by_sentiment[str(sim.get("sentiment", "unknown"))].append(sim)
    lines.append("## Representative Simulated Comments")
    for sentiment in ("positive", "neutral", "negative"):
        bucket = by_sentiment.get(sentiment, [])
        if not bucket:
            continue
        chosen = sorted(bucket, key=lambda s: str(s.get("person_id", "")))[:max_comments_per_bucket]
        lines.append(f"### {sentiment.title()} ({len(bucket)} total, showing {len(chosen)})")
        for sim in chosen:
            seg = sim.get("segment", {}) if isinstance(sim.get("segment"), dict) else {}
            tag = f"{seg.get('country', '?')} / {seg.get('sex', '?')} / {seg.get('age_band', '?')}"
            comment = str(sim.get("simulated_comment", "")).strip().replace("\n", " ")
            lines.append(f"- **{tag}** [`{sim.get('person_id')}`]: {comment}")
        lines.append("")

    # Designer signal × scores cross-check (helps catch contradictions)
    lines.append("## Designer Signal Cohorts")
    signal_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for sim in simulations:
        signal_groups[str(sim.get("designer_signal", "unknown"))].append(sim)
    lines.append("| Signal | N | Avg Hier | Avg Type | Avg Contr | Avg Rhythm | Avg Space | Avg Compr | Avg Trust |")
    lines.append("|---|---|---|---|---|---|---|---|---|")
    for signal in ("keep", "adjust", "rethink", "unknown"):
        bucket = signal_groups.get(signal, [])
        if not bucket:
            continue
        sc = average_scores(bucket)
        compr = average_field(bucket, "comprehension")
        trust = average_field(bucket, "trust")
        lines.append(
            f"| {signal} | {len(bucket)} | {sc['hierarchy']:.1f} | {sc['type']:.1f} | "
            f"{sc['contrast']:.1f} | {sc['rhythm']:.1f} | {sc['space']:.1f} | "
            f"{compr:.1f} | {trust:.1f} |"
        )
    lines.append("")

    return "\n".join(lines) + "\n"


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
