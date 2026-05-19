---
name: taste-skill
description: Visual taste evaluator for brand design assets. Runs anti-AI-slop checklist against generated images and scores "soul" vs "template." Use after imagegen calls or as a standalone audit.
triggers:
  - taste check
  - anti slop
  - visual taste
  - does this look generic
  - 有没有品位
  - 是否像AI生成的
---

# Taste Skill — Anti-AI-Slop Evaluator

Use `image_analyze` on each asset, then score against the checklist below. Do NOT just read the prompt — look at the actual image.

---

## The Seven Cardinal Sins (P0 — must fix)

For each generated asset, check whether any of these are present. Each sin = automatic flag.

| # | Sin | What to look for |
|---|-----|-----------------|
| 1 | **Generic gradient as hero** | Purple→blue, blue→cyan, indigo→pink two-stop gradient as background |
| 2 | **AI-default indigo/purple accent** | Dominant #6366f1 / #4f46e5 / #8b5cf6 or similar indigo fill with no brief justification |
| 3 | **Emoji as design elements** | ✨ 🚀 🎯 ⚡ 🔥 💡 appearing as feature icons or decoration |
| 4 | **Rounded card with colored left-border accent** | The canonical AI dashboard tile — rounded container + single colored left stripe |
| 5 | **Invented / placeholder text** | "Feature One", "Lorem ipsum", "Sample content", "Brand Name Here" |
| 6 | **Zero cultural specificity** | Generic imagery despite brief calling for specific cultural DNA |
| 7 | **Everything competing equally** | No dominant focal point; 3+ elements at same visual weight |

## Soft Tells (P1 — should fix)

- Decorative blob or wave SVG backgrounds with no functional purpose
- More than 2 visible uses of the accent color per composition
- Uniform spacing — every element equidistant, no rhythm variation
- Graduated weight ladder (regular → medium → semibold → bold) with no jumps
- Symmetric layout with no visual tension or asymmetric energy

## Soul Checklist (P2 — what separates good from generic)

A piece has soul when a viewer who didn't brief it could identify the brand from the image alone. Check for:

- [ ] One bold visual move tied specifically to the brand's Cultural DNA (Section 5 of brief)
- [ ] Typography choice that has personality, not just legibility
- [ ] One unexpected proportion or scale decision (not the "safe" default)
- [ ] Color palette traceable to brief Section 7/8, not generic "looks professional"
- [ ] If text is present: microcopy with voice, not placeholder labels

---

## Scoring Output

For each asset, output:

```
## Taste Audit: [filename]

### Cardinal Sins Found
- [list sins present, or "None — clean"]

### Soft Tells Found
- [list P1 issues, or "None"]

### Soul Assessment
- Bold move: [present / absent — describe]
- Cultural specificity: [strong / weak / absent]
- Focal clarity: [one dominant / competing / flat]
- Overall soul score: X/10

### Verdict
PASS / REVISE / REJECT
- PASS: ≤0 cardinal sins, soul score ≥6
- REVISE: 1 cardinal sin OR soul score 4-5
- REJECT: ≥2 cardinal sins OR soul score ≤3

### Suggested fix (if REVISE or REJECT)
[One specific actionable prompt change]
```

---

## How to invoke as standalone

Call `image_analyze` on each PNG with this question:

```
Evaluate this brand design image for visual quality and originality.
Identify: (1) any generic AI-default patterns like purple/indigo gradients, rounded cards with left-border accents, or emoji as icons; (2) whether the composition has a single clear focal point; (3) any culturally specific elements vs. generic stock imagery; (4) whether the color palette appears intentional and brand-specific or default/generic. Be specific about what you see.
```

Then apply the scoring rubric above.
