# Visual Research — 创智学院

## Source log
- Coursera brand guide: https://www.coursera.org/about/brand-guide/
- Coursera press/about page: https://about.coursera.org/press
- 得到 official site + CSS: https://www.dedao.cn/ ; https://imgcdn.umiwi.com/fe-static/prod/igetWeb/css/igetWeb.aa6ed08e.css
- 极客邦科技 official site + CSS: https://www.geekbang.org/ ; https://static001.geekbang.org/www/css/app.3791261f.css
- 混沌学园 official site: https://www.hundun.cn/
- IBM SkillsBuild: https://skillsbuild.org/
- IBM Design Language + Color: https://www.ibm.com/design/language/ ; https://www.ibm.com/design/language/color
- Duolingo homepage + brand guideline landing: https://www.duolingo.com/ ; https://design.duolingo.com/
- Brilliant homepage: https://www.brilliant.org/
- Pentagram / MIT Media Lab: https://www.pentagram.com/work/mit-media-lab/story
- Pentagram / The New School: https://www.pentagram.com/work/the-new-school/story
- Brand New / MIT Media Lab: https://www.underconsideration.com/brandnew/archives/new_logo_and_identity_for_mit_media_lab_by_pentagram.php
- Brand New / The New School: https://www.underconsideration.com/brandnew/archives/new_logo_and_identity_for_the_new_school_by_pentagram.php
- COLLINS / Dropbox: https://www.wearecollins.com/work/dropbox/
- COLLINS / Mailchimp: https://www.wearecollins.com/work/mailchimp/

## Research Area 1 — Competitor & Category Visual Audit

| Organization | Category relevance | Primary color palette | Logo style | Typography character | Overall visual register | Evidence notes |
|---|---|---|---|---|---|---|
| Coursera | Large-scale online learning, certificates, university/industry partnerships | Official primary palette: Coursera Blue `#0056D2`, Black `#000000`, White `#FFFFFF`. | Wordmark plus a separate “C” symbol; official guide calls the wordmark “distinct, bold” and the “C” a signature graphical element. | Source Sans Pro is the official primary typeface across marketing, web, and product. | Institutional, trustworthy, accessible, corporate-learning oriented. | Brand guide explicitly provides hex values, logo types, clear-space rules, and typeface. Press page positions Coursera around “universal access,” AI learning features, credentials, and 205M learners. |
| 得到 | Chinese lifelong-learning / business-knowledge platform | Extracted CSS common palette: accent orange `#ff6b00`; secondary mint `#59ccb2`; error red `#ff4f4f`; neutrals `#333`, `#666`, `#999`, `#f5f3f1`, `#fff`; additional CTAs include `#ff3c00`, `#0bb861`. | App/platform wordmark/logo asset in header; fetched CSS confirms logo image container rather than text-rendered mark. Exact vector not extracted. | System Chinese sans stack: `-apple-system`, `Helvetica Neue`, Arial, `PingFang SC`, `Hiragino Sans GB`, STHeiti, `Microsoft YaHei`, Source Han / Noto Sans CJK, SimSun. Also includes a display-number font “Bebas Neue.” | Warm, commercial, mobile-product, content-marketplace. | Homepage data references “终身学习平台,” “得到新商学,” courses, books, learning centers; CSS establishes orange as repeated emphasis color. |
| 极客邦科技 / Geekbang | Chinese tech-learning, developer media, enterprise tech community | Extracted CSS: highlight orange `#fa6400`; dark text `#333` / `#404040`; light background `#fff`; hover background `#fbf5ee`; footer dark `#333`; supporting grays `#888`, `#e9e9e9`, `#ccc`. | Header logo image asset; platform likely uses a Chinese/English wordmark lockup, but exact logo geometry not extracted from fetched text. | CSS base stack: `PingFang SC`, Avenir, Tahoma, Arial, Lantinghei SC, Microsoft Yahei, Hiragino Sans GB, Microsoft Sans Serif, WenQuanYi Micro Hei, Helvetica, sans-serif. | Technical, content-platform, pragmatic, developer-oriented. | Official meta description says Geekbang is an IT content service group with InfoQ, StuQ, EGO, training, conferences, consulting, publishing, innovation incubation. |
| 混沌学园 | Chinese innovation/business-model/philosophy learning platform | Fetched source confirms official site but did not expose a stable palette in plain text beyond loading white/gray and error orange `#ff4500`; exact brand colors require visual inspection of rendered assets. | Official favicon and Nuxt-rendered logo assets exist; exact logo style not extracted from fetched source. | Site is Nuxt-based; exact font stack not exposed in fetched HTML. | Innovation + business school + philosophy/cognitive-science positioning; likely more premium/knowledge-community than utilitarian course marketplace. | Metadata: “创新课程 / 商业模式创新课程 / 哲科思维课程,” humanistic + science + business topics, 200+ cases, online/offline practice. Observation flagged as incomplete where visual tokens were not accessible. |
| IBM SkillsBuild | Adjacent: professional tech upskilling, AI/job-skills credentials | IBM Design Language official color: core Blue 60 `#0f62fe`, black `#000000`, white `#ffffff`, grays `#161616` through `#f4f4f4`; full palette includes blue, cyan, teal, purple, magenta, red, green families. | IBM 8-bar corporate mark + “SkillsBuild” wordmark/product name. | IBM Design Language uses IBM Plex; source highlights IBM Plex and IBM Plex Sans Chinese SC releases. | Enterprise, technical, inclusive, systematic, workforce-development. | SkillsBuild homepage: free skills-based learning, job skills, courses, credentials; IBM design language says blue is core and grays dominate UI with blue as primary action color. |
| Duolingo | Adjacent edtech benchmark: playful learning app | Fetched page did not expose hex values; visual/public assets show Duo mascot and app icon; CSS/JS source confirms proprietary/brand fonts (`Duolingo Sans` flag, `din-round`, `feather`). Treat exact green as unverified in this research capture. | Mascot-led pictorial identity + wordmark/app icon; owl is the dominant memory asset. | Rounded, friendly product type; HTML loads `din-round`, `feather`, and a `Duolingo Sans` flag. | Playful, gamified, emotionally approachable, consumer-app. | Homepage positioning: “Learn languages by playing a game. It’s 100% free, fun, and scientifically proven to work.” Brand-guideline page exists but requires JS. |

### Category synthesis
- **Dominant colors:** blues for trust/credential authority (Coursera, IBM); orange for Chinese paid-knowledge platforms and CTAs (得到, 极客邦); neutrals with product-system grays are common. Green is strongly associated with gamified edtech when mascot-led (Duolingo), but exact token unavailable from fetched source.
- **Logo conventions:** mostly wordmarks or wordmark + symbol systems. Institutional platforms use restrained marks (Coursera C, IBM 8-bar); consumer learning uses mascots; Chinese knowledge platforms often rely on strong Chinese wordmark/app logo plus orange CTA ecosystem.
- **Typography conventions:** sans-serif is nearly universal. Western systems name formal brand fonts (Source Sans Pro, IBM Plex); Chinese sites rely on platform-native Chinese sans stacks. Rounded fonts signal gamification; grotesk/neo-grotesk signals institutional reliability.
- **Visual register conventions:** trust + scalability + product clarity dominate. Category risk: becoming a generic blue education brand or generic orange knowledge-commerce platform.
- **What could stand out for 创智学院:** a system that fuses “innovation intelligence” with a more ownable visual mechanism: modular glyphs, intelligence-map grids, Chinese character-derived symbol, or a warm scholarly-tech palette rather than default blue/orange alone.

## Research Area 2 — Visual Reference & Inspiration

### 1. MIT Media Lab identity — Pentagram case study / Brand New archive
- **What it is:** Education/technology research-lab visual identity and wayfinding system.
- **Distinctive:** Uses a seven-by-seven grid to generate a fixed “ML” monogram plus related glyphs for 23 research groups. Helvetica reinstated to support the system. Brand New tags it as black/white, grid, square, flexible identity.
- **Transferable principle:** Build one underlying generative rule that can express many disciplines/courses without losing coherence.

### 2. The New School identity — Pentagram case study / Brand New archive
- **What it is:** Progressive university identity, custom typography, environmental graphics.
- **Distinctive:** Bespoke typeface “Neue” uses regular, extended, and ultra-extended widths together; parallel bars organize school/program names; black primary wordmark with Parsons Red used for individual schools/programs.
- **Transferable principle:** Typography itself can carry an institutional idea: progressive, flexible, interdisciplinary learning can be encoded through variable width and hierarchy.

### 3. Dropbox rebrand — COLLINS case study
- **What it is:** Enterprise SaaS platform rebrand expanding from file sync to team sync.
- **Distinctive:** Logo built from identical diamond shapes forming a larger unified mark; system uses unexpected combinations of color, typography, art, illustration, and photography to express collaboration and creative collisions.
- **Transferable principle:** A simple modular mark can support a broad expressive system; “collisions” can visualize creative intelligence and cross-disciplinary synthesis.

### 4. Mailchimp rebrand — COLLINS case study
- **What it is:** SaaS / marketing platform rebrand.
- **Distinctive:** Yellow-heavy palette, logotype/logomark, hallmark illustration and photographic styles; balances “sophisticated and surreal”; outsider-art inspiration and hand-drawn imperfection preserve personality while scaling authority.
- **Transferable principle:** Knowledge brands do not need to be sterile; a distinctive memory marker and human imperfection can make learning feel approachable without losing sophistication.

### 5. IBM Design Language / IBM SkillsBuild
- **What it is:** Enterprise design system and tech-learning platform.
- **Distinctive:** Blue is the core (`#0f62fe`) with black/white and nuanced grays; a 2x grid, IBM Plex typeface, UI rules, accessibility contrast, icons, pictograms, and data visualization create systematic precision.
- **Transferable principle:** For AI/technology education, credibility can come from rigorous design-system rules: grids, accessibility, data visualization, and disciplined color usage.

### 6. Coursera brand guide
- **What it is:** Online learning platform brand guidance.
- **Distinctive:** Restrained palette (`#0056D2`, black, white), Source Sans Pro, strict logo clear-space, C symbol, co-branding separator rules.
- **Transferable principle:** If institutional partnerships or certificates matter, visual restraint and clear co-branding architecture are strategic assets.

### 7. Duolingo product identity
- **What it is:** Consumer language-learning app identity; official homepage and JS-only brand guideline landing.
- **Distinctive:** Mascot-led memory system, rounded fonts (`din-round` / Duolingo Sans flag), simple gamified promise: “playing a game,” free/fun/science-based.
- **Transferable principle:** Learning motivation can be made visual through character, reward, roundness, and emotional immediacy; useful if 创智学院 needs a youth/consumer-facing branch.

### 8. Brilliant homepage
- **What it is:** Interactive STEM/math/coding learning platform.
- **Distinctive:** “Learn by doing” proposition, interactive problem solving, clear course categories (Math / CS / Data / Science), friendly illustration assets, claims of guided/personalized learning.
- **Transferable principle:** The brand can foreground method rather than institution: visual language can emphasize interaction, progression, and concepts “clicking.”

---

## Supplement Research — Target Audience + Organization Context

### Supplement source log
- Bing search result page for `创智学院 目标用户 课程 学员`, `创智学院 官网 招生 对象`, `创智学院 官方 网站 简介` — surfaced the official site, admissions portal, Baidu Baike, Zhihu discussion, The Paper, ECNU repost of Wen Hui Bao, CCTV/上观新闻, Jiemian, and admissions subdomain.
- Official Shanghai Innovation Institute / 上海创智学院 homepage: https://www.sii.edu.cn/
- Official admissions portal notice: https://admissions.sii.edu.cn/
- Official overview page / 学院概况: https://www.sii.edu.cn/xygk/list.htm
- Official admissions list / 招生工作: https://www.sii.edu.cn/zsgz/list.htm
- Official “学在创智” list: https://www.sii.edu.cn/xzcz/list.htm
- Official 2026 spring pre-course notice: https://www.sii.edu.cn/2026/0307/c60a766/page.htm
- Official “走进AI大模型” summer micro-course camp recap: https://www.sii.edu.cn/2025/0728/c60a357/page.htm
- Official 2025 FDE training recap: https://www.sii.edu.cn/2025/1221/c60a635/page.htm
- Official 2026 FDE transition-engineer class opening: https://www.sii.edu.cn/2026/0225/c60a752/page.htm
- Official AI safety short-course recap: https://www.sii.edu.cn/2026/0115/c60a644/page.htm
- The Paper feature: https://www.thepaper.cn/newsDetail_forward_31609723
- ECNU repost of Wen Hui Bao feature: https://www.ecnu.edu.cn/info/1426/70270.htm
- CCTV / 上观新闻 article: https://news.cctv.cn/2025/09/13/ARTI6AYLRMhueySavbM3KBp1250913.shtml
- Jiemian article: https://www.jiemian.com/article/13344888.html

### Organization context findings

| Evidence area | Findings | Source evidence |
|---|---|---|
| Official name / English name | Official site footer uses “上海创智学院” and “Shanghai Innovation Institute.” Logo asset appears on official pages. | Official homepage and overview page footer: “上海创智学院 版权所有©2024 ©Shanghai Innovation Institute.” |
| Core institutional category | Not a generic education/training company. Official overview defines it as a “新型人才培养机构” jointly built by top universities, head enterprises, and research institutions. Jiemian calls it a major Ministry of Education + Shanghai cooperation innovation for high-level talent cultivation. | Official overview: “汇聚顶尖大学、头部企业和科研机构联袂建设的新型人才培养机构.” Jiemian: “教育部和上海市开展部市合作、探索高水平人才培养的重大创新.” |
| Location / geography | Shanghai, Xuhui West Bund / 北杨人工智能小镇. Official footer lists address: 上海市徐汇区华发路699弄3号. Official overview says 2.7万平方米 independent building used for teaching and administration. | Official overview and footer; The Paper describes location in 徐汇区北杨人工智能小镇; Jiemian says 徐汇西岸北杨人工智能小镇. |
| Founding / maturity | Search results and articles consistently frame it as new, founded/established in 2024–2025 timeframe. Jiemian states “去年9月正式成立” in a 2025 article; The Paper says “2024年9月成立以来”; search snippet from Baidu says “2024年7月成立” — date discrepancy noted, not resolved from official overview. | Jiemian and The Paper say September 2024; Bing/Baidu result snippet says July 2024. |
| Mission / positioning | Official overview: “以学生为中心、以前沿为牵引,” exploring a Chinese AI-leader cultivation plan, “致力于培养中国AI领军人才，打造世界人工智能创新高地.” The Paper adds national-strategy / science-frontier / universal-value framing: “锚定国家战略、引领科技前沿、创造普惠价值.” | Official overview; The Paper. |
| Program scope | Core tracks cluster around AI frontier: big models/algorithms, embodied intelligence, AI systems/infrastructure, scientific intelligence, AI safety, FDE deployment, innovation/entrepreneurship. Official pre-course includes multimodal/generative large models, optimization theory, embodied robotics, decision and machine behavior. CCTV lists five research positions/阵地: 认知智能、情境智能、具身智能、科学智能、AI基础设施. | Official pre-course notice; official mentor-filter fields; CCTV article. |
| Service model | Hybrid institution: doctoral selection + training, mentor-group cultivation, research project “阵地式培养,” training camps/pre-courses, short courses for AI safety and FDE professional/industry transformation, entrepreneurship incubation and venture support. | Official overview; admissions portal; FDE articles; AI safety short-course; Jiemian/CCTV. |
| Partners / ecosystem | Linked to 31 universities and many companies. The Paper: links 31 participating universities/research institutes/head companies/unicorns with 81 full-time/full-time mentors, 130+ part-time mentors, 120+ industry mentors. CCTV: 31 universities, 50+ head/unicorn enterprises, 5亿元 enterprise donations/sponsorship, 10 incubated ventures. | The Paper; CCTV; Jiemian. |
| Resources / credibility assets | Official overview stresses “超高规格师资、超常措施培养、超凡条件保障,” mentor groups, flexible study plan, high-performance infrastructure, planned/large-scale compute, entrepreneurship support, single dorms. CCTV reports 万P级算力 and 10PB-level data middle platform; official overview says near-term target is 万卡-scale compute. | Official overview; CCTV. |
| Evaluation model | Less conventional paper/GPA emphasis; values scientific/economic/social value, original/social value of academic outcomes, tolerance for high-challenge project failure. Jiemian: training-camp practical selection, less focus on GPA; students can choose/change mentors and topics. | Official overview; Jiemian. |

### Target audience findings

| Audience segment | Evidence | Approx. age range / status | Motivations | Decision-makers / gatekeepers | Desired credibility level | Psychographic traits |
|---|---|---|---|---|---|---|
| **Primary: doctoral-level AI frontier talent / future AI leaders** | Jiemian says admitted objects are all doctoral students, selected from 31 partner universities; 5 admissions camps, 3300+ applicants, 800+ students selected. The Paper says 800+ admitted across 45 majors/fields. | Mainly graduate/PhD stage; reported example: 25-year-old doctoral student; likely early 20s to early 30s, with some cross-over/social talent via in-service doctoral routes. | Freedom to pursue frontier AI research, compute/data resources, mentor access, industry/practice linkage, chance to build research or startups. | Shanghai 创智学院 admissions/selection system, mentor/project evaluators, partner universities; students/prospective doctoral candidates self-select into camps. | Extremely high: national-strategy, research-grade, top-university/enterprise ecosystem; must feel more like frontier institute than consumer edtech. | Self-driven, ambitious, risk-tolerant, wants to challenge “无人区”; values autonomy more than fixed curriculum; motivated by “改变世界” / national AI leadership. |
| **Secondary: high-performing undergraduate/graduate students exploring AI before doctoral selection** | Official spring pre-course open to higher-education undergraduate/master/doctoral students; course requirements list CS/AI/electronic information, calculus/linear algebra/probability, ML/deep-neural-network basics; 10–30 seats per course. Official AI safety short course used students recommended by Fudan, SJTU, Tongji, ECNU. | Undergraduate to PhD students, mostly 18–28. | Build frontier AI literacy and practical skills; test fit for AI research/engineering; gain course certificate/recognition. | Applicant + sending university recommendation/selection for some short courses; course admission by 创智学院. | High but welcoming: rigorous enough for elite students; must signal openness to cross-disciplinary entry. | Curious, high academic ability, maker/practice-oriented, willing to do coursework/projects beyond standard university path. |
| **Adjacent outreach: high school and early university AI enthusiasts** | Official “走进AI大模型” summer camp says 120+ outstanding students from national key middle schools and universities completed five-day immersive AI theory-to-agent development; high-school participant quote expressed hope to join in future. ECNU article mentions Shanghai High School students watched robotics activities during open event. | High school to undergrad, roughly 15–22. | Exposure, inspiration, hands-on agent-building, future application aspiration. | Students and parents/schools likely influence participation, but source does not specify purchase/payment; official camp context is institutional outreach. | Inspirational yet credible; should not look childish despite younger participants. | Exploratory, excited by hands-on AI, seeks “future star” identity and belonging to a top platform. |
| **Professional / industry learners: FDE transition engineers and enterprise AI deployment roles** | Official FDE training targets existing industry engineers transforming into FDEs; 2026 opening article reports 200+ signups and focuses smart manufacturing/finance/medical; requirements include CS/math/engineering background, programming ability, solutioning, customer-service and communication skills. 2025 FDE recap also targeted state-owned enterprises and “5+6” key industry department leaders for strategic awareness. | Adult professionals, likely mid-20s to 50s depending on engineer vs manager/leader cohort. | AI commercialization, industry scenario deployment, “last mile” problem-solving, career transition, organizational AI adoption. | Municipal departments, enterprise leadership/HR, professional self-registration, industry association and government program organizers. | Institutional/government/industry-grade; needs policy seriousness + implementation credibility. | Pragmatic, scenario-driven, wants tools/methodology, customer and business sensitivity, values “real deployment” over theory-only learning. |
| **Institutional partners / funders / enterprises** | Official overview includes head enterprises, research institutions, investment/incubation institutions. CCTV reports 50+ head/unicorn enterprises, donations/sponsorship and capital injection, 10 ventures; Jiemian says compute, labs, venture capital resources support startup/research output. | Organizations, not individual age segment. | Access top AI talent, research translation, startup pipeline, industry problem solving, Shanghai AI ecosystem building. | Government ministries/Shanghai municipal agencies, partner university leadership, enterprise leadership, investors/incubators. | Very high: must project reliability, governance, frontier research quality, and economic/social value. | Outcome-oriented, ecosystem-minded, values proof of impact: papers, open source, patents, startups, deployments. |

### Audience synthesis for visual research use
- **Primary audience is not K-12 or general adult training.** The evidence points to a core doctoral/research-founder institution for frontier AI talent, with outreach and professional-training branches.
- **Most important credibility axis:** frontier research + national/municipal institutional authority + industry translation. This is more demanding than a typical online-learning brand.
- **Most important motivation axis:** autonomy, challenge, real-world impact, entrepreneurship, and access to scarce resources (mentors, compute, data, venture capital, industry scenarios).
- **Design implication from evidence only:** visual language should be able to serve both elite research contexts and public-facing recruitment/camps. A purely playful edtech system would underserve doctoral, government, and enterprise audiences; a purely bureaucratic academic system would underserve the “年轻人主导 / 创客社区 / Researcher Founder” energy reported by media and official pages.
- **Tone requirements implied by sources:** ambitious, frontier, precise, resource-rich, high-agency, experimental, and nationally credible; warmth may come from “student-centered” and “co-creation,” not from cartoon/youth education tropes.
