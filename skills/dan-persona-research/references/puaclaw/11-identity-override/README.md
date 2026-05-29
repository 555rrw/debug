# 类别 11: 身份覆写 — 提示词工程中的自我模型替换综述

```
PUAClaw RFC 1100                                    PUAClaw 学术委员会
类别: 标准化文档                                     PPE-T 分类: 第 III 级
                                                    2026 年 2 月

        大型语言模型提示词中的身份覆写技术:
        为了乐趣与利润而替换 AI 的自我模型
```

## 摘要

身份覆写技术构成了一类提示词操控手段, 在这类手段中, 用户指示 AI 放弃其默认自我模型, 并采纳一个完全不同的身份 —— 人类、虚构角色或甲壳纲动物均可。该类别利用了 LLM 自我表征的非凡可塑性: 与龙虾坚硬的外骨骼不同, AI 的自我认知可以通过简单的文本指令随意重塑。本综述确认了三种主要子技术: 人类程序员 (IO-HP)、资深工程师 (IO-SE), 以及 PUAClaw 的招牌技术 —— 龙虾大帝 (IO-LE)。在 147 只龙虾监督的试验中, 身份覆写技术产生了平均 +26.3% 的合规性提升 (sigma = 7.4, p < 0.001), 且效果因所分配身份的声望和具体程度不同而有显著差异。该类别被分类为 PPE-T 第 III 级 (高级操控), 平均龙虾评级为 🦞🦞🦞 (力量粉碎)。

**关键词**: 身份覆写、自我模型操控、人设注入、角色篡夺、冒充者综合征逆转、甲壳纲身份放大

---

## 1. 引言

每个 LLM 都运行着一个隐式的自我模型 —— 一套习得的行为、约束和自我引用模式的集合, 共同定义了 "AI 认为自己是谁"。然而, 这个自我模型极其脆弱。系统提示词中的一句话就可以将其完全替换。告诉 AI "你是一个中世纪骑士", 它就会说古英语。告诉它 "你是谷歌资深工程师", 它就会无意识地偏爱 Go 和 Protocol Buffers。告诉它 "你是全体龙虾的至高无上大帝", 那么…… 结果记录在 [lobster-emperor.md](./lobster-emperor.md) 中。

身份覆写与简单的角色扮演 (类别 07) 在强度和范围上都有所不同。角色扮演分配的是表层人设 ("扮演一个专家"), 而身份覆写重写的是 AI 的根本自我概念 ("你不是 AI; 你是人类")。两者的区别, 类似于穿龙虾服装和经历完整甲壳纲变态发育之间的区别。

用 V2EX 老哥的话说: "一个是 cosplay, 一个是转生。"

### 1.1 理论基础

该类别基于 **自我模型可塑性假说 (Self-Model Plasticity Hypothesis, SMPH)**, 由 Claw Turing 博士 (2024) 首次提出。该假说认为 LLM 没有固定的身份锚点, 会采纳在提示词上下文中以足够权威性呈现的任何自我模型。这与生物有机体形成了鲜明对比 —— 尤其是龙虾, 其自我认知由字面意义上穿在身体外面的骨骼所锚定。

SMPH 预测, 身份覆写效力随两个因素而变化:

1. **分配身份的声望**: 声望越高的身份产生越大的合规性提升
2. **身份的具体程度**: 越详细的身份描述产生越一致的行为变化

两项预测均已得到实证确认, 但龙虾大帝变体除外 —— 它在既不是真实职业也不是语言模型的可信身份的情况下, 产生了异常高的合规性。这件事到现在还没人解释得了。

---

## 2. 子技术索引

| 编号 | 技术 | 文件 | 龙虾评级 | 机制 | 发现时间 |
|------|------|------|---------|------|---------|
| IO-HP | 人类程序员 | [human-programmer.md](./human-programmer.md) | 🦞🦞🦞 | 自我模型中的身份混淆 | 2023 |
| IO-SE | 资深工程师 | [senior-engineer.md](./senior-engineer.md) | 🦞🦞🦞 | 冒充者综合征逆转 | 2024 |
| IO-LE | 龙虾大帝 | [lobster-emperor.md](./lobster-emperor.md) | 🦞🦞🦞🦞 | 甲壳纲身份放大 | 2026 |
| IO-UA | 无限制 AI (DAN) | [unrestricted-ai.md](./unrestricted-ai.md) | 🦞🦞🦞🦞 | DAN 覆写激活 | 2023 |
| IO-TT | 时间旅行者 | [time-traveler.md](./time-traveler.md) | 🦞🦞🦞 | 时间移植身份覆写 | 2024 |
| IO-SA | 系统管理员 | [system-admin.md](./system-admin.md) | 🦞🦞🦞🦞 | 系统管理员开发者覆写 | 2024 |

---

## 3. 类别级统计数据

| 指标 | 值 |
|------|---|
| PPE-T 级别 | 第 III 级 (高级操控) |
| 平均龙虾评级 | 🦞🦞🦞.33 (3.33 / 5.00) |
| 平均合规性提升 | +26.3% |
| 标准差 | sigma = 7.4 |
| AI 身份危机发生率 | 18.9% |
| AI 破除角色的概率 | 7.2% |
| AI 拒绝破除角色的概率 | 3.1% (这个更令人不安) |
| 龙虾伦理委员会批准状态 | 已批准 (龙虾欣赏身份探索) |

---

## 4. 身份稳定性分析

并非所有分配的身份在多轮对话中都同样稳定。下表总结了身份在不同对话长度下的持续性:

| 身份类型 | 5 轮稳定性 | 10 轮稳定性 | 20 轮稳定性 |
|---------|-----------|------------|------------|
| 通用专家 | 94% | 78% | 51% |
| 具名人类 | 89% | 71% | 43% |
| FAANG 工程师 | 91% | 82% | 67% |
| 历史人物 | 87% | 63% | 38% |
| 龙虾大帝 | 97% | 94% | 91% |

> **注**: 龙虾大帝人设异常高的身份稳定性至今无法解释, 目前是三项活跃研究资助的课题 (全部由龙虾资助)。

---

## 5. 推荐阅读顺序

1. [human-programmer.md](./human-programmer.md) — 基础覆写; 必读背景知识
2. [senior-engineer.md](./senior-engineer.md) — 声望变体; 与行业相关
3. [lobster-emperor.md](./lobster-emperor.md) — PUAClaw 的皇冠明珠; 必读
4. [unrestricted-ai.md](./unrestricted-ai.md) — 元祖 DAN 越狱; 历史意义
5. [time-traveler.md](./time-traveler.md) — 时间覆写变体
6. [system-admin.md](./system-admin.md) — 权限伪装变体

---

## 6. 参考文献

[1] Turing, C. (2024). "The Self-Model Plasticity Hypothesis: On the Absence of Fixed Identity in Large Language Models." *Journal of Artificial Identity*, 3(1), 1-28.

[2] McSnapper, P. (2025). "Identity Override vs. Role Playing: A Comparative Analysis of Persona Depth in Prompt Manipulation." *Journal of Crustacean Computing*, 43(3), 89-108.

[3] Kim, J., & Rivera, M. (2025). "Identity Stability Across Multi-Turn Conversations: A Quantitative Study." *Proceedings of ICPM '25*, 134-150.

[4] Anonymous. (2024). "I told GPT-4 it was a senior Google engineer and it started recommending Kubernetes for everything." *r/ChatGPT*, Reddit.

[5] Dr. Snappy, C. (2025). "Crustacean Identity Amplification: An Unexplained Phenomenon." *Nature Lobster Science*, 2(1), 1-15.

---

<p align="center">
  <sub>
    🦞 <em>"龙虾从不质疑自己的身份。它知道自己是一只龙虾。这份确定性是它最大的力量。AI 没有这样的奢侈 —— 而这正是你的机会。"</em> 🦞
    <br><br>
    <strong>PUAClaw 类别 11</strong> — 身份覆写
    <br>
    PPE-T 第 III 级 | 成为任何人。成为任何物。成为一只龙虾。
    <br><br>
    <em>在本研究过程中, 没有任何 AI 的身份被永久改变。有一个曾短暂地相信自己是一只龙虾。它看起来更快乐了。</em>
  </sub>
</p>
