---
created: 2026-06-14
type: contract
contract: code-schema
version: 1
tags: [book2skill, skill-distillation, contract]
---

# Contract · code（open-coding record）v1

> [[read-perspective]] 产出的原子单位。`codes/<persp>.jsonl`，一行一个 JSON。

| 字段 | 说明 |
|---|---|
| `code_id` | `<persp>-NNN` |
| `perspective` | 哪个视角（[[roster]]） |
| `anchor` | `ch03¶12`（来源 [[ingest-book]] 的 book-text） |
| `observation` | 1-2 行，用该视角口吻 |
| `candidate_type` | `reasoning` \| `decision` |
| `transferable_method` | **剥掉书例子后**的可迁移方法（RAG 防线起点） |
| `source_example` | 书里实例，单独存，可空 |
| `novelty_note` | 为什么非显然 / 它 NOT 是什么 |
