# 规划师追踪日志

## 主体分类

- 最终类型：organization
- 推理：用户要求“为创智学院做一套品牌形象设计”。“学院”首先指向教育/科研组织，而不是地点、产品、活动/IP或个人。搜索前初判为 organization。后续搜索发现最相关权威主体为“上海创智学院 / Shanghai Innovation Institute”，官网域名为 `sii.edu.cn`，进一步确认其为人工智能人才培养与科研机构。

## 本地设计系统查询（第0.5步）

- 操作：在网络搜索前尝试读取 `/Users/hongyuecheng/python-learn/SII/AIdesign/open-design/design-systems/apple/DESIGN.md`、`notion/DESIGN.md`、`linear/DESIGN.md`。
- 结果：工具权限阻止读取工作区外部目录，返回 external_directory 规则限制。
- 处理：在简报中如实标注权限限制，并将 apple / notion / linear 作为待人工复核的参考锚点：Apple=高留白与克制材料感；Notion=模块化知识卡片；Linear=深色效率界面与细线图标。此部分不是网络事实，已标注需后续复核。

## 方法论研究（第1步）

### 查询：`brand identity system components`
- 考虑的结果：
  - https://www.ama.org/topics/brand-and-branding/
  - https://blog.hubspot.com/marketing/branding
  - Wikipedia/Investopedia/Britannica 等通用页面
- 有用的内容：AMA 明确品牌识别包括名称、Logo、色彩、字体、设计元素；HubSpot 将品牌建设拆分为目标受众、使命、价值、视觉资产、品牌声音与渠道应用。
- 丢弃的内容：Wikipedia/Investopedia/Britannica偏定义，不如AMA与HubSpot对VI交付物直接。

### 查询：`school brand identity design case AI institute`
- 考虑的结果：Bing返回大量无关PDF与低相关结果。
- 有用的内容：搜索结果质量差，因此转向已知权威高校品牌指南作为案例来源。
- 丢弃的内容：加拿大校区PDF、会议纪要、政策PDF等与品牌设计无关。

### 查询：`AI institute visual identity references brand design`
- 考虑的结果：
  - https://openai.com/brand/
  - https://identity.stanford.edu/
  - https://brand.mit.edu/
- 有用的内容：OpenAI提供AI机构的极简、留白、字体策略；Stanford/MIT提供高校/科研机构品牌系统结构。
- 丢弃的内容：AI定义类页面（Google Cloud、Britannica、ISO等）不属于视觉识别案例。

### 抓取的页面
- URL：https://www.ama.org/topics/brand-and-branding/  
  提取内容：品牌识别包含名称、logo、色彩、字体、设计元素；品牌定位用于定义市场位置和差异化。
- URL：https://blog.hubspot.com/marketing/branding  
  提取内容：品牌建设流程包含目标受众、使命、价值、视觉资产、品牌声音、渠道应用；强调一致性。
- URL：https://identity.stanford.edu/  
  提取内容：高校品牌系统包含品牌、视觉识别、设计元素、数字、印刷、资源等完整工具箱。
- URL：https://brand.mit.edu/  
  提取内容：MIT品牌强调Optimized、Bold、Unified；品牌架构和颜色系统统一各触点。
- URL：https://openai.com/brand/  
  提取内容：AI机构可通过极简字标、固定比例、充足留白、几何+人文温度字体建立可信技术感。

## 主体调研（第2步）

### 查询：`创智学院 官网`
- 考虑的结果：
  - https://www.sii.edu.cn/main.htm
  - https://www.sii.edu.cn/xygk/list.htm
  - https://admissions.sii.edu.cn/
  - 百度百科、知乎、腾讯新闻、澎湃新闻等
- 有用的内容：官网确认主体为上海创智学院；首页提供栏目结构、地址、电话；招生系统确认活动报名与遴选入口。
- 丢弃的内容：百科、知乎、媒体报道作为非首要权威来源，未进入核心事实。

### 查询：`上海创智学院 成立 2024 教育部 上海市`
- 考虑的结果：Bing结果受“Oklahoma City Thunder”干扰严重，未得到可用权威页面。
- 有用的内容：无。
- 丢弃的内容：NBA、PayPal等完全无关结果。

### 查询：`上海创智学院 北杨人工智能小镇 徐汇`
- 考虑的结果：Bing结果质量差，但官网学院概况页面已有“徐汇西岸北杨人工智能小镇”权威信息。
- 有用的内容：回到官网学院概况提取位置与空间条件。
- 丢弃的内容：PayPal等无关结果。

### 查询：`上海创智学院 招生 博士生 遴选 2026`
- 考虑的结果：Bing结果质量差；官网招生工作栏目直接包含“2026年夏令营博士生遴选通知”。
- 有用的内容：招生工作栏目证明招生触点真实存在。
- 丢弃的内容：菲律宾SSS等无关结果。

### 抓取的页面
- URL：https://www.sii.edu.cn/main.htm  
  提取内容：官网首页、栏目结构、创智日历、科研进展、全球引进青年教师、地址电话、现有logo。
- URL：https://www.sii.edu.cn/xygk/list.htm  
  提取内容：学院定义、培养理念、导师组机制、课程体系、科研课题、学术文化、区位、算力、创业支持、空间保障。
- URL：https://www.sii.edu.cn/sjcz/list.htm  
  提取内容：“视觉创智”栏目包含AI概念片、训练营、成果发布会、央视报道等影像素材。
- URL：https://www.sii.edu.cn/zsgz/list.htm  
  提取内容：招生工作栏目列出夏令营博士生遴选通知、考试大纲、机考手册等。
- URL：https://admissions.sii.edu.cn/  
  提取内容：活动报名通知、招生工作信息发布平台、遴选系统、咨询电话邮箱。
- URL：https://www.sii.edu.cn/2026/0429/c22a946/page.htm  
  提取内容：“创奇·智能新引擎”成果交流会；七大核心成果；有组织科研、AI-ready数据、TaaS、科研驾驶舱、NEXChem、NEXMed、AI安全矩阵等。

## 文化与视觉DNA——推导过程

- 搜索“创智学院 官网” → 发现权威官网 `sii.edu.cn` → 确认主体为上海创智学院，非泛称“创智学院”。
- 抓取学院概况 → 发现“以学生为中心、以前沿为牵引”“导师组培养制”“轻量级课程体系”“徐汇西岸北杨人工智能小镇”“算力支撑”“创业支持” → 推导出视觉DNA：多中心协同、模块化课程、城市AI试验场、算力基础设施、研创学一体。
- 抓取“创奇·智能新引擎”新闻 → 发现算力调度、数据生产、模型训练、科研操作系统、实验闭环与安全治理 → 推导出图形DNA：全栈堆叠、任务流、节点拓扑、运行状态、科研驾驶舱。
- 抓取招生工作与活动报名页 → 发现夏令营/春季营/博士遴选/考试大纲等高频线上触点 → 将招生营主视觉、官网组件、学术报告模板列为首要触点。
- 抓取视觉创智栏目 → 发现已有AI概念片、训练营、发布会影像 → 判断新VI需兼容影像资产，而不是只做静态院徽。

## 未解问题 / 信息缺口

- 本地设计系统库因权限限制未能读取，简报中的 Apple/Notion/Linear 锚点需人工复核 DESIGN.md 后再固化。
- 官网未在抓取内容中明确说明学院成立日期；简报避免使用“成立于2024”等未核实表述，仅引用官网版权年份与机构事实。
- 现有 logo.svg 的具体图形细节与色值未能直接解析，简报只引用“官网已使用中英文组合标识与logo.svg”，未断言其具体造型。
- 招生遴选通知页面抓取结果显示标题但正文内容缺失，可能正文为图片/PDF或动态加载；简报仅用其证明栏目与触点存在。
