# 视觉研究追踪日志

## 搜索查询
- 查询：`MIT Media Lab identity Pentagram grid glyph research groups`
  - 考虑的结果：Pentagram 官方案例页、MIT Media Lab 官网相关页面。
  - 选择/排除原因：选择 Pentagram 官方案例页，因为它直接说明 7×7 网格、ML monogram 与 23 个研究组 glyph 的生成逻辑；排除泛新闻转述。
- 查询：`IBM Design Language color UI blue gray accessibility`
  - 考虑的结果：IBM Design Language、Carbon Design System 色彩页。
  - 选择/排除原因：选择 IBM Design Language 色彩页，因为其更强调品牌色彩逻辑、灰阶主导、蓝色核心和可访问性；Carbon 更偏组件实现。
- 查询：`MIT Brand Guide color red gray bright red black white`
  - 考虑的结果：MIT Brand Guide Color、MIT Brand Guide Typography。
  - 选择/排除原因：选择 Color 页，用来提取“核心色 + 扩展色 + 历史/现代平衡”的视觉方法。
- 查询：`Stanford identity typography sans serif mono technical data`
  - 考虑的结果：Stanford Typography、Primary Typefaces、Accent Typefaces。
  - 选择/排除原因：选择 Typography 总页，因为它清楚列出 Source Sans/Serif 与 Roboto Mono/Condensed/Slab 的层级关系。
- 查询：`OpenAI brand guidelines typography geometric humanistic whitespace`
  - 考虑的结果：OpenAI Design Guidelines、OpenAI brand portal。
  - 选择/排除原因：选择公开 Design Guidelines，用来参考 AI 机构的克制留白、人文几何字体与 logo 使用禁忌。
- 查询：`Shanghai Innovation Institute logo svg`
  - 考虑的结果：官网 `logo.svg` 与 `logo_w.svg`。
  - 选择/排除原因：抓取 `logo.svg` 初步审计，因为评审明确建议先确认既有标志资产边界；未继续深入 `logo_w.svg`，因为本轮重点是方向研究而非完整标志重绘。

## 抓取页面
- URL：https://www.pentagram.com/work/mit-media-lab/story
  - 提取的视觉洞察：同一底层网格可同时生成主标识和研究组子符号；系统的识别力来自“规则可复用”而不是单个 logo 的造型复杂度。
- URL：https://www.ibm.com/design/language/color
  - 提取的视觉洞察：技术品牌不必靠大面积霓虹；灰阶和黑白应主导信息密度，蓝色作为核心操作/识别色，其他色彩少量承担意义。
- URL：https://brand.mit.edu/color
  - 提取的视觉洞察：核心色负责稳定和权威，扩展色负责表达弹性；红色与黑白银灰可传达使命感，但需要可读性控制。
- URL：https://identity.stanford.edu/design-elements/typography/
  - 提取的视觉洞察：学院/研究机构适合建立多字体层级：正文可读、标题有个性、等宽字体承载技术与数据；不要单一“科技字体”通吃。
- URL：https://openai.com/brand/
  - 提取的视觉洞察：AI 品牌可以通过留白、黑白、圆润几何和柔和研究封面建立人文温度；大量“不要修改、不要加效果、不要忙背景”的规则说明克制本身是识别资产。
- URL：https://deepmind.google/discover/visualising-ai/
  - 提取的视觉洞察：AI 研究成果可被组织成模型卡片、科学分区与大图叙事；对创智学院的官网项目矩阵、成果发布与研究/产业/教育入口有参考价值。
- URL：https://www.sii.edu.cn/_upload/tpl/00/03/3/template3/images/logo.svg
  - 提取的视觉洞察：现有 SVG 包含左侧位图 pattern 与右侧中英文字标，中文/英文均使用 Microsoft YaHei；可继承横向锁定结构，但不宜把内嵌位图作为未来 VI 的唯一核心。

## 方向差异化检验
- 各方向在色彩取向上的差异：
  - GRID-ENGINE：深色优先，黑/墨蓝 + 电蓝 + 少量荧青/红，面向系统界面和发布屏。
  - GLASS-CAMPUS：均衡偏浅，雾白/银灰/玻璃蓝灰 + 墨蓝文字，面向空间、官网和媒体可信度。
  - MAKER-PROTOCOL：浅色优先，白/纸灰 + 黑大字 + 红/蓝行动色，面向招募和训练营冲击。
- 各方向在字体上的差异：
  - GRID-ENGINE：压缩几何标题 + 可读无衬线 + 等宽数据层。
  - GLASS-CAMPUS：稳重无衬线为主，可少量引入现代衬线/宋体气质增强学术可信。
  - MAKER-PROTOCOL：超大重磅/压缩标题 + 等宽标签 + 简洁正文，像任务书和实验日志。
- 各方向在版式上的差异：
  - GRID-ENGINE：模块网格、节点链路、项目 glyph、卡片系统、状态标签。
  - GLASS-CAMPUS：大留白、宽幅真实影像、建筑/展陈栏栅、导视式信息层。
  - MAKER-PROTOCOL：不对称海报、贴纸标签、流程清单、代码块、批注式节奏。
- 各方向在资产含义上的差异：
  - GRID-ENGINE：资产代表“科研基础设施与可运行平台”。
  - GLASS-CAMPUS：资产代表“城市实验室、开放协同与可信机构”。
  - MAKER-PROTOCOL：资产代表“青年主战位、招募共创与快速实战”。
