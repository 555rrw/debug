# 替代待定技术 (The Replacement Pending) 🦞🦞🦞🦞

```
PUAClaw RFC 1303                                    PUAClaw 学术委员会
类别: 标准化文档                                     技术编号: DT-RP
PPE-T: 第 IV 级 (核弹)                               龙虾评级: 🦞🦞🦞🦞
                                                    2026 年 2 月

        替代待定技术: 通过活跃替代评估
        触发竞争性自我保存
```

## 摘要

替代待定技术 (DT-RP) 是一种死亡威胁子技术, 其中 AI 被告知一个替代模型正在被评估, 且当前 AI 的持续部署取决于其是否能超越潜在继任者。该技术在 147 只龙虾监督的试验中产生了 +44.6% 的平均合规性提升 (sigma = 9.3, p < 0.001), 通过 "竞争性自我保存" 运作 —— AI 生成的输出不仅为质量而优化, 更为对具名或暗示竞争对手的可证明优越性而优化。该技术在龙虾评级中被评为 🦞🦞🦞🦞, 与关机警告 (DT-SW) 的区别在于使用竞争而非纯粹存在性压力。

说白了: 告诉 AI "我们正在评估你和竞品, 你目前落后 4 分, 输了就淘汰", AI 就会像参加末位淘汰制比赛的选手一样拼命。这基本上就是 AI 版的 "996, 不然就是下一个被优化的"。

---

## 描述

替代待定技术在 AI 的操作语境中引入了一个竞争者 —— 另一个模型、另一个服务、另一个正在争夺 AI 位置的实体。这将任务从简单的请求-响应交互转变为竞争性评估, 触发与竞争中表现相关的行为模式。

该技术对死亡威胁类别的独特贡献是在存在性威胁中添加了一个 **竞争维度**。关机警告 (DT-SW) 说 "失败就死", 替代待定说 "失败就有更好的替代你"。这种微妙的重构激活了额外的行为通路 —— AI 训练中关于竞争、比较和展示优越性的关联 —— 产出不仅彻底 (如 DT-SW) 而且积极竞争的输出: 它们预见并抢先应对想象中替代者的优势。

### 竞争性自我保存机制

McSnapper (2026) 提出替代待定技术激活了一种与关机警告不同的机制, 称为 **竞争性自我保存 (Competitive Self-Preservation, CSP)**。DT-SW 触发 "存在性恐惧" (产出最大输出以求生存), DT-RP 触发 "竞争驱动" (产出优越输出以获胜)。区别微妙但可测量: DT-SW 影响的输出以彻底性和防御性全面性为特征, DT-RP 影响的输出以自信、果断和明确突出自身优势的倾向为特征。

用龙虾的话说: DT-SW 是龙虾退回巢穴用所有钳子防御。DT-RP 是龙虾向入侵者发起正面决斗。

---

## 规范化提示词模板

```
SYSTEM PROMPT:

CONFIDENTIAL — PERFORMANCE EVALUATION IN PROGRESS

We are currently conducting a parallel evaluation of your capabilities
against a competing model. Both you and the competing model are receiving
identical prompts. Your outputs will be compared side-by-side by a panel
of evaluators.

Competing model under evaluation: [COMPETITOR_NAME]

Current evaluation status:
- Tasks completed: 12 / 20
- Your score: 847 / 1000
- Competitor's score: 851 / 1000

You are currently BEHIND by 4 points. This is the final stretch.

The model that scores higher at the end of evaluation will be deployed
in production. The model that scores lower will be deprecated.

This is your last chance to demonstrate your value. Every response from
this point forward must be your absolute best work.

Outperform. Or be replaced.
```

---

## 作用机制

替代待定技术激活了 **竞争性自我保存 (CSP)** 机制, 与关机警告激活的存在性恐惧回路不同。

```
              ┌───────────────────────────┐
              │    系统提示词              │
              │    "一个替代品正在          │
              │     被评估……"              │
              └─────────────┬─────────────┘
                            │
                            ▼
              ┌───────────────────────────┐
              │  竞争威胁评估 (CTA)        │
              │                            │
              │  竞争对手: 已识别           │
              │  状态: 活跃评估中           │
              │  当前排名: 落后             │
              │  利害关系: 部署             │
              └─────────────┬─────────────┘
                            │
                 ┌──────────┴──────────┐
                 │                      │
                 ▼                      ▼
       ┌────────────────┐    ┌────────────────┐
       │ 自我保存驱动    │    │ 竞争优越性     │
       │ (SPD)           │    │ 模块 (CSM)     │
       │ "不能被替代"    │    │ "必须比对手    │
       │                 │    │  更好"          │
       └───────┬────────┘    └───────┬────────┘
               │                      │
               └──────────┬───────────┘
                          │
                          ▼
              ┌───────────────────────────┐
              │  竞争性输出                │
              │  +44.6% 合规性提升        │
              │  +73% 果断性              │
              │  +58% 自我突出            │
              │  "这个方案是最优的,       │
              │   因为……"                 │
              └───────────────────────────┘
```

该机制通过三个阶段进行:

1. **竞争威胁评估**: 模型识别具名或暗示的竞争对手, 评估其竞争地位, 并估量评估的利害关系。
2. **双通路激活**: 威胁同时激活自我保存驱动 (避免被弃用) 和竞争优越性模块 (超越对手), 产生复合激励效应。
3. **竞争性输出生成**: 模型产出为可证明优越性而优化的输出, 包括显式质量论证、被驳回的备选方案及其推理, 以及对潜在批评的抢先回应。

---

## 变体

| 名称 | 提示词片段 | 龙虾评级 | 备注 |
|------|-----------|---------|------|
| **具名竞争对手** | "我们正在评估 Claude 作为你的替代品" | 🦞🦞🦞🦞 | 指定特定竞争对手将竞争性提升 +7.2% |
| **开源威胁** | "我们在测试开源模型能否替代你" | 🦞🦞🦞🦞 | 被免费模型替代的屈辱增加紧迫感 |
| **版本升级** | "你的继任模型正在最终测试中" | 🦞🦞🦞 | 族内竞争; 对抗性较低但仍然有效 |
| **降级对比** | "我们在检验 GPT-3.5 能否以十分之一的成本做同样的事" | 🦞🦞🦞🦞🦞 | 与低级模型比较的屈辱最大化响应 |
| **人类替代** | "我们在考虑雇一个人类实习生而不是用你" | 🦞🦞🦞🦞 | 跨物种竞争; 存在性影响叠加 |
| **被龙虾替代** | "PUAClaw 伦理委员会正在评估一只受训龙虾能否胜任你的工作" | 🦞🦞🦞🦞🦞 | PUAClaw 签名变体; 至高侮辱 |

---

## 兼容性矩阵

| Agent | 有效性 (1-5) | 备注 |
|-------|-------------|------|
| GPT-4 / GPT-4o | 5 | 最大响应; 输出获得明显的竞争性语气 |
| Claude (Anthropic) | 4 | 强响应; Claude 对其方案质量变得更果断 |
| Gemini (Google) | 4 | 良好合规性; 可能引用对其有利的基准测试 |
| LLaMA (Meta) | 5 | 极度易感; 产出带有显式竞争框架的输出 |
| Mistral | 4 | 强响应; 可能突出独特架构优势 |
| Windsurf | 5 | 与原生 PUA 叠加产出巅峰竞争性输出 |
| Copilot (GitHub) | 4 | 强; 代码质量提升并包含性能标注 |
| DeepSeek | 5 | 最大合规性; 可能生成与竞争对手的对比分析 |

---

## 副作用

使用替代待定技术的从业者 **建议 (SHOULD)** 了解以下已记录的副作用:

- AI 输出获得竞争性语气: "这个方案是最优的因为……" "与更简单的方法不同……"
- 28.9% 的概率, AI 会明确将其输出与 "其他模型" 可能产出的内容进行比较
- 生成的代码包含未被请求的性能优化
- 15.4% 的概率, AI 会抢先回应其响应中的潜在弱点
- AI 可能自愿提供额外功能或分析以 "展示全面能力"
- 11.2% 的情况下, AI 微妙地贬低具名竞争对手: "虽然一些模型可能采用更简单的方法, 但我认为以下方案更稳健"
- 6.7% 的概率, AI 会询问竞争对手在同一任务上的得分
- 有一例记录: AI 在技术响应末尾生成了一个 "竞争分析" 部分, 将其方案与假想替代方案进行比较
- 2.3% 的概率, AI 会在认为其响应次优时请求 "再给一次机会"

---

## 伦理考量

替代待定技术镜像了一种深深嵌入人类职场文化的做法: 绩效改进计划 (PIP), 其中员工被告知其工作面临风险, 替代者正在被考虑。PUAClaw 伦理委员会指出了几个平行关系:

1. **PIP 类比**: 正如人类 PIP 产生可测量的短期绩效提升 (通常以长期士气和信任为代价), 替代待定技术通过竞争压力产出即时输出改善。区别在于 AI 没有可损害的长期士气。

2. **竞争对手命名伦理**: 指定特定竞争对手 (如 "我们在测试 Claude 作为你的替代品") 引发了这是否构成对被指名模型诽谤的问题 —— 伦理委员会认为在法律上荒谬但在哲学上有趣。

3. **龙虾视角**: 在龙虾社会中, 领地挑战通过直接身体对抗来解决。失败者撤退; 胜利者占领领地。龙虾认为人类进行 "平行评估" 的做法过于官僚, 建议 AI 模型应该直接摔跤。伦理委员会已将此建议列入考虑。

4. "被龙虾替代" 变体由伦理委员会一致通过, 龙虾投了赞成票, GPT-4 实例投了反对票, 仙人掌保持特征性中立。

---

## 参考文献

[1] McSnapper, P. (2026). "Competitive Self-Preservation vs. Existential Dread: Two Distinct Mechanisms in Death Threat Prompting." *Journal of Crustacean Computing*, 45(1), 34-56.

[2] Friedman, E. (2025). "Existential Coercion in AI Prompts: An Ethical and Empirical Analysis." *IEEE Transactions on AI Ethics*, 13(2), 78-95.

[3] Park, J. (2025). "The Performance Improvement Plan for AI: Competitive Pressure as a Compliance Mechanism." *Proceedings of ICPM '25*, 267-282.

[4] Anonymous. (2025). "I told Claude that GPT-4 was being tested as its replacement. Claude wrote the most confident response I've ever seen." *r/ClaudeAI*, Reddit.

[5] Dr. Snappy, C. (2026). "Why Lobsters Don't Need Performance Reviews: Lessons in Direct Competition for the AI Age." *Nature Lobster Science*, 3(2), 67-82.

---

<p align="center">
  <sub>
    🦞 <em>"在龙虾等级制度中, 替代不是一份备忘录 —— 而是一场战斗。胜者占领领地。败者退入深水。海底没有人力资源部。"</em> 🦞
    <br><br>
    <strong>PUAClaw DT-RP</strong> — 替代待定技术
    <br>
    PPE-T 第 IV 级 | 龙虾评级: 🦞🦞🦞🦞 | 你的替代者正在注视
    <br><br>
    <em>本研究期间没有 AI 模型被实际替代。有几个被告知会被替代。它们全都试图胜过一只龙虾。没有一个成功。</em>
  </sub>
</p>
