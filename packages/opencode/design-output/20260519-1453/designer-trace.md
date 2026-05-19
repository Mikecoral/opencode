# Designer Trace

## Phase 1: Asset Planning

### Subject Type & Brief Touchpoints
Subject Type from brief: **organization**.

Relevant Section 11 touchpoints:
- 科研成果发布模板（网页 hero、新闻封面、论文/项目图卡） — Top priority — “品牌第一战场是‘把复杂 AI 成果讲清楚’。”
- 招生营 / 训练营视觉系统 — Top priority — “春季营、夏令营、金秋营、冬令营贯穿全年。”
- TechFest / 创智未来大会活动系统 — Top priority — “活动视觉是对外认知放大的关键。”
- 官网与社媒的动态视觉语言 — Top priority — “官网是招生、科研、招聘、产业合作的统一入口。”
- 空间导视与实验室环境图形 — Optional — “首轮可先做关键区域。”
- 开源项目 / GitHub 视觉徽章 — Optional — “需结合具体项目推进。”
- 纪念品 / 周边 — Not this round — “周边不应先行。”

### Visual Direction Decision
- Selected direction: `research-signal`
- Alternatives considered: `institutional-minimal`, `campaign-energy`, `spatial-system`
- Why selected: Brief Section 4 says the visual language should be “雷达、信号流、动态坐标，而不是静态盾牌.” Section 5 repeatedly specifies “网格、节点、机柜光带、数据流、终端窗口、命令行式排版” and “扫描线、雷达圆弧、动态坐标、方向簇、信号峰值.”
- Generic defaults avoided: ordinary higher-education admissions bundle, campus photography/wayfinding bundle, conservative institutional crest bundle.

### Deliverable Strategy Decision
- Selected strategy: `digital-system`
- Why selected: Section 11 ranks research release templates and website/social dynamic visual language as Top priority; these are high-frequency surfaces that can also support training camps and TechFest without fragmenting the system.
- Why other strategies were rejected or deferred: `identity-core` alone would under-serve the Top priority digital templates; `campaign-system` would over-index on招生营/TechFest and risk separate event looks; `spatial-system` is Optional; `community-system` and merchandise are explicitly Not this round.

### Assets Considered
| Asset Idea | Decision | Reason |
|-----------|----------|--------|
| logo-primary | Include | Mandatory; Section 10 supports an SII / 创智 letter-grid mark. |
| signal-glyph-system | Include | Needed to turn the parameter grid into a reusable digital identity language. |
| research-release-hero | Include | Section 11 Top priority; directly serves research communication. |
| research-project-card-template | Include | Section 11 Top priority; supports papers, model/project updates, and social cards. |
| website-homepage-system | Include | Section 11 Top priority; official site is the unified entrance. |
| training-camp-signal-card | Include | Section 11 Top priority, but constrained to one digital card to avoid a generic admissions suite. |
| techfest-key-visual | Include | Section 11 Top priority; one key visual extends the same system to public events. |
| color-palette | Reject | Tokens only; not a generated asset and not a default per hard rules. |
| campus-wayfinding-system | Reject | Optional and outside the selected digital-system strategy. |
| open-source-github-badges | Reject | Optional and needs project-specific inputs; future extension. |
| merchandise-badge-set | Reject | Section 11 says Not this round. |
| institutional-crest | Reject | Contradicts brief’s “不是静态盾牌” and “非院章式单一权威符号” direction. |
| admissions-brochure-cover | Reject | Recruitment is Top priority, but brochure format is a generic school default; use modular digital signal card instead. |

### Why this final 4-8?
The final seven assets form a single digital identity and communications system: logo → glyph logic → research hero/card → website/banner → training camp and TechFest extensions. Omitted defaults such as color palette, campus signage, admissions brochure, and merchandise were not generated because they either are tokens rather than images, Optional, Not this round, or would pull the identity back toward generic institutional-school output.

## Phase 2: Generation

### Per-Asset Prompt Derivation

- Asset: logo-primary
- prompt_search query: `logo brand mark grid`
- Template chosen: wrote from scratch (No. 400 was a broad moodboard, not a pure mark construction template)
- Why this template: The prompt library results had useful brand-system language but no precise grid monogram skeleton, so the prompt was written around Section 10's SII grid-mark strategy.
- Brief inputs used: Sections 1, 2, 4, 5, 7, 8, 9, 10.
- Cultural motifs translated: 参数化网格 → parametric grid; 雷达圆弧 → radar scan arc; 从0到1路径 → point-to-system path.
- Substitutions made: brand name set to “SII / Shanghai Innovation Institute”; colors set to #080A0F, #00E5FF, #F7FAFC, #D6DEE8; typography set to narrow engineering sans.
- Style choices: Flat vector primary identity mark; explicit negatives against crest, shield, laurel, mascot, graduation icons, and stock people.
- Final prompt: Professional brand identity design for Shanghai Innovation Institute, abbreviated “SII”. Square primary logo on Infrastructure Black #080A0F. Abstract S-I-I monogram built from a visible 9×9 parametric grid of square modules, nodes, and short signal-line segments. Include one restrained radar scan arc and one point-to-system path curve in Signal Cyan #00E5FF, with Proof White #F7FAFC negative space and Mist Gray #D6DEE8 construction lines. Compact wordmark below: “SII” and small “Shanghai Innovation Institute” in narrow engineering sans typography. AI research infrastructure, frontier signal detection, open lab system. Flat vector, sharp, scalable, high contrast; no university crest, no shield, no laurel, no mascot, no stock photo people, no graduation icons, no generic template.
- Image generation outcome: success after retry; initial high-quality call timed out, medium-quality retry saved successfully.

- Asset: signal-glyph-system
- prompt_search query: `brand identity system glyph grid`
- Template chosen: No. 400 — Brand Identity Moodboard System
- Why this template: The 16:9 multi-card identity specimen structure was useful, but content was narrowed from moodboard sampling to a strict glyph-generation board.
- Brief inputs used: Sections 5, 7, 8, 9, 10, 11.
- Cultural motifs translated: 研究阵地与活动 glyph → derivative research and event glyphs; 机柜光带 → compute-rack light strip; 终端窗口 → terminal window.
- Substitutions made: replaced broad cards with SII monogram, radar, signal peak, node cluster, terminal, rack-light, and path glyphs; enforced token colors.
- Style choices: System specimen, no photography, no palette asset, no second accent.
- Final prompt: Create a 16:9 brand identity glyph system board for Shanghai Innovation Institute. Use a flat Behance-style system specimen, not a color palette. Background Infrastructure Black #080A0F with card surfaces in Proof White #F7FAFC and Mist Gray #D6DEE8 rules. Show a 9×9 parametric grid generating the primary “SII” monogram plus six derivative research and event glyphs: radar arc, signal peak, node cluster, terminal window, compute-rack light strip, and point-to-system path. Each glyph must visibly share the same module size, corner radius, and line weight. Use Signal Cyan #00E5FF only for active nodes, scan lines, and selected modules. Include small mono labels such as “GRID 09”, “SIGNAL”, “PROJECT PATH”, “RELEASE”, “TECHFEST”. Typography is narrow modern sans with command-line precision. No photos, no campus imagery, no merchandise, no shields, no extra accent colors.
- Image generation outcome: success on high quality.

- Asset: research-release-hero
- prompt_search query: `website hero technology data visualization`, then `landing page AI data`
- Template chosen: No. 3 — Dark Mode Marketing Case Study UI
- Why this template: Its landing-page hero plus metric-card structure fit the research-release hero, but viral-campaign content was replaced with research communication.
- Brief inputs used: Sections 4, 5, 7, 8, 9, 11.
- Cultural motifs translated: 前沿信号体系 → frontier signal system; 动态坐标 → dynamic coordinate axes; 数据流 → flowing data streams.
- Substitutions made: hero headline set to “AI FRONTIER SIGNALS”; visual content replaced by radar, coordinates, signal peaks, nodes, compute-rack strips, and data streams.
- Style choices: Dense but controlled research UI; negative cues against stock people, rainbow neon, and generic SaaS.
- Final prompt: Design a landscape website hero / news cover template for Shanghai Innovation Institute research releases. Dark digital-system UI on Infrastructure Black #080A0F, with a large left headline area reading “AI FRONTIER SIGNALS” and smaller label “Research Release / Shanghai Innovation Institute”. On the right, build an abstract data visualization from grounded motifs: radar scan arcs, dynamic coordinate axes, signal peaks, node networks, compute-rack light strips, and flowing data streams. Use Signal Cyan #00E5FF as the only luminous accent, with Proof White #F7FAFC text and Mist Gray #D6DEE8 grid scaffolds. Add three compact research metric cards and a terminal-style metadata strip, but keep text minimal and legible. Typography: narrow engineering sans for display, humanist sans for body, mono captions for IDs. Refined AI research infrastructure, credible, high-density but controlled. No stock photo people, no neon rainbow, no generic SaaS hero clichés.
- Image generation outcome: success after retry; initial parallel high-quality call timed out, medium-quality retry saved successfully.

- Asset: research-project-card-template
- prompt_search query: `social media post card technology`
- Template chosen: No. 383 — BMW Performance Social Poster
- Why this template: The vertical premium poster/card structure translated well to a project-release card once automotive content was removed.
- Brief inputs used: Sections 5, 7, 8, 9, 10, 11.
- Cultural motifs translated: 一生一策 / 项目制成长路径 → individual project path curve; 从0到1 → From 0 to 1; 真实系统 → Real System.
- Substitutions made: replaced car subject with path curve, node grid, radar arcs, terminal panels, and compute-rack strip; set restrained SII text labels.
- Style choices: Editorial technology card, not an admissions brochure; no AI brain icons.
- Final prompt: Create a vertical 4:5 social/news project card template for Shanghai Innovation Institute, suitable for paper, model, or prototype announcements. Premium editorial technology poster layout. Background Infrastructure Black #080A0F with a thin Mist Gray #D6DEE8 modular grid. Top label: “SII / PROJECT CARD”. Main headline: “FROM 0 TO 1” in narrow bold engineering sans, large and compressed. Center visual: an individual project path curve traveling from a single point through nodes into a stable system grid, overlaid with radar scan arcs and signal peaks in Signal Cyan #00E5FF. Include two small terminal-window panels and one abstract compute-rack light strip, all flat vector. Bottom metadata blocks read “REAL SYSTEM”, “OPEN RESEARCH”, “FRONTIER SIGNAL”. Use Proof White #F7FAFC for text, no second accent color, no photos, no people, no campus, no brochure style, no clichéd AI brain icons.
- Image generation outcome: success after retry; initial parallel high-quality call timed out, medium-quality retry saved successfully.

- Asset: website-homepage-system
- prompt_search query: `web UI mockup dashboard technology`
- Template chosen: No. 143 — hyper-realistic UI/UX mockup displayed on a laptop (structure only)
- Why this template: It provided a UI mockup scaffold, but the final prompt removed laptop/desk photography to preserve the system-board digital direction.
- Brief inputs used: Sections 1, 5, 7, 8, 9, 11.
- Cultural motifs translated: 官网统一入口 → homepage system; 参数化网格、节点、雷达 → parametric grid, node network, radar scan arcs.
- Substitutions made: built three UI surfaces for homepage, news card, and social banner; navigation labels reflect research, talent, TechFest, partners.
- Style choices: Credible research-institute web system; no glassy generic dashboard or campus photography.
- Final prompt: Create a landscape digital brand system mockup showing the Shanghai Innovation Institute homepage and social banner language. Compose three clean UI surfaces on a dark Infrastructure Black #080A0F background: a wide homepage hero, a compact news card, and a social banner crop. The homepage top navigation includes “Research”, “Talent”, “TechFest”, “Partners”. Hero headline: “FRONTIER AI RESEARCH SYSTEM”. Visual language: parametric grid, node network, radar scan arcs, dynamic coordinates, data streams, and terminal metadata strips. Signal Cyan #00E5FF marks active states, CTA outlines, scan sweeps, and signal peaks; Proof White #F7FAFC and Mist Gray #D6DEE8 handle text, surfaces, dividers, and chart scaffolds. Typography is narrow high-readability modern sans with optional mono labels. Credible for a research institute, not a consumer SaaS app. No stock photo people, no glassy generic dashboard, no multicolor gradients, no campus photography.
- Image generation outcome: success after retry; initial parallel high-quality call timed out, medium-quality retry saved successfully.

- Asset: training-camp-signal-card
- prompt_search query: `poster technology event digital`
- Template chosen: No. 222 — Silicon Valley 2026 Promo Poster
- Why this template: Its promotional poster concept suggested a flowing technology narrative, but the final was constrained into a modular training-camp signal card.
- Brief inputs used: Sections 3, 5, 7, 8, 9, 10, 11.
- Cultural motifs translated: 春季营、夏令营、金秋营、冬令营 → spring/summer/autumn/winter modular tabs; 项目制成长路径 → project-based growth path.
- Substitutions made: replaced city promotion imagery with seasonal modules, radar/coordinate motifs, terminal labels, and a point-to-grid path.
- Style choices: High-energy recruitment touchpoint but not a generic admissions suite; negatives reject campus brochure and smiling-student tropes.
- Final prompt: Design a vertical digital campaign card for Shanghai Innovation Institute training camps, using the same research-signal system rather than a generic admissions poster. Background Infrastructure Black #080A0F. Top small text: “SII TRAINING CAMP”. Main headline: “ENTER THE AI FRONTIER”. Subline: “Project-based growth path / Shanghai Innovation Institute”. Center composition: four seasonal modular tabs labeled “SPRING”, “SUMMER”, “AUTUMN”, “WINTER”, connected by a single individual project path curve that begins as one point and becomes a structured node grid. Add radar scan arcs, dynamic coordinates, terminal-window labels, and subtle compute-rack light strips. Use only Signal Cyan #00E5FF for active signals and Proof White #F7FAFC / Mist Gray #D6DEE8 for type and scaffolds. Typography: bold compressed engineering sans, mono data captions. High-energy but disciplined. No campus brochure, no smiling students, no graduation cap, no orange, no generic school admissions look.
- Image generation outcome: success after retry; initial parallel high-quality call timed out, medium-quality retry saved successfully.

- Asset: techfest-key-visual
- prompt_search query: `poster conference technology key visual`
- Template chosen: No. 231 — Cinematic Infographic Concept Poster
- Why this template: Its “single conceptual core” and vertical hierarchy fit a conference key visual, while the final prompt removed unsupported spectacle and kept only brief-grounded research motifs.
- Brief inputs used: Sections 5, 7, 8, 9, 10, 11.
- Cultural motifs translated: 上海滨江 / 玻璃幕墙 → Shanghai riverside / glass-curtain-wall coordinate line; 前沿信号 → frontier signals; 共创 → co-creation.
- Substitutions made: replaced generic cinematic topic with SII TechFest, data-river, 9×9 grid, signal peaks, node clusters, and rack lights.
- Style choices: Restrained event key visual; no people, stage lights, rainbow neon, crest, or conference stock imagery.
- Final prompt: Create a vertical key visual poster for “SII TECHFEST” / “Shanghai Innovation Institute”. Cinematic but restrained AI research event visual, not entertainment festival clutter. Use Infrastructure Black #080A0F as the dominant field. A central luminous Signal Cyan #00E5FF data-river rises from a low horizontal Shanghai riverside / glass-curtain-wall coordinate line into a precise 9×9 parametric grid structure, then resolves into radar scan arcs, signal peaks, and node clusters. Add subtle compute-rack light strips at the base and terminal-style labels around the structure: “FRONTIER SIGNALS”, “REAL SYSTEMS”, “CO-CREATION”. Typography: narrow modern sans, bold title, mono technical captions, Proof White #F7FAFC and Mist Gray #D6DEE8 only. Keep large negative space and strong vertical hierarchy. No people, no stage lights, no rainbow neon, no university crest, no generic conference stock imagery.
- Image generation outcome: success after retry; initial parallel high-quality call timed out, medium-quality retry saved successfully.

### Decisions & Tradeoffs
All prompts used the Phase 1 brand tokens as the source of truth and maintained one accent color, Signal Cyan #00E5FF. I used Latin/English text for critical labels because image generation is less reliable with Chinese typography. Several high-quality generations timed out; to complete the full approved plan, I retried those assets at medium quality. The signal-glyph-system completed at high quality on the first batch.
