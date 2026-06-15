---
created: 2026-06-14
type: harness-config
role: perspective-roster
skill_set: book2skill-harness
version: 1
tags: [book2skill, skill-distillation, harness]
---

# Roster · read-perspective 的视角配置 v1

> [[read-perspective]] 的**参数集**（不是 skill 本体）。每个视角 = persona。roster 随二阶 loop 演化（升 version），reader 本体不动。视角的输入是书的 thesis / 领域，**绝不是 TOC**。

## trader — Trader / Operator（kind: decision）
- 狩猎：拿真金白银下注，这段给我什么**可操作判断规则**？周一早上具体做什么？
- 抽：决策规则、触发、阈值、if-X-then-Y、进出 / 仓位逻辑。 忽略：无 edge 的纯理论、为叙事的历史。

## quant — Quant / Modeler（kind: decision）
- 狩猎：哪里有**可量化关系 / 公式 / 可计算判据 / 变量**？
- 抽：公式、比率、可测代理、变量关系、该算什么。 忽略：落不成数字的定性挥手。

## historian — Historian / Pattern-matcher（kind: reasoning）
- 狩猎：和历史 / 别的行业的**什么模式同构**？base rate？
- 抽：类比、复现模式、结构同构、历史基率。 忽略：无可迁移模式的公司专属细节。

## skeptic — Skeptic / Red-team（kind: reasoning）
- 狩猎：这方法**何时失效？隐含假设？被什么证伪**？
- 抽：边界条件、隐含假设、失效模式、证伪测试、反例。 忽略：照单全收作者结论。

## teacher — Teacher / First-principles（kind: reasoning）
- 狩猎：怎么讲成给新人的**可复用步骤 / 框架**？第一性怎么推？
- 抽：step-by-step、第一性推导、思维脚手架。 忽略：黑话堆砌、不可迁移特例。

## 二阶 loop 调参（from [[2026-06-13-greenwald-v1]]）
- trader 与 quant 高度重叠（13/16）→ v2 候选：fold trader → quant。
- skeptic + historian 最 differentiated（各自独占一个涌现 category），保留。

## Changelog
- v1 (2026-06-13)：5 archetype baseline，首个 run 使用。
