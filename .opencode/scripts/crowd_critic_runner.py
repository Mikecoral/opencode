#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
from collections import defaultdict
import json
import os
from pathlib import Path
import re
import sys
import urllib.error
import urllib.request

from crowd_critic_schema import analysis_markdown, validation_report, write_json, write_jsonl


SOCIOBENCH_ROOT = Path("/Users/hongyuecheng/python-learn/SII/AIdesign/SocioBench-main")
DATA_DIR = SOCIOBENCH_ROOT / "Dataset_all" / "A_GroundTruth_sampling500"
DEFAULT_BASE_URL = "https://api.openai.com/v1"
DEFAULT_SAMPLE_SIZE = 100
SMOKE_SAMPLE_SIZE = 24
STANDARD_MIN_SAMPLE_SIZE = 100
MAX_SAMPLE_SIZE = 200

DOMAIN_FILE = {
    "citizenship": "issp_answer_citizenship.json",
    "environment": "issp_answer_environment.json",
    "family": "issp_answer_family.json",
    "health": "issp_answer_health.json",
    "nationalidentity": "issp_answer_nationalidentity.json",
    "religion": "issp_answer_religion.json",
    "roleofgovernment": "issp_answer_roleofgovernment.json",
    "socialinequality": "issp_answer_socialinequality.json",
    "socialnetworks": "issp_answer_socialnetworks.json",
    "workorientations": "issp_answer_workorientations.json",
}

PROFILE_FIELDS = [
    "Country Prefix ISO 3166",
    "Sex of Respondent",
    "Sex of respondent",
    "Age of respondent",
    "Year of birth",
    "Highest completed education level: Categories for international comparison",
    "ISCED 2011 simplified: highest completed degree of education",
    "Education I: years of schooling",
    "Years of full-time schooling",
    "Currently, formerly, or never in paid work",
    "Hours worked weekly",
    "Main status",
    "Employment relationship",
    "Occupation ISCO/ ILO 2008",
    "Supervise anyone directly responsible",
    "Trade union membership",
    "Type of organisation, for-profit/ non-profit",
    "Type of organisation, public/ private",
    "Living in steady partnership",
    "Legal partnership status",
    "Groups of religious affiliations (derived from nat_RELIG)",
    "Comparative: groups of religious affiliations",
    "Attendance of religious services",
    "Top-Bottom self-placement",
    "Did respondent vote in last general election",
    "R: Party voted for in last general election: left-right (derived from nat_PRTY)",
    "Party respondent voted for in last general election: left-right scale",
    "How many persons in household",
    "How many adults in household",
    "How many children in household: children between [school age] and 17 years of age",
    "Place of living: urban - rural",
    "Administrative mode of data-collection",
]

FIELD_ALIASES = {
    "country": [
        "Country Prefix ISO 3166",
        "Country/ Sample Prefix ISO 3166 Code - alphanumeric",
        "Country/ Sample Prefix ISO 3166 code - alphanumeric",
        "Country Prefix ISO 3166 Code - alphanumeric",
        "Country Code",
    ],
    "sex": ["Sex of Respondent", "Sex of respondent"],
    "age": ["Age of respondent"],
    "work": ["Main status", "Currently, formerly, or never in paid work"],
}

SAMPLING_STRATEGIES = ("country_diverse", "llm_plan")
DOMAIN_SELECTORS = ("keyword", "llm")


def clean(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    text = value.strip()
    if not text or re.match(r"^(NAP|NAV|Not available|No answer)", text, re.I):
        return None
    return text


def first_value(attributes: dict[str, object], fields: list[str]) -> str | None:
    return next((value for value in (clean(attributes.get(field)) for field in fields) if value), None)


def age_band(attributes: dict[str, object]) -> str:
    try:
        age = int(first_value(attributes, FIELD_ALIASES["age"]) or "")
    except ValueError:
        return "Unknown"
    if age <= 30:
        return "18-30"
    if age <= 45:
        return "31-45"
    if age <= 60:
        return "46-60"
    if age <= 75:
        return "61-75"
    return "76+"


def stable_hash(text: str) -> int:
    value = 2166136261
    for char in text:
        value = (value * 31 + ord(char)) & 0xFFFFFFFF
    return value


def infer_domain(project_summary: str) -> str:
    text = project_summary.lower()
    if re.search(r"health|medical|hospital|care|wellness", text):
        return "health"
    if re.search(r"environment|climate|sustainability|green|energy", text):
        return "environment"
    if re.search(r"family|parent|child|gender", text):
        return "family"
    if re.search(r"government|policy|public sector|civic", text):
        return "roleofgovernment"
    if re.search(r"religion|faith|spiritual", text):
        return "religion"
    if re.search(r"national|identity|culture|country", text):
        return "nationalidentity"
    if re.search(r"inequality|class|income|fairness|equity", text):
        return "socialinequality"
    if re.search(r"network|community|social|friend|relationship", text):
        return "socialnetworks"
    if re.search(r"citizen|citizenship|rights|participation", text):
        return "citizenship"
    return "workorientations"


def project_context(output_dir: Path, project_summary: str) -> str:
    parts = [f"Project summary:\n{project_summary}"]
    for filename in ("brief.md", "design-assets.md"):
        path = output_dir / filename
        if path.exists():
            parts.append(f"{filename}:\n{path.read_text(encoding='utf-8')[:6000]}")
    return "\n\n".join(parts)


def strip_jsonc(text: str) -> str:
    output: list[str] = []
    in_string = False
    escaped = False
    index = 0
    while index < len(text):
        char = text[index]
        nxt = text[index + 1] if index + 1 < len(text) else ""
        if char == '"' and not escaped:
            in_string = not in_string
        if not in_string and char == "/" and nxt == "/":
            while index < len(text) and text[index] != "\n":
                index += 1
            output.append("\n")
            continue
        output.append(char)
        escaped = char == "\\" and not escaped
        if char != "\\":
            escaped = False
        index += 1
    return re.sub(r",\s*([}\]])", r"\1", "".join(output))


def option_string(value: object) -> str | None:
    return value.strip() if isinstance(value, str) and value.strip() else None


def read_openai_config(repo_root: Path) -> tuple[str, str, str]:
    config_path = repo_root / ".opencode" / "opencode.jsonc"
    config = json.loads(strip_jsonc(config_path.read_text(encoding="utf-8"))) if config_path.exists() else {}
    options = config.get("provider", {}).get("openai", {}).get("options", {})
    api_key = option_string(os.environ.get("OPENAI_API_KEY")) or option_string(options.get("apiKey"))
    if not api_key:
        raise RuntimeError("No OpenAI API key configured. Set OPENAI_API_KEY or provider.openai.options.apiKey.")
    base_url = option_string(os.environ.get("OPENAI_BASE_URL")) or option_string(options.get("baseURL")) or DEFAULT_BASE_URL
    model = (
        option_string(os.environ.get("OPENAI_VISION_MODEL"))
        or option_string(options.get("visionModel"))
        or option_string(options.get("modelId"))
        or "gpt-4o"
    )
    return api_key, base_url.rstrip("/"), model


def select_domain_llm(api_key: str, base_url: str, model: str, context: str) -> dict[str, object]:
    prompt = f"""Select exactly one SocioBench domain for an audience simulation.

Allowed domains:
{", ".join(DOMAIN_FILE)}

Input context:
{context}

Return only strict JSON:
{{
  "selected_domain": "one allowed domain",
  "alternatives": ["allowed domain", "allowed domain"],
  "confidence": 0.0,
  "rationale": "why this single domain is the best profile pool"
}}

Constraints:
- Pick one domain only. Do not mix domains.
- The domain is a profile pool, not a direct audience label.
- Prefer the domain whose demographic fields and survey theme best support downstream audience sampling."""
    raw_response, raw_payload = post_chat(api_key, base_url, model, prompt, max_tokens=900)
    parsed = extract_json_object(raw_response)
    selected = parsed.get("selected_domain")
    if selected not in DOMAIN_FILE:
        raise ValueError(f"LLM selected invalid domain: {selected}")
    parsed["alternatives"] = [item for item in parsed.get("alternatives", []) if item in DOMAIN_FILE]
    return {
        "selector": "llm",
        "model": model,
        "prompt": prompt,
        "raw_response": raw_response,
        "raw_payload": raw_payload,
        **parsed,
    }


def profile_from_record(record: dict[str, object]) -> dict[str, object]:
    attributes = record.get("attributes") if isinstance(record.get("attributes"), dict) else {}
    assert isinstance(attributes, dict)
    country = first_value(attributes, FIELD_ALIASES["country"])
    country = "United States" if country == "United Stated" else country
    return {
        "person_id": record.get("person_id") if isinstance(record.get("person_id"), (int, str)) else None,
        "segment": {
            "country": country or "Unknown",
            "sex": first_value(attributes, FIELD_ALIASES["sex"]) or "Unknown",
            "age_band": age_band(attributes),
            "work_status": first_value(attributes, FIELD_ALIASES["work"]) or "Unknown",
            "place": clean(attributes.get("Place of living: urban - rural")) or "Unknown",
        },
        "attributes": {field: clean(attributes.get(field)) for field in PROFILE_FIELDS if clean(attributes.get(field))},
    }


def load_domain_profiles(domain: str) -> list[dict[str, object]]:
    records = json.loads((DATA_DIR / DOMAIN_FILE[domain]).read_text(encoding="utf-8"))
    return [profile_from_record(record) for record in records]


def country_diverse_sample(profiles: list[dict[str, object]], sample_size: int, seed: str) -> list[dict[str, object]]:
    profiles = sorted(profiles, key=lambda item: stable_hash(f"{seed}:{item.get('person_id')}"))
    by_country: dict[str, list[dict[str, object]]] = defaultdict(list)
    for profile in profiles:
        by_country[str(profile["segment"]["country"])].append(profile)  # type: ignore[index]
    countries = sorted(by_country, key=lambda country: stable_hash(f"{seed}:country:{country}"))
    sampled: list[dict[str, object]] = []
    for index in range(sample_size):
        for country in countries:
            if index < len(by_country[country]):
                sampled.append(by_country[country][index])
            if len(sampled) == sample_size:
                return sampled
    return sampled


def domain_profile_summary(profiles: list[dict[str, object]]) -> dict[str, object]:
    def counts(values: list[str], limit: int = 30) -> dict[str, int]:
        counter: dict[str, int] = defaultdict(int)
        for value in values:
            if value and value != "Unknown":
                counter[value] += 1
        return dict(sorted(counter.items(), key=lambda item: (-item[1], item[0]))[:limit])

    def attr_values(pattern: str) -> dict[str, int]:
        values: list[str] = []
        for profile in profiles:
            attributes = profile.get("attributes", {})
            if not isinstance(attributes, dict):
                continue
            for field, value in attributes.items():
                if pattern.lower() in field.lower() and isinstance(value, str):
                    values.append(value)
        return counts(values)

    segments = [profile.get("segment", {}) for profile in profiles]
    return {
        "profile_count": len(profiles),
        "allowed_plan_fields": [
            "age_band",
            "sex",
            "country",
            "work_status_contains",
            "education_contains",
            "place_contains",
            "self_placement_range",
        ],
        "segment_distributions": {
            "age_band": counts([str(segment.get("age_band", "Unknown")) for segment in segments]),
            "sex": counts([str(segment.get("sex", "Unknown")) for segment in segments]),
            "country": counts([str(segment.get("country", "Unknown")) for segment in segments], limit=60),
            "work_status": counts([str(segment.get("work_status", "Unknown")) for segment in segments]),
            "place": counts([str(segment.get("place", "Unknown")) for segment in segments]),
        },
        "attribute_value_examples": {
            "education": attr_values("education") | attr_values("degree") | attr_values("schooling"),
            "self_placement": attr_values("Top-Bottom self-placement"),
        },
    }


def sampling_plan_llm(
    api_key: str,
    base_url: str,
    model: str,
    context: str,
    summary: dict[str, object],
    sample_size: int,
) -> dict[str, object]:
    prompt = f"""Create an executable sampling plan for a single SocioBench domain.

Input context:
{context}

Empirical domain profile summary:
{json.dumps(summary, ensure_ascii=False, indent=2)}

Sample size: {sample_size}

Return only strict JSON:
{{
  "strategy": "llm_plan",
  "buckets": [
    {{
      "name": "short_bucket_name",
      "weight": 0.25,
      "constraints": {{
        "age_band": ["18-30"],
        "work_status_contains": ["paid work"],
        "education_contains": ["tertiary", "university"]
      }},
      "fallback": {{"drop": ["education_contains"]}},
      "rationale": "why this bucket matters for the design audience"
    }}
  ],
  "rationale": "overall sampling rationale",
  "confidence": 0.0
}}

Rules:
- Use only allowed_plan_fields shown in the profile summary.
- Do not invent fields such as industry_partner, student, government_official, applicant, or parent.
- Bucket constraints must be executable against the profile summary values.
- Weights must sum approximately to 1.0.
- Every bucket must include a fallback.drop list, even if empty."""
    raw_response, raw_payload = post_chat(api_key, base_url, model, prompt, max_tokens=1800)
    return {
        "model": model,
        "prompt": prompt,
        "raw_response": raw_response,
        "raw_payload": raw_payload,
        "parsed": extract_json_object(raw_response),
    }


def profile_text(profile: dict[str, object], field_hint: str) -> str:
    segment = profile.get("segment", {})
    attributes = profile.get("attributes", {})
    values: list[str] = []
    if isinstance(segment, dict):
        values.extend(str(value) for value in segment.values())
    if isinstance(attributes, dict):
        values.extend(str(value) for field, value in attributes.items() if field_hint.lower() in field.lower())
    return " ".join(values).lower()


def matches_constraints(profile: dict[str, object], constraints: dict[str, object], ignored: set[str] | None = None) -> bool:
    ignored = ignored or set()
    segment = profile.get("segment", {})
    attributes = profile.get("attributes", {})
    if not isinstance(segment, dict) or not isinstance(attributes, dict):
        return False
    if "age_band" not in ignored and constraints.get("age_band") and segment.get("age_band") not in constraints["age_band"]:
        return False
    if "sex" not in ignored and constraints.get("sex") and segment.get("sex") not in constraints["sex"]:
        return False
    if "country" not in ignored and constraints.get("country") and segment.get("country") not in constraints["country"]:
        return False
    if "work_status_contains" not in ignored and constraints.get("work_status_contains"):
        text = str(segment.get("work_status", "")).lower()
        if not any(str(needle).lower() in text for needle in constraints["work_status_contains"]):
            return False
    if "place_contains" not in ignored and constraints.get("place_contains"):
        text = str(segment.get("place", "")).lower()
        if not any(str(needle).lower() in text for needle in constraints["place_contains"]):
            return False
    if "education_contains" not in ignored and constraints.get("education_contains"):
        text = profile_text(profile, "education") + " " + profile_text(profile, "degree") + " " + profile_text(profile, "schooling")
        if not any(str(needle).lower() in text for needle in constraints["education_contains"]):
            return False
    if "self_placement_range" not in ignored and constraints.get("self_placement_range"):
        value = attributes.get("Top-Bottom self-placement")
        try:
            score = int(str(value).strip())
            low, high = constraints["self_placement_range"]  # type: ignore[index]
            if score < int(low) or score > int(high):
                return False
        except (TypeError, ValueError):
            return False
    return True


def bucket_targets(buckets: list[dict[str, object]], sample_size: int) -> list[int]:
    weights = [max(0.0, float(bucket.get("weight", 0))) for bucket in buckets]
    total = sum(weights) or 1.0
    raw = [sample_size * weight / total for weight in weights]
    targets = [int(value) for value in raw]
    for index in sorted(range(len(raw)), key=lambda i: raw[i] - targets[i], reverse=True)[: sample_size - sum(targets)]:
        targets[index] += 1
    return targets


def execute_sampling_plan(
    profiles: list[dict[str, object]],
    plan: dict[str, object],
    sample_size: int,
    seed: str,
) -> tuple[list[dict[str, object]], dict[str, object]]:
    buckets = plan.get("buckets")
    if not isinstance(buckets, list) or not buckets:
        raise ValueError("sampling plan must contain non-empty buckets")
    selected: list[dict[str, object]] = []
    selected_ids: set[str] = set()
    bucket_reports: list[dict[str, object]] = []
    for bucket, target in zip(buckets, bucket_targets(buckets, sample_size)):
        if not isinstance(bucket, dict):
            continue
        constraints = bucket.get("constraints") if isinstance(bucket.get("constraints"), dict) else {}
        fallback = bucket.get("fallback") if isinstance(bucket.get("fallback"), dict) else {}
        drop = set(fallback.get("drop", [])) if isinstance(fallback.get("drop"), list) else set()
        candidates = [profile for profile in profiles if matches_constraints(profile, constraints)]  # type: ignore[arg-type]
        relaxed = False
        if len(candidates) < target and drop:
            candidates = [profile for profile in profiles if matches_constraints(profile, constraints, drop)]  # type: ignore[arg-type]
            relaxed = True
        available = [profile for profile in candidates if str(profile.get("person_id")) not in selected_ids]
        picked = country_diverse_sample(available, min(target, len(available)), f"{seed}:{bucket.get('name')}")
        selected.extend(picked)
        selected_ids.update(str(profile.get("person_id")) for profile in picked)
        bucket_reports.append(
            {
                "bucket": bucket.get("name"),
                "target": target,
                "strict_candidates": len([profile for profile in profiles if matches_constraints(profile, constraints)]),  # type: ignore[arg-type]
                "relaxed": relaxed,
                "selected": len(picked),
            }
        )
    if len(selected) < sample_size:
        remaining = [profile for profile in profiles if str(profile.get("person_id")) not in selected_ids]
        fill = country_diverse_sample(remaining, sample_size - len(selected), f"{seed}:fill")
        selected.extend(fill)
        bucket_reports.append({"bucket": "__fill__", "target": sample_size - len(selected) + len(fill), "selected": len(fill)})
    return selected[:sample_size], {
        "status": "pass" if len(selected) >= sample_size else "partial",
        "bucket_reports": bucket_reports,
        "selected_count": len(selected[:sample_size]),
    }


def resolve_asset(repo_root: Path, output_dir: Path, mention: str) -> Path:
    cleaned = mention.strip("`'\",.;:)")
    candidates = [
        Path(cleaned) if Path(cleaned).is_absolute() else repo_root / cleaned,
        repo_root / "packages" / "opencode" / cleaned,
        output_dir / cleaned,
        output_dir / Path(cleaned).name,
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()
    raise FileNotFoundError(f'Could not resolve asset mention "{mention}" from {output_dir}')


def asset_paths(repo_root: Path, output_dir: Path) -> list[Path]:
    manifest_path = output_dir / "design-assets.md"
    manifest = manifest_path.read_text(encoding="utf-8")
    mentions = list(dict.fromkeys(re.findall(r"[`|(\s]([^`|()\s]+\.png)[`|)\s]", manifest)))
    if not mentions:
        raise RuntimeError(f"No PNG assets found in {manifest_path}")
    return [resolve_asset(repo_root, output_dir, mention) for mention in mentions]


def post_chat(api_key: str, base_url: str, model: str, content: object, max_tokens: int = 1400) -> tuple[str, dict[str, object]]:
    request = urllib.request.Request(
        f"{base_url}/chat/completions",
        data=json.dumps({"model": model, "max_tokens": max_tokens, "messages": [{"role": "user", "content": content}]}).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"OpenAI-compatible API error {exc.code}: {exc.read().decode('utf-8', 'ignore')[:1000]}") from exc
    result = payload.get("choices", [{}])[0].get("message", {}).get("content")
    if not result:
        raise RuntimeError(f"OpenAI-compatible API returned no content: {json.dumps(payload)[:500]}")
    return result, payload


def analyze_image(api_key: str, base_url: str, model: str, image_path: Path, prompt: str) -> tuple[str, dict[str, object]]:
    return post_chat(
        api_key,
        base_url,
        model,
        [
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{base64.b64encode(image_path.read_bytes()).decode('ascii')}",
                    "detail": "high",
                },
            },
            {"type": "text", "text": prompt},
        ],
    )


def observation_prompt(profile: dict[str, object], project_summary: str) -> str:
    return f"""Analyze this brand design image from the perspective of this sampled audience profile.

Project summary:
{project_summary}

Profile JSON:
{json.dumps(profile, ensure_ascii=False, indent=2)}

Return concise but specific observations with:
- visible elements this profile would notice
- hierarchy, type, contrast, rhythm, and space scores on a 0-10 scale
- immediate comprehension
- trust signal
- emotional tone
- memorability
- perceived audience fit
- cultural or demographic friction
- concrete visible details that support the reaction

Do not invent preferences. Ground the critique in the visible image."""


def extract_json_object(text: str) -> dict[str, object]:
    stripped = re.sub(r"^```json\s*|\s*```$", "", text.strip())
    start = stripped.find("{")
    end = stripped.rfind("}")
    if start == -1 or end <= start:
        raise RuntimeError(f"Model did not return a JSON object: {text[:300]}")
    return json.loads(stripped[start : end + 1])


def simulate_profile(
    api_key: str,
    base_url: str,
    model: str,
    profile: dict[str, object],
    observations: list[dict[str, object]],
) -> dict[str, object]:
    content = f"""You are simulating one audience member's response to a brand design system.

Profile:
{json.dumps(profile, ensure_ascii=False, indent=2)}

Per-asset visual observations:
{chr(10).join(f"Asset: {item['asset']}{chr(10)}{item['response']}" for item in observations)}

Return only strict JSON with this shape:
{{
  "first_impression": "...",
  "simulated_comment": "casual first-person audience comment",
  "sentiment": "positive | neutral | negative",
  "stance": "accept | confused | reject",
  "comprehension": 0,
  "trust": 0,
  "action_readiness": 0,
  "scores": {{"hierarchy": 0, "type": 0, "contrast": 0, "rhythm": 0, "space": 0}},
  "main_objection": "...",
  "most_effective_asset": "...",
  "weakest_asset": "...",
  "requested_change": "...",
  "designer_signal": "keep | adjust | rethink"
}}

Scores are 0-10. Sentiment, stance, and designer_signal must use the exact enum labels."""
    raw_response, raw_payload = post_chat(api_key, base_url, model, content)
    return {
        "prompt": content,
        "raw_response": raw_response,
        "raw_payload": raw_payload,
        "parsed": extract_json_object(raw_response),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--project-summary", required=True)
    parser.add_argument(
        "--sample-size",
        type=int,
        default=DEFAULT_SAMPLE_SIZE,
        help=(
            f"Number of sampled audience profiles. Default {DEFAULT_SAMPLE_SIZE}; "
            f"use {SMOKE_SAMPLE_SIZE} for cheaper smoke tests. "
            f"Hard limit {MAX_SAMPLE_SIZE} to avoid accidental large VLM runs."
        ),
    )
    parser.add_argument("--seed", default="crowd-critic")
    parser.add_argument("--domain", choices=["auto", *DOMAIN_FILE], default="auto")
    parser.add_argument(
        "--domain-selector",
        choices=DOMAIN_SELECTORS,
        default="keyword",
        help="How to choose the single SocioBench domain when --domain=auto.",
    )
    parser.add_argument(
        "--sampling-strategy",
        choices=SAMPLING_STRATEGIES,
        default="country_diverse",
        help="country_diverse is deterministic round-robin by country; llm_plan asks the model for executable buckets based on this domain's empirical fields.",
    )
    parser.add_argument(
        "--sampling-only",
        action="store_true",
        help="Only write domain/profile/sampling artifacts, then stop before any VLM or simulation calls.",
    )
    parser.add_argument(
        "--allow-small-sample",
        action="store_true",
        help=f"Allow sample sizes below {STANDARD_MIN_SAMPLE_SIZE}. Use only for smoke tests or explicit debugging.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.sample_size < 1 or args.sample_size > MAX_SAMPLE_SIZE:
        raise ValueError(f"--sample-size must be between 1 and {MAX_SAMPLE_SIZE}; got {args.sample_size}")
    if args.sample_size < STANDARD_MIN_SAMPLE_SIZE and not args.allow_small_sample:
        raise ValueError(
            f"--sample-size {args.sample_size} is below the standard simulation minimum {STANDARD_MIN_SAMPLE_SIZE}. "
            "Use --allow-small-sample only for smoke tests or explicit debugging."
        )
    repo_root = Path.cwd()
    output_dir = (repo_root / args.output_dir).resolve() if not Path(args.output_dir).is_absolute() else Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    assets = asset_paths(repo_root, output_dir)
    api_key, base_url, model = read_openai_config(repo_root)
    seed = f"{args.seed}:{output_dir}"
    context = project_context(output_dir, args.project_summary)
    if args.domain == "auto" and args.domain_selector == "llm":
        domain_selection = select_domain_llm(api_key, base_url, model, context)
        domain = str(domain_selection["selected_domain"])
    else:
        domain = infer_domain(args.project_summary) if args.domain == "auto" else args.domain
        domain_selection = {
            "selector": "keyword" if args.domain == "auto" else "manual",
            "selected_domain": domain,
            "confidence": None,
            "rationale": "keyword inference" if args.domain == "auto" else "user-specified domain",
        }

    profiles_all = load_domain_profiles(domain)
    summary = domain_profile_summary(profiles_all)
    write_json(output_dir / "crowd-domain-selection.json", domain_selection)
    write_json(output_dir / "crowd-domain-profile-summary.json", summary)

    if args.sampling_strategy == "llm_plan":
        plan_bundle = sampling_plan_llm(api_key, base_url, model, context, summary, args.sample_size)
        profiles, sampling_validation = execute_sampling_plan(profiles_all, plan_bundle["parsed"], args.sample_size, seed)  # type: ignore[arg-type]
        write_json(output_dir / "crowd-sampling-plan.json", plan_bundle)
        write_json(output_dir / "crowd-sampling-validation.json", sampling_validation)
    else:
        profiles = country_diverse_sample(profiles_all, args.sample_size, seed)
        write_json(
            output_dir / "crowd-sampling-plan.json",
            {
                "strategy": "country_diverse",
                "rationale": "seed-stable country-diverse round-robin sampling from one SocioBench domain",
            },
        )
        write_json(
            output_dir / "crowd-sampling-validation.json",
            {"status": "pass" if len(profiles) == args.sample_size else "partial", "selected_count": len(profiles)},
        )

    write_json(
        output_dir / "crowd-profiles.json",
        {
            "source": {
                "dataset": "SocioBench ISSP sampling500",
                "path": str(DATA_DIR / DOMAIN_FILE[domain]),
                "domain": domain,
                "sample_size": len(profiles),
                "seed": seed,
            },
            "note": "Profiles are demographic context for simulated audience critique, not real design preference labels.",
            "profiles": profiles,
        },
    )
    write_json(
        output_dir / "crowd-run-manifest.json",
        {
            "runner": "crowd_critic_runner.py",
            "model": model,
            "base_url": base_url,
            "output_dir": str(output_dir),
            "project_summary": args.project_summary,
            "sample_size": args.sample_size,
            "seed": seed,
            "domain": domain,
            "domain_selector": args.domain_selector,
            "sampling_strategy": args.sampling_strategy,
            "assets": [str(asset) for asset in assets],
            "artifact_contract": {
                "crowd-visual-analysis.jsonl": "one row per profile x asset, includes prompt, full VLM response, and raw API payload",
                "crowd-critic-raw.jsonl": "one row per profile, includes parsed simulation fields plus prompt, raw response, and raw API payload",
                "crowd-simulation-raw.jsonl": "one row per profile, exact simulation prompt/raw/parsed bundle for analysis",
            },
        },
    )

    if args.sampling_only:
        print(f"Sampling-only run complete for {output_dir}.")
        print(f"Domain: {domain}")
        print(f"Profiles: {len(profiles)}")
        print("Files: crowd-domain-selection.json, crowd-domain-profile-summary.json, crowd-sampling-plan.json, crowd-sampling-validation.json, crowd-profiles.json, crowd-run-manifest.json")
        return 0

    observations: list[dict[str, object]] = []
    simulations: list[dict[str, object]] = []
    log_path = output_dir / "crowd-critic-full-log.md"
    log_path.write_text(f"# Crowd Critic Full Log\n\nModel: {model}\n\n", encoding="utf-8")

    for profile_index, profile in enumerate(profiles):
        profile_observations: list[dict[str, object]] = []
        for asset in assets:
            prompt = observation_prompt(profile, args.project_summary)
            response, raw_payload = analyze_image(api_key, base_url, model, asset, prompt)
            observation = {
                "profile_index": profile_index,
                "person_id": profile.get("person_id"),
                "segment": profile.get("segment"),
                "asset": asset.name,
                "asset_path": str(asset),
                "model": model,
                "prompt": prompt,
                "response": response,
                "raw_payload": raw_payload,
            }
            observations.append(observation)
            profile_observations.append(observation)
            with log_path.open("a", encoding="utf-8") as log:
                log.write(
                    f"\n---\nProfile: {profile.get('person_id')}\nAsset: {asset.name}\n\n"
                    f"Prompt:\n{prompt}\n\nResponse:\n{response}\n"
                )
        simulation = simulate_profile(api_key, base_url, model, profile, profile_observations)
        simulations.append(
            {
                "person_id": profile.get("person_id"),
                "segment": profile.get("segment"),
                "model": model,
                "prompt": simulation["prompt"],
                "raw_response": simulation["raw_response"],
                "raw_payload": simulation["raw_payload"],
                **simulation["parsed"],
            }
        )

    write_jsonl(output_dir / "crowd-visual-analysis.jsonl", observations)
    write_jsonl(output_dir / "crowd-critic-raw.jsonl", simulations)
    write_jsonl(
        output_dir / "crowd-simulation-raw.jsonl",
        [
            {
                "person_id": item.get("person_id"),
                "segment": item.get("segment"),
                "model": item.get("model"),
                "prompt": item.get("prompt"),
                "raw_response": item.get("raw_response"),
                "raw_payload": item.get("raw_payload"),
                "parsed": {
                    key: value
                    for key, value in item.items()
                    if key
                    not in {
                        "person_id",
                        "segment",
                        "model",
                        "prompt",
                        "raw_response",
                        "raw_payload",
                    }
                },
            }
            for item in simulations
        ],
    )
    (output_dir / "crowd-simulation-analysis.md").write_text(analysis_markdown(simulations, assets), encoding="utf-8")

    report = validation_report(
        sample_size=args.sample_size,
        profiles=profiles,
        assets=assets,
        observations=observations,
        simulations=simulations,
    )
    write_json(output_dir / "crowd-critic-validation.json", report)
    if report["status"] != "pass":
        raise RuntimeError(f"Crowd critic validation failed: {json.dumps(report, ensure_ascii=False)}")

    print(f"Crowd critic runner complete for {output_dir}.")
    print(f"Profiles: {len(profiles)}")
    print(f"Assets: {len(assets)}")
    print(f"Visual observations: {len(observations)}")
    print(f"Simulated comments: {len(simulations)}")
    print(f"Validation: {report['status']}")
    print(
        "Files: crowd-run-manifest.json, crowd-profiles.json, crowd-visual-analysis.jsonl, "
        "crowd-critic-raw.jsonl, crowd-simulation-raw.jsonl, crowd-simulation-analysis.md, "
        "crowd-critic-validation.json, crowd-critic-full-log.md"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
