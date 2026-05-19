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

## Stage 1: Brand Strategy Research (Planner Agent)

Dispatch the @planner sub-agent with this message:

```
Please research and analyze the brand design requirements for the following request:

[INSERT USER'S ORIGINAL REQUEST HERE]

Your task:
1. Research the organization thoroughly using web search
2. Analyze the brand context, positioning, and design opportunity
3. Produce a comprehensive design brief covering all 10 sections
4. Save the brief to `[RUN_DIR]/brief.md`

Be thorough — the Designer agent will use your brief to generate actual visual assets.
```

After the planner completes, read `[RUN_DIR]/brief.md` and show the user a summary. Ask:

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

## Stage 2: Visual Asset Generation (Designer Agent)

Once the user approves the brief, dispatch the @designer sub-agent with this message:

```
The brand design brief is ready at `[RUN_DIR]/brief.md`.

Please read the brief carefully, then generate the 5 brand visual assets:
1. logo-primary (1024x1024, high quality)
2. logo-horizontal (1792x1024, high quality)  
3. color-palette (1792x1024, high quality)
4. typography-specimen (1792x1024, high quality)
5. brand-mockup (1792x1024, high quality)

For each asset, craft a detailed imagegen prompt that reflects the brand strategy from the brief. Save generated images to `[RUN_DIR]/` and the manifest to `[RUN_DIR]/design-assets.md`.
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

## Stage 4: Iteration (Optional)

If the user wants to iterate on specific assets, first determine the iteration number:

- Check how many `iter-N` subfolders already exist under `[RUN_DIR]/`
- Set `ITER_DIR = [RUN_DIR]/iter-1` (or `iter-2`, `iter-3`, etc. — increment from the highest existing number)
- Tell the user: "Saving iteration to `[ITER_DIR]/`."

Then dispatch the @designer sub-agent with targeted regeneration instructions:

```
Please regenerate the following assets based on the critique feedback:

[LIST THE SPECIFIC ASSETS AND WHAT TO CHANGE]

Use these ready-to-use prompts from the critique:
[PASTE THE RELEVANT PROMPTS FROM [RUN_DIR]/critique.md]

Save regenerated images to `[ITER_DIR]/` and save the updated manifest to `[ITER_DIR]/design-assets.md` listing each asset, the issue it addresses, and the new prompt used.

The original assets remain untouched in `[RUN_DIR]/`.
```

After iteration, run Stage 3 again (dispatch @critic) with paths pointing to `[ITER_DIR]/` so the new assets are evaluated. Update `ITER_DIR` as the active directory for any further iterations.

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
- `logo-primary.png` — Primary logo mark
- `logo-horizontal.png` — Horizontal logo lockup
- `color-palette.png` — Brand color system
- `typography-specimen.png` — Typography specimen
- `brand-mockup.png` — Brand application mockup

## Quality Assessment
Overall Score: [X]/10
See `critique.md` for detailed evaluation.

## Asset Manifest
See `design-assets.md` for prompts and technical details.

## Creative Copy
See `copy.md` for taglines, brand voice, and touchpoint copy.
```

Tell the user: "Brand design complete. All assets are in `[RUN_DIR]/`. Open `[RUN_DIR]/README.md` for a summary."
