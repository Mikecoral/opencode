# Designer Trace

## Phase 1: Asset Planning

### Subject Type & Brief Touchpoints
Subject Type quoted from brief: **organization**.

Relevant Section 11 touchpoints classified:
- Top priority: 官网首页与科研新闻卡片系统; 招生营/夏令营视觉模板; 科研成果发布与开源项目模板; 人才引进/导师招募视觉.
- Optional: 学术讲坛/TechFest/开放日活动系统; 空间导视与实验区玻璃膜.
- Not this round: 周边文创/纪念品.

### Visual Direction Decision
- Selected direction: research-signal
- Alternatives considered: institutional-minimal, campaign-energy, spatial-system
- Why selected: The brief’s Section 5 and Section 7 define the institution through frontiers, signal pulses, scanning grids, coordinates, co-creation networks, compute matrices, and cool high-energy research credibility.
- Generic defaults avoided: education admissions bundle, campus architecture bundle, shield/book/laurel school emblem, consumer AI neon campaign bundle.

### Deliverable Strategy Decision
- Selected strategy: digital-system
- Why selected: Section 11’s Top priority items are recurring digital communications: website homepage/news cards, admissions camp notices, research/open-source releases, and talent recruitment CTAs.
- Why other strategies were rejected or deferred: identity-core alone would under-serve the ranked digital touchpoints; campaign-system would over-amplify admissions/open-day spectacle; spatial-system is explicitly Optional; publishing-system is relevant to research but narrower than the full website/recruitment/admissions digital ecosystem; community-system and merchandise are Not this round.

### Assets Considered
| Asset Idea | Decision | Reason |
|-----------|----------|--------|
| logo-primary | Include | Mandatory; also needed to anchor the SII / signal-to-impact / open-frontier symbol exploration from Section 10. |
| web-homepage-system | Include | Section 11 Top priority; best container for homepage, news, calendar, research, and recruitment modules. |
| research-release-card | Include | Section 11 Top priority; gives recurring科研成果 a credible, consistent release format. |
| open-source-project-template | Include | Section 7 keyword “开源实验” and Section 11 research/open-source template need. |
| admissions-camp-template | Include | Section 11 Top priority; included narrowly as a selection/summer-camp notice, not as a generic admissions suite. |
| talent-recruitment-cta | Include | Section 11 Top priority; supports mentor/faculty recruitment and the co-creation network personality. |
| spatial-wayfinding-signage | Reject | Optional touchpoint; would prematurely shift the run to environmental graphics. |
| merchandise-badge-system | Reject | Not this round in Section 11; would make the set feel like a school merchandise sampler. |
| color-palette-board | Reject | Tokens already document colors; an image asset would not serve a Top-priority touchpoint. |
| campus-architecture-poster | Reject | Optional physical-campus evidence; risks generic campus branding. |

### Why this final 4-8?
The final six assets form a compact digital identity system: one mandatory mark plus five recurring communication surfaces tied to the brief’s Top priority contexts. Omitted defaults such as color-palette, campus, brochure, and merchandise were rejected because they either duplicate tokens, belong to Optional/Not-this-round priorities, or would dilute the research-signal strategy into a generic school identity package.

## Phase 2: Generation

### Per-Asset Prompt Derivation

- Asset: logo-primary
- prompt_search query: `logo minimalist monogram emblem brand mark` returned no matches; broader retry `logo` returned No. 67 — YouTube Thumbnail - VTuber Streaming Overlay Layout, No. 1 — VR Headset Exploded View Poster, No. 4 — E-commerce Live Stream UI Mockup.
- Template chosen: wrote from scratch (no good match)
- Why this template: the library did not contain a suitable pure institutional mark skeleton; available logo matches were incidental UI/logo placements rather than identity design prompts.
- Brief inputs used: Sections 2, 5, 7, 8, 9, 10, 11.
- Cultural motifs translated: 前沿牵引 / Signal → frontier signal pulses and scanning lines; 导师组共创网络 → mentor co-creation node network; AI 基础设施 / 算力矩阵 → AI compute matrix and stacked grid layers; 无人区攻关 → open frontier frame with unfinished boundaries; 徐汇西岸 AI 小镇 → cool glass-and-lab precision.
- Substitutions made: used Deep Compute Blue #071A3A, Signal Cyan #00D4FF, Paper White #F7F9FC, Muted Grey #8A93A3; replaced wordmark text with a pure abstract symbol to avoid garbled typography.
- Style choices: Swiss design principles, minimalist corporate research identity, explicit no-text/no-letters discipline, and negatives for chip/robot/shield/book/laurel/campus clichés.
- Final prompt: Create a professional brand identity design for Shanghai Innovation Institute / SII as a pure abstract symbol. Style anchor: Swiss design principles, minimalist corporate research identity, precise vector geometry. Use an open frontier frame: an unfinished rectangular coordinate boundary in Deep Compute Blue #071A3A, containing a single Signal Cyan #00D4FF pulse point that expands into three thin scanning lines and a compact AI compute matrix of stacked grid layers. The form should suggest frontier signal pulses, mentor co-creation node network, compute infrastructure, and cool glass-lab precision without depicting a chip, robot, shield, book, laurel, or campus building. Center the mark on Paper White #F7F9FC with subtle Muted Grey #8A93A3 construction guides. no text, no letters, pure symbol, no watermark, no generic templates, no stock icons.
- Image generation outcome: success on retry after initial parallel timeout.

- Asset: web-homepage-system
- prompt_search query: `website homepage UI mockup technology dashboard` returned no matches; broader retry `website` returned No. 112 — E-commerce Main Image - Cyberpunk Flash Sale Landing Hero.
- Template chosen: No. 112 — E-commerce Main Image - Cyberpunk Flash Sale Landing Hero
- Why this template: the content was off-brand, but the skeleton of a desktop first-view page with top navigation, hero column, CTA buttons, and right-side graphic structure fit the homepage-system asset.
- Brief inputs used: Sections 1, 2, 5, 7, 8, 9, 10, 11.
- Cultural motifs translated: 前沿信号 → frontier signal pulse and scanning grid; 共创网络 → node network; 算力矩阵 → compute matrix layers; 开放边界 / 无人区 → open frontier frame.
- Substitutions made: replaced cyber sale campaign with institutional homepage; replaced magenta/neon palette with #071A3A, #00D4FF, #F7F9FC, #8A93A3; replaced e-commerce sections with research news, admissions, open-source, calendar, and talent CTA modules.
- Style choices: retained website hero structure but removed neon spectacle; used exact English nav and CTA text for legibility; excluded people and campus photography.
- Final prompt: Professional brand identity website mockup for Shanghai Innovation Institute. 16:9 desktop homepage, no browser chrome, Swiss research-signal UI. Use only Deep Compute Blue #071A3A, Signal Cyan #00D4FF, Paper White #F7F9FC, Muted Grey #8A93A3. Header: abstract SII symbol plus “RESEARCH”, “ADMISSIONS”, “TALENT”, “NEWS”, “ABOUT”. Hero headline “Frontier AI Talent & Research Accelerator”; subline “Signal → Co-create → Open Impact”; buttons “Explore Research” and “Join SII”. Right hero: open frontier frame, scanning grid, signal pulse node, compute matrix layers. Below: modular research news cards, admissions notice tile, open-source release tile, calendar strip, mentor recruitment CTA. Typography: rational modern humanist-geometric sans, precise high-density layout. No people, no campus photo, no shield, no book, no robot, no neon spectacle.
- Image generation outcome: initial high-quality generation timed out; success on retry at medium quality.

- Asset: research-release-card
- prompt_search query: `social media post quote card technology poster` returned no matches; broader retry `poster` returned No. 31 — Social Media Post - Lisbon Vintage Tram Travel Poster, No. 33 — Social Media Post - Anime Streetwear Poster Design, No. 36 — Infographic / Edu Visual - AI Infrastructure Infographic Poster.
- Template chosen: No. 36 — Infographic / Edu Visual - AI Infrastructure Infographic Poster
- Why this template: the technical infographic skeleton provided dense, readable panels, diagrams, metadata, and a research communication rhythm suitable for科研成果发布.
- Brief inputs used: Sections 1, 5, 7, 8, 9, 10, 11.
- Cultural motifs translated: 科研前沿 → frontier problem to verified prototype; 前沿信号 → scanning lines and coordinate points; 算力矩阵 → compute-matrix layers; 开源成果 → open link metadata.
- Substitutions made: replaced AI infrastructure explainer content with SII research release labels and MOSS/robotics/multimodal title; removed violet/orange from template palette.
- Style choices: dense corporate technical poster, portrait card, exact English text for key zones, negatives for robot mascot/chip icon/generic education poster.
- Final prompt: Create a vertical research announcement card template for Shanghai Innovation Institute. Style: professional brand identity design, dense corporate technical poster, Swiss grid hierarchy, cool high-energy but credible. Use Deep Compute Blue #071A3A as the main field, Paper White #F7F9FC panels, Signal Cyan #00D4FF for signal lines and data highlights, Muted Grey #8A93A3 metadata only. Exact visible text: “RESEARCH SIGNAL 024”, “MOSS / ROBOTICS / MULTIMODAL REASONING”, “From frontier problem to verified prototype”, “Shanghai Innovation Institute”. Layout: top-left small SII abstract symbol, large title zone, central open frontier frame with scanning lines, coordinate points, compute-matrix layers, and a simple result graph; bottom metadata rows for Lab, Date, Open Link. Use rational modern sans typography with precise numerals. No stock photo people, no robot mascot, no chip icon, no generic education poster, no extra accent colors.
- Image generation outcome: success in initial parallel generation.

- Asset: open-source-project-template
- prompt_search query: `product marketing launch page dashboard interface` returned no matches; broader retry `dashboard` returned No. 65 — YouTube Thumbnail - Cyberpunk Account Migration Streamer and No. 36 — Infographic / Edu Visual - AI Infrastructure Infographic Poster.
- Template chosen: No. 36 — Infographic / Edu Visual - AI Infrastructure Infographic Poster
- Why this template: No. 36’s panel, flow, and technical-diagram structure was more useful than the anime dashboard result for a credible open-source release surface.
- Brief inputs used: Sections 1, 5, 7, 8, 9, 10, 11.
- Cultural motifs translated: 开源实验 → open-source experiment; 前沿信号 → frontier signal pulses; 导师组共创网络 → dependency/co-creation nodes; 算力矩阵 → technical module grid; 无人区攻关 → open boundary frame.
- Substitutions made: replaced infrastructure education sections with release title, version pill, paper/code CTAs, code panels, benchmark bars, commit timeline, API block, and dependency nodes.
- Style choices: repository-like product-interface rather than public campaign; exact English text for legibility; explicit no GitHub logo or fake brand logos.
- Final prompt: Landscape digital release template for an open-source AI project by Shanghai Innovation Institute. Style: professional brand identity design, minimalist corporate product-interface, Swiss grid, repository-like information architecture. Palette only: Deep Compute Blue #071A3A, Signal Cyan #00D4FF, Paper White #F7F9FC, Muted Grey #8A93A3. Text: “OPEN-SOURCE EXPERIMENT”, “MOSS Lab Release”, “Model · Data · Evaluation · Demo”, “Fork the frontier signal”. Left column: release title, version pill “v0.9”, buttons “Read Paper” and “View Code”. Right: modular code panels, benchmark bars, commit timeline, API endpoint block, dependency nodes. Motifs: frontier signal pulses, mentor co-creation node network, AI compute matrix, open boundary frame, cool glass-lab materiality. No GitHub logo, no fake logos, no people, no rainbow gradients.
- Image generation outcome: initial high-quality generation timed out; success on retry at medium quality.

- Asset: admissions-camp-template
- prompt_search query: `poster announcement event typography technology` returned no matches; broader retry `poster` returned No. 31 — Social Media Post - Lisbon Vintage Tram Travel Poster, No. 33 — Social Media Post - Anime Streetwear Poster Design, No. 36 — Infographic / Edu Visual - AI Infrastructure Infographic Poster.
- Template chosen: No. 36 — Infographic / Edu Visual - AI Infrastructure Infographic Poster
- Why this template: the structured technical poster skeleton was adaptable to a rigorous selection/summer-camp notice while avoiding lifestyle admissions imagery.
- Brief inputs used: Sections 3, 5, 7, 8, 9, 10, 11.
- Cultural motifs translated: 无人区攻关 → challenge the AI frontier; 前沿牵引 → signal node and scanning lines; 导师组 → mentor match timeline; 自主课题/攻关项目 → lab sprint and demo sequence.
- Substitutions made: replaced educational infrastructure content with summer camp headline, challenge language, selection skills, timeline cards, and abstract QR placeholder.
- Style choices: Swiss typographic poster, high-challenge tone, English exact copy to preserve legibility, negatives for students/campus/brochure/orange/confetti.
- Final prompt: Vertical admissions-camp notice template for Shanghai Innovation Institute, not generic student recruitment. Style: professional brand identity design, Swiss typographic poster, research-signal digital system. Palette: Paper White #F7F9FC, Deep Compute Blue #071A3A, Signal Cyan #00D4FF as only accent, Muted Grey #8A93A3 metadata. Text: “SUMMER CAMP 2026”, “Challenge the AI Frontier”, “Logic · Math · Code · Research Prototype”, “Apply Now”, “Shanghai Innovation Institute”. Layout: top open frontier frame with one signal node expanding into scanning lines; central stacked timeline cards: Test, Mentor Match, Lab Sprint, Demo; bottom QR placeholder as abstract square grid. Modern Chinese/Latin sans feeling, widened headline behavior. No students, no campus, no brochure look, no orange accent, no confetti.
- Image generation outcome: initial high-quality generation timed out; success on retry at medium quality.

- Asset: talent-recruitment-cta
- prompt_search query: `banner recruitment CTA technology social media` returned no matches; broader retry `social` returned No. 83 — Comic / Storyboard - Social Media Anime Fashion Lineup, No. 20 — Profile / Avatar - Pastel Zodiac Avatar Grid, No. 21 — Social Media Post - Long Exposure Motion Blur Photography.
- Template chosen: wrote from scratch (no good match)
- Why this template: social prompt matches were character/avatar/photo concepts and would have pushed the asset toward people, lifestyle, or spectacle; the brief needs a mentor network CTA.
- Brief inputs used: Sections 3, 4, 5, 7, 8, 9, 10, 11.
- Cultural motifs translated: 导师组共创网络 → co-creation node network with mentor clusters; 前沿信号 → central frontier signal point; AI 基础设施 / 算力矩阵 → layered compute matrix; 无人区攻关 → open unfinished boundary frame.
- Substitutions made: used recruitment CTA text from the plan and brief priorities; limited palette to one accent and removed people/handshake hiring clichés.
- Style choices: landscape CTA, minimalist corporate research communications, exact English copy, no stock people, no campus, no generic hiring icons.
- Final prompt: Design a landscape talent recruitment CTA visual for Shanghai Innovation Institute. Style anchor: professional brand identity design, minimalist corporate research communications, Swiss grid with a high-signal network field. Palette: Deep Compute Blue #071A3A dark background, Paper White #F7F9FC text panels, Signal Cyan #00D4FF active nodes and lines, Muted Grey #8A93A3 secondary labels; no second accent. Exact visible text: “JOIN THE FRONTIER”, “Mentor Groups · Research Leads · Industry Tutors”, “Build AI systems that move from signal to impact”, “Apply / Connect”. Visual system: a co-creation node network connecting three mentor clusters to a central frontier signal point, layered compute matrix, scanning coordinate grid, open unfinished boundary frame. Typography: rational humanist-geometric sans, bold widened headline, precise caption numerals. No stock photo people, no handshakes, no campus, no generic hiring icons, no neon consumer-AI look.
- Image generation outcome: success in initial parallel generation.

### Decisions & Tradeoffs
Several high-quality image generations timed out, so the website, open-source template, and admissions template were retried at medium quality with tighter prompts while preserving the approved asset plan and brand tokens. I used English-facing text for most surfaces because image generation is more reliable with Latin typography; Chinese identity is carried through the organizational name in the brief, research-signal motifs, and modern Chinese/Latin sans typographic direction rather than attempting fragile Chinese text rendering. The one-accent discipline was maintained: Signal Cyan #00D4FF is the only active accent, and violet/orange were deliberately excluded even for admissions and recruitment.
