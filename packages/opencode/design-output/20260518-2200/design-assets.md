# 创智学院品牌视觉资产清单

生成状态：已生成可编辑 SVG 资产。PNG 图像生成工具现在会优先读取环境变量 `OPENAI_API_KEY` / `OPENAI_BASE_URL` / `OPENAI_IMAGE_MODEL`，未设置时回退到 `.opencode/opencode.jsonc` 的 `provider.openai.options.apiKey` / `baseURL` / `imageModel`；以下 PNG 提示词可直接继续生成高质量 PNG 版本。

已生成文件：

- `logo-primary.svg`
- `logo-horizontal.svg`
- `color-palette.svg`
- `typography-specimen.svg`
- `brand-mockup.svg`

## 1. logo-primary.png

- SVG版本：`logo-primary.svg`
- 尺寸：1024x1024
- 质量：high
- 用途：主标志、头像、图标、品牌封面

```text
Create a primary square logo design for 创智学院, a future-oriented education and innovation academy combining creativity, artificial intelligence literacy, project-based learning, and human-centered technology. The mark should be clean, vector-like, geometric, and professional, suitable for institutional use. Design a distinctive Chinese-focused symbol inspired by the characters 创 and 智, integrating an upward creative spark and subtle AI knowledge-node connections. Use a bright but credible palette: technology blue #2563EB, wisdom purple #7C3AED, small accents of warm yellow #FBBF24 and teal #14B8A6, on a clean mist-white background. Include the Chinese name 创智学院 below or beside the mark in a modern customized sans-serif style. Avoid robots, generic brains, complex circuit boards, childish cartoons, excessive 3D, and cyberpunk neon. High legibility at small sizes, balanced whitespace, premium academy identity.
```

## 2. logo-horizontal.png

- SVG版本：`logo-horizontal.svg`
- 尺寸：1536x1024
- 质量：high
- 用途：官网导航、课件页眉、证书抬头、机构合作文件

```text
Create a horizontal logo lockup for 创智学院, a modern academy for creative intelligence, AI literacy, innovation education, and future learning. Compose a compact geometric symbol on the left and the Chinese wordmark 创智学院 on the right, with an optional small English subtitle Creative Intelligence Academy. The symbol should abstract Chinese character structure, a rising creative spark, and connected AI knowledge nodes, but remain simple and memorable. Use technology blue #2563EB and wisdom purple #7C3AED as primary colors, with restrained teal #14B8A6 and warm yellow #FBBF24 highlights. Style should be flat vector, crisp edges, customized modern sans-serif Chinese typography, excellent spacing, suitable for website headers, certificates, slides, and signage. White or very light background, no mockup perspective, no gradients that reduce print usability, no robot icon, no generic brain, no overly thin circuitry.
```

## 3. color-palette.png

- SVG版本：`color-palette.svg`
- 尺寸：1536x1024
- 质量：high
- 用途：品牌色彩规范页、提案展示、设计系统基础页

```text
Design a polished brand color palette board for 创智学院, a future learning academy blending creativity and intelligent technology. The board should feel like a professional brand guideline page, landscape format, with color swatches, hex codes, names, and usage notes. Include primary technology blue #2563EB, wisdom purple #7C3AED, active teal #14B8A6, creative spark yellow #FBBF24, deep ink blue #0F172A, and mist white #F8FAFC. Show a blue-to-purple gradient for digital hero visuals, plus neutral combinations for educational certificates and documents. Use clean grid layout, modern Chinese typography, subtle knowledge-node line patterns, generous whitespace, and small examples of buttons, tags, and highlight chips. Mood: bright, credible, innovative, educational, not childish, not cyberpunk. Include the brand name 创智学院 prominently and keep all text crisp and guideline-like.
```

## 4. typography-specimen.png

- SVG版本：`typography-specimen.svg`
- 尺寸：1536x1024
- 质量：high
- 用途：字体规范页、品牌指南、PPT 模板基础

```text
Create a landscape typography specimen board for the brand identity of 创智学院, a creative intelligence and future learning academy. Present Chinese and English typography guidance using modern sans-serif styles resembling HarmonyOS Sans SC, Source Han Sans, Inter, Manrope, and Space Grotesk. Show hierarchy examples: large Chinese headline 创造力与智能同行, subheading 面向未来的创新学习学院, body text blocks about AI literacy and project-based learning, English subtitle Creative Intelligence Academy, numerals, course tags, and UI labels. Use the brand palette: deep ink #0F172A for text, technology blue #2563EB, wisdom purple #7C3AED, teal #14B8A6, warm yellow #FBBF24 accents, mist white #F8FAFC background. Layout should be premium, clean, modular, with light knowledge-node graphic accents and ample whitespace. Avoid decorative calligraphy, cartoon type, excessive effects, and unreadable tiny text.
```

## 5. brand-mockup.png

- SVG版本：`brand-mockup.svg`
- 尺寸：1536x1024
- 质量：high
- 用途：品牌提案总览、应用场景展示、官网与课程物料风格参考

```text
Create a professional brand application mockup for 创智学院, an innovation education academy focused on creativity, AI literacy, and future learning. Show a coherent identity system across realistic but clean applications: website hero section, course certificate, business card, notebook cover, presentation slide cover, social media avatar, and course card UI. Use a primary logo with a geometric Chinese-inspired creative spark and AI node symbol, modern Chinese wordmark 创智学院, optional English Creative Intelligence Academy. Palette: technology blue #2563EB, wisdom purple #7C3AED, teal #14B8A6, warm yellow #FBBF24 accents, deep ink #0F172A, mist white #F8FAFC. Visual language: modular grids, knowledge-node patterns, light gradients, confident education professionalism, friendly future-tech atmosphere. Avoid clutter, stock-photo people, childish school motifs, robots, generic brain icons, heavy neon, and overly glossy 3D. Make it presentation-ready for a brand proposal.
```

## 生成说明

设置 `OPENAI_API_KEY`，或在 `.opencode/opencode.jsonc` 中配置 OpenAI provider 后，可使用上述提示词分别生成 5 个文件：

- `logo-primary.png`
- `logo-horizontal.png`
- `color-palette.png`
- `typography-specimen.png`
- `brand-mockup.png`
