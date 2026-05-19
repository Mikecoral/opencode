# 视觉研究追踪日志

## 搜索查询
- 查询：`AI research institute visual identity grid system education technology Pentagram`
  - 考虑的结果：MIT Media Lab by Pentagram；MIT Media Lab 官网运行态。
  - 选择/排除原因：选择 MIT Media Lab，因为其把研究组多样性转化为同一网格下的 glyph 系统，且官网能看到真实新闻/研究组/标签的运行形态。排除泛 AI 品牌集合页，因为多为二手转载，视觉说明不够权威。
- 查询：`progressive university visual identity custom typography flexible structure`
  - 考虑的结果：The New School by Pentagram。
  - 选择/排除原因：选择该案例，因为其核心不是科技感，而是用定制字宽、横线和母子品牌结构处理多学院/项目演化，可作为避免“全是蓝绿网格”的差异化参考。
- 查询：`enterprise design system dark light theme data dense UI typography tokens`
  - 考虑的结果：IBM Carbon color overview、IBM Carbon typography overview、Material Design 3 color/typography。
  - 选择/排除原因：选择 Carbon，因为页面可抓取到颜色图层模型、浅深主题、token、productive/expressive 字阶等具体规则；Material Design 页面抓取结果主要提示需要 JavaScript，未提取到足够视觉细节，因此不作为主要参考。
- 查询：`上海创智学院 官网 视觉创智 科研进展 视觉触点`
  - 考虑的结果：上海创智学院官网首页、视觉创智栏目。
  - 选择/排除原因：选择官方现有触点，用于判断新视觉必须兼容哪些内容模块：Logo、导航、科研进展、创智日历、招聘号召、视频/训练营/成果发布会等。该部分只提取触点和素材类型，不重做事实性品牌调研。

## 抓取页面
- URL：[https://www.pentagram.com/work/mit-media-lab](https://www.pentagram.com/work/mit-media-lab)
  - 提取的视觉洞察：7×7 网格可以同时生成主标和多个研究组 glyph；系统价值在“固定身份 + 多元研究活动”的同源派生，而不是单个漂亮 Logo。对创智学院可转译为 SII、创/智笔画、研究阵地、招生营、TechFest、开源项目的生成规则。
- URL：[https://www.media.mit.edu/](https://www.media.mit.edu/)
  - 提取的视觉洞察：官网把研究内容当作可浏览数据库：每条内容组合标题、类别、来源、日期、研究组、标签与 glyph。创智学院科研进展模板应重视 metadata、标签、开源入口和项目组信息，而不只是封面图。
- URL：[https://www.pentagram.com/work/the-new-school/story](https://www.pentagram.com/work/the-new-school/story)
  - 提取的视觉洞察：通过正常/宽/超宽字形混排和横线装置，建立“整体品牌 + 各学院/项目”的层级关系；黑色主标与红色项目名形成清晰角色。创智学院可借鉴字宽变化表达项目演化，但需控制中文可读性。
- URL：[https://carbondesignsystem.com/elements/color/overview/](https://carbondesignsystem.com/elements/color/overview/)
  - 提取的视觉洞察：颜色应按角色与主题组织：背景、图层、边框、文本、链接、状态、交互；浅色主题通过 White / Gray 10 交替，深色主题逐层变亮。对创智学院的启发是把深空蓝黑、智能蓝、荧光绿、暖橙变成 token，而不是同时大面积使用。
- URL：[https://carbondesignsystem.com/elements/typography/overview/](https://carbondesignsystem.com/elements/typography/overview/)
  - 提取的视觉洞察：productive 字阶适合官网与科研界面，expressive 字阶适合活动传播；Sans / Serif / Mono 家族分工能处理长文、标题、代码和数据。创智学院应建立“科研阅读模式”和“活动传播模式”两套字阶。
- URL：[https://www.sii.edu.cn/main.htm](https://www.sii.edu.cn/main.htm)
  - 提取的视觉洞察：现有官网首屏、创智日历、科研进展、加入我们等模块已经形成内容结构；新系统要优先统一科研封面、日期模块、标签、项目卡片和招聘/招生活动入口。
- URL：[https://www.sii.edu.cn/sjcz/list.htm](https://www.sii.edu.cn/sjcz/list.htm)
  - 提取的视觉洞察：“视觉创智”栏目包含训练营、成果发布会、央视报道、AI 概念片、合影等素材类型；需要影像裁切、封面生成和活动命名规则，避免素材风格碎片化。

## 方向差异化检验
- 各方向在色彩取向上的差异：
  - RUNNING-GRID：深色优先，深空蓝黑为底，蓝/绿为运行信号，橙色极少量用于价值节点。
  - WEST-BUND-MAKER：浅色优先，灰白/白为底，橙色权重提高以表达招募、路演和转化，蓝色用于结构，绿色仅作状态标签。
  - PUBLIC-ENGINE：均衡偏浅，白/灰报告底 + 深蓝黑标题 + 蓝色结构 + 橙色公共价值章节，整体不发光。
- 各方向在字体上的差异：
  - RUNNING-GRID：工程 Grotesk + 局部 Mono + 可变字宽短标题，强调系统运行与版本感。
  - WEST-BUND-MAKER：更人文、更开阔的中文无衬线，允许批注/草图层，降低冷硬科技感。
  - PUBLIC-ENGINE：强编辑字阶，正式中文正文 + 大号可变宽英文/数字标题 + 数据表 Mono，强调报告与公共传播。
- 各方向在版式上的差异：
  - RUNNING-GRID：仪表盘、网格、节点、metadata 面板，节奏偏冷静精密。
  - WEST-BUND-MAKER：工作台、卡片、照片/截图/白板叠放，节奏偏现场与共同体。
  - PUBLIC-ENGINE：大标题、横线/竖线分栏、数据图表、引文短句，节奏偏编辑与权威发布。
- 各方向在资产含义上的差异：
  - RUNNING-GRID 的资产是“可生成的研究系统”：主标、子 glyph、科研封面、开源项目卡。
  - WEST-BUND-MAKER 的资产是“真实现场证据”：人物、讨论、屏幕、demo、空间、训练营与开放日物料。
  - PUBLIC-ENGINE 的资产是“公共可信叙事”：报告模板、合作生态图、政策/产业提案、年度影响和媒体包。
