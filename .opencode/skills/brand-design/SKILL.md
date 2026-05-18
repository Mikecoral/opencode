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

You are orchestrating a multi-agent brand design workflow. Execute the stages in order. At each boundary, summarize for the user and **wait for confirmation** before proceeding.

## When to Activate

Brand design, brand identity, logo, or visual identity work — for organizations, schools, companies, or products.

---

## Session Setup (Before Stage 1)

**Generate a timestamp-based run directory and hold it for the entire session.**

Compute `RUN_DIR` as:
```
design-output/YYYYMMDD-HHMM
```
using the current date and time (e.g. `design-output/20260518-1423`).

All files for this session go under `RUN_DIR`. Never mix files from different runs. Tell the user:

> "Starting brand design session. Output directory: `design-output/YYYYMMDD-HHMM/`"

---

## Stage 1: Brand Strategy Research (Planner)

Dispatch `@planner`:

```
Please research and produce a brand design brief for:

[INSERT USER'S ORIGINAL REQUEST]

Follow the Research Protocol in your instructions: at least 3 websearch queries
and 2 webfetch calls on authoritative sources. Cite every factual claim with
inline URLs.

Output directory: [RUN_DIR]
Save brief to: [RUN_DIR]/brief.md
```

After completion, read `[RUN_DIR]/brief.md` and summarize the key strategic directions for the user.

---

## Stage 1.5: Brief Review (Critic, Mode A)

**This stage is mandatory** — it catches weak research before we spend image-generation budget on a bad foundation.

Dispatch `@critic`:

```
Output directory: [RUN_DIR]

Please review the brand design brief at `[RUN_DIR]/brief.md` in Brief Review
mode (Mode A). Score across all 5 dimensions and produce a verdict
(PASS / REVISE / RESEARCH-AGAIN). Save to `[RUN_DIR]/brief-critique.md`.
```

Read `[RUN_DIR]/brief-critique.md`, present the verdict and dimension scores to the user. Then:

- **If verdict = PASS** → ask: *"Brief approved by critic with score X/10. Proceed to design generation? (yes/no)"*
- **If verdict = REVISE** → list the specific fixes; ask: *"Critic requests these revisions. Options: (1) I edit the brief now (2) Re-dispatch planner with these fixes (3) Proceed anyway"*
- **If verdict = RESEARCH-AGAIN** → re-dispatch `@planner` with the specific search queries from the critique and the same `RUN_DIR`, then loop back to Stage 1.5.

### Retry Guard (MANDATORY)

Track how many times Planner has been re-dispatched in this session. **Hard cap: 2 re-research attempts** (3 total Planner runs). On the 3rd `RESEARCH-AGAIN` verdict, do NOT auto-loop. Instead, present to the user:

> "Brief failed Critic review 3 times. The research subject may be obscure or the entity may not exist online. Options: (1) Proceed with the current best brief despite warnings (2) Provide source material manually (paste text / give URLs) (3) Abort workflow"

This prevents infinite loops when the organization has insufficient web presence.

---

## Stage 2a: Asset Planning (Designer, Phase 1)

Once brief is approved, dispatch `@designer`:

```
Output directory: [RUN_DIR]

The approved brief is at `[RUN_DIR]/brief.md`. Run Phase 1 only: propose
4-8 brand assets tailored to this organization. Save to
`[RUN_DIR]/asset-plan.md` and STOP — do not generate images yet.
```

Read `[RUN_DIR]/asset-plan.md`. Present the proposed asset list to the user. Ask:

> "Designer proposes these N assets: [list]. Approve to generate? (yes / modify list / change scope)"

If user wants modifications, edit `asset-plan.md` directly or re-dispatch designer with constraints.

---

## Stage 2b: Visual Generation (Designer, Phase 2)

Once the asset plan is approved, dispatch `@designer`:

```
Output directory: [RUN_DIR]

The asset plan at `[RUN_DIR]/asset-plan.md` is approved. Run Phase 2:
generate every asset in the plan via `imagegen` using `[RUN_DIR]/<filename>`
as the filename parameter (e.g. `20260518-1423/logo-primary`), then save
the manifest to `[RUN_DIR]/design-assets.md`.
```

After completion, list the generated files for the user. Ask:

> "All N assets generated. Proceed to visual critique? (yes/no)"

---

## Stage 3: Visual Critique (Critic, Mode B)

Dispatch `@critic`:

```
Output directory: [RUN_DIR]

Please evaluate the generated brand assets in Visual Review mode (Mode B):
- Read `[RUN_DIR]/brief.md` and `[RUN_DIR]/design-assets.md`
- Score across all 5 visual dimensions
- Provide top 3 iteration recommendations with ready-to-use imagegen prompts
- Save to `[RUN_DIR]/critique.md`
```

Present the scores and top recommendation. Ask:

> "Critique complete. Overall: X/10. Options: (1) Accept (2) Iterate on specific assets (3) Full redesign"

---

## Stage 4: Iteration (Optional)

If user picks iteration, dispatch `@designer` again with targeted regeneration:

```
Output directory: [RUN_DIR]

Regenerate the following assets based on critique feedback:

[LIST ASSETS + WHAT TO CHANGE]

Use these prompts from the critique:
[PASTE PROMPTS FROM [RUN_DIR]/critique.md]

Use `[RUN_DIR]/<filename>` as the filename parameter for imagegen.
Overwrite the originals and update `[RUN_DIR]/design-assets.md`.
```

---

## Final Output

Write `[RUN_DIR]/README.md`:

```markdown
# Brand Design System: [Organization Name]

Generated: [date]

## Run Directory
`[RUN_DIR]/`

## Brief
See `brief.md` (reviewed: `brief-critique.md`)

## Assets
[List of actually-generated files with one-line descriptions, pulled from design-assets.md]

## Quality Assessment
Overall Score: X/10 — see `critique.md`

## Asset Manifest
See `design-assets.md` for prompts and technical details.

## Reasoning Traces (for audit)
- `planner-trace.md` — search queries, fetched URLs, Subject Type reasoning, DNA derivation
- `critic-mode-a-trace.md` — per-dimension scoring rationale for the brief
- `designer-trace.md` — asset selection tradeoffs and per-prompt derivation
- `critic-mode-b-trace.md` — per-asset observations and recommendation derivation
```

Tell the user: *"Brand design complete. All assets are in `[RUN_DIR]/`. See `[RUN_DIR]/README.md` for the summary."*
