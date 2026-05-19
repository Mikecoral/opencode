# 设计师追踪日志

## 阶段一：资产规划

### 主体类型与简报触点
主体类型：organization。简报第11章已提供优先级：官网首页与科研进展模板、招生营/博士遴选视觉系统、科研项目与开源成果发布模板、创智未来大会 / TechFest 活动系统为首要；合作生态与产业伙伴提案模板、空间导视与实验室门牌为可选；校园周边与纪念品、传统招生宣传册大套装为本轮不做。本轮在首要触点中优先选择官网、科研/开源发布与招生数字入口；TechFest 因更偏 campaign-system，先推迟。

### 视觉方向决策
- 所选方向：`research-signal`（RUNNING-GRID 可运行网格）
- 考虑过的备选方向：`campaign-energy`、`spatial-system`、`editorial-authority`
- 选择原因：用户明确要求以“RUNNING-GRID 可运行网格”为起点；该方向最能回应简报第5章“模型、网络、推理路径、迭代版本”“可组合模块、节点连接、可变网格”和第10章“可运行的创字 / 9×9 网格 / 子符号派生”。
- 使用的视觉研究：`direction-options.md` 推荐 RUNNING-GRID；参考 MIT Media Lab 网格派生、MIT Media Lab 官网研究列表、IBM Carbon 色彩/图层/字体规则、The New School 可变字宽。
- 规避的默认套路：传统高校院徽、校园宣传照、招生海报大套装、三维赛博神经网络、蓝绿霓虹科技背景、纯创业园区生活方式摄影。

### 交付策略决策
- 所选策略：`digital-system`
- 选择原因：第11章证据最强的触点是官网首页与科研进展、科研项目与开源成果发布，以及招生营/博士遴选入口；这些都需要可复用数字模板、metadata 层级和链接/标签系统。
- 其他策略被排除或推迟的原因：`campaign-system` 虽适合 TechFest，但会把本轮拉向活动主视觉；`spatial-system` 对应导视但简报列为可选；`publishing-system` 适合报告/白皮书但不是第11章首要；`community-system` 周边被简报明确列为本轮不做；`identity-core` 只做 Logo 与规范不足以覆盖首要数字触点。

### 考虑的资产
| 资产创意 | 决策 | 原因 |
|---------|------|------|
| logo-primary | 包含 | 必须项；承担可运行网格的符号锚点。 |
| web-hero | 包含 | 关联官网首页与科研入口，符合 digital-system。 |
| research-list-template | 包含 | 关联科研进展高频更新，承载项目 metadata 与开源链接。 |
| project-release-card-template | 包含 | 关联科研项目与开源成果发布，适合官网与社媒复用。 |
| program-entry-card-template | 包含 | 关联招生营/博士遴选首要触点，但限定为数字入口模板。 |
| ui-glyph-system | 包含 | 让研究方向、项目状态和导师组标签共享底层网格。 |
| event-poster | 排除 | TechFest 是首要触点，但海报属于 campaign-system，本轮推迟。 |
| entrance-signage | 排除 | 空间导视为可选触点，属于 spatial-system，本轮推迟。 |
| partnership-deck | 排除 | 合作生态提案为可选触点，且更偏 publishing / business deck。 |
| merchandise-mockup | 排除 | 简报明确校园周边与纪念品本轮不做，且容易泛高校化。 |
| traditional-brochure | 排除 | 简报明确传统招生宣传册大套装本轮不做。 |

### 最终4-8个资产的整体逻辑
最终 6 个资产围绕“底层网格—数字入口—科研 metadata—开源发布”建立，而不是围绕学校行业惯例建立。Logo 作为锚点，网页、列表、发布卡、项目入口卡和 glyph 系统共同服务第11章首要数字触点；省略 color-palette、campus、admissions brochure 和 merchandise，是为了避免把新型 AI 研究型学院误做成传统高校品牌包。

## 阶段二：生成

### 各资产提示词推导过程

- 资产：logo-primary
- prompt_search 查询："logo minimalist monogram"；补充查询 "标志 极简 品牌"
- 选择的模板：从头编写（无合适模板；提示词库加载返回 0 prompts / no matches）
- 选择该模板的原因：Logo 类模板在库中未命中；资产需要纯抽象符号与 9×9 可运行网格，直接按工程准则编写更可控。
- 使用的简报输入：第5章文化与视觉 DNA、第7章设计关键词、第8/9/10章视觉路线与网格规则、第11章数字触点。
- 文化意象翻译：模型层与推理路径 → AI model layers and inference paths；可组合节点 → modular nodes on variable grid；西岸实验室 → West Bund riverside glass laboratory precision。
- 替换内容：色彩替换为 #07111F / #176BFF / #F5F7FA / #E8EDF3；字体替换为 engineering Grotesk logic；文字纪律设为 no text。
- 风格选择：使用 professional brand identity design、Swiss design principles、minimalist corporate；强调纯符号以规避乱码和传统院徽。
- 最终提示词：Professional brand identity design, Swiss design principles, minimalist corporate symbol for an AI research institute. Create a pure abstract mark built from a precise 9×9 variable grid: modular nodes connected by inference paths, stacked AI model layers, and a subtle running-grid motion logic. The symbol should hint at SII and the Chinese idea of “创智” only through geometric stroke rhythm, not literal letters or characters. Use deep space blue-black #07111F for the main solid form, intelligent blue #176BFF for one active signal path or key node, background gray-white #F5F7FA, and cool hierarchy gray #E8EDF3 for faint construction lines. Style: engineering Grotesk logic, crisp vector edges, balanced negative space, scalable app-icon clarity. Include a small grid construction ghost behind the mark, very restrained. no text, no letters, no Chinese characters, pure symbol. Cultural imagery translated visually: AI model layers and inference paths, modular nodes on variable grid, West Bund riverside glass laboratory precision. no stock photo people, no clichéd icons, no generic AI-style gradients, no 3D chip tunnel, no neon particle sea, no cluttered layout.
- 生图结果：成功；首次 high 并行调用超时，改用 medium 单张生成成功。

- 资产：web-hero
- prompt_search 查询："web hero UI brand technology"；补充查询 "网页 UI 科技"
- 选择的模板：从头编写（无合适模板；提示词库加载返回 0 prompts / no matches）
- 选择该模板的原因：需要官网首屏、导航、CTA 与研究项目卡片的复合 UI，库中未提供可用骨架。
- 使用的简报输入：第5章文化意象、第7章关键词、第10章 RUNNING-GRID、第11章官网首页与科研入口。
- 文化意象翻译：西岸滨江玻璃实验室夜景 → West Bund riverside glass laboratory at night abstracted into glass-line panels；开源成果 metadata → repository-style metadata cards。
- 替换内容：中文文本指定为“创智学院”“运行中的AI研究引擎”等；颜色和字体均来自 brand-tokens。
- 风格选择：以 minimalist corporate digital-system mockup 和 Swiss grid 控制层级；加入中文字符负向引导。
- 最终提示词：Professional brand identity design for a desktop website hero, Swiss design principles, minimalist corporate digital-system mockup. Create a 1536×1024 web hero for an AI research institute using the RUNNING-GRID visual language: a 9×9 modular grid, active inference paths, AI model layers, metadata cards, and a quiet West Bund riverside glass laboratory at night abstracted into glass-line panels. Exact Chinese text must appear: top-left brand text "创智学院"; navigation labels "科研进展" "开源成果" "招生入口" "合作生态"; hero headline "运行中的AI研究引擎"; subtitle "项目制导师组 · 开源系统 · 从0到1"; buttons "查看科研进展" and "进入招生入口". Add small cards labeled "MOSS-VL", "LWD", "MOSS-TTS-Nano", "智能体" with tags "论文" "代码" "模型". Colors: #07111F deep background, #176BFF single accent for CTA and signal lines, #F5F7FA content panels, #E8EDF3 dividers. Typography: clean Chinese humanist sans-serif, compact mono feel for version tags. no warped Chinese characters, no fake gibberish glyphs, no scrambled hanzi, no Lorem ipsum, no English filler where Chinese is required; no stock photo people, no clichéd icons, no generic AI-style gradients, no cluttered layout.
- 生图结果：成功；首次 high 并行调用超时，改用 medium 并行生成成功。

- 资产：research-list-template
- prompt_search 查询："website list template research UI"；补充查询 "网站 列表 模板"
- 选择的模板：从头编写（无合适模板；提示词库加载返回 0 prompts / no matches）
- 选择该模板的原因：资产是科研进展高频列表模板，核心是 metadata 结构而非普通网页展示。
- 使用的简报输入：第5章 open-source repository metadata、第7章真实系统/开源引擎、第11章科研进展模板。
- 文化意象翻译：开源仓库 metadata 和版本标签 → open-source repository lists and version tags；推理路径 → thin inference-path connectors。
- 替换内容：列表行替换为 MOSS-VL、LWD、MOSS-TTS-Nano、智能体；筛选与按钮全指定中文。
- 风格选择：12-column Swiss grid + RUNNING-GRID，避免新闻门户化与论文海报化；加入中文字符负向引导。
- 最终提示词：Professional brand identity design, Swiss design principles, minimalist corporate research-list UI template. Design a landscape website page showing a reusable research progress list, not a one-off article. The layout uses a 12-column Swiss grid with underlying RUNNING-GRID nodes, thin inference-path connectors, and card metadata layers inspired by open-source repository lists. Exact Chinese text: header "科研进展"; subheader "按项目、论文、代码与模型版本追踪真实系统"; filter chips "全部" "多模态" "语言模型" "智能体" "语音"; list rows titled "MOSS-VL 多模态理解更新", "LWD 世界模型实验", "MOSS-TTS-Nano 轻量语音系统", "智能体工具链发布". Each row includes labels "日期" "导师组" "论文" "代码" "开源" and buttons "查看详情". Palette: #F5F7FA background, #07111F headlines, #E8EDF3 card layers and dividers, #176BFF as the only accent for active filter, links, and running signal nodes. Typography: rational Chinese humanist sans-serif, compact neutral sans / mono for metadata. Include modular nodes connected on a variable grid, AI model layers, version tags. no warped Chinese characters, no fake gibberish glyphs, no scrambled hanzi, no Lorem ipsum, no English filler where Chinese is required; no stock photo people, no clichéd icons, no generic AI-style gradients, no cluttered layout.
- 生图结果：成功；首次 high 并行调用超时，改用 medium 并行生成成功。

- 资产：project-release-card-template
- prompt_search 查询："social card template technology project release"；补充查询 "社交 卡片 科技"
- 选择的模板：从头编写（无合适模板；提示词库加载返回 0 prompts / no matches）
- 选择该模板的原因：需要将开源项目发布、官网封面与中文社交分享合并为可复用竖版卡片，库中未命中。
- 使用的简报输入：第5章 maker workbench / repository metadata、第7章开源引擎、第11章科研项目与开源成果发布。
- 文化意象翻译：创客工作台与代码演示 → maker workbench with code demos；系统架构草图 → system architecture sketches translated into abstract panels。
- 替换内容：示例项目为 MOSS-VL；指定“开源成果发布”“论文 · 代码 · 模型权重同步开放”等中文文本。
- 风格选择：深色主面板承接 logo 的压舱色，单一智能蓝作为运行路径；加入中文字符负向引导。
- 最终提示词：Professional brand identity design for a reusable portrait project-release card template, Swiss design principles, minimalist corporate digital card. Format 1024×1536, suitable for website cover and Chinese social sharing. Build the composition around a large RUNNING-GRID field: 9×9 modular nodes, one active inference path in #176BFF, layered AI model panels, and open-source repository metadata. Exact Chinese text: top label "开源成果发布"; project name "MOSS-VL"; main title "多模态理解系统更新"; subtitle "论文 · 代码 · 模型权重同步开放"; metadata chips "版本 v0.9" "导师组" "多模态" "开放仓库"; CTA "查看项目"; footer text "创智学院". Use #07111F for the main dark panel and title, #176BFF as the only accent, #F5F7FA for background fields, #E8EDF3 for card separators and metadata chips. Typography: bold engineering Grotesk-like Chinese display for title, rational humanist sans for body, mono feel for v0.9 and repository tags. Cultural imagery: maker workbench with code demos and system architecture sketches translated into abstract panels, not photos. no warped Chinese characters, no fake gibberish glyphs, no scrambled hanzi, no Lorem ipsum, no English filler where Chinese is required; no stock photo people, no clichéd icons, no generic AI-style gradients, no cluttered layout.
- 生图结果：成功；high 并行生成成功。

- 资产：program-entry-card-template
- prompt_search 查询："program entry card UI Chinese"；补充查询 "中文 卡片 UI"
- 选择的模板：从头编写（无合适模板；提示词库加载返回 0 prompts / no matches）
- 选择该模板的原因：该资产必须是招生/博士遴选数字入口模板，不是传统招生海报，需自定义结构。
- 使用的简报输入：第7章青年合伙人/真实系统/从0到1、第11章招生营/博士遴选视觉系统。
- 文化意象翻译：项目制导师组和真实系统 → project-based mentor group and real systems；代码窗口与架构草图 → code-window blocks and architecture sketch lines。
- 替换内容：指定“招生营 / 博士遴选”“项目制导师组入口”与四步流程中文。
- 风格选择：流程卡片化、数字入口化，明确排除校园照、毕业帽与传统招生海报；加入中文字符负向引导。
- 最终提示词：Professional brand identity design, Swiss design principles, minimalist corporate portrait digital entry card for program admissions flow, not a traditional school poster. Create a reusable 1024×1536 card built from RUNNING-GRID modules, metadata blocks, and a clear step sequence. Exact Chinese text: top brand "创智学院"; main heading "招生营 / 博士遴选"; subheading "项目制导师组入口"; supporting line "面向真实系统、开源引擎与从0到1研究"; four step labels "了解方向" "提交材料" "机考评估" "导师匹配"; information labels "时间" "对象" "入口"; CTA "立即查看". Visual language: modular nodes connected on a variable 9×9 grid, AI model layers and inference paths as subtle background, a maker workbench logic represented through code-window blocks and architecture sketch lines. Palette strictly uses #07111F, #176BFF as only accent, #F5F7FA, #E8EDF3. Typography: clean Chinese humanist sans-serif, bold Neo-grotesk display, compact mono for dates and process numbers. Keep hierarchy calm, systematic, high-potential student oriented. no warped Chinese characters, no fake gibberish glyphs, no scrambled hanzi, no Lorem ipsum, no English filler where Chinese is required; no stock photo people, no clichéd graduation caps, no campus photo, no generic AI-style gradients, no cluttered layout.
- 生图结果：成功；high 并行生成成功。

- 资产：ui-glyph-system
- prompt_search 查询："app icon glyph system grid brand"；补充查询 "图标 系统 网格"
- 选择的模板：从头编写（无合适模板；提示词库加载返回 0 prompts / no matches）
- 选择该模板的原因：需要展示同一底层网格派生多个中文标签 glyph，库中未命中网格规范板结构。
- 使用的简报输入：第5章模块节点与推理路径、第7章研究关键词、第10章子符号派生、第11章数字模板一致性。
- 文化意象翻译：可运行网格 → one RUNNING-GRID base；开源版本标签 → repository version tags；研究方向/项目状态 → research directions and project-status digital badges。
- 替换内容：指定 10 个 glyph 的中文标签；颜色与字体替换为 brand-tokens。
- 风格选择：品牌规范页而非图标商城；用单一智能蓝表示 active node；加入中文字符负向引导。
- 最终提示词：Professional brand identity design, Swiss design principles, minimalist corporate UI glyph system board. Create a landscape 1536×1024 presentation sheet showing how one RUNNING-GRID base generates digital glyphs for an AI research institute. Use a visible 9×9 construction grid, modular nodes, inference paths, AI model layers, repository version tags, and small UI badges. Show 10 clean vector glyphs derived from the same grid, each in a card: exact Chinese labels "模型层" "推理路径" "开源仓库" "导师组" "多模态" "智能体" "语音系统" "数据集" "论文" "活动". Include title text "可运行网格 Glyph 系统" and subtitle "同一底层网格派生研究方向、项目状态与数字标签". Colors: #F5F7FA background, #07111F glyph strokes and headings, #E8EDF3 construction lines and cards, #176BFF as the only active node/accent. Typography: rational Chinese humanist sans-serif, compact neutral sans / mono feel for labels. Make it look like a precise brand guideline page, not an icon marketplace. no warped Chinese characters, no fake gibberish glyphs, no scrambled hanzi, no Lorem ipsum, no English filler where Chinese is required; no stock photo people, no clichéd icons, no generic AI-style gradients, no cluttered layout.
- 生图结果：成功；首次 high 并行调用超时，medium 单张重试成功。

### 决策与取舍
提示词库调用按要求完成，但本地库返回 0 prompts / no matches，因此六个资产均按工程准则从头编写。部分 high 质量并行生成超时；为完成整套资产，超时资产改用 medium 质量重试。所有文件均按批准计划生成，路径使用 `20260519-1141/<文件名>`，未添加计划外资产。
