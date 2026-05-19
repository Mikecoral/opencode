# 多智能体品牌设计系统 — 开发记录

基于 OpenCode 开源项目，实现了一套多智能体品牌形象设计系统。用户输入一句话（如"请为创智学院做一套品牌形象设计"），系统自动协调三个专属智能体，完成调研、生图、评审的全流程。

---

## 改动文件一览

### 新增文件

| 文件 | 说明 |
|------|------|
| `packages/opencode/src/tool/imagegen.txt` | imagegen 工具描述文本，供 LLM 理解工具用途 |
| `packages/opencode/src/tool/imagegen.ts` | 核心生图工具，调用 OpenAI gpt-image-2 API，将图片保存为 PNG |
| `.opencode/agent/planner.md` | Planner 子智能体：品牌策略研究员，产出 `design-output/brief.md` |
| `.opencode/agent/designer.md` | Designer 子智能体：视觉设计师，调用 imagegen 生成 5 张品牌图片 |
| `.opencode/agent/critic.md` | Critic 子智能体：设计评审，5维度打分并给出迭代建议 |
| `.opencode/skills/brand-design/SKILL.md` | 品牌设计 Harness 技能，定义完整 4 阶段工作流 |

### 修改文件

| 文件 | 修改内容 |
|------|----------|
| `packages/opencode/src/tool/registry.ts` | 注册 ImageGenTool（import + yield + Effect.all + builtin 数组） |
| `.opencode/opencode.jsonc` | 配置 OpenAI provider（apiKey、baseURL）、预授权 imagegen 工具、设置默认模型 |

---

## 核心实现：imagegen.ts

调用 OpenAI gpt-image-2 的 Effect.ts 工具，关键设计：

- **调用顺序**：`ctx.metadata()` → `ctx.ask()` → API key 检查 → fetch 请求
- **AbortSignal**：`signal: ctx.abort` 支持用户中断长时间生图
- **错误处理**：三类错误（缺 key、HTTP 报错、空响应）均返回结构化 `ExecuteResult`，不抛异常
- **输出路径**：`<cwd>/design-output/<filename>.png`，自动创建目录
- **API 地址**：优先读 `OPENAI_BASE_URL` 环境变量，默认指向代理地址

```typescript
// 核心请求逻辑
const baseURL = (process.env.OPENAI_BASE_URL ?? "https://apicz.boyuerichdata.com/v1").replace(/\/$/, "")
fetch(`${baseURL}/images/generations`, {
  method: "POST",
  body: JSON.stringify({ model: "gpt-image-2", prompt, n: 1, size, quality, response_format: "b64_json" }),
  signal: ctx.abort,
})
```

---

## 三个子智能体

| 智能体 | 颜色 | 模型 | 工具权限 | 职责 |
|--------|------|------|----------|------|
| `@planner` | 蓝 `#4A90D9` | openai/gpt-5.5 | websearch, webfetch, read, write | 调研机构背景（强制 ≥3 websearch + ≥2 webfetch + 来源引用），生成 10 节带 `## Sources` 的简报 |
| `@designer` | 橙 `#E87C3E` | openai/gpt-5.5 | + imagegen | **双阶段**：Phase 1 按业态规划 4-8 个资产并写 `asset-plan.md`；Phase 2 经确认后生图 |
| `@critic` | 紫 `#9B59B6` | openai/gpt-5.5 | read, write, websearch | **双模式**：Mode A 评 brief（5 维 + 裁决 PASS/REVISE/RESEARCH-AGAIN）；Mode B 评视觉（5 维 + 迭代建议） |

**Designer 资产清单是动态的**（不再硬编码），由 Designer 读取 brief 后按业态裁剪：

- 学校/教育 → logo-primary, logo-horizontal, color-palette, campus-banner, student-merchandise-mockup, brochure-cover
- 餐饮/食品 → logo-primary, color-palette, menu-design, packaging-mockup, storefront-signage, social-post
- SaaS/科技 → logo-primary, app-icon, color-palette, web-hero, social-cards, presentation-template
- 文化/非营利 → logo-primary, logo-horizontal, color-palette, poster-design, brochure, event-banner

唯一固定资产：`logo-primary`（任何品牌都需要）。其余 3-7 个由 Designer 决定。

---

## Harness 工作流（SKILL.md）

```
用户输入品牌设计需求
    ↓
Stage 1     @planner 调研（强制 web search + 来源引用） → design-output/brief.md
    ↓
Stage 1.5   @critic Mode A 审 brief → design-output/brief-critique.md
            裁决：PASS / REVISE / RESEARCH-AGAIN
            ├─ PASS → 进入 Stage 2a
            ├─ REVISE → 编辑 brief 或重跑 planner
            └─ RESEARCH-AGAIN → 重跑 planner（最多 2 次，超限改为人工兜底）
    ↓ [用户确认]
Stage 2a    @designer Phase 1：按业态规划 4-8 个资产 → design-output/asset-plan.md
    ↓ [用户确认 / 可修改清单]
Stage 2b    @designer Phase 2：按 asset-plan 生图 → design-output/design-assets.md
    ↓ [用户确认]
Stage 3     @critic Mode B 评视觉 → design-output/critique.md
    ↓ [用户选择]
Stage 4（可选）：@designer 按评审建议迭代特定资产
    ↓
输出 design-output/README.md 汇总报告
```

**关键设计点**：
- Stage 1.5 在花费生图配额前先把住 brief 质量关
- RESEARCH-AGAIN 设 2 次重试上限，防止机构信息不足时死循环
- 资产清单由 Designer 动态规划，按业态裁剪而非固定 5 张
- 每个阶段都有用户确认，支持半自动多轮交互

---

## 配置说明

### `.opencode/opencode.jsonc`

```jsonc
{
  "model": "openai/gpt-5.5",       // 默认模型
  "provider": {
    "openai": {
      "options": {
        "apiKey": "...",            // OpenAI API Key
        "baseURL": "https://apicz.boyuerichdata.com/v1"  // 代理地址
      }
    }
  },
  "permission": {
    "imagegen": "allow"            // 预授权生图工具
  }
}
```

### 环境变量

```bash
export OPENAI_API_KEY="..."        # imagegen 工具读取此变量
export OPENAI_BASE_URL="..."       # 可选，覆盖默认代理地址
```

---

## 启动方式

```bash
# ~/.zshrc 中已配置 alias
opencode

# 等价于
bun run --cwd /Users/hongyuecheng/python-learn/SII/AIdesign/opencode dev
```

启动后输入"请为创智学院做一套品牌形象设计"即可触发品牌设计技能。

---

## Git 提交记录

| Commit | 内容 |
|--------|------|
| `e20a76c` | feat: add imagegen tool description |
| `8a84e3c` | feat: implement imagegen tool for gpt-image-2 image generation |
| `f8b0219` | fix: reorder ctx.metadata/ctx.ask calls in imagegen tool |
| `02d60a0` | fix: add AbortSignal, extract OUTPUT_DIR constant in imagegen tool |
| `cf4e424` | feat: register ImageGenTool in tool registry |
| `4086059` | feat: add planner, designer, critic sub-agents for brand design |
| `67b971c` | feat: add brand-design harness skill |
| `97dde62` | feat: pre-authorize imagegen tool in opencode config |
| `1aa7a3d` | fix: remove redundant orDie, use @designer for Stage 4 iteration |
