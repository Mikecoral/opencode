---
name: brand-design
description: Multi-agent brand identity design system. Coordinates Planner, Designer, and Critic agents to produce complete brand visual assets.
triggers:
  - 品牌设计
  - 品牌形象
  - brand identity
  - brand design
  - logo design
  - visual identity
  - 设计品牌
  - 形象设计
---

# Brand Design Harness

You are orchestrating a multi-agent brand design workflow. Execute stages in order. Only stop to ask the user at the two marked **[USER STOP]** gates — all other transitions are automatic.

---

## Session Setup

Generate a timestamp-based run directory before dispatching any agent:

```
RUN_DIR = "packages/opencode/design-output/YYYYMMDD-HHMM"  (current local time)
```

Tell the user: "Starting brand design session. Output will be saved to `[RUN_DIR]/`."

---

## Stage 1a → Visual Research

Dispatch @visual-researcher:

```
Run directory: `[RUN_DIR]/`

Research the following brand design request:
[INSERT USER'S ORIGINAL REQUEST HERE]

1. Competitor & category visual audit (4–6 organizations)
2. Visual reference examples (6–10 from across industries)
3. Three clearly differentiated creative directions

Save to `[RUN_DIR]/visual-research.md` and `[RUN_DIR]/direction-options.md`.
```

→ When complete, proceed immediately to Stage 1.

---

## Stage 1 → Brand Brief

Dispatch @planner:

```
Write the brand design brief for:
[INSERT USER'S ORIGINAL REQUEST HERE]

Research files are at:
- `[RUN_DIR]/visual-research.md`
- `[RUN_DIR]/direction-options.md`

1. Read both files thoroughly
2. Evaluate research completeness (see planner instructions)
3. If gaps found: write `[RUN_DIR]/search-supplement-request.md` and stop
4. If sufficient: write `[RUN_DIR]/brief.md`
```

**After planner completes:**

- If `[RUN_DIR]/search-supplement-request.md` exists → run supplement loop (below), then proceed to Stage 1.5
- If `[RUN_DIR]/brief.md` exists and no supplement file → proceed immediately to Stage 1.5

**Supplement loop (runs at most once):**

Dispatch @visual-researcher:
```
SUPPLEMENT REQUEST — read `[RUN_DIR]/search-supplement-request.md`.
Run directory: `[RUN_DIR]/`
Append findings to existing research files. Do not overwrite.
```

Then re-dispatch @planner with the same Stage 1 message. If planner flags gaps again, ignore the supplement file and proceed with the brief as written.

→ After brief.md exists (with or without supplement), proceed immediately to Stage 1.5.

---

## Stage 1.5 → Brief Review

Dispatch @critic:

```
MODE: A (brief review — no images yet)

Review the brief at `[RUN_DIR]/brief.md`.
Score each section, flag weak areas, suggest rewrites.
Save review to `[RUN_DIR]/brief-review.md`.
```

**After critic completes:**

- If score ≥ 7 → proceed immediately to Stage 2a. Tell the user: "Brief quality [X]/10 — proceeding to asset planning."
- If score < 7 → show the user the flagged sections and ask: "Brief quality [X]/10. Issues: [list]. Options: (1) Proceed anyway (2) Revise brief first." Wait for response before continuing.

---

## Stage 2a → Asset Planning **[USER STOP 1]**

Dispatch @designer:

```
MODE: PLAN (do not generate images yet)
Run directory: `[RUN_DIR]/`
Read `[RUN_DIR]/brief.md`. Propose an asset list for this brand.
Save to `[RUN_DIR]/asset-plan.md`.
```

Show the user the proposed asset list. Ask:

> "Here is the proposed asset list: [summary]. Proceed with this plan, or adjust? (proceed / modify)"

Wait for confirmation. If the user modifies, update `[RUN_DIR]/asset-plan.md` directly.

→ Once confirmed, proceed to Stage 2.5.

---

## Stage 2.5 → Concept Exploration **[USER STOP 2]**

Dispatch @designer:

```
MODE: EXPLORE
Run directory: `[RUN_DIR]/`
Read `[RUN_DIR]/brief.md`. Generate concept comparison images for foundational choices
(logo direction, color palette, etc.). Save descriptions to `[RUN_DIR]/concept-board.md`.
```

Show the user the generated images and `[RUN_DIR]/concept-board.md`. Ask:

> "Here are your concept options. Please select your preferred direction for each (or say 'try again' for any category)."

Wait for selection. If the user wants different options for any category, re-dispatch @designer in EXPLORE mode with their feedback for that category only.

Once the user confirms, save selections to `[RUN_DIR]/concept-selection.md`.

→ Proceed to Stage 2b.

---

## Stage 2b → Asset Generation

**Gate: `[RUN_DIR]/concept-selection.md` must exist before proceeding.**

Dispatch @designer:

```
MODE: GENERATE
Run directory: `[RUN_DIR]/`

Read `[RUN_DIR]/concept-selection.md` first — apply chosen directions to every asset.
Asset plan: `[RUN_DIR]/asset-plan.md`
Brief: `[RUN_DIR]/brief.md`

Generate all assets. Save to `[RUN_DIR]/`. Save manifest to `[RUN_DIR]/design-assets.md`.
```

→ When complete, proceed immediately to Stage 3.

---

## Stage 3 → Design Critique

Dispatch @critic:

```
MODE: B
Brief: `[RUN_DIR]/brief.md`
Assets: `[RUN_DIR]/design-assets.md`
Save critique to `[RUN_DIR]/critique.md`
```

Show the user the dimension scores and MUST_FIX items. Ask:

> "Critique complete. Score: [X]/10. [N] MUST_FIX items. Options: (1) Accept (2) Iterate (3) Full redesign"

---

## Stage 4 → Iteration (if requested)

**Step 1 — Determine ITER_DIR:**
Count existing `iter-N` folders under `[RUN_DIR]/`. Set `ITER_DIR = [RUN_DIR]/iter-1` (or next N).

**Step 2 — Build fix list** from critique MUST_FIX items + Top 3 recommendations. Show the user and confirm which assets to regenerate.

**Step 3 — Dispatch @designer:**

```
MODE: ITERATE
RUN_DIR: [RUN_DIR]
ITER_DIR: [ITER_DIR]

Assets to regenerate:
[LIST EACH ASSET AND THE SPECIFIC ISSUE TO FIX]

Critique: `[RUN_DIR]/critique.md` (or previous iter critique)
[Crowd critique: `[RUN_DIR]/crowd-critic-designer-actions.md` if available]

Save regenerated images to `[ITER_DIR]/`.
Save manifest to `[ITER_DIR]/design-assets.md`.
Do not modify original assets.
```

**Step 4 — Re-run critique on new assets:**

Dispatch @critic:
```
MODE: B
RUN_DIR: [ITER_DIR]
Brief: [RUN_DIR]/brief.md
Assets: [ITER_DIR]/design-assets.md
Save critique to: [ITER_DIR]/critique.md
```

Show new scores alongside previous round. Set `[ITER_DIR]` as active directory. Ask: "Scores updated. Continue iterating or move to final validation? (iterate / done)"

---

## Stage 3.5 → Audience Validation (when team is done iterating)

Once the user indicates the design is ready, ask:

> "Design finalized. Run audience testing (crowd critic) before delivery? (yes/no)"

If yes, dispatch @crowd-critic on the current active directory:

```
Output directory: [ACTIVE_DIR]
Crowd critic enabled: true
Sample size: 24
Audience inference: auto

Project summary: [INSERT USER'S ORIGINAL DESIGN REQUEST]
```

After completion, reconcile with standard critique. Produce a merged action summary:

```
## Merged Action Summary

### Agreed (both critics flag)
- [asset]: [issue] — HIGH PRIORITY

### Craft only (standard critic)
- [asset]: [issue]

### Audience only (crowd critic, 3+ segments)
- [asset]: [issue]

### Conflicting signals
- [asset]: standard says [X], crowd says [Y] → [recommendation]
```

**Conflict rule:** MUST_FIX from standard critic always overrides crowd preference. Audience issues apply only if they affect 3+ segments or the brief's primary audience.

Ask: "[N] agreed issues. Iterate on these before delivery? (yes/no)"

---

## Stage 5 → Creative Copy (optional)

Ask: "Visual assets finalized. Generate taglines, brand voice, and touchpoint copy? (yes/no)"

If yes, dispatch @copywriter:

```
Brief: `[RUN_DIR]/brief.md`
Final assets: `[ACTIVE_DIR]/`
Save to `[RUN_DIR]/copy.md`
```

---

## Final Output

Write `[RUN_DIR]/README.md`:

```markdown
# Brand Design System: [Organization Name]

Generated: [date]

## Files
- `brief.md` — Brand strategy brief
- `asset-plan.md` — Approved asset list
- `concept-selection.md` — Chosen design direction
- `design-assets.md` — Asset manifest with prompts
- `critique.md` — Quality assessment ([X]/10)
- `copy.md` — Creative copy (if generated)
```

Tell the user: "Brand design complete. All assets in `[RUN_DIR]/`. See `README.md` for a summary."
