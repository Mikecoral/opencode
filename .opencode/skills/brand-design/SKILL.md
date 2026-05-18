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

## Stage 1: Brand Strategy Research (Planner Agent)

Dispatch the @planner sub-agent with this message:

```
Please research and analyze the brand design requirements for the following request:

[INSERT USER'S ORIGINAL REQUEST HERE]

Your task:
1. Research the organization thoroughly using web search
2. Analyze the brand context, positioning, and design opportunity
3. Produce a comprehensive design brief covering all 10 sections
4. Save the brief to `design-output/brief.md`

Be thorough — the Designer agent will use your brief to generate actual visual assets.
```

After the planner completes, read `design-output/brief.md` and show the user a summary. Ask:

> "The brand strategy brief is ready. Here are the key design directions: [summary]. Shall I proceed to visual design generation? (yes/no/modify)"

If the user wants modifications, incorporate their feedback and re-run the planner or edit the brief directly.

---

## Stage 2: Visual Asset Generation (Designer Agent)

Once the user approves the brief, dispatch the @designer sub-agent with this message:

```
The brand design brief is ready at `design-output/brief.md`.

Please read the brief carefully, then generate the 5 brand visual assets:
1. logo-primary (1024x1024, high quality)
2. logo-horizontal (1792x1024, high quality)  
3. color-palette (1792x1024, high quality)
4. typography-specimen (1792x1024, high quality)
5. brand-mockup (1792x1024, high quality)

For each asset, craft a detailed imagegen prompt that reflects the brand strategy from the brief. Save the manifest to `design-output/design-assets.md`.
```

After the designer completes, show the user the list of generated files. Ask:

> "Visual assets generated. Files saved to design-output/. Shall I proceed to design critique and quality evaluation? (yes/no)"

---

## Stage 3: Design Critique (Critic Agent)

Once approved, dispatch the @critic sub-agent with this message:

```
Please evaluate the brand design system:
- Read the design brief at `design-output/brief.md`
- Review the asset manifest at `design-output/design-assets.md`
- Score across all 5 dimensions
- Identify top 3 improvements with ready-to-use imagegen prompts
- Save your critique to `design-output/critique.md`
```

After the critic completes, show the user the scores and top recommendations. Ask:

> "Critique complete. Overall score: [X]/10. Top recommendation: [summary]. Options: (1) Accept current results (2) Iterate on specific assets (3) Full redesign"

---

## Stage 4: Iteration (Optional)

If the user wants to iterate on specific assets, use the ready-to-use prompts from the critique to regenerate those assets via the imagegen tool directly, then update the manifest.

---

## Final Output

After the workflow completes, write a summary report to `design-output/README.md`:

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
```

Tell the user: "Brand design complete. All assets are in the `design-output/` directory. Open `design-output/README.md` for a summary."
