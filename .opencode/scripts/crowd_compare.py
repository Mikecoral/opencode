#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from crowd_critic_schema import aggregate_simulations, read_jsonl


def delta(after: float, before: float) -> str:
    change = after - before
    sign = "+" if change >= 0 else ""
    return f"{sign}{change:.2f}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--before-dir", required=True)
    parser.add_argument("--after-dir", required=True)
    parser.add_argument("--output", default=None)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    before_dir = Path(args.before_dir).resolve()
    after_dir = Path(args.after_dir).resolve()
    output = Path(args.output).resolve() if args.output else after_dir / "crowd-before-after.md"
    before = aggregate_simulations(read_jsonl(before_dir / "crowd-critic-raw.jsonl"))
    after = aggregate_simulations(read_jsonl(after_dir / "crowd-critic-raw.jsonl"))
    lines = [
        "# Crowd Simulation Before/After",
        "",
        "## Compared Directories",
        f"- Before: `{before_dir}`",
        f"- After: `{after_dir}`",
        "",
        "## Metric Movement",
        "| Metric | Before | After | Change |",
        "|--------|--------|-------|--------|",
        f"| Average comprehension | {before['average_comprehension']} | {after['average_comprehension']} | {delta(after['average_comprehension'], before['average_comprehension'])} |",
        f"| Average trust | {before['average_trust']} | {after['average_trust']} | {delta(after['average_trust'], before['average_trust'])} |",
        f"| Average action readiness | {before['average_action_readiness']} | {after['average_action_readiness']} | {delta(after['average_action_readiness'], before['average_action_readiness'])} |",
        f"| Sentiment distribution | {before['sentiment']} | {after['sentiment']} | n/a |",
        f"| Stance distribution | {before['stance']} | {after['stance']} | n/a |",
        "",
        "## Interpretation Notes",
        "- Review `crowd-critic-summary.md` in both directories for repeated issues resolved or remaining.",
        "- Use this file as the quantitative anchor; add image-level visible-change notes after inspecting regenerated assets.",
        "",
    ]
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
