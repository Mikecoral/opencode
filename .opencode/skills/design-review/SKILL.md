---
name: design-review
description: Visual audit of generated brand assets against craft rules (color, typography, hierarchy, anti-slop). Produces a before/after diff of issues found and a ranked fix list for the designer.
triggers:
  - design review
  - visual audit
  - before after
  - pre-delivery check
  - 设计复审
  - 交付检查
---

# Design Review Skill

A structured visual audit run after all assets are generated and before final delivery. Uses `image_analyze` on every PNG, cross-references against the brief and craft rules, and outputs a ranked fix list.

Craft rules source: `/Users/hongyuecheng/python-learn/SII/AIdesign/open-design/craft/`

---

## Step 1 — Gather Context

Read:
- `{OUTPUT_DIR}/brief.md` — brand strategy, color/type direction, cultural DNA
- `{OUTPUT_DIR}/brand-tokens.md` — declared hex values and type descriptions
- `{OUTPUT_DIR}/design-assets.md` — list of files and prompts used

---

## Step 2 — Image Analysis Pass

For each PNG in `design-assets.md`, call `image_analyze` twice:

**Pass A — Content inventory:**
```
List every visual element in this image: shapes, symbols, colors used, typography style, layout structure, any text present, background treatment, and any decorative elements.
```

**Pass B — Quality audit:**
```
Assess this brand design image: (1) Is there one clear dominant focal point or are multiple elements competing? (2) Does the color palette appear intentional and limited, or scattered? (3) Does typography have clear hierarchy with distinct primary/secondary levels? (4) Are there any generic AI patterns: purple/indigo gradients, rounded cards with colored left-border, emoji icons, placeholder text, or stock-image feel? (5) Does anything feel culturally specific and earned, or generic?
```

---

## Step 3 — Craft Rule Checks

For each asset, run these checks using the image analysis results:

### Color checks (from craft/color.md)
- [ ] Accent used ≤2 visible times per composition
- [ ] No uninstructed indigo/purple (#6366f1 family) as dominant color
- [ ] No two-stop "trust" gradient (purple→blue, blue→cyan) as hero background
- [ ] Background is off-black/off-white if dark/light (not pure #000 or #fff)
- [ ] Colors traceable to brief Section 7/8 or brand-tokens.md

### Typography checks (from craft/typography-hierarchy.md)
- [ ] One unambiguously dominant element (not 2-3 co-equal primaries)
- [ ] At least two hierarchy vectors active on the dominant element (scale + weight, or scale + spacing)
- [ ] Adjacent levels differ in ≥2 of: scale, weight, spacing, tracking
- [ ] No graduated weight ladder (regular → medium → semibold → bold without jumps)

### Anti-slop checks (from craft/anti-ai-slop.md)
- [ ] No emoji used as decorative/icon elements
- [ ] No rounded card with colored left-border accent pattern
- [ ] No placeholder or filler text
- [ ] No generic stock-photo feel despite culturally specific brief
- [ ] Single dominant focal point per composition

### Brief fidelity checks
- [ ] All key visual elements traceable to brief Sections 5, 7, or 8
- [ ] No invented elements without brief basis (cross-ref with designer-trace.md if available)
- [ ] Cultural motifs, if present, match brief Section 5 specifically

---

## Step 4 — Issue Ranking

Collect all failed checks across all assets. Rank by severity:

| Severity | Criteria |
|----------|----------|
| **P0 — Block delivery** | Cardinal sin present (gradient hero, indigo-default, left-border card, placeholder text) |
| **P1 — Fix before delivery** | Typography hierarchy flat, color undisciplined, zero cultural specificity |
| **P2 — Improve if time allows** | Soft tells, weak soul score, symmetric-only layout |

---

## Step 5 — Output

Save to `{OUTPUT_DIR}/design-review.md`:

```markdown
# Design Review: [Organization Name]
Reviewed: [date]

## Summary
- Total assets reviewed: N
- P0 issues: X (must fix)
- P1 issues: Y (should fix)
- P2 issues: Z (optional)

## P0 Issues (Block Delivery)

### [Asset filename]
- Issue: [specific problem]
- Evidence: [what image_analyze saw]
- Fix: [exact prompt change or regeneration instruction]

## P1 Issues (Fix Before Delivery)

### [Asset filename]
- Issue: [specific problem]
- Fix: [specific action]

## P2 Issues (Optional Improvements)

### [Asset filename]
- Issue: [soft tell or polish opportunity]
- Fix: [suggestion]

## Assets That Passed
- [filename] — [brief note on why it's solid]

## Recommended Action
APPROVE / REVISE [N assets] / FULL REGENERATION
```

If any P0 issues exist, do not approve. Pass the fix list to the designer for targeted regeneration.
