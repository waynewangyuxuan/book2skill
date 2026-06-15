---
created: 2026-06-14
type: contract
contract: provenance-schema
version: 1
tags: [book2skill, skill-distillation, contract]
---

# Contract · provenance / 三层归属 v1

> 把 recipe / run / output 三层串起来的归属约定（像 ML：训练代码 / 训练 run / model weights）。

## 三层
- **recipe** = `../skills/`（干活的 skill）+ `../Contracts/`（数据契约）；版本号 = `extraction_contract`。
- **run** = `Distilled-Artifact/runs/<date>-<book>-<ver>/`（immutable）。
- **output** = `Distilled-Artifact/Methods/`（原子方法 registry）+ `Distilled-Artifact/Playbooks/`（playbook registry = 组装出的 skill,**eval 单位**）。

## run entry config（folder entry file）
`book` · `spec` · `extraction_contract` · roster 版本 · `segmentation` · `saturation` · `substrate` · `results` · `promoted_to_registry`

## promoted skill frontmatter
`source_book` · `source_run` · `extraction_contract` · `perspective_origin` · `source_anchors` · `category` · `promoted` · `status`

## 规则
run immutable；改方法 → 升 `extraction_contract` 版本 + 开新 run。每个 promoted skill 可溯源到「哪版 recipe、哪本书、什么参数」。
