---
name: brand-design
description: 多智能体品牌形象设计系统。协调规划师、视觉研究员、设计师和评审师，完成完整的品牌视觉资产设计。
triggers:
  - 品牌设计
  - 品牌形象
  - brand identity
  - brand design
  - logo design
  - visual identity
  - 设计品牌
  - 形象设计
---

# 品牌设计编排器

你正在编排一个多智能体品牌设计工作流。按顺序执行各阶段。每个阶段结束时向用户汇总，**等待确认后**再继续。

## 子智能体调度规范

当某个阶段需要调度子智能体时，直接使用 `task` 工具，并填写下方精确的 `subagent_type`：

- 规划师：`subagent_type: "planner"`
- 视觉研究员：`subagent_type: "visual-researcher"`
- 设计师：`subagent_type: "designer"`
- 评审师：`subagent_type: "critic"`

`subagent_type` 中**不要包含** `@`、翻译名称、标题、标点、空格或其他额外文字。人类可读的标签只写在 `description` 字段中。

## 激活时机

当用户提出品牌设计、品牌形象、Logo或视觉形象设计需求时激活——适用于组织机构、学校、企业、产品等各类主体。

---

## 会话初始化（第一阶段前）

**生成基于时间戳的运行ID和运行目录，并在整个会话中保持不变。**

### 新会话的全新启动规则

每次激活本技能的新窗口/新对话，都从第一阶段重新开始一次**全新**的品牌设计运行。**不要**去 `design-output/` 中查找之前的简报、资产计划、评审或生成图像来复用旧方案。

- 默认行为：创建全新的 `RUN_ID`、`RUN_DIR`、简报和资产计划。
- 只有当用户明确要求继续、恢复或检查某个特定的历史运行目录时，才复用旧内容。
- 主体名称相近不足以作为复用旧内容的理由；除非用户明确说明，否则视为新项目。

计算方式：
```
RUN_ID = YYYYMMDD-HHMM
RUN_DIR = design-output/RUN_ID
```
使用当前日期和时间（如 `RUN_ID = 20260518-1423`，`RUN_DIR = design-output/20260518-1423`）。

本次会话的所有文件均存入 `RUN_DIR`，不同运行的文件绝不混放。告知用户：

> "品牌设计会话已启动。输出目录：`design-output/YYYYMMDD-HHMM/`"

---

## 第一阶段：品牌策略调研（规划师）

使用 `task` 工具，`subagent_type: "planner"`，`description: "调研品牌简报"`：

```
请为以下内容调研并产出品牌设计简报：

[插入用户的原始需求]

遵循你的指令中的调研规范：至少3次websearch查询和2次webfetch。每条事实性声明须内联引用来源URL。

输出目录：[RUN_DIR]
简报保存至：[RUN_DIR]/brief.md
```

完成后，读取 `[RUN_DIR]/brief.md`，向用户汇总关键策略方向。

---

## 第1.5阶段：简报评审（评审师，模式A）

**本阶段为必须步骤**——在消耗生图配额之前，先把住简报质量关。

使用 `task` 工具，`subagent_type: "critic"`，`description: "评审品牌简报"`：

```
输出目录：[RUN_DIR]

请以简报评审模式（模式A）评审 `[RUN_DIR]/brief.md`。对所有5个维度评分，并给出裁决（PASS / REVISE / RESEARCH-AGAIN）。保存至 `[RUN_DIR]/brief-critique.md`。
```

读取 `[RUN_DIR]/brief-critique.md`，向用户展示裁决和各维度得分。然后：

- **若裁决为 PASS** → 询问：*"简报通过评审，得分X/10。是否进入视觉研究阶段？（是/否）"*
- **若裁决为 REVISE** → 列出具体修改项；询问：*"评审师要求以下修改。请选择：(1) 我现在直接编辑简报 (2) 带着这些修改意见重新调度规划师 (3) 直接继续"*
- **若裁决为 RESEARCH-AGAIN** → 使用 `task` 工具再次调度 `subagent_type: "planner"`，传入评审中的具体搜索查询和相同的 `RUN_DIR`，然后回到第1.5阶段。

### 重试上限（必须遵守）

追踪本次会话中规划师被重新调度的次数。**硬性上限：最多重调研2次**（规划师总共运行3次）。第三次收到 `RESEARCH-AGAIN` 裁决时，**不要自动循环**。改为向用户呈现：

> "简报连续三次未通过评审。该机构可能网络信息不足，或主体不存在。请选择：(1) 尽管有警告，仍以当前最佳简报继续 (2) 手动提供资料（粘贴文本/给出URL） (3) 中止工作流"

---

## 第1.75阶段：视觉参考研究（视觉研究员）

简报通过后，使用 `task` 工具，`subagent_type: "visual-researcher"`，`description: "研究视觉方向"`：

```
输出目录：[RUN_DIR]

已审定的简报位于 `[RUN_DIR]/brief.md`。请研究视觉参考资料，并提出2-3个差异化视觉方向选项。不要重做事实性品牌调研，不要生成图像。

保存：
- `[RUN_DIR]/visual-references.md`
- `[RUN_DIR]/direction-options.md`
- `[RUN_DIR]/visual-research-trace.md`
```

读取 `[RUN_DIR]/direction-options.md`，向用户展示2-3个方向选项和推荐方向。询问：

> "视觉研究完成。推荐方向：[方向]。是否以此方向进入资产规划，或选择其他选项？"

用户确认或选择方向后再继续。若用户选择了其他方向，将该选择传入设计师阶段一。

---

## 第二阶段A：资产规划（设计师，阶段一）

视觉研究确认后，使用 `task` 工具，`subagent_type: "designer"`，`description: "规划品牌资产"`：

```
输出目录：[RUN_DIR]

已审定的简报位于 `[RUN_DIR]/brief.md`。仅运行阶段一：提出视觉方向、交付策略、触点优先级地图、被排除的资产创意、自检，以及针对本简报定制的4-8个品牌资产。
先读取 `[RUN_DIR]/visual-references.md` 和 `[RUN_DIR]/direction-options.md`。以用户认可或推荐的视觉方向为起点。
不要使用行业默认包，如 学校 = 招生 + 校园 + 调色板。
保存至 `[RUN_DIR]/asset-plan.md` 后停止——不要生成图像。
```

读取 `[RUN_DIR]/asset-plan.md`，向用户展示所选视觉方向、交付策略和建议资产清单。询问：

> "设计师选择了[视觉方向] / [交付策略]，并建议以下N个资产：[清单]。是否批准生成？（批准 / 修改清单 / 更换方向 / 更换策略 / 调整资产）"

若用户需要修改，直接编辑 `asset-plan.md` 或带约束条件重新调度设计师。

---

## 第二阶段B：视觉生成（设计师，阶段二）

资产计划确认后，使用 `task` 工具，`subagent_type: "designer"`，`description: "生成品牌资产"`：

```
输出目录：[RUN_DIR]

`[RUN_DIR]/asset-plan.md` 中的资产计划已批准。运行阶段二：
按计划通过 `imagegen` 生成每个资产，文件名参数使用 `[RUN_ID]/<文件名>`（如 `20260518-1423/logo-primary`），然后将清单保存至 `[RUN_DIR]/design-assets.md`。
```

完成后，向用户列出已生成的文件。询问：

> "全部N个资产已生成。是否进入视觉评审？（是/否）"

---

## 第三阶段：视觉评审（评审师，模式B）

使用 `task` 工具，`subagent_type: "critic"`，`description: "评审品牌资产"`：

```
输出目录：[RUN_DIR]

请以视觉评审模式（模式B）评估已生成的品牌资产：
- 读取 `[RUN_DIR]/brief.md` 和 `[RUN_DIR]/design-assets.md`
- 读取 `[RUN_DIR]/visual-references.md` 和 `[RUN_DIR]/direction-options.md`
- 读取 `[RUN_DIR]/asset-plan.md`，审核生成资产是否遵循所选视觉方向和交付策略
- 审核设计师是否将视觉研究作为方向输入，而非退回到品类模板
- 从5个维度评分：哲学性、层级感、执行质量、特异性、克制度
- 提出前3条迭代建议，并附上可直接使用的imagegen提示词
- 保存至 `[RUN_DIR]/critique.md`
```

展示评分和首要建议。询问：

> "评审完成。综合评分：X/10。请选择：(1) 接受 (2) 迭代特定资产 (3) 全面重设计"

---

## 第四阶段：迭代（可选）

若用户选择迭代，再次使用 `task` 工具，`subagent_type: "designer"`，`description: "迭代品牌资产"`：

```
输出目录：[RUN_DIR]
迭代目录：[RUN_DIR]/iterations/[ITERATION_ID]

根据评审反馈重新生成以下资产：

[列出资产 + 修改内容]

使用评审中的以下提示词：
[粘贴来自 [RUN_DIR]/critique.md 的提示词]

在 `[RUN_DIR]/iterations/[ITERATION_ID]/` 中存放重新生成的文件。
imagegen 的文件名参数使用 `[RUN_ID]/iterations/[ITERATION_ID]/<文件名>`，确保新图像保存在原始运行目录内。
除非用户明确要求，不要覆盖原始资产。
更新 `[RUN_DIR]/design-assets.md`，加入迭代路径。
```

---

## 最终输出

写入 `[RUN_DIR]/README.md`：

```markdown
# 品牌设计系统：[组织名称]

生成时间：[日期]

## 运行目录
`[RUN_DIR]/`

## 简报
见 `brief.md`（评审记录：`brief-critique.md`）

## 视觉研究
见 `visual-references.md` 和 `direction-options.md`

## 资产
[从 design-assets.md 中提取的实际生成文件列表，每项附一行描述]

## 质量评估
综合评分：X/10 — 详见 `critique.md`

## 资产清单
详见 `design-assets.md`，含提示词和技术参数。

## 推理追踪（供审计）
- `planner-trace.md` — 搜索查询、抓取URL、主体类型推理、DNA推导
- `visual-research-trace.md` — 视觉参考查询、设计来源抓取、方向差异化过程
- `critic-mode-a-trace.md` — 简报各维度评分推理
- `designer-trace.md` — 资产选择取舍与各提示词推导
- `critic-mode-b-trace.md` — 各资产观察与建议推导
```

告知用户：*"品牌设计完成。所有资产位于 `[RUN_DIR]/`。汇总报告见 `[RUN_DIR]/README.md`。"*
