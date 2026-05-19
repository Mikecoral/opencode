# Designer Trace

## Phase 1: Asset Planning

### Subject Type & Brief Touchpoints
Subject Type quoted from brief: “organization.”

Relevant Section 11 touchpoints classified:
- Top priority: 官网首页与科研成果页视觉系统
- Top priority: 招生营 / 开放日 / TechFest 活动物料
- Top priority: 科研项目与五大阵地的子品牌系统
- Top priority: 招聘/导师引进主视觉
- Optional: 研究报告 / 开源项目封面模板
- Optional: 空间导视与实验室门牌
- Not this round: 周边服饰与纪念品

### Visual Direction Decision
- Selected direction: research-signal
- Alternatives considered: institutional-minimal, campaign-energy, spatial-system
- Why selected: The brief repeatedly foregrounds frontier AI research, a “frontier signal system,” open-source infrastructure, a generative grid identity, and project-based research fronts. Section 10 specifically asks for an SII generative grid mark and a three-stage path system.
- Generic defaults avoided: education admissions bundle, campus image bundle, conventional school crest, generic AI chip/robot-head symbols, merchandise-first community bundle.

### Deliverable Strategy Decision
- Selected strategy: digital-system
- Why selected: Section 11 makes the official homepage and research-results pages the first Top priority, and the remaining Top priority touchpoints can all be served by a digital modular system: project subbrands, open-day/TechFest visuals, and recruitment banners.
- Why other strategies were rejected or deferred: `identity-core` is important but too narrow because the brief’s immediate application context is digital research communication; `campaign-system` would over-index on招生/开放日; `spatial-system` is Optional; `publishing-system` is Optional until the core visual language is unified; `community-system` and merchandise are Not this round.

### Assets Considered
| Asset Idea | Decision | Reason |
|-----------|----------|--------|
| logo-primary | Include | Mandatory identity anchor and foundation for the grid system. |
| generative-grid-subbrand-system | Include | Top priority project/five-front subbrand need; strong fit with Section 10. |
| website-research-hero | Include | Top priority official homepage and research page visual system. |
| research-project-card-system | Include | Supports research progress pages and modular project communication. |
| techfest-open-day-key-visual | Include | Top priority event/recruitment context; avoids generic admissions framing. |
| talent-recruitment-banner | Include | Top priority mentor/young PI recruitment and “Calling for Marvellers” tone. |
| research-report-cover-template | Reject / Defer | Optional in Section 11; better after core digital system is established. |
| campus-wayfinding-signage | Reject / Defer | Optional in Section 11 and would require a spatial-system strategy. |
| admissions-brochure | Reject | Would make the output generic; Section 11 supports events, not a default brochure. |
| merchandise-badge-or-hoodie | Reject | Section 11 explicitly says Not this round. |
| color-palette | Reject | Tokenized in `brand-tokens.md`; standalone swatch asset would be a default rather than an application. |

### Why this final 4-8?
The final six assets are enough to establish one coherent digital research-signal identity: primary mark, scalable subbrand glyph logic, homepage/research hero, repeatable project cards, event key visual, and recruitment banner. Omitted defaults such as color palette, campus signage, admissions brochure, and merchandise were not generated because they are either token/documentation needs, Optional, Not this round, or likely to dilute the system into a generic school sampler.

## Phase 2: Generation

### Per-Asset Prompt Derivation

- Asset: logo-primary
- prompt_search query: `logo minimalist monogram generative grid` (no matches); fallback query `logo`
- Template chosen: wrote from scratch (no good match)
- Why this template: The library results for `logo` were unrelated UI/live-stream or product poster prompts, and pure logo templates were sparse. A custom prompt better enforced no-text symbol discipline.
- Brief inputs used: Sections 5, 7, 8, 9, 10, 11; brand-tokens color and typography tables.
- Cultural motifs translated: AI 前沿网络 → AI frontier network of nodes, connections, and emergence; 北杨人工智能小镇 / 徐汇西岸 → North Yang AI Town and Xuhui West Bund riverfront night laboratories with glass curtain wall geometry; 从不可能到普惠 → three-stage path from impossible to possible to public benefit.
- Substitutions made: Used exact palette #07111F, #00E0FF, #E7EBF0, #2B313A; substituted school/AI clichés with generative grid, modular rounded rectangles, nodes, and signal paths.
- Style choices: Professional brand identity design, Swiss design principles, pure symbol, no text/no letters/no Chinese characters to avoid garbled typography and preserve scalability.
- Final prompt: Professional brand identity design for Shanghai Innovation Institute / SII. Create a pure abstract primary symbol only: no text, no letters, no Chinese characters, no wordmark. The mark should feel like a generative grid produced by intelligence and creation: an implied S/I/I structure or abstracted creation-intelligence logic built from modular rounded rectangles, nodes, and connecting signal paths. Use Swiss design principles, institutional credibility, and research-signal precision. Cultural context: AI frontier network of nodes, connections, and emergence; North Yang AI Town and Xuhui West Bund riverfront night laboratories with glass curtain wall geometry; a three-stage path from impossible to possible to public benefit expressed as three progressing nodes. Colors: Deep Space Ink Blue #07111F as ground, SII Electric Cyan #00E0FF for active signal, West Bund Silver #E7EBF0 highlights, Graphite Gray #2B313A grid. Centered on clean dark background, high contrast, vector-like, scalable, no stock icons, no robot head, no chip, no shield crest.
- Image generation outcome: success after retry; first high-quality parallel attempt timed out, medium-quality sequential retry succeeded.

- Asset: generative-grid-subbrand-system
- prompt_search query: `brand identity system grid glyph` (no matches); fallback query `infographic`
- Template chosen: wrote from scratch (no good match)
- Why this template: The fallback infographic templates provided useful panel-density cues but did not fit a formal identity construction board; a custom system-board prompt was clearer.
- Brief inputs used: Sections 5, 7, 8, 9, 10, 11; brand-tokens cultural motifs and accent discipline.
- Cultural motifs translated: 五大阵地 → five research-front subbrand symbols; 可生成网格 → modular generative grid identity system; 从不可能到普惠 → three-stage path from impossible to public benefit.
- Substitutions made: Replaced optional project colors from the brief with the approved single-accent token system; labeled five fronts in English to reduce Chinese typography errors.
- Style choices: Swiss identity-board layout, construction guides, compact labels, negative cues against AI brain/chip/robot/school crest.
- Final prompt: Professional brand identity system board for Shanghai Innovation Institute / SII, landscape 16:9. Show one main generative grid logic producing six related glyphs: primary SII grid mark plus five research-front subbrand symbols labeled in clean English as “Cognitive AI”, “Context AI”, “Embodied AI”, “Science AI”, and “AI Infrastructure”. Use a modular square grid, rounded nodes, connective cyan signal strokes, and small construction guides. Style anchor: Swiss design principles, minimalist corporate research system, not a colorful sampler. Cultural motifs: AI frontier network of nodes and emergence; creation plus intelligence through abstract S/I/I geometry; West Bund glass laboratory night-grid; three-stage path from impossible to public benefit. Exact palette: #07111F background, #00E0FF single active accent, #E7EBF0 labels and panels, #2B313A grid lines. Typography: compact humanist-geometric sans, precise data labels. Include visible construction lines and spacing rules, no extra colors, no clichéd AI brain, chip, robot, or school crest.
- Image generation outcome: success on first high-quality parallel generation.

- Asset: website-research-hero
- prompt_search query: `website hero technology dashboard` (no matches); fallback query `web UI`
- Template chosen: No. 112 — E-commerce Main Image - Cyberpunk Flash Sale Landing Hero
- Why this template: The content was irrelevant, but its two-column first-view landing-page structure, top navigation, CTA area, and right hero graphic skeleton fit the website hero asset.
- Brief inputs used: Sections 5, 7, 8, 9, 10, 11; Top priority official homepage/research pages.
- Cultural motifs translated: 官网首页与科研成果页 → official homepage and research-page hero; 滨江夜航 → riverfront night laboratory geometry; 前沿信号体系 → active signal paths and moving-frontier highlights.
- Substitutions made: Replaced sale campaign content with SII navigation, research headline, metrics, and three-node public-benefit narrative; replaced neon magenta with only #00E0FF.
- Style choices: Digital-system hero, no browser chrome, exact English text, no people, no stock/circuit-board clichés.
- Final prompt: Create a polished desktop website homepage and research-page hero mockup for Shanghai Innovation Institute / SII, professional brand identity design with research-signal direction. Canvas 16:9, no browser chrome. Dark Deep Space Ink Blue #07111F full-bleed hero, with West Bund Silver #E7EBF0 content cards and Graphite Gray #2B313A structural grid. Use only SII Electric Cyan #00E0FF for active signal paths, nodes, CTA outlines, and moving-frontier highlights. Header: simple abstract SII grid mark at left, navigation labels “Research”, “Projects”, “Talent”, “Open Day”, “Join Us”. Main headline exact text: “AI Frontier Research, Built in Public”. Subtitle: “From impossible to possible to public benefit.” Right side: generative network field over subtle riverfront night laboratory geometry, glass curtain wall perspective, no photos of people. Include three small metric cards: “31 Universities”, “50+ Partners”, “5 Research Fronts”. Typography: rational humanist-geometric sans, bold display and compact captions. No stock templates, no generic circuit board, no extra colors.
- Image generation outcome: success after retry; first high-quality parallel attempt timed out, medium-quality sequential retry succeeded.

- Asset: research-project-card-system
- prompt_search query: `cards system interface dashboard` (no matches); fallback query `social card`
- Template chosen: wrote from scratch (no good match)
- Why this template: The social-card templates were character/trading-card oriented and would have pulled the system away from institutional research UI. A custom UI-card prompt preserved the digital research strategy.
- Brief inputs used: Sections 5, 7, 8, 9, 10, 11; Top priority research results pages and project subbrand system.
- Cultural motifs translated: 项目制攻关 → project-based research cards; 科研成果页 → research results and project pages; 三段路径 → three-node progress path from impossible to value to public benefit.
- Substitutions made: Used six English project examples drawn from the brief’s research/venture ecosystem; used exact token colors and compact metadata typography.
- Style choices: Modular UI identity board, six-card responsive grid, no people/campus imagery/chips/robots/rainbow categories.
- Final prompt: Design a landscape brand-system mockup showing repeatable digital cards for Shanghai Innovation Institute research results and project pages. Use professional UI identity design, Swiss grid, dark research base, and modular project-card system. Show 6 cards arranged in a precise responsive grid on #07111F background, with #E7EBF0 card surfaces, #2B313A dividers, and #00E0FF as the only accent for tags, progress paths, and active nodes. Each card should include a small generative glyph, project title in English, metadata, progress status, and simple diagram: “AI Infra Release”, “Embodied Agent Lab”, “Science AI Model”, “Open-Source Dataset”, “Young PI Project”, “Industry Venture Pilot”. Cultural motifs: AI frontier network, project-based research, generative grid identity, three-node path from impossible to value to public benefit, West Bund night-lab interface. Typography: compact humanist-geometric sans for data labels, bold narrow display for section title “Research Project System”. Avoid people, campus photography, clichéd chips, robot heads, or rainbow category colors.
- Image generation outcome: success on high-quality retry after first parallel attempt timed out.

- Asset: techfest-open-day-key-visual
- prompt_search query: `poster technology event key visual` (no matches); fallback query `poster`
- Template chosen: No. 36 — Infographic / Edu Visual - AI Infrastructure Infographic Poster
- Why this template: The poster template’s dark technical visual language, dense cyan schematics, and technical explainer hierarchy were useful, but the prompt was rewritten as a portrait event key visual rather than an infographic.
- Brief inputs used: Sections 4, 5, 7, 8, 9, 10, 11; Top priority admissions camp/open-day/TechFest touchpoint.
- Cultural motifs translated: 招生营 / 开放日 / TechFest → TechFest and Open Day maker/research event; 科学家创客社区 → scientist-maker community; AI 无人区 → AI frontier.
- Substitutions made: Replaced AI-infrastructure explanatory sections with event copy, maker nodes, abstract workbench silhouettes, and SII research-signal grid.
- Style choices: Campaign energy constrained by research-signal identity; exact English event text; no admissions brochure framing, smiling stock students, robot mascot, or extra accents.
- Final prompt: Create a portrait event key visual poster for Shanghai Innovation Institute / SII TechFest and Open Day. Professional brand identity design with campaign energy inside a research-signal system, not an admissions brochure. Background #07111F with a generative grid tunnel and West Bund riverfront night-laboratory glass geometry. Use #00E0FF as the only active accent for signal beams, maker nodes, and three-stage path; use #E7EBF0 for main typography and #2B313A for structural lines. Exact visible text in English: “SII TechFest / Open Day”, “Calling for Marvellers”, “Build at the AI Frontier”, “Project Camps · Maker Challenges · Research Demos”. Add abstract modular devices, data nodes, and collaborative workbench silhouettes without identifiable people. Typography: bold narrow humanist-geometric display, compact captions, high-contrast Swiss poster layout. Cultural motifs: frontier AI network, scientist-maker community, impossible-to-public-benefit path. No school crest, no smiling student stock photo, no robot mascot, no extra accent colors, no generic university admissions design.
- Image generation outcome: success after retry; first high-quality parallel attempt timed out, medium-quality sequential retry succeeded.

- Asset: talent-recruitment-banner
- prompt_search query: `recruitment banner technology social media` (no matches); fallback query `banner`
- Template chosen: No. 65 — YouTube Thumbnail - Cyberpunk Account Migration Streamer
- Why this template: Its ultra-wide banner/HUD panel structure and nocturnal city interface mood fit a recruitment banner after removing the character focus and cyberpunk excess.
- Brief inputs used: Sections 3, 4, 5, 7, 8, 9, 10, 11; Top priority recruitment/mentor introduction touchpoint.
- Cultural motifs translated: 全球引进青年教师 / 加入我们 → young PI and mentor recruitment; Calling for Marvellers → direct campaign line; 滨江夜航 → West Bund glass lab nightline.
- Substitutions made: Replaced streamer character and multiple dashboards with a disciplined left text block, right abstract research-signal landscape, proof chips, and CTA.
- Style choices: Minimalist corporate research, no portraits/handshake/stock people, single cyan accent, rounded spacing for warmth.
- Final prompt: Design a wide recruitment banner for Shanghai Innovation Institute / SII young PI and mentor recruitment. Style: professional brand identity design, minimalist corporate research, digital-system banner. Dark #07111F base with a disciplined Swiss layout: left side text block, right side abstract research signal landscape of nodes, emergent network, and West Bund glass lab nightline. Use #00E0FF only for CTA, active routes, and luminous node cluster; #E7EBF0 for headline text and card surfaces; #2B313A for grids and secondary labels. Exact visible text: “Join SII as a Young PI”, “Calling for Marvellers”, “Frontier AI · Open Infrastructure · Project-Based Research”, CTA button “Start a Lab”. Include three small proof chips: “Global Talent”, “Industry Partners”, “Compute Platform”. Typography: humanist-geometric sans, bold display with precise compact metadata. Express human warmth through rounded geometry and breathing space, not extra colors. No portraits, no stock photo people, no clichéd handshake, no chip icon, no generic recruitment template.
- Image generation outcome: success on first high-quality parallel generation.

### Decisions & Tradeoffs
Initial high-quality parallel generation caused timeouts for several assets; successful files were kept, and the timed-out assets were retried sequentially at medium quality to complete the approved plan. To protect text quality, most visible copy was rendered in English rather than Chinese; the logo was specified as a pure symbol with no text. The token file’s single-accent discipline overrode the brief’s optional warm gold and project colors, so all assets use cyan as the only active accent.
