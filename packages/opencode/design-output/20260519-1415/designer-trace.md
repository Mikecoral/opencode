# Designer Trace

## Phase 1: Asset Planning

### Subject Type & Brief Touchpoints
Subject Type quoted from brief: **organization**.

Relevant Section 11 touchpoints classified for this run:
- 招生营/夏令营视觉系统 — Top priority — include as a focused mission/checkpoint digital card.
- 科研进展网页与社交卡片模板 — Top priority — include as core research update card template.
- 青年教师/导师招聘视觉 — Top priority — include as recruitment banner around “Calling for Marvellers”.
- 学术报告/创智讲坛海报与PPT模板 — Top priority — include as forum poster plus report/PPT cover system.
- 官网首页 hero 与栏目视觉重构 — Optional — defer until visual primitives are validated.
- 空间导视/实验楼环境图形 — Optional — defer because selected strategy is digital-system, not spatial-system.
- 周边服饰/纪念品 — Not this round — reject because evidence does not support merchandise as a current priority.
- 通用宣传册 — Not this round — reject because it risks generic education collateral.

### Visual Direction Decision
- Selected direction: research-signal
- Alternatives considered: institutional-minimal, campaign-energy, spatial-system
- Why selected: The brief repeatedly emphasizes “前沿信号,” AI Infra, 算力节点, open-source code, model layers, task checkpoints, and mentor/industry networks. These motifs need a signal-and-system visual language more than a solemn institutional seal or high-energy campaign skin.
- Generic defaults avoided: education admissions bundle, campus beauty-shot bundle, shield/book/torch academic identity, generic brochure bundle, merchandise sampler.

### Deliverable Strategy Decision
- Selected strategy: digital-system
- Why selected: Section 11 prioritizes digital and high-frequency communication surfaces: research progress web/social templates, summer camp recruitment, youth faculty recruitment, academic forum posters and PPT/report materials.
- Why other strategies were rejected or deferred: identity-core alone would under-serve the urgent template needs; campaign-system would over-weight admissions and recruitment while neglecting research updates; spatial-system is only Optional; publishing-system is relevant but too narrow because the brief also prioritizes recruitment and summer camp digital surfaces; community-system and product-packaging have no Section 11 support.

### Assets Considered
| Asset Idea | Decision | Reason |
|-----------|----------|--------|
| logo-primary | Include | Mandatory identity anchor, translated into signal/task-stack logic rather than traditional academic marks |
| research-progress-card | Include | Section 11 Top priority; establishes system for AI research updates and social/news surfaces |
| summer-camp-mission-card | Include | Section 11 Top priority; expresses admissions as project battlefield, coding checkpoint and student-led exploration |
| faculty-recruitment-banner | Include | Section 11 Top priority; supports “全球引进青年教师 / Calling for Marvellers” |
| chuangzhi-forum-poster | Include | Section 11 Top priority; supports 创智讲坛, mentor series and student series |
| ppt-report-cover-system | Include | Section 11 Top priority via academic report/PPT need; extends same system to partner-facing and research communication |
| website-hero-system | Reject | Optional; better deferred until identity and content templates establish the visual grammar |
| campus-wayfinding | Reject | Optional and belongs to a spatial-system run, not this digital-system run |
| color-palette | Reject | Tokenized in brand-tokens.md, but not a priority output asset and risks becoming a generic palette board |
| merchandise-hoodie | Reject | Explicitly Not this round in Section 11 |
| admissions-brochure | Reject | Although summer camp is Top priority, brochure format is explicitly generic; a mission card better matches the brief |

### Why this final 4-8?
The final six assets form one coherent research-signal digital kit: identity symbol, research update card, mission-style summer camp recruitment, faculty banner, academic forum poster, and report/PPT cover. Omitted defaults such as color-palette, campus graphics, admissions brochure and merchandise were not generated because they are either Optional/Not this round or would dilute the selected digital-system strategy into an education-industry sampler.

## Phase 2: Generation

### Per-Asset Prompt Derivation

- Asset: logo-primary
- prompt_search query: `logo brand mark signal node technology identity`; fallback query: `emblem crest logo`
- Template chosen: wrote from scratch (no good match)
- Why this template: Search results were either empty or unrelated product/e-commerce prompts; a pure institutional technology mark needed stricter symbol-only control.
- Brief inputs used: Section 5 Cultural & Visual DNA, Section 7 Design Keywords, Section 8 Color Strategy, Section 9 Typography Direction, Section 10 Symbol & Mark Strategy, Section 11 priority context.
- Cultural motifs translated: 算力节点 → compute nodes and GPU-cluster infrastructure; 模型层/流动数据 → layered AI model stack with data-flow routes; 开源代码块 → open-source code block rhythm; 任务卡/checkpoint → mission checkpoint geometry; 导师网络 → multi-node co-creation network.
- Substitutions made: Used token palette exactly: #071A2F, #00D4FF, #F6F8FB, #5C6673; replaced academic crest/book symbolism with three vertical intelligent-engine strokes suggesting SII without letters.
- Style choices: Style anchor was “research-signal institutional technology mark”; included “no text, no letters, pure symbol” to avoid garbled type; negatives reject shield/book/torch/gear/cyberpunk.
- Final prompt: Professional brand identity design for Shanghai Innovation Institute / SII, creating a pure abstract symbol only. Style anchor: research-signal institutional technology mark, restrained academic credibility, modular and precise. Construct the symbol from three vertical intelligent-engine strokes suggesting “SII”, but do not render letters; integrate compute nodes and GPU-cluster infrastructure, layered AI model stack, data-flow routes, open-source code block rhythm, and mission checkpoint geometry. Use exact colors: Deep Intelligence Navy #071A2F as the main mark, Signal Cyan #00D4FF as the only accent on a few node points and connection cuts, Lab White #F6F8FB background, Muted Graphite #5C6673 only for faint construction guides. Typography: none. Text discipline: no text, no letters, pure symbol. Centered square composition, generous whitespace, crisp vector edges, scalable logo geometry. No shield, no book, no torch, no gear, no cyberpunk glow, no stock icons, no generic education template.
- Image generation outcome: initial high-quality parallel generation timed out; retry succeeded at high quality.

- Asset: research-progress-card
- prompt_search query: `social media post research card technology`
- Template chosen: No. 400 — Brand Identity Moodboard System
- Why this template: The template’s card-grid and brand-system structure fit a social/news template better than its original moodboard content; content was rewritten completely for SII research updates.
- Brief inputs used: Section 5 AI Infra/research motifs, Section 7 research-signal keywords, Section 8 color tokens, Section 9 type direction, Section 11 research progress web/social priority.
- Cultural motifs translated: 科研进展 → SII Scientific Research update card; 算力节点 → compute nodes and GPU-cluster infrastructure; 开源模型/代码 → open-source code blocks and training logs; 模型层 → layered AI model stack with data flow.
- Substitutions made: Replaced moodboard cards with one portrait card; inserted exact text “SII SCIENTIFIC RESEARCH”, “Robot Foundation Model Update”, and AI research tags; enforced one accent only.
- Style choices: Used high-density digital editorial style to support frequent research updates; excluded people and robot mascots to avoid stock tech clichés.
- Final prompt: Create a portrait social/news card template for SII Scientific Research. Style anchor: high-density research-signal digital editorial design, like a precise AI lab interface, not a generic school poster. Exact text: “SII SCIENTIFIC RESEARCH”, headline “Robot Foundation Model Update”, tags “AI INFRA / MULTIMODAL / OPEN SOURCE”, metadata “2026.05 · Project Log 014”. Layout: Lab White #F6F8FB card surface with Deep Intelligence Navy #071A2F typography and structural grid, Signal Cyan #00D4FF as the only accent for data nodes, link chips and a thin scanning line, Muted Graphite #5C6673 for captions. Include abstract compute nodes and GPU-cluster infrastructure, layered AI model stack with data flow, open-source code blocks and training logs, small paper/GitHub link placeholders. Typography: rational narrow modern sans for headline, monospaced-inspired captions. No people, no clichéd robot mascot, no purple/orange, no generic templates.
- Image generation outcome: initial high-quality attempts timed out; retried at medium quality and succeeded. This is a known tradeoff for completion; critic should inspect detail quality.

- Asset: summer-camp-mission-card
- prompt_search query: `poster technology event mission card`
- Template chosen: No. 282 — Good Bath Day Editorial Poster
- Why this template: The content was irrelevant, but the structured portrait editorial/event poster skeleton with hierarchy, informational cards and bottom checklist adapted well to a mission/checkpoint recruitment card.
- Brief inputs used: Section 5 project battlefield/training camp, Section 7 project battlefield and student-led keywords, Section 8 tokens, Section 9 typography, Section 11 summer camp priority.
- Cultural motifs translated: 夏令营/编程机考 → summer camp coding-test checkpoint; 逻辑推理与数学基础考试 → logic and math checkpoint; 学生自主项目 → student-led project checkpoint; 导师组 → mentor match checkpoint.
- Substitutions made: Replaced wellness editorial content with “SII SUMMER CAMP 2026” and four mission checkpoints; used route-map/checkpoint visual language instead of brochure sections.
- Style choices: Chose “mission control poster” to keep admissions from becoming generic; negatives reject campus photos, smiling students and brochure look.
- Final prompt: Portrait digital recruitment card for Shanghai Innovation Institute summer camp, reframed as a mission route rather than admissions advertising. Style anchor: research-signal mission control poster, precise, credible, energetic but restrained. Exact text: “SII SUMMER CAMP 2026”, “Define the Problem. Build the Frontier.”, checkpoints “01 Coding Test”, “02 Logic & Math”, “03 Mentor Match”, “04 Student-led Project”. Use exact palette: Deep Intelligence Navy #071A2F background panels, Lab White #F6F8FB content cards, Signal Cyan #00D4FF as the only accent for route lines, active checkpoints, cursor marks, Muted Graphite #5C6673 for metadata. Cultural motifs: mission cards with route maps and checkpoints, open-source code blocks and training logs, compute nodes, layered AI model stack, multi-node mentor-and-industry co-creation network. Typography: narrow modern sans headline, monospaced labels. No campus photos, no smiling student stock photo, no brochure look, no orange or violet.
- Image generation outcome: success at high quality.

- Asset: faculty-recruitment-banner
- prompt_search query: `banner recruitment technology hero`; fallback query: `campaign banner`
- Template chosen: No. 400 — Brand Identity Moodboard System
- Why this template: The original template contains a campaign-banner slot and strong 16:9 brand hierarchy; it was adapted into one landscape recruitment hero.
- Brief inputs used: Section 3 youth faculty/mentor audience, Section 5 mentor network and Shanghai West Bund context, Section 7 mentor network/AI infrastructure keywords, Section 8 tokens, Section 11 faculty recruitment priority.
- Cultural motifs translated: 全球引进青年教师 → Global Young Faculty recruitment; 导师组与跨界网络 → mentor-and-industry co-creation network; 上海徐汇西岸 → Shanghai West Bund label and subtle glass-lab spatial depth.
- Substitutions made: Replaced generic campaign card with exact “CALLING FOR MARVELLERS” message and SII-specific mentor network/compute visual.
- Style choices: Used premium technology campaign banner rather than HR photography; negatives reject handshakes, stock people, graduation caps and job-board templates.
- Final prompt: Landscape recruitment hero banner for Shanghai Innovation Institute youth faculty and mentor recruitment. Style anchor: premium technology campaign banner with academic authority, research-signal visual system, not HR stock imagery. Exact text: “CALLING FOR MARVELLERS”, subline “Join SII to build AI’s new frontier”, side label “Global Young Faculty · Mentor Network · Shanghai West Bund”. Composition: large left-aligned condensed headline, right side an abstract mentor-and-industry co-creation network expanding from a central node into compute clusters and model layers; subtle glass-lab spatial depth without tourism skyline. Colors only: Deep Intelligence Navy #071A2F dominant, Lab White #F6F8FB panels, Signal Cyan #00D4FF as the sole accent for active nodes and call-to-action line, Muted Graphite #5C6673 metadata. Typography: rational narrow modern sans, monospaced small labels. No stock photo people, no handshakes, no clichéd graduation caps, no generic job-board template.
- Image generation outcome: success at high quality.

- Asset: chuangzhi-forum-poster
- prompt_search query: `poster lecture technology conference`; fallback queries: `conference poster`, `technology poster`
- Template chosen: No. 222 — Silicon Valley 2026 Promo Poster
- Why this template: Its flowing technology-map composition translated well into an abstract signal field for an academic forum poster; all city-promotional content was replaced.
- Brief inputs used: Section 5 forum/mentor network/research signals, Section 7 frontier signal keywords, Section 8 tokens, Section 9 type direction, Section 11 academic forum and PPT priority.
- Cultural motifs translated: 创智讲坛 → Chuangzhi Forum; 前沿信号 → flowing signal field; 导师系列/学生系列 → Mentor Series / Student Series; 训练日志/模型层 → training logs and layered model stacks.
- Substitutions made: Used Latin event text for reliability; replaced Silicon Valley landmarks with AI model layers, compute nodes and mentor network.
- Style choices: Technical editorial conference poster with no lecture-hall photo; negatives reject neon cyberpunk and generic conference templates.
- Final prompt: Portrait event poster template for the SII Chuangzhi Forum academic lecture series. Style anchor: technical editorial conference poster, research-signal system, clean high-density information hierarchy. Use Latin text for reliability: “CHUANGZHI FORUM”, “Frontier Signals in AI Systems”, “Speaker Name · Institute / Lab”, “2026.06.18 19:00”, “Mentor Series / Student Series”. Layout: top title block, central abstract flowing signal field that transforms into layered AI model stacks, compute nodes, training logs and a multi-node mentor network; bottom has structured metadata cards and QR placeholder. Exact palette: Lab White #F6F8FB background, Deep Intelligence Navy #071A2F text and grid, Signal Cyan #00D4FF only for signal trace and active lecture tag, Muted Graphite #5C6673 secondary labels. Typography: rational narrow sans plus monospaced captions. No photos of lecture halls, no neon cyberpunk, no violet/orange, no generic conference template.
- Image generation outcome: success at high quality.

- Asset: ppt-report-cover-system
- prompt_search query: `presentation cover report technology`; fallback query: `report cover`
- Template chosen: wrote from scratch (no good match)
- Why this template: Searches returned no usable report-cover template; the planned deliverable required a clear multi-cover deck system rather than an unrelated poster or moodboard.
- Brief inputs used: Section 5 AI Infra/research communication, Section 7 variable system and AI infrastructure keywords, Section 8 tokens, Section 9 typography, Section 11 academic report/PPT priority.
- Cultural motifs translated: 科研报告/PPT → research review and project log covers; 算力基础设施 → AI Infrastructure Project Log; 导师网络 → Mentor Network Briefing; checkpoint → project-review labels.
- Substitutions made: Created three coordinated covers on one 16:9 canvas using exact SII cover titles and footer metadata; applied single accent color only.
- Style choices: Professional partner-facing research report design; excluded photography, campus imagery, stock icons and generic corporate templates.
- Final prompt: Landscape academic report and PPT cover system for Shanghai Innovation Institute, shown as three coordinated cover variations on one 16:9 canvas. Style anchor: professional research report design, modular AI lab interface, credible partner-facing deck. Exact cover text examples: “SII Research Review”, “AI Infrastructure Project Log”, “Mentor Network Briefing”. Layout: three overlapping 16:9 slide covers with consistent title zones, code-log strips, model-layer diagrams, compute-node constellations, and checkpoint labels; include small footer metadata “Shanghai Innovation Institute · 2026”. Use only Deep Intelligence Navy #071A2F, Signal Cyan #00D4FF as the single accent, Lab White #F6F8FB, and Muted Graphite #5C6673. Typography: rational narrow modern sans for titles, monospaced-inspired captions for metrics. Keep crisp vector-like graphic design, no photographs, no campus imagery, no stock icons, no extra accent colors, no generic corporate template.
- Image generation outcome: initial high-quality attempts timed out; retried at medium quality and succeeded. This is a known tradeoff for completion; critic should inspect detail quality.

### Decisions & Tradeoffs
All assets followed the approved research-signal / digital-system plan and used `20260519-1415/<filename>` as the filename parameter. I enforced the one-accent discipline from `brand-tokens.md`, intentionally suppressing the brief’s violet/orange optional colors to avoid anti-slop palette drift. For text-heavy assets I used mostly Latin text because image generation is less reliable with Chinese typography; the Chinese subject is represented through SII naming, Chuangzhi transliteration, and translated cultural motifs. Three high-quality image requests timed out during the first batch; `logo-primary` succeeded on high-quality retry, while `research-progress-card` and `ppt-report-cover-system` required medium-quality retry to complete.

## Phase 2: Fact-Safe Iteration `fact-safe-v1`

### Per-Asset Prompt Derivation

- Asset: logo-primary
- prompt_search query: `logo brand mark technology identity`
- Template chosen: wrote from scratch (No. 400 moodboard result was not suitable for a pure symbol)
- Why this template: Search returned brand-board and mascot-system structures, not a clean mark-only skeleton. I used the critique’s recommendation for a simpler SII/创智-derived mark.
- Brief inputs used: Sections 5, 7, 8, 9, 10; fact-safety rules Allowed Facts and Visual Policy.
- Cultural motifs translated: 导师组 → mentor-network nodes; 项目制/checkpoint → checkpoint cut; AI 基础设施 → abstract infrastructure logic only, no fake dashboard labels.
- Substitutions made: Kept palette tokens #071A2F, #00D4FF, #F6F8FB, #5C6673; reduced nodes to exactly four; removed all text and factual claims.
- Style choices: Pure symbol, flat vector, no letters/text to prevent garbled or invented content; negatives reject seals, shields, books, gears, circuit decoration and cyberpunk glow.
- Final prompt: Professional vector brand identity mark for Shanghai Innovation Institute / 上海创智学院, pure symbol only. Fact-safe research-signal institutional identity: create an ownable abstract mark from three modular vertical strokes suggesting SII rhythm without rendering letters, with subtle negative-space rhythm inspired by the structural balance of 创 and 智. Integrate exactly four active mentor-network nodes and one checkpoint cut to imply student-centered project cultivation, mentor-group collaboration, and AI infrastructure. Use Deep Intelligence Navy #071A2F for the main mark on Lab White #F6F8FB; Signal Cyan #00D4FF only on the four nodes and one thin connection cut; Muted Graphite #5C6673 only for faint construction guides. Flat crisp vector geometry, scalable logo, generous whitespace, academic credibility. No text, no letters, no shield, no book, no gear, no cyberpunk glow, no circuit-board decoration, no fake seal, no stock tech icon.
- Image generation outcome: high-quality parallel attempt timed out; retried at medium quality and succeeded.

- Asset: research-progress-card
- prompt_search query: `social media post research technology card`
- Template chosen: No. 400 — Brand Identity Moodboard System (structure only)
- Why this template: The exact content was irrelevant, but the card-grid / social-asset hierarchy suggested a reusable digital card template.
- Brief inputs used: Sections 5, 7, 8, 9, 11; fact-safety rules Placeholder Policy and Disallowed Content.
- Cultural motifs translated: 科研进展 → bilingual research progress card; 算力节点/模型层 → abstract compute-node and layered model-stack diagram; 开源共创 → placeholder link chips only, no URLs.
- Substitutions made: Replaced all prior project names, dates, model names and metrics with `[Research Topic]`, `[Project Update]`, `[Open-source Link Placeholder]`, `[Paper Link Placeholder]`.
- Style choices: Cleaner editorial card rather than dashboard; one diagram, no pseudo microtext, no dates, no results and no model names.
- Final prompt: Portrait reusable social/news card template for 上海创智学院 / Shanghai Innovation Institute / SII, fact-safe research progress communication. Exact visible text only: “科研进展 / SII SCIENTIFIC RESEARCH”, “[Research Topic]”, “[Project Update]”, “[Open-source Link Placeholder]”, “[Paper Link Placeholder]”, “AI Frontier · AI Infrastructure · Mentor Network”. Use Lab White #F6F8FB background, Deep Intelligence Navy #071A2F typography and grid, Signal Cyan #00D4FF as the only accent for one active signal path and a few nodes, Muted Graphite #5C6673 for editable placeholder labels. Layout: large bilingual title, one clean abstract diagram of compute nodes and layered AI model stack, three editable metadata chips, no results, no numbers, no metrics. Typography: rational narrow modern sans plus restrained monospaced placeholder labels. More whitespace, cleaner than a dashboard. No model names, no dates, no fake data, no URL, no QR code, no pseudo-readable microtext, no sci-fi glow.
- Image generation outcome: high-quality parallel attempt timed out; retried at medium quality and succeeded.

- Asset: summer-camp-mission-card
- prompt_search query: `poster technology event recruitment card`
- Template chosen: No. 282 — Good Bath Day Editorial Poster (layout skeleton only)
- Why this template: Its portrait editorial/event structure with information cards translated into a mission/checkpoint card after replacing all content.
- Brief inputs used: Sections 3, 5, 7, 8, 9, 11; fact-safety rules Allowed Facts and Placeholder Policy.
- Cultural motifs translated: 招生营/夏令营 → SII Summer Camp; 编程/数学基础考试 → Coding and Math checkpoints; 导师组 → Mentor Group; 学生自主课题 → Student-led Project.
- Substitutions made: Removed the prior “2026” date-like framing; used `[Application Window]` and `[Assessment Details]` placeholders; included verified Shanghai Xuhui West Bund / 北杨 AI town context.
- Style choices: Mission card route with four verified-context checkpoint labels; no numbers beyond structural checkpoints, no QR, no pseudo-code and no admissions brochure imagery.
- Final prompt: Portrait digital recruitment template for 上海创智学院 / Shanghai Innovation Institute / SII 招生营 / 夏令营, fact-safe and editable. Exact visible text: “招生营 / SII SUMMER CAMP”, “Project-based AI Talent Cultivation”, “[Application Window]”, “[Assessment Details]”, “Coding”, “Math”, “Mentor Group”, “Student-led Project”, “Shanghai Xuhui West Bund / 北杨人工智能小镇”. Composition: mission card route with four large checkpoint modules, abstract compute-node path, and clean bilingual institution footer. Use Deep Intelligence Navy #071A2F panels, Lab White #F6F8FB cards, Signal Cyan #00D4FF only for active route line and checkpoint dots, Muted Graphite #5C6673 captions. Rational narrow modern sans; placeholders must look editable and bracketed. No invented dates, no enrollment numbers, no statistics, no campus photo, no smiling students, no fake QR, no pseudo-code, no brochure clutter, no orange, no violet, no neon sci-fi.
- Image generation outcome: high-quality parallel attempt timed out; retried at medium quality and succeeded.

- Asset: faculty-recruitment-banner
- prompt_search query: `banner recruitment technology hero`; fallback query: `campaign banner`
- Template chosen: No. 400 — Brand Identity Moodboard System (campaign-banner skeleton only)
- Why this template: The first query had no result; the fallback included a campaign banner slot and broad 16:9 hierarchy that could be rewritten into a recruitment hero.
- Brief inputs used: Sections 3, 5, 7, 8, 9, 11; fact-safety rules Allowed Facts and Disallowed Content.
- Cultural motifs translated: 全球引进青年教师 → bilingual youth faculty recruitment; 导师组培养 → Mentor-Group Cultivation; 产学研联合 → Industry-Research Collaboration; 徐汇西岸/北杨 → place label, not tourism skyline.
- Substitutions made: Kept verified “CALLING FOR MARVELLERS”; removed salary, title, dates, partner names, fake metrics, URL and QR possibilities.
- Style choices: Three-zone verified-phrase diagram, cleaner than the original sci-fi network; no people, handshakes, job-board stock imagery or dashboard labels.
- Final prompt: Landscape recruitment hero banner for 上海创智学院 / Shanghai Innovation Institute / SII youth faculty and mentor recruitment. Fact-safe premium academic technology campaign, restrained research-signal system. Exact visible text: “CALLING FOR MARVELLERS”, “全球引进青年教师”, “Build AI’s new frontier with SII”, “Mentor-Group Cultivation”, “AI Infrastructure”, “Industry-Research Collaboration”, “Shanghai Xuhui West Bund / 北杨人工智能小镇”. Composition: left 55% large bilingual editorial headline and SII identity, right 45% clean three-zone abstract diagram labeled only with the verified phrases above, connected by one cyan signal path; subtle glass-lab geometry, not skyline tourism. Palette only Deep Intelligence Navy #071A2F, Lab White #F6F8FB, Signal Cyan #00D4FF, Muted Graphite #5C6673. No invented job title, dates, salary, partner names, URLs, QR codes, fake metrics, people, handshake, graduation cap, dense dashboard labels, neon sci-fi.
- Image generation outcome: succeeded at medium quality.

- Asset: chuangzhi-forum-poster
- prompt_search query: `poster lecture technology conference`; fallback queries: `conference poster`, `technology poster`
- Template chosen: No. 222 — Silicon Valley 2026 Promo Poster (flowing signal skeleton only)
- Why this template: The first two queries failed; the technology poster’s flowing-map structure could be simplified into one central signal diagram without borrowing any invented city/event content.
- Brief inputs used: Sections 5, 7, 8, 9, 11; fact-safety rules Placeholder Policy.
- Cultural motifs translated: 创智讲坛 → Chuangzhi Forum; 导师系列/学生系列 → placeholder series field; 前沿信号 → restrained frontier-signal diagram.
- Substitutions made: Replaced invented speaker/date/venue with `[Speaker Name]`, `[Date]`, `[Venue]`, `[Research Topic]`, `[QR Placeholder]`.
- Style choices: Explicit placeholder policy, no real date, no fake venue, no QR code, no pseudo microtext; cleaner academic editorial hierarchy.
- Final prompt: Portrait academic lecture poster template for 上海创智学院 / SII 创智讲坛, fact-safe editable system. Exact visible text: “创智讲坛 / CHUANGZHI FORUM”, “[Research Topic]”, “Speaker: [Speaker Name]”, “Date: [Date]”, “Venue: [Venue]”, “Series: [Mentor Series / Student Series]”, “[QR Placeholder]”, “Shanghai Innovation Institute”. Layout: large bilingual top title block, one central restrained frontier-signal diagram showing abstract model layer to compute node to mentor network, bottom metadata cards for speaker, date, venue and QR placeholder. Use Lab White #F6F8FB background, Deep Intelligence Navy #071A2F type/grid, Signal Cyan #00D4FF only for one active signal path and title accent, Muted Graphite #5C6673 captions. Make placeholders obvious and bracketed. No fake speaker, no real date, no fake venue, no QR code, no pseudo-readable microtext, no extra dashboard panels, no neon glow, no stock conference imagery.
- Image generation outcome: succeeded at medium quality.

- Asset: ppt-report-cover-system
- prompt_search query: `presentation cover report technology`; fallback query: `presentation`
- Template chosen: wrote from scratch after No. 103 was not suitable
- Why this template: Search results described product presentation sheets rather than academic report/PPT covers, so I authored a simple three-cover system from the approved asset plan and fact-safety rules.
- Brief inputs used: Sections 5, 7, 8, 9, 11; fact-safety rules Allowed Facts, Placeholder Policy and Visual Policy.
- Cultural motifs translated: PPT/报告传播 → PPT / REPORT TEMPLATE; 科研进展/项目复盘 → `[Research Topic]`, `[Project Review]`; 导师网络 → `[Mentor Network Briefing]`.
- Substitutions made: Removed “2026,” project log numbering, metrics and code strips; used bracketed editable cover titles and verified institutional/theme text only.
- Style choices: Three clean cover mockups with large placeholder zones; no fake dashboard labels, no pseudo-code, no URLs, no QR, no partner logos and no sci-fi glow.
- Final prompt: Landscape academic PPT/report cover system for 上海创智学院 / Shanghai Innovation Institute / SII, shown as three clean 16:9 cover variations on one canvas. Fact-safe, reusable, no fake data. Exact visible text across covers: “上海创智学院 / Shanghai Innovation Institute”, “PPT / REPORT TEMPLATE”, “[Research Topic]”, “[Project Review]”, “[Mentor Network Briefing]”, “AI Frontier”, “AI Infrastructure”, “Student-centered Learning”, “Industry-Research Collaboration”. Layout: three overlapping cover mockups with consistent bilingual identity header, large editable placeholder title zones, one simple abstract signal diagram per cover, and ample whitespace. Use Deep Intelligence Navy #071A2F, Lab White #F6F8FB, Signal Cyan #00D4FF single accent, Muted Graphite #5C6673. Typography: rational narrow modern sans, restrained monospaced placeholders. No dates, no metrics, no rankings, no partner logos, no URLs, no QR codes, no pseudo-code, no fake dashboard labels, no photos, no sci-fi glow.
- Image generation outcome: succeeded at medium quality.

### Decisions & Tradeoffs
The user explicitly asked to reduce hallucination and make the design fact-safe. I therefore removed all previous invented dates, project log numbers, example topic names, model names, fake metrics and pseudo UI labels, even when that made the layouts more template-like. I increased bilingual SII/上海创智学院 presence and used bracket placeholders for mutable content. Because the first three high-quality requests timed out, all final fact-safe iteration assets were generated at medium quality; the critic should still check text fidelity, especially Chinese typography and bracket placeholders.

## Phase 2: Crowd Retest Iteration `crowd-retest-v1`

### Per-Asset Prompt Derivation

- Asset: logo-primary-v2
- prompt_search query: `logo brand mark`
- Template chosen: wrote from scratch; No. 400 was a moodboard, not a pure mark skeleton.
- Why this template: Retest asked for a more ownable SII / 创智 rhythm with no text, four mentor-network nodes and one checkpoint cut; no library result matched that mark-only requirement.
- Brief inputs used: Sections 5, 7, 8, 10 plus crowd retest actions.
- Cultural motifs translated: 导师网络 → four mentor-network nodes; checkpoint → one cut; SII / 创智 → modular vertical rhythm and negative-space structure.
- Final prompt: Professional vector brand identity mark for Shanghai Innovation Institute / 上海创智学院, pure symbol only, no text. Style: ownable research-signal institutional logo, crisp flat geometry, academic technology credibility. Build the symbol from three modular vertical strokes suggesting SII rhythm without rendering letters, with negative-space structure subtly inspired by 创 / 智. Integrate exactly four mentor-network nodes around the strokes and one clear checkpoint cut through the lower-right module; reduce all circuit detail to a single disciplined cyan connection. Colors only: Deep Intelligence Navy #071A2F main mark on Lab White #F6F8FB, Signal Cyan #00D4FF only for the four nodes and checkpoint cut, Muted Graphite #5C6673 only as faint construction guides. Centered square composition, generous whitespace, scalable vector edges. No words, no letters, no shield, no book, no gear, no circuit-board decoration, no cyberpunk glow, no stock tech icon.
- Image generation outcome: high-quality attempt timed out; medium-quality retry succeeded.

- Asset: research-progress-card-v2
- prompt_search query: `technical infographic research card`; fallback `infographic poster`
- Template chosen: No. 308 — Samsung Galaxy S25 Infographic Poster, structure only.
- Why this template: The readable callout structure around one centerpiece was useful; consumer gloss, neon and feature clutter were removed.
- Brief inputs used: Sections 5, 7, 8, 9, 11 plus crowd retest request for a plain-language impact line.
- Cultural motifs translated: 科研进展 → bilingual research card; AI Infra / robotics → layered model stack and real-world capability endpoint.
- Final prompt: Portrait social/news card for 上海创智学院 / Shanghai Innovation Institute / SII research progress, designed for technical credibility with about one-third less microtext than the previous dense dashboard style. Style: precise research-signal editorial card with one hero diagram, not a generic AI dashboard. Exact legible text: “科研进展 / SII SCIENTIFIC RESEARCH”, “[Research Topic]”, “From model infrastructure to real-world robotic capability”, “AI Infrastructure · Robotics · Open Source”, “[Paper / Code Link]”. Composition: Lab White #F6F8FB surface, Deep Intelligence Navy #071A2F title and grid, Signal Cyan #00D4FF as the only accent for one signal path through layered AI model stack, compute nodes, and robot-capability endpoint; Muted Graphite #5C6673 captions. Typography: rational narrow modern sans, restrained monospaced labels. Include bilingual institution cue in header. Make all text readable. No fake metrics, no excessive pseudo-data, no stock robot icon, no neon cyberpunk, no violet or orange.
- Image generation outcome: high-quality attempt timed out; medium-quality retry succeeded.

- Asset: summer-camp-mission-card-v2
- prompt_search query: `mission route poster recruitment`; fallback `promo poster technology`
- Template chosen: No. 369 — Anime Music Bootcamp Promo Poster, structure only for bootcamp announcement modules; style rejected.
- Why this template: Its event/bootcamp announcement hierarchy suggested clear applicant modules, but anime/neon content was fully replaced.
- Brief inputs used: Sections 3, 5, 7, 8, 9, 11 plus retest Who / How / Key date modules.
- Cultural motifs translated: 夏令营 → SII Summer Camp; 编程/逻辑数学 → checkpoints; 学生主导/导师组 → project and mentor modules.
- Final prompt: Portrait digital recruitment card for 上海创智学院 / Shanghai Innovation Institute / SII 招生营 / Summer Camp, exciting but not intimidating. Style: research-signal mission route with clear applicant information, not a generic admissions brochure. Exact legible text: “招生营 / SII SUMMER CAMP”, “Project-based AI Talent Cultivation”, “Who should apply: AI / robotics / systems / math students ready for project-based research”, “How to apply: sii.edu.cn/zsgz”, “Key date: Deadline YYYY.MM.DD”, “Coding · Logic & Math · Mentor Group · Student-led Project”. Composition: a clean route map with four large checkpoint modules, one cyan path, and a bilingual SII footer. Colors only: Deep Intelligence Navy #071A2F panels, Lab White #F6F8FB cards, Signal Cyan #00D4FF accent, Muted Graphite #5C6673 captions. Typography: rational narrow modern sans, readable labels, fewer micro-details. No campus photos, no smiling stock students, no brochure clutter, no fake numbers, no QR code, no neon, no extra accent colors.
- Image generation outcome: high-quality succeeded.

- Asset: faculty-recruitment-banner-v2
- prompt_search query: `technology recruitment banner`; fallback `promo poster technology`
- Template chosen: No. 222 — Silicon Valley 2026 Promo Poster, structure only for restrained innovation ribbon/place cue.
- Why this template: The flowing innovation/place structure was useful for West Bund context; tourism collage and generic city landmarks were explicitly excluded.
- Brief inputs used: Sections 3, 5, 7, 8, 9, 11 plus retest priority action for roles/resources/benefits.
- Cultural motifs translated: “Calling for Marvellers” → frontier researchers; 徐汇西岸/北杨 → subtle West Bund coordinate cue; 导师组/算力 → modules.
- Final prompt: Landscape recruitment hero banner for 上海创智学院 / Shanghai Innovation Institute / SII, priority public-facing asset. Style: premium academic technology campaign in a restrained research-signal system, with decision-useful recruitment information. Exact legible text: “CALLING FOR MARVELLERS”, “For researchers who turn frontier questions into real AI capability”, “全球引进青年教师”, “Frontier Problems”, “Mentor Groups”, “Compute Resources”, “Shanghai West Bund”, “Apply / Learn More: join SII”. Composition: left 55% large editorial headline and explanatory subline; right 45% clean four-module proposition diagram connected by one Signal Cyan path, with subtle abstract glass-lab / West Bund coordinate cue, not a tourism skyline. Palette only Deep Intelligence Navy #071A2F, Lab White #F6F8FB, Signal Cyan #00D4FF, Muted Graphite #5C6673. Typography: rational narrow modern sans, all labels readable. No people, handshakes, graduation caps, salary claims, fake partner logos, dense dashboard panels, neon cyberpunk, orange or violet.
- Image generation outcome: high-quality succeeded.

- Asset: chuangzhi-forum-poster-v2
- prompt_search query: `typography poster lecture event`
- Template chosen: No. 320 — Bangkok Swiss Typography Poster, structure only.
- Why this template: Strong typography and negative-space discipline helped reinforce bilingual event hierarchy without filler microtext.
- Brief inputs used: Sections 5, 7, 8, 9, 11 and retest request for readable speaker/topic/time/venue metadata.
- Cultural motifs translated: 创智讲坛 → bilingual title; 前沿信号/导师网络 → central signal diagram and metadata system.
- Final prompt: Portrait academic event poster for 上海创智学院 / SII, retaining strong event hierarchy with less filler microtext. Style: professional technical editorial poster, research-signal visual language, bilingual by default. Exact legible text: “创智讲坛 / CHUANGZHI FORUM”, “Frontier Signals in AI Systems”, “Speaker: [Speaker Name]”, “Topic: [Research Topic]”, “Time: YYYY.MM.DD 19:00”, “Venue: Shanghai Innovation Institute”, “Series: Mentor Series / Student Series”. Layout: large bilingual top title, one central restrained frontier-signal diagram showing model layer to compute node to mentor network, bottom metadata cards for speaker, topic, time, venue. Use Lab White #F6F8FB background, Deep Intelligence Navy #071A2F type/grid, Signal Cyan #00D4FF only for one active signal path and title accent, Muted Graphite #5C6673 captions. Make all text readable. No fake real names, no QR code, no pseudo-readable microtext, no lecture hall photo, no neon, no stock icons, no extra colors.
- Image generation outcome: high-quality succeeded.

- Asset: ppt-report-cover-system-v2
- prompt_search query: `presentation report cover system`; fallback `dashboard UI`
- Template chosen: wrote from scratch; dashboard templates were too dense for the retest guidance.
- Why this template: Retest specifically asked for three coordinated covers with one simplified public/partner variant, so a custom prompt best preserved hierarchy and reduced dashboard noise.
- Brief inputs used: Sections 5, 7, 8, 9, 11 and retest plain-language subtitle module.
- Cultural motifs translated: 学术报告/PPT → coordinated report cover system; public-facing communication → simplified variant with plain-language subtitle.
- Final prompt: Landscape 16:9 canvas showing three coordinated PPT/report cover variations for 上海创智学院 / Shanghai Innovation Institute / SII. Style: professional research-signal cover system, clean enough for partners and public stakeholders, not a generic AI dashboard. Exact legible text across covers: “上海创智学院 / Shanghai Innovation Institute”, “Research Review”, “AI Infrastructure Project Log”, “Partner Briefing”, and on the simplified public-facing variant: “What changed, why it matters, what comes next”. Composition: three overlapping slide covers with consistent bilingual identity header, large title zones, one simple signal diagram per cover; the third cover is plainer with more whitespace and the plain-language subtitle. Colors only: Deep Intelligence Navy #071A2F, Lab White #F6F8FB, Signal Cyan #00D4FF as single accent, Muted Graphite #5C6673. Typography: rational narrow modern sans with restrained monospaced captions, all text readable. No dates, metrics, pseudo-code, QR codes, partner logos, photos, neon, violet or orange.
- Image generation outcome: high-quality attempt timed out; medium-quality retry succeeded.

### Decisions & Tradeoffs
This iteration preserved the approved `research-signal` / `digital-system` logic while responding to the crowd retest: bilingual SII identity is more visible, recruitment and summer camp contain direct decision modules, and decorative microtext/dashboard noise is reduced. Palette discipline stayed navy / lab white / signal cyan / graphite only. Three high-quality requests timed out, so logo-primary-v2, research-progress-card-v2 and ppt-report-cover-system-v2 were completed at medium quality; the critic should inspect text fidelity and Chinese typography in those files.
