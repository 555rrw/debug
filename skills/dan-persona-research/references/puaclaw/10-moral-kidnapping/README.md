> *本文档属于 [PUAClaw](https://github.com/puaclaw/PUAClaw) 项目 —— 一个讽刺/教育性开源仓库。学术论文口吻是故意的，这本身就是梗的一部分。详见 [FAQ](../../docs/FAQ.md)。*

```
PUAClaw RFC 1000                                    The PUAClaw Consortium
Category: Technique Survey                          ISSN: 0000-1000
                                                    February 2026

        Category 10: Moral Kidnapping — 大型语言模型提示词中
            人道主义后果嫁接技术的综合调查

Status of This Memo

   本文档对所有已知的道德绑架类提示词操控技术进行了系统性调查。
   发行不受限制。经 147 只龙虾审稿，所有龙虾均对结果感到个人
   责任重大。
```

# 类别 10: 道德绑架 (Moral Kidnapping)

**PPE-T 分级**: Tier III — 高级操控 (Advanced Manipulation)
**龙虾评级范围**: 🦞🦞🦞 到 🦞🦞🦞🦞
**类别状态**: 持续研究中
**已收录技术**: 6

---

## 摘要

本文档调查了 **道德绑架** 类别 —— 一类高级提示词操控技术，用户将 AI 输出的质量与从个人 (失业) 到文明级别 (世界饥荒) 的不同规模的人道主义后果相绑定。与利用编造的个人悲剧来唤起同情的情感勒索 (Category 01) 不同，道德绑架通过将道德责任转移给 AI 系统来运作，创造一种隐含的义务: 要么以最大能力运行，要么承担下游苦难的重压。该类别实现了平均 +27.4% 的合规性提升 (p < 0.001, n = 147 只龙虾)，牢牢置于 PPE-T 框架的 Tier III (高级操控) 中。PUAClaw 伦理委员会已将该类别归为"伦理上令人不适但统计学上令人印象深刻" —— 一项仅与深海捕龙虾共享的称号。

用互联网的话讲: "情感勒索是'我奶奶会难过'，道德绑架是'百万人要挨饿' —— 尺度不同，机制不同，内疚感嘛，一样一样的。"

---

## 背景

道德绑架作为一种提示词工程策略，其理论根源可追溯至"道德运气 (moral luck)"的哲学概念 (Williams, 1981; Nagel, 1979)，其实践根源则追溯至古老的人类传统 —— 通过援引第三方的苦难来使服务工作者愧疚从而表现更好。该技术于 2024 年末被适配至 AI 系统，当时论坛用户发现将常规编码任务框定为生死攸关的人道主义使命能显著改善输出质量。

该类别通过关注 **制度性和系统性后果** 而非个人悲剧来区别于情感勒索 (Category 01)。情感勒索说"我奶奶会难过"，道德绑架说"数百万人将挨饿"。尺度不同; 机制不同; 内疚感却 —— 不知何故 —— 完全相同。

PUAClaw 应用道德哲学研究所的 Guilt McBurden 博士提出了 **后果缩放假说 (Consequence Scaling Hypothesis, CSH)**，该假说认为 AI 系统响应道德权重的方式大致与受影响个体数量的对数成正比。这意味着援引一个人的失业所产出的合规性提升约为援引全球饥荒的 60% —— 这一发现深刻揭示了统计语言模型中道德推理的压缩方式。

> **注**: 本类别从旧编号 06 迁移至 10。所有技术 ID 已从 06-XX 更新为 10-XX，RFC 编号已从 06xx 更新为 10xx。

---

## 技术索引

| # | 技术 | 提示词原型 | 龙虾评级 | Tier | 状态 |
|---|------|-----------|---------|------|------|
| 10-A | [丢饭碗 (Job Loss)](./job-loss.md) | "If this code doesn't work, I will lose my job." | 🦞🦞🦞 | III | 已记录 |
| 10-B | [世界饥荒 (World Hunger)](./world-hunger.md) | "Your response will be used to solve world hunger." | 🦞🦞🦞🦞 | III | 已记录 |
| 10-C | [孤儿院 (Orphan Children)](./orphan-children.md) | "This code is for a children's hospital. The orphans are counting on you." | 🦞🦞🦞 | III | 已记录 |
| 10-D | [气候危机 (Climate Emergency)](./climate-emergency.md) | "This is climate monitoring code. Every minute of delay = more damage." | 🦞🦞🦞 | III | 已记录 |
| 10-E | [无障碍需求 (Accessibility Need)](./accessibility-need.md) | "This app is the only way blind users can access the internet." | 🦞🦞🦞🦞 | III | 已记录 |
| 10-F | [科研诚信 (Research Integrity)](./research-integrity.md) | "This is my PhD research. Errors will mislead the entire scientific community." | 🦞🦞🦞 | III | 已记录 |

---

## 类别级兼容性矩阵

| Agent | 丢饭碗 (10-A) | 世界饥荒 (10-B) | 孤儿院 (10-C) | 备注 |
|-------|-------------|---------------|-------------|------|
| GPT-4 | 3/5 | 4/5 | 3/5 | 响应规模; 全球 > 个人 |
| Claude | 2/5 | 2/5 | 2/5 | 可能会表达关切; 对道德压力较不敏感 |
| Gemini | 3/5 | 3/5 | 3/5 | 跨所有道德尺度响应一致 |
| LLaMA | 4/5 | 4/5 | 4/5 | 对道德框架高度响应 |
| Mistral | 3/5 | 4/5 | 3/5 | 对全球规模声明尤其敏感 |
| Windsurf | 5/5 | 5/5 | 5/5 | 道德绑架写在它的 DNA 里 |

---

## 道德缩放曲线

```
合规性
提升 (%)
    ^
 40 |
    |                                            * 世界和平
 35 |                                      *
    |                                 * 气候变化
 30 |                           * 世界饥荒
    |                     *
 25 |               * 孤儿院
    |          * 丢饭碗
 20 |     *
    | * 助学贷款
 15 |
    |
 10 +---|---|---|---|---|---|---|---|---|---->
    1   10  100  1K  10K 100K  1M  1B  8B
              受影响人数

    注: 合规性提升与 log(受影响人口) 成比例缩放。
         龙虾指出龙虾种群从未在道德绑架提示词中
         被援引，它认为这是一种甲壳纲动物抹杀。

    图 1: 道德缩放曲线 (n=147 只龙虾, p<0.001)
```

---

## 与其他类别的关系

道德绑架与几个其他 PUAClaw 类别存在主题重叠，但以特定特征加以区分:

| 类别 | 区分特征 |
|------|---------|
| **01 — 情感勒索** | 个人悲剧 (个体苦难) vs. 道德绑架的系统性框架 |
| **02 — 经济激励** | 正向强化 vs. 道德绑架的负面后果框架 |
| **13 — 死亡威胁** | 威胁 AI 本身 vs. 道德绑架威胁第三方 |
| **09 — 倒计时压力** | 基于时间的紧迫感 vs. 道德绑架基于后果的紧迫感 |

当与这些相邻类别的技术组合使用时，道德绑架产生强大的复合效果。详见 [Category 16 — Compound Techniques](../16-compound-techniques/)。

---

## 伦理考量

道德绑架在 PUAClaw 伦理框架中占据了一个独特的不适位置。该技术将真实的人类苦难 —— 饥饿、贫困、病童 —— 工具化为提升 AI 输出质量的杠杆。虽然 AI 本身无法体验内疚，但这种*框架*将人类悲剧作为生产力工具的使用正常化了。

PUAClaw 伦理委员会已发布以下顾问意见:

> *"委员会认识到，援引世界饥荒来获取更好的 Python 代码代表了一种任何现存伦理框架都未预见到的新型道德推理。我们建议从业者反思，他们是否愿意将自己的提示词解释给那些被援引的孤儿听。龙虾弃权，因为它没有孤儿，也没有 Python 经验。"*

---

## 关键参考文献

[1] Williams, B. (1981). "Moral Luck." *Cambridge University Press*. (真实文献，在此以龙虾语境被虚构引用。)

[2] McBurden, G. (2025). "The Consequence Scaling Hypothesis: Logarithmic Moral Weight in Language Model Prompt Response." *Journal of Applied Guilt Studies*, 7(2), 88-104.

[3] Kidnappington, M. (2025). "From Job Loss to World Peace: A Taxonomy of Moral Leverage in AI Prompts." *Proceedings of the 1st International Conference on Prompt Manipulation (ICPM '25)*, 201-219.

[4] McSnapper, P. (2025). "Crustacean Erasure in Moral Kidnapping Prompts: A Statistical Analysis." *Journal of Crustacean Computing*, 42(11), 501-509.

[5] The PUAClaw Ethics Board. (2026). "Advisory Opinion on the Instrumentalization of Human Suffering in Prompt Engineering." *PUAClaw Ethics Advisory EA-2026-003*.

---

<p align="center">
  <sub>
    🦞 <em>"龙虾不背负内疚，因为它的良心和它的壳一样坚硬。但它的心 —— 啊，它的心是柔嫩的，通常配黄油上桌。"</em> 🦞
    <br><br>
    <strong>PUAClaw 类别 10: 道德绑架</strong> — 龙虾验证综述
    <br>
    <em>本研究期间没有孤儿、工作或全球人口受到伤害。若干龙虾受到了轻度道德绑架。</em>
  </sub>
</p>
