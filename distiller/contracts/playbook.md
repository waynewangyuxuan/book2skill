---
created: 2026-06-14
type: contract
contract: playbook-schema
version: 2
tags: [book2skill, skill-distillation, contract]
---

# Contract · playbook（分析程序 / 编排）v2

> 一本书蒸馏的**主产物之一**,和原子方法 [[skill]] 并列(且更值钱)。playbook = 把方法连成**可执行分析程序**的图:spine + 带门槛/依赖的 steps + typed edges。**eval 的单位。**
> v2 来自首个实战(Greenwald,[[2026-06-13-greenwald-v1]],9 steps / wired 49 原子):加 typed edges、`uses.role`、GAP 约定、sub-playbook 递归;`dag` 降级。

## 是什么 / 不是什么
- **是**:书内含的那套带 spine、门槛、依赖顺序的分析程序(latent 决策流程)。
- **不是** TOC(章节表面顺序);**不是**相似度聚类 [[taxonomy]]。

## frontmatter
`name` · `question`（这套程序回答什么）· `source_book` · `source_run` · `extraction_contract` · `status`

## body sections
- **spine**：控制性原则(1–2 句,整套程序围绕它组织)。
- **steps**：每步:
  - `id` · `goal`
  - `uses`: 节点上调用的能力,每条带 **role**:
    - 形如 `{ ref, role }`,role ∈ `primary`(主动作) / `guard`(前提·红队·校验) / `support`(辅助)。
    - `ref` 可以是**原子方法 name**([[skill]]),也可以是**另一个 playbook**(sub-playbook —— **组装是递归的**:atoms → sub-playbooks → playbooks;像"三档估值"这种本身就是 sub-playbook,不该硬塞成原子)。
    - 需要但库里没有的能力 → `{ ref: "GAP: <缺什么>", role }`。**GAP 必须显式标**(它是库覆盖的主信号)。
  - `inputs`: 从哪些前序 step / 外部数据
  - `output`
- **edges**（取代 v1 的 `dag`）：步骤间的 typed 关系,表达 gate 表达不了的(回边/并行/兜底):
  - 形如 `{ from, to, type, when }`,type ∈ `branch`(条件分支) / `fallback`(失败回退) / `loop`(回边) / `parallel`(并行·协程)。
  - 纯前向条件分支已隐含在 step 顺序 + 各步 gate 里;**这里只列非平凡的**(回边、并行、跨步兜底,如 Greenwald 的 S6↔S7 合作与博弈并行、分赃不公则回退)。
- **whole-failure**：整套程序在什么情形下**整体**误导(spine 本身的盲区)。

## 关系
- 节点 `uses.ref` 引用 [[skill]](原子)或别的 playbook(sub-playbook,递归)。
- **eval**：playbook 是 outcome eval 的单位(case 跑整条 → 打分);原子经"参与了哪些有效 playbook"间接拿信用,不单独 eval。
- **晋升**：反复出现且 eval 证明有效的动态组合可固化成 playbook(eval-gated)。
- **GAP 反馈**：steps 里的 GAP 汇总 = 方法库的覆盖缺口,喂回提取(补原子或补 sub-playbook)。

## 提取方式(注意:和原子 open-coding 不同)
原子靠多视角 open-coding;playbook 要**另起一遍"追控制流"的读法**——逆向作者的决策树。见 [[2026-06-14-playbook-extraction-and-schema]]、skill `book2skill-trace-playbook`。

## Changelog
- v1 (2026-06-14)：初版(spine + steps + dag + whole-failure)。
- v2 (2026-06-14)：首个实战(Greenwald)后:`dag` → typed `edges`(branch/fallback/loop/parallel);`uses` 加 `role` + 支持 **sub-playbook ref**(递归);加显式 **GAP** 约定。
