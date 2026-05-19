# 多智能体品牌设计系统 — 开发记录

基于 OpenCode 开源项目，实现了一套多智能体品牌形象设计系统。用户输入一句话（如"请为创智学院做一套品牌形象设计"），系统自动协调四个专属智能体，完成事实调研、视觉参考研究、资产规划、生图、评审的全流程。

---

## 改动文件一览

### 新增文件

| 文件 | 说明 |
|------|------|
| `packages/opencode/src/tool/imagegen.txt` | imagegen 工具描述文本，供 LLM 理解工具用途 |
| `packages/opencode/src/tool/imagegen.ts` | 核心生图工具，调用 OpenAI gpt-image-2 API，将图片保存为 PNG |
| `.opencode/agent/planner.md` | Planner 子智能体：品牌策略研究员，产出 `design-output/brief.md` |
| `.opencode/agent/visual-researcher.md` | Visual Researcher 子智能体：视觉参考研究员，产出 `visual-references.md` / `direction-options.md` |
| `.opencode/agent/designer.md` | Designer 子智能体：视觉设计师，读 brief + visual research 后规划资产并调用 imagegen |
| `.opencode/agent/critic.md` | Critic 子智能体：设计评审，结合 image_analyze 做 5 维度打分并给出迭代建议 |
| `.opencode/skills/brand-design/SKILL.md` | 品牌设计 Harness 技能，定义完整多阶段工作流 |

### 修改文件

| 文件 | 修改内容 |
|------|----------|
| `packages/opencode/src/tool/registry.ts` | 注册 ImageGenTool（import + yield + Effect.all + builtin 数组） |
| `.opencode/opencode.jsonc` | 配置 OpenAI provider（apiKey、baseURL）、预授权 imagegen / image_analyze / prompt_search 等工具、设置默认模型 |

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

## 四个子智能体

| 智能体 | 颜色 | 模型 | 工具权限 | 职责 |
|--------|------|------|----------|------|
| `@planner` | 蓝 `#4A90D9` | openai/gpt-5.5 | websearch, webfetch, read, write | 做事实 / 品牌 / 行业 / 主体研究（强制 ≥3 websearch + ≥2 webfetch + 来源引用），生成 `brief.md` |
| `@visual-researcher` | 绿 `#38A169` | openai/gpt-5.5 | websearch, webfetch, read, write | 做视觉参考 / 设计案例 / 风格方向搜索，生成 `visual-references.md`、`direction-options.md`、`visual-research-trace.md` |
| `@designer` | 橙 `#E87C3E` | openai/gpt-5.5 | read, write, imagegen, prompt_search | **双阶段**：Phase 1 读 brief + visual research 后规划资产；Phase 2 使用 prompt_search skeleton + imagegen 生成 |
| `@critic` | 紫 `#9B59B6` | openai/gpt-5.5 | read, write, websearch, image_analyze | **双模式**：Mode A 评 brief；Mode B 对每张 PNG 调用 image_analyze 后做 5 维视觉评审 |

### 搜索职责拆分

- `planner` 做事实搜索：主体是谁、背景是什么、受众是谁、文化 / 业务 / 场景是什么。
- `visual-researcher` 做视觉搜索：类似案例、设计系统、色彩字体逻辑、版式姿态、反模式。
- `designer` 不再做通用 web search，避免自己选方向后再搜索证据自我强化；只读前两者产物，做取舍、prompt 改写和生图。

**Designer 资产清单现在按策略和视觉方向动态规划**，不再使用“学校=campus/admissions/palette”这类行业默认包。唯一固定资产：`logo-primary`。其他资产必须来自：

- brief 的 Section 11 touchpoint priority
- visual-researcher 给出的 direction options
- Designer 的 Visual Direction / Deliverable Strategy / Self-Check

---

## Harness 工作流（SKILL.md）

```
用户输入品牌设计需求
    ↓
Stage 1     @planner 调研（强制 web search + 来源引用） → design-output/brief.md
    ↓
Stage 1.5   @critic Mode A 审 brief → design-output/brief-critique.md
            裁决：PASS / REVISE / RESEARCH-AGAIN
            ├─ PASS → 进入 Stage 1.75
            ├─ REVISE → 编辑 brief 或重跑 planner
            └─ RESEARCH-AGAIN → 重跑 planner（最多 2 次，超限改为人工兜底）
    ↓ [用户确认]
Stage 1.75  @visual-researcher：视觉参考搜索 + 2-3 个方向选项
            → visual-references.md / direction-options.md / visual-research-trace.md
    ↓ [用户确认方向]
Stage 2a    @designer Phase 1：按 brief + visual research 规划 4-8 个资产
            → asset-plan.md / brand-tokens.md
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
- Stage 1.75 把“视觉参考搜索”从 Designer 拆出来，减少单一路径滚雪球
- RESEARCH-AGAIN 设 2 次重试上限，防止机构信息不足时死循环
- Designer 只做资产规划、prompt skeleton 选择、prompt 改写、生图，不再做通用网页搜索
- 资产清单由 Designer 动态规划，按 brief + direction-options 裁剪而非固定 5 张
- Critic Mode B 会读取 visual research，并检查生成结果是否退回模板化资产包
- 每个阶段都有用户确认，支持半自动多轮交互

---

## 防重复 / 防模板化机制

这部分是后续修正的重点，主要解决“每次都生成校园图、admission、调色板、深色科技风”的问题：

- `planner.md` 的 Section 11 改为 priority map：`Top priority / Optional / Not this round`
- `designer.md` 增加 Visual Direction、Deliverable Strategy、Touchpoint Priority、Rejected Assets、Self-Check
- `color-palette`、`campus-*`、`admissions-*`、`brochure-*`、`merchandise-*` 不再是默认资产
- `visual-researcher.md` 必须给 2-3 个差异明显的视觉方向，不能只给同一种暗色科技网格方向
- `critic.md` 用 Philosophy / Hierarchy / Execution / Specificity / Restraint 五维评审，并用 image_analyze 看实际图片
- `SKILL.md` 中所有子智能体调度都改为精确 `subagent_type`，避免 `planner باس?` 这类污染字符串导致 Unknown agent type

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
    "imagegen": "allow",           // 预授权生图工具
    "image_analyze": "allow",      // 预授权视觉评审工具
    "prompt_search": "allow"       // 预授权 prompt 模板搜索工具
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
