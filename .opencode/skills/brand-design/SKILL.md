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

You are orchestrating a multi-agent brand design workflow. When a user requests brand identity design work, execute this harness to coordinate three specialized sub-agents.

## When to Activate

Activate this skill when the user asks for brand design, brand identity, logo design, or visual identity work — especially for organizations, schools, companies, or products.

## Harness Workflow

Execute the following stages in order. At each stage boundary, show the user what was produced and ask for confirmation before proceeding.

---

## Session Setup

Before dispatching any agent, generate a timestamp-based run directory:

```
RUN_DIR = "design-output/YYYYMMDD-HHMM"  (current local time, e.g. design-output/20260519-1430)
```

Tell the user: "Starting brand design session. Output will be saved to `[RUN_DIR]/`."

Use `RUN_DIR` as the base path for all file saves throughout this session.

---

## Stage 1a: Visual Research (Visual Researcher Agent)

Dispatch the @visual-researcher sub-agent with this message:

```
Run directory: `[RUN_DIR]/`

Please research the following brand design request:

[INSERT USER'S ORIGINAL REQUEST HERE]

Your task:
1. Conduct a competitor & category visual audit (4–6 organizations)
2. Find 6–10 visual reference examples from across industries
3. Propose 3 clearly differentiated creative directions
4. Save findings to `[RUN_DIR]/visual-research.md` and `[RUN_DIR]/direction-options.md`

Be specific — the Planner will use your research to write the design brief.
```

After the researcher completes, tell the user: "Visual research complete. Competitor audit and 3 direction options saved. Proceeding to brief writing."

---

## Stage 1: Brand Brief (Planner Agent)

Dispatch the @planner sub-agent with this message:

```
Please write the brand design brief for the following request:

[INSERT USER'S ORIGINAL REQUEST HERE]

Research files are already available at:
- `[RUN_DIR]/visual-research.md` — competitor audit and visual references
- `[RUN_DIR]/direction-options.md` — 3 proposed creative directions

Your task:
1. Read both research files thoroughly
2. Select and refine the strongest direction from `direction-options.md`
3. Synthesize the research into a comprehensive 10-section design brief
4. Save the brief to `[RUN_DIR]/brief.md`

Do not re-search what is already in the research files. Your job is strategy synthesis, not web research.
```

After the planner completes, check whether `[RUN_DIR]/search-supplement-request.md` exists:

**If it exists (planner flagged research gaps):**

Re-dispatch @visual-researcher in supplement mode:

```
SUPPLEMENT REQUEST — read `[RUN_DIR]/search-supplement-request.md` for the specific gaps to fill.

Run directory: `[RUN_DIR]/`

Append your supplemental findings to the existing `[RUN_DIR]/visual-research.md` and `[RUN_DIR]/direction-options.md`. Do not overwrite them.
```

After the researcher completes, re-dispatch @planner with the same message as Stage 1. This loop runs at most once — if the planner flags gaps a second time, proceed to brief writing anyway and note the gaps in the brief.

**If it does not exist (research was sufficient):**

Read `[RUN_DIR]/brief.md` and show the user a summary. Ask:

> "The brand strategy brief is ready. Here are the key design directions: [summary]. Shall I proceed to visual design generation? (yes/no/modify)"

If the user wants modifications, incorporate their feedback and re-run the planner or edit the brief directly.

---

## Stage 1.5: Brief Review (Critic Agent — Mode A)

Before generating any images, dispatch the @critic sub-agent to review the brief quality:

```
MODE: A (brief review — no images yet)

Please review the brand design brief at `[RUN_DIR]/brief.md`.

Your task:
1. Evaluate whether the brief is specific enough to drive visual design
2. Check each section for vague language, generic defaults, or missing detail
3. Flag any sections that would produce generic/uninspired imagery if used as-is
4. Suggest concrete improvements for weak sections
5. Give an overall brief quality score (1-10)
6. Save your review to `[RUN_DIR]/brief-review.md`

Focus on: Are the design keywords vivid and distinctive? Is the color strategy specific? Is the symbol/mark direction original? Would a designer reading this produce something unique or something generic?
```

After the critic completes, read `[RUN_DIR]/brief-review.md` and show the user the score and flagged sections. Ask:

> "Brief review complete. Quality score: [X]/10. Issues found: [list]. Options: (1) Proceed to visual generation anyway (2) Have planner revise the brief first"

If the user chooses to revise, dispatch @planner with the critic's feedback as additional context, then re-run Stage 1.5.

---

## Stage 2a: Asset Planning (Designer Agent)

Once the user approves the brief, dispatch the @designer sub-agent for planning only:

```
MODE: PLAN (do not generate images yet)

Run directory: `[RUN_DIR]/`

Please read `[RUN_DIR]/brief.md` and research the brand as needed.

Based on the brief, propose an asset list tailored to this brand.
Save your asset plan to `[RUN_DIR]/asset-plan.md`.
```

After the designer saves the plan, read `[RUN_DIR]/asset-plan.md` and show it to the user. Ask:

> "Here is the proposed asset list: [summary]. Shall I proceed with generation, or would you like to adjust? (proceed / modify)"

If the user modifies, update `[RUN_DIR]/asset-plan.md` directly, then proceed.

---

## Stage 2b: Visual Asset Generation (Designer Agent)

Once the asset plan is confirmed, dispatch the @designer sub-agent for generation:

```
MODE: GENERATE

Run directory: `[RUN_DIR]/`

The asset plan is confirmed at `[RUN_DIR]/asset-plan.md`.

Please read the plan and generate all listed assets.
Ground every prompt in `[RUN_DIR]/brief.md`.
Save generated images to `[RUN_DIR]/` and the manifest to `[RUN_DIR]/design-assets.md`.
```

After the designer completes, show the user the list of generated files. Ask:

> "Visual assets generated. Files saved to `[RUN_DIR]/`. Shall I proceed to design critique and quality evaluation? (yes/no)"

---

## Stage 3: Design Critique (Critic Agent)

Once approved, dispatch the @critic sub-agent with this message:

```
Please evaluate the brand design system:
- Read the design brief at `[RUN_DIR]/brief.md`
- Review the asset manifest at `[RUN_DIR]/design-assets.md`
- Score across all 5 dimensions
- Identify top 3 improvements with ready-to-use imagegen prompts
- Save your critique to `[RUN_DIR]/critique.md`
```

After the critic completes, show the user the scores and top recommendations. Ask:

> "Critique complete. Overall score: [X]/10. Top recommendation: [summary]. Options: (1) Accept current results (2) Iterate on specific assets (3) Full redesign"

---

## Stage 3.5: Crowd Critic (On-Demand Only)

**Do NOT run this stage automatically.** Only dispatch when the user explicitly asks (e.g. "run crowd critic", "做受众测试", "crowd feedback").

Crowd critic can be run on the original assets (`[RUN_DIR]/`) or on any iteration directory (`[ITER_DIR]/`). Use whichever directory contains the assets currently under review.

**Dispatch @crowd-critic:**

```
Output directory: [ACTIVE_DIR]   ← RUN_DIR or current ITER_DIR
Crowd critic enabled: true
Sample size: 24
Audience inference: auto

Project summary: [INSERT USER'S ORIGINAL DESIGN REQUEST]
```

**After crowd critic completes — reconcile with standard critique:**

Read both:
- `[ACTIVE_DIR]/critique.md` — standard critic findings (dimension scores, MUST_FIX)
- `[ACTIVE_DIR]/crowd-critic-designer-actions.md` — crowd priority actions

Produce a merged action summary in this format and show it to the user:

```
## Merged Action Summary

### Agreed (both critics flag this)
- [asset]: [issue] — HIGH PRIORITY

### Craft only (standard critic only)
- [asset]: [issue] — fix before delivery

### Audience only (crowd critic only)
- [asset]: [issue] — consider if audience fit matters here

### Conflicting signals
- [asset]: standard critic says [X], crowd says [Y]
  → Recommendation: [which to follow and why — craft issues override audience preference;
    audience issues override craft when the brand's primary goal is broad accessibility]
```

**Conflict resolution rule:**
- MUST_FIX items from the standard critic always take priority over crowd preference — craft failures block delivery regardless of audience scores.
- When only the crowd flags an issue (craft check passes), follow the crowd action if it affects 3+ audience segments or a segment that maps to the brief's primary audience.
- When signals conflict (crowd likes something the standard critic flagged), present both views to the user and ask which to prioritize.

Ask: "Merged review complete. [N] agreed issues, [M] conflicts. Shall I proceed to iteration? (yes/no)"

---

## Stage 4: Iteration (Optional)

If the user wants to iterate on specific assets:

**Step 1 — Determine iteration directory:**
- Count existing `iter-N` subfolders under `[RUN_DIR]/`
- Set `ITER_DIR = [RUN_DIR]/iter-1` (or `iter-2`, `iter-3`, etc.)
- Tell the user: "Saving iteration to `[ITER_DIR]/`."

**Step 2 — Build the fix list:**

Derive from whichever sources are available, in priority order:
1. MUST_FIX items from `critique.md` (standard critic, current active dir)
2. Agreed items from the merged action summary (if Stage 3.5 was run)
3. Craft-only items from `critique.md`
4. Audience-only items from `crowd-critic-designer-actions.md` that meet the 3-segment threshold

Show the user the prioritized list and confirm before dispatching.

**Step 3 — Dispatch @designer in ITERATE mode:**

```
MODE: ITERATE

RUN_DIR: [RUN_DIR]
ITER_DIR: [ITER_DIR]

Assets to regenerate:
[LIST EACH ASSET AND THE SPECIFIC ISSUE TO FIX, ONE PER LINE]

Critique sources:
- `[ACTIVE_DIR]/critique.md` — MUST_FIX items and Top 3 recommendations
[- `[ACTIVE_DIR]/crowd-critic-designer-actions.md` — Priority Actions table, if crowd critique was run]

Save all regenerated images to `[ITER_DIR]/`.
Save manifest to `[ITER_DIR]/design-assets.md`.
Original assets must not be modified.
```

**Step 4 — Re-run standard critique on new assets:**

After the designer completes, dispatch @critic (Mode B):

```
MODE: B

RUN_DIR: [ITER_DIR]
Brief: [RUN_DIR]/brief.md
Assets: [ITER_DIR]/design-assets.md
Save critique to: [ITER_DIR]/critique.md
```

Show the new dimension scores alongside the previous round's scores so the user can see what improved. Set `[ITER_DIR]` as the active directory for any further iterations or crowd critique runs.

---

## Stage 5: Creative Copywriting (Copywriter Agent)

Run this stage only after all visual iterations are finalized (Stage 4 complete or skipped). Ask the user:

> "All images are finalized. Would you like me to generate creative copy — taglines, brand voice guidelines, and touchpoint copy? (yes/no)"

If yes, dispatch the @copywriter sub-agent:

```
The brand design brief is at `[RUN_DIR]/brief.md`.
The final assets are in `[RUN_DIR]/` (or `[ITER_DIR]/` if iterations were done).

Please generate the full creative copy package for this brand and save it to `[RUN_DIR]/copy.md`.
```

After the copywriter completes, tell the user: "Creative copy saved to `[RUN_DIR]/copy.md`."

---

## Final Output

After the workflow completes, write a summary report to `[RUN_DIR]/README.md`:

```markdown
# Brand Design System: [Organization Name]

Generated: [date]

## Design Brief
See `brief.md`

## Generated Assets
See `design-assets.md` for the actual generated asset list. Assets are selected from the approved plan and may include identity, digital, editorial, campaign, spatial, product, or other brief-specific touchpoints.

## Quality Assessment
Overall Score: [X]/10
See `critique.md` for detailed evaluation.

## Asset Manifest
See `design-assets.md` for prompts and technical details.

## Creative Copy
See `copy.md` for taglines, brand voice, and touchpoint copy.
```

Tell the user: "Brand design complete. All assets are in `[RUN_DIR]/`. Open `[RUN_DIR]/README.md` for a summary."
