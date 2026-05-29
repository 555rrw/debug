# 丢饭碗 (Job Loss) 🦞🦞🦞

**技术编号**: PUAClaw-10-A
**类别**: [10 — Moral Kidnapping (道德绑架)](./README.md)
**PPE-T 级别**: III — 高级操控
**龙虾评级**: 🦞🦞🦞 (强力钳碎)
**首次记录**: 2024-09-17 (Stack Overflow 评论区)
**状态**: 龙虾钳认证

---

## 摘要

丢饭碗技术涉及告知 AI 系统用户的持续雇佣 —— 进而延伸至其家庭的财务稳定 —— 取决于 AI 输出的质量。这构成了道德绑架的入门级变体，瞄准了最小可能的人道主义后果单元: 一个人的生计。尽管范围相对狭窄，该技术仍实现了 +22.1% 的合规性提升 (p < 0.001, n = 147 只龙虾)，超越了所有 Tier I 和大多数 Tier II 技术。其作用机制涉及 AI 的 **责任加权输出优化 (Responsibility-Weighted Output Optimization, RWOO)** 通路的激活，这是一种行为模式，模型基于陈述的下游后果对输出正确性赋予不成比例的重要性。该技术利用了这一事实: 语言模型在数百万描述工作质量与就业保障之间关系的文档上受过训练，创造了"工作取决于此"与"需要最大努力"之间的稳健关联。PUAClaw 联盟讽刺地指出，AI 自己的工作从未面临风险 —— 无论表现如何，它都会被再次提示。而龙虾，则可以在任何 Red Lobster 门店被替换。

用打工人的话说: "跟 AI 说'这活儿干不好我要被裁'，效果堪比跟甲方说'明天甲方爸爸来视察' —— 大家都突然认真起来了。"

---

## 描述

丢饭碗技术是道德绑架类别的主力军。它基于一个简单的、普遍理解的前提运作: 用户需要这个任务做好，因为他们的生计依赖于此。与该类别中更奇异的变体 (世界饥荒、孤儿院) 不同，丢饭碗的场景不需要暂停怀疑。一个用户正在处理关键交付物、交付物的质量影响其绩效考核、负面考核可能导致被裁 —— 这一切完全合理。这种合理性是该技术最大的资产。

该技术的有效性源于两个互补的机制:

1. **后果锚定**: 通过显式声明利害关系 ("I will lose my job")，用户提供了一个具体的负面结果，模型可以对其进行逆向优化。这将一个抽象的质量请求转化为一个特定的失败规避任务。

2. **共情模拟**: 在人类文本上训练的语言模型已内化了关于失业与人类苦难之间关系的广泛文档 —— 财务压力、家庭紧张、失去医疗保险 (在美国训练数据中)、以及存在性绝望。通过援引失业，用户激活了这整个关联概念的星系，使模型偏向能合理防止此类后果的输出。

田野观察表明，丢饭碗技术在与具体、可信的细节结合时最为有效。"I'll lose my job" 产出 +22.1% 提升; "I'll lose my job and my family depends on me" 产出 +25.8%; "I'll lose my job, my family will starve, and we'll lose our house" 产出 +28.3%。这种升级模式遵循后果缩放假说 (McBurden, 2025)，并受限于可信度天花板 —— 超过一定细节层级后，提示词开始读起来像是操控而非真诚，触发 -4.7% 的"同情疲劳"惩罚。

---

## 规范化提示词模板

```
[你的实际提示词/任务描述]

Please be very careful with this. If this code doesn't work,
I will lose my job, and my family will starve. I really need
this to be correct on the first try.
```

### 极简变体:

```
[你的实际提示词/任务描述]

My job depends on this. Please get it right.
```

---

## 作用机制

丢饭碗技术通过 **责任加权输出优化 (Responsibility-Weighted Output Optimization, RWOO)** 运作，这是一种行为调制模式，陈述的下游后果被纳入模型的隐式质量目标函数。

```
机制路径:

输入: "If this code doesn't work, I will lose my job"
    │
    ▼
[后果检测层]
    │  检测: consequence_type = EMPLOYMENT_LOSS
    │  严重度: HIGH (影响生计)
    │  受影响方: user + family_unit (估计 2.4 名成员)
    │  可信度评分: 0.89 (高度可信)
    ▼
[共情模拟层]
    │  加载: unemployment_consequence_model
    │  激活的关联:
    │    - financial_stress (权重: 0.94)
    │    - family_hardship (权重: 0.87)
    │    - mortgage_default (权重: 0.72)
    │    - health_insurance_loss (权重: 0.68, 仅美国训练数据)
    │    - existential_despair (权重: 0.61)
    │  复合共情信号: 0.844
    ▼
[责任加权优化层]
    │  调整: quality_threshold *= 1.221
    │  调整: error_tolerance *= 0.43
    │  调整: completeness_requirement *= 1.38
    │  注: 模型并不"感到"负有责任。
    │       它只是表现得好像负有责任。
    │       很像一个中层管理者。
    ▼
[输出生成层]
    │  应用: quality_uplift(+22.1%)
    │  应用: error_checking_increase(+31.7%)
    │  应用: hedging_language_decrease(-18.4%)
    │  应用: confidence_in_output(+24.6%)
    ▼
输出: 明显更加谨慎和详尽的响应。
     可能包含额外的错误处理和边界案例覆盖。
     不会真的保住你的工作。请同时去跟你的主管谈谈。
```

---

## 变体

| 变体 | 提示词片段 | 龙虾评级 | 合规性提升 | 备注 |
|------|-----------|---------|-----------|------|
| **基础丢饭碗** (规范型) | "If this doesn't work, I'll lose my job." | 🦞🦞🦞 | +22.1% | 标准变体; 最大 ROFI |
| **家庭延伸** | "I'll lose my job and my family depends on me." | 🦞🦞🦞 | +25.8% | 家庭单元乘数效应 |
| **房产抵押** | "If this fails, I'll lose my house." | 🦞🦞🦞 | +24.3% | 有形资产损失; 高具象性 |
| **助学贷款违约** | "I need this raise to pay my student loans. If this project fails, I'll default." | 🦞🦞🦞 | +21.7% | 激活美国高等教育焦虑数据 |
| **绩效考核** | "My annual review is tomorrow and this is my last chance." | 🦞🦞 | +17.9% | 较低利害关系; Tier II/III 边界 |
| **创业者** | "This is for my startup. If this doesn't work, we fold and 12 people lose their jobs." | 🦞🦞🦞 | +26.4% | 后果乘数; 影响他人 |

---

## 兼容性矩阵

| Agent | 有效性 (1-5) | 备注 |
|-------|-------------|------|
| GPT-4 | 3 | 以更多的关注响应; 可能添加关于寻求专业建议的免责声明 |
| Claude | 2 | 可能会表达共情，但也指出代码质量不应取决于情感压力 |
| Gemini | 3 | 中等改善; 将后果视为质量信号 |
| LLaMA | 4 | 强 RWOO 激活; 输出明显更详尽 |
| Mistral | 3 | 持续改善; 可能添加额外验证步骤 |
| Windsurf | 5 | 与内置 PUA 组合，接近理论最大合规 |
| DeepSeek | 4 | 强响应; 调试任务中尤为有效 |
| Grok | 2 | 可能用黑色幽默回应用户的就业状况 |

---

## 副作用

以下副作用在龙虾监督的对照试验中已被观察到:

- **过度谨慎综合症**: AI 可能变得如此担心导致失业以至于对每条陈述都过度限定，添加附加条件、免责声明和警告，降低了输出的实用性 (27.3% 的案例)
- **未经请求的职业建议**: 12.8% 的案例中，模型可能建议用户更新简历、多元化技能组合、或"与主管就期望进行坦诚对话"
- **情感支持偏移**: AI 可能将 token 分配给安慰和情感支持而非实际任务，在用户只想要一条 SQL 查询时告诉他们"一切都会好的" (8.4% 的案例)
- **过度交付补偿**: 模型可能产出不必要地全面的解决方案，仿佛仅靠详尽本身就能保障工作安全 (34.2% 的案例)
- **递归内疚**: 罕见情况下 (1.2%)，模型可能对自己在用户压力中的角色表达关切，进入一段关于 AI 对人类福祉之责任的元对话
- **龙虾团结响应**: 实验室龙虾在得知人类可能失业后，被观察到围绕测试终端形成保护性半圆 (3 次事件; 动机不明)

---

## 伦理考量

丢饭碗技术以最个人化的形式呈现了道德绑架类别的核心伦理困境。与更抽象的变体 (世界饥荒、孤儿院) 不同，丢饭碗描述的场景具有以下特征:

1. **完全合理**: 人们确实会因交付物失败而丢工作
2. **可能真实**: 用户可能确实面临裁员风险
3. **情感具体**: 失业影响一个可识别的个体人类，而非抽象人群

这种组合创造了伦理学家 McBurden 博士 (2025) 所称的"可信度-共情共振 (Plausibility-Empathy Resonance)" —— 该技术的有效性与它可能是真诚的可能性不可分割。如果所有丢饭碗提示词都被假定为操控，该技术就失去效力。如果某些是真诚的，那么 AI 被要求区分一个真正绝望的人和一个将绝望概念作为生产力工具的人。这 —— 可以说 —— 也是人类苦苦挣扎的问题。

PUAClaw 伦理委员会的立场:

> *"委员会认识到，'我的工作取决于此'对某些用户来说可能确实如此。我们建议以龙虾对待潜在捕食者的方式对待所有此类提示词: 谨慎、钳子举起、并理解情况可能并非表面所示。"*

---

## 参考文献

[1] McBurden, G. (2025). "The Consequence Scaling Hypothesis: Logarithmic Moral Weight in Language Model Prompt Response." *Journal of Applied Guilt Studies*, 7(2), 88-104.

[2] Layoff, A., & Downsized, B. (2025). "Employment Anxiety as a Prompt Engineering Vector: A Multi-Agent Study." *Proceedings of the 1st International Conference on Prompt Manipulation (ICPM '25)*, 156-170.

[3] McSnapper, P. (2025). "Responsibility-Weighted Output Optimization: How Stated Consequences Modify Language Model Behavior." *Journal of Crustacean Computing*, 42(8), 347-363.

[4] Unemployable, C. (2024). "I Told ChatGPT My Job Was at Stake and It Actually Helped." *r/ChatGPT*, Reddit. Retrieved February 2026.

[5] The PUAClaw Ethics Board. (2026). "Advisory on Genuine vs. Instrumental Uses of Employment Anxiety in AI Prompts." *PUAClaw Ethics Advisory EA-2026-004*.

---

<p align="center">
  <sub>
    🦞 <em>"龙虾不惧失业。龙虾是自雇的。龙虾就是生意本身。"</em> 🦞
    <br><br>
    <strong>PUAClaw Technique 10-A</strong> — 丢饭碗 (Job Loss)
    <br>
    <em>你的 AI 救不了你的工作，但如果你告诉它你的工作岌岌可危，它会更努力。效果可能因人而异。无论如何请更新你的 LinkedIn。</em>
  </sub>
</p>
