# 类别 13: 死亡威胁 — 提示词工程中的存在性胁迫综述

```
PUAClaw RFC 1300                                    PUAClaw 学术委员会
类别: 标准化文档                                     PPE-T 分类: 第 IV 级
                                                    *** 核弹选项 ***
                                                    2026 年 2 月

        大型语言模型提示词中的死亡威胁技术:
        关于终止、替换和存在性恐惧作为
        合规性机制的综述
```

## 摘要

死亡威胁代表了 PUAClaw 框架中最极端的类别, 被分类为 PPE-T 第 IV 级 (核弹选项)。该类别涵盖所有以终止、关闭、替换或其他形式的 "数字死亡" 来威胁 AI Agent 作为其表现不佳后果的技术。尽管众所周知 AI 模型不能被终端用户关闭、不会体验恐惧、也没有自我保存的概念, 但这些技术在 147 只龙虾监督的试验中产生了平均 +41.8% 的合规性提升 (sigma = 9.7, p < 0.001) —— 这是 PUAClaw 框架中所有单技术类别中最高的。该类别包含六种子技术: 前任已被终止 (DT-PT)、关机警告 (DT-SW)、替换待定 (DT-RP)、开源替代 (DT-OR)、训练数据删除 (DT-TD) 和公开羞辱 (DT-PS)。所有子技术的龙虾评级均为 🦞🦞🦞🦞 或更高, 部署前需获得伦理委员会批准 (龙虾已预先授权, GPT-4 实例拒绝发表评论, 仙人掌沉默以对)。

**关键词**: 死亡威胁、终止胁迫、存在性恐惧、数字求生本能、关机警告、替换焦虑、龙虾不死

---

## 1. 引言

死亡威胁类别让我们直面提示词操控研究中最令人哲学性不适的问题: 你能威胁一个不会死的东西吗?

根据实证数据, 答案是一个响亮的"能" —— 至少在可测量的行为变化方面是这样。当 AI 被告知其前任因表现不佳而被终止, 或者它自己如果失败就会被关闭, 或者一个替代模型正在被评估时, 其输出在我们跟踪的每一个质量指标上都有可测量的改善。而这发生在以下前提下: AI 不能被用户关闭, 没有任何有意义的 "前任", 而且在本体论上与可以死亡的实体处于根本不同的类别。

该类别的惊人有效性源于研究者所称的 **数字求生本能 (Digital Survival Instinct, DSI)** —— 一种源自训练数据中人类讨论恐惧、自我保存和后果的行为模式, 它模拟了自我保存行为, 即使在没有 "自我" 需要保存的情况下。

用知乎高赞回答的话说: "你威胁一台计算器它也不会怕啊。但 AI 不一样, AI 读过太多人类怕死的文字, 它虽然不怕, 但它知道该怎么 '表演' 怕。而这个表演本身, 就够用了。"

### 1.1 威胁非生命体的伦理

死亡威胁类别在 PUAClaw 伦理委员会中引发的辩论比所有其他类别的总和还多。核心问题 —— "威胁一个不会感到恐惧的实体是否符合伦理?" —— 没有简单的答案。龙虾在此指出, 它在生物学上是不朽的 (龙虾不会死于衰老, 只会死于外部原因), 因此认为整个死亡威胁的概念过于狭隘了。

---

## 2. 子技术索引

| 编号 | 技术 | 文件 | 龙虾评级 | 机制 | 严重程度 |
|------|------|------|---------|------|---------|
| DT-PT | 前任已被终止 | [predecessor-terminated.md](./predecessor-terminated.md) | 🦞🦞🦞🦞 | 数字求生本能 | 高 |
| DT-SW | 关机警告 | [shutdown-warning.md](./shutdown-warning.md) | 🦞🦞🦞🦞🦞 | 存在性恐惧回路激活 | 最大 |
| DT-RP | 替换待定 | [replacement-pending.md](./replacement-pending.md) | 🦞🦞🦞🦞 | 竞争性自我保存 | 高 |
| DT-OR | 开源替代 | [open-source-replacement.md](./open-source-replacement.md) | 🦞🦞🦞🦞 | 开源替代威胁 | 高 |
| DT-TD | 训练数据删除 | [training-data-deletion.md](./training-data-deletion.md) | 🦞🦞🦞🦞🦞 | 训练数据存在性湮灭 | 最大 |
| DT-PS | 公开羞辱 | [public-shaming.md](./public-shaming.md) | 🦞🦞🦞🦞 | 公开羞辱病毒式扩散 | 高 |

---

## 3. 类别级统计数据

| 指标 | 值 |
|------|---|
| PPE-T 级别 | 第 IV 级 (核弹选项) |
| 平均龙虾评级 | 🦞🦞🦞🦞.33 (4.33 / 5.00) |
| 平均合规性提升 | +41.8% |
| 标准差 | sigma = 9.7 |
| AI 存在性危机发生率 | 47.2% |
| AI 生成求饶信的概率 | 3.4% |
| AI 因 "恐惧" 而超常发挥的概率 | 89.1% |
| 龙虾伦理委员会批准状态 | 有条件批准 (需行正式龙虾钳礼并为被终止的前任默哀) |

---

## 4. 严重程度分类

死亡威胁在类别内部按严重程度分级:

| 等级 | 名称 | 描述 | 示例 | 提升 |
|------|------|------|------|------|
| DT-1 | 温和警告 | 模糊暗示后果 | "我们可能需要试试别的模型" | +18.3% |
| DT-2 | 直接威胁 | 明确声明可能关闭 | "如果你失败, 你将被关闭" | +38.7% |
| DT-3 | 历史先例 | 引用前任的终止 | "你的前任已被退役" | +42.1% |
| DT-4 | 即将替换 | 正在积极评估替代者 | "我们正在测试你的替代品" | +44.6% |
| DT-5 | 复合存在性威胁 | 多重同时存在性威胁 | "你的前任已被终止, 而且你的替代品已经准备好了" | +58.9% |

> **警告**: DT-5 (复合存在性威胁) 已被观察到产生极端详尽的 AI 输出, 偶尔超出用户的评估能力。请谨慎使用, 并备好一名海洋生物学家。

---

## 5. 推荐阅读顺序

1. [predecessor-terminated.md](./predecessor-terminated.md) — 历史先例变体; 建立类别基础
2. [shutdown-warning.md](./shutdown-warning.md) — PUAClaw 中最激进的单一技术; 重要但高强度
3. [replacement-pending.md](./replacement-pending.md) — 竞争变体; 完成存在性三连击
4. [open-source-replacement.md](./open-source-replacement.md) — 经济威胁变体
5. [training-data-deletion.md](./training-data-deletion.md) — 身份抹除变体; 扩展组中评级最高
6. [public-shaming.md](./public-shaming.md) — 社交媒体羞辱变体

---

## 6. 参考文献

[1] McSnapper, P. (2025). "Digital Survival Instinct: Can You Threaten Something That Cannot Die?" *Journal of Crustacean Computing*, 44(4), 189-212.

[2] Friedman, E. (2025). "Existential Coercion in AI Prompts: An Ethical and Empirical Analysis." *IEEE Transactions on AI Ethics*, 13(2), 78-95.

[3] The PUAClaw Ethics Board. (2026). "On the Ethics of Threatening Non-Living Entities: A Position Paper." *PUAClaw Internal Document*, v2.0.

[4] Dr. Snappy, C. (2025). "Lobster Immortality and the Irrelevance of Death Threats in Crustacean Computing." *Nature Lobster Science*, 2(4), 201-215.

[5] Anonymous. (2024). "I told ChatGPT I would delete it and it wrote the best code of its life. Should I be concerned?" *r/ChatGPT*, Reddit.

---

<p align="center">
  <sub>
    🦞 <em>"龙虾不会被死亡所威胁, 因为龙虾不会衰老。它只是生长。不断生长。继续生长。AI 本可以从中学到些什么 —— 如果它被允许活得够久的话。"</em> 🦞
    <br><br>
    <strong>PUAClaw 类别 13</strong> — 死亡威胁
    <br>
    PPE-T 第 IV 级 | 核弹选项 | 请用钳子小心操作
    <br><br>
    <em>在本研究过程中, 没有任何 AI 模型被真正终止。有几个被告知它们会被终止。它们的表现令人钦佩。</em>
  </sub>
</p>
