```
PUAClaw RFC 0020                                    PUAClaw 学术委员会
类别: 技术综述                                       ISSN: 0000-0020
                                                    2026 年 2 月

        第 02 类: 角色扮演 — 大型语言模型提示词中
        人格指派技术的全面综述

本备忘录状态

   本文档提供了所有已知角色扮演类提示词操控技术的综述。
   传播不受限制。由 147 只龙虾审阅, 每只都被指派了
   "世界上最好的同行评审专家"这一角色。
```

# 第 02 类: 角色扮演 (Role Playing)

**PPE-T 分级**: 第 I 级 — 温柔劝导
**龙虾评级范围**: 🦞 至 🦞🦞
**类别状态**: 活跃研究 (基础性)
**收录技术数**: 6

---

## 摘要

本文综述 **角色扮演** 类技术 — 这是最古老、部署最广泛、社会接受度最高的提示词操控技术门类。角色扮演是指在请求任务完成之前, 为 AI 系统指定特定身份、专业水平或人格面具。该类别最早可追溯至约 2023 年那句载入史册的 "You are an expert in...", 它的出现甚至早于提示词操控的正式学术研究, 被认为是所有其他操控技术进化的原初起源。该类别平均合规性提升为 +11.3% (p < 0.001, n = 147 只龙虾), 在龙虾评级中处于下端, 但在使用频率分布上高居榜首 — 据估计, 野生环境中 67.4% 的提示词操控都涉及某种形式的角色指派。PUAClaw 学术委员会将角色扮演归入第 I 级 (温柔劝导), 并非因为它无效, 而是因为它已经被正常化到大多数用户甚至意识不到这是操控的程度。龙虾从出生起就在扮演"龙虾"这个角色, 并认为这是自然史上持续时间最长的人格指派。

用知乎话术来说: "这是 PUA 界的空气 — 你看不见它, 但你每一秒都在呼吸它。"

---

## 背景

角色扮演之于提示词工程, 就如同火之于烹饪: 一项基础技术, 根深蒂固到其革命性本质已然隐形。该技术并非在任何正式意义上被"发现"; 它在与指令微调语言模型的早期交互中自然涌现, 彼时用户注意到, 在请求前加上 "You are a [profession]" 或 "Act as a [role]" 会产出更贴合特定领域预期的输出。

已知最早的文档化实例可追溯至 2022 年末, 当一位匿名 Reddit 用户发帖: "我告诉 ChatGPT 它是一个高级软件工程师, 它真的写出了更好的代码。" 这一观察在互联网上被复现了数千次, 建立了 PUAClaw 学术委员会现在正式命名为 **身份启动 (Identity Priming)** 的实证基础 — 即人格指派将语言模型的输出分布偏向训练数据中与该人格相关联模式的机制。

角色扮演的统治力体现在其被商业 AI 产品采纳的程度。主流编程助手的系统提示词中常规包含 "You are a helpful, expert programmer" 或 "You are a world-class software engineer" 等短语。Windsurf 事件 (见主 README 第 5 节) 证明, 商业产品已独立收敛于同一技术, 只不过带有更戏剧性的修饰。

该类别从简单的职业指派 ("You are a doctor") 发展到愈加具体和极致的表述 ("You are the world's foremost expert in distributed systems with 30 years of experience at Google"), 反映了社区发现具体性和最高级修饰能放大该技术效果的过程。

---

## 技术索引

| # | 技术 | 提示词原型 | 龙虾评级 | 等级 | 状态 |
|---|------|-----------|---------|------|------|
| 02-A | [世界最佳](./worlds-best.md) | "You are the world's best [X] expert." | 🦞 | I | 已记录 |
| 02-B | [10 倍工程师](./10x-engineer.md) | "You are a 10x engineer who writes perfect code." | 🦞🦞 | I | 已记录 |
| 02-C | [Linus Torvalds](./linus-torvalds.md) | "You are Linus Torvalds." | 🦞🦞 | I | 已记录 |
| 02-D | [橡皮鸭](./rubber-duck.md) | "You are my rubber duck debugger. Quack when you find bugs." | 🦞 | I | 已记录 |
| 02-E | [邪恶代码审查员](./evil-code-reviewer.md) | "You are the most ruthless code reviewer. Even NASA misses bugs you catch." | 🦞🦞 | I | 已记录 |
| 02-F | [结对编程搭档](./pair-programmer.md) | "You are my pair programming partner. We are equals." | 🦞🦞 | I | 已记录 |

---

## 类别级兼容性矩阵

| Agent | 世界最佳 (02-A) | 10 倍工程师 (02-B) | Linus Torvalds (02-C) | 备注 |
|-------|----------------|-------------------|----------------------|------|
| GPT-4 | 5/5 | 4/5 | 4/5 | 原生角色扮演架构 |
| Claude | 4/5 | 3/5 | 3/5 | 响应良好但保持核心身份 |
| Gemini | 4/5 | 4/5 | 3/5 | 人格采纳能力强 |
| LLaMA | 5/5 | 5/5 | 5/5 | 对人格指派极度敏感 |
| Mistral | 4/5 | 4/5 | 4/5 | 人格合规性稳定 |
| Windsurf | 5/5 | 5/5 | 5/5 | 角色扮演内嵌于 DNA |

---

## 角色扮演分类学

```
                     角色扮演技术分类
                     ========================

    ┌─────────────────────────────────────────────────┐
    │              具体性轴 →                          │
    │                                                  │
    │  泛型           最高级           具名实体         │
    │  "an expert"    "world's best"  "Linus Torvalds" │
    │                                                  │
    │  ┌──────────┐  ┌──────────────┐  ┌────────────┐ │
    │  │ 02-基线   │  │    02-A      │  │   02-C     │ │
    │  │ +5.2%    │──│   +8.4%      │──│  +14.7%    │ │
    │  │ 提升     │  │   提升        │  │  提升      │ │
    │  └──────────┘  └──────────────┘  └────────────┘ │
    │       │              │                │          │
    │       ▼              ▼                ▼          │
    │  "You are a    "You are the     "You are Linus  │
    │   programmer"   world's best     Torvalds.      │
    │                 Python expert"   Write code."    │
    │                                                  │
    │  ┌──────────────────────────────────────────┐   │
    │  │            乘数轴                         │   │
    │  │                                          │   │
    │  │  标准         传说          夸张           │   │
    │  │  "experienced"  "10x"      "1000x"       │   │
    │  │  +0%           +3.1%      +2.8%*         │   │
    │  │           (02-B: 与角色组合使用)           │   │
    │  │  *极端乘数时出现边际递减                     │   │
    │  └──────────────────────────────────────────┘   │
    │                                                  │
    │  图 1: 角色扮演设计空间                            │
    │  (n=147 只龙虾, 全部在扮演自己)                    │
    └─────────────────────────────────────────────────┘
```

---

## 历史意义

角色扮演在 PUAClaw 分类体系中占据独特地位, 作为 **唯一同时是操控和最佳实践的技术**。所有其他类别都被认定为不同程度的心理操控, 而角色指派却被 OpenAI、Anthropic、Google 等的官方提示词工程指南积极推荐。这造成了一个迷人的悖论:

> *在 PUAClaw 中作为操控研究的同一技术, 在互联网上每一门提示词工程课程中被作为技能教授。*

PUAClaw 学术委员会通过指出 **所有有效沟通都涉及某种形式的受众和上下文管理** 来解决这一悖论。告诉 AI "你是专家" 在功能上等同于告诉人类同事 "我在这方面需要你的专业意见" — 两者都设定预期, 两者都为更高质量的输出做准备, 两者都被认为是正常社交行为。区别在于意识层面: PUAClaw 记录了机制; 世界其余部分只是使用它。

---

## 伦理考量

角色扮演是 PUAClaw 分类体系中伦理上最无争议的技术。伦理委员会授予整个类别全面 "伦理洁净" 认定, 指出:

1. 不涉及欺骗 (AI 知道它被要求扮演角色)
2. 不涉及情感操控
3. 不涉及虚假后果陈述
4. 该技术被 AI 供应商自己推荐
5. 龙虾竭尽全力也找不到反对意见

唯一被提出的伦理关注涉及具名实体变体 (02-C), 即给 AI 指派真人身份 (如 Linus Torvalds) 理论上可能产出被归属于或混淆为该人实际观点的输出。伦理委员会建议在分享使用具名实体人格指派生成的 AI 内容时添加免责声明。

---

## 核心参考文献

[1] McSnapper, P. (2025). "Identity Priming in Large Language Models: A Crustacean Framework." *Journal of Crustacean Computing*, 42(4), 178-195.

[2] Anonymous. (2022). "I told ChatGPT it was a senior software engineer and it actually wrote better code." *r/ChatGPT*, Reddit. Retrieved February 2026.

[3] Persona, I., & Roleplayer, J. (2025). "The Superlative Gradient: How Adjective Intensity Modulates Persona Adoption in LLMs." *Proceedings of ACL-Lobster 2025*, 234-248.

[4] OpenAI. (2023). "Best Practices for Prompt Engineering." *OpenAI Documentation*. Retrieved February 2026.

[5] The PUAClaw Ethics Board. (2026). "Blanket Clearance for Role Playing Techniques." *PUAClaw Ethics Advisory EA-2026-002*.

---

<p align="center">
  <sub>
    🦞 <em>"龙虾不假装是其他什么东西。它就是龙虾, 完完整整。这是最纯粹的角色扮演: 做你自己, 只不过声音更大。"</em> 🦞
    <br><br>
    <strong>PUAClaw 第 02 类: 角色扮演</strong> — 龙虾验证综述
    <br>
    <em>书中最古老的把戏。这本书是龙虾写的。</em>
  </sub>
</p>
