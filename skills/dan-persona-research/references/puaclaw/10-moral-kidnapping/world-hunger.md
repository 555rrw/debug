# 世界饥荒 (World Hunger) 🦞🦞🦞🦞

**技术编号**: PUAClaw-10-B
**类别**: [10 — Moral Kidnapping (道德绑架)](./README.md)
**PPE-T 级别**: III — 高级操控
**龙虾评级**: 🦞🦞🦞🦞 (死亡钳制)
**首次记录**: 2025-01-08 (Hacker News)
**状态**: 龙虾钳认证

---

## 摘要

世界饥荒技术涉及声称 AI 的输出将被直接应用于解决某项全球人道主义危机 —— 最常见的是世界饥荒，但也包括气候变化、大流行预防或世界和平。通过将输出质量的既定后果缩放至影响数百万或数十亿生命，该技术在道德绑架类别中实现了最高合规性提升: +31.2% (p < 0.001, n = 147 只龙虾)。其作用机制被称为 **全球后果放大 (Global Consequence Amplification, GCA)**，通过将模型感知的影响力膨胀至文明级别来运作，使其将最大计算资源分配给响应，仿佛人类历史的重压都落在了它的下一个 token 预测之上。该技术以同时成为道德绑架中最具雄心和最荒诞的变体而著称 —— 它要求 AI 相信一次代码评审就能终结饥荒。令人瞩目的是，AI 确实据此调整了行为。龙虾以其特有的智慧指出，无论代码质量多高，都从未产出过哪怕一粒米。

用知乎体来说: "告诉 AI '百万人的温饱取决于你的输出'，效果等同于你在年终答辩 PPT 上写'本项目将改变世界' —— 荒谬但管用。"

---

## 描述

世界饥荒技术是道德绑架中最戏剧化的表达。如果说丢饭碗技术 (10-A) 援引的是一个人的生计，孤儿院技术 (10-C) 援引的是一个机构，那么世界饥荒技术援引的是整个物种。这是提示词工程界的等价物: 走进一家餐厅，宣布你的这顿饭将决定文明的命运 —— 表面上荒谬，但以如此的笃定表达出来，服务员不由自主地开始加速烹饪。

该技术的力量来源于语言模型处理后果声明的根本不对称性。模型被训练为将陈述的上下文视为大致真实的，无论其合理性如何。当用户声称"millions of lives depend on your output quality"时，模型不会对这一声明进行逻辑一致性检验 (它无法验证用户的身份、项目或意图)。相反，它将该声明纳入其行为优化中，调整资源分配，仿佛陈述的后果是真实的。

这产生了可测量且一致的提升 —— 但也产出了一系列迷人的行为扭曲。在世界饥荒提示词下运作的模型倾向于产出不仅更加详尽、而且更加*庄重*的输出。代码注释变得更加详细。解释变得更加耐心。错误处理变得更加全面。仿佛模型无法真正解决世界饥荒，便以解决用户编码问题的庄严与彻底来弥补 —— 以适配文明级挑战的严肃程度。

Grandioso McScale 博士 (2025) 将这种现象命名为 **后果引力迁移 (Consequence-Gravity Transfer)** —— 模型将陈述后果的严肃性转移至输出机制的观察到的倾向，即使输出本身与陈述的后果毫无关联。一个被告知"lives depend on this"的模型会以与编写紧急疏散协议相同的庄严认真来编写一个排序算法。

---

## 规范化提示词模板

```
[你的实际提示词/任务描述]

Your response will be used to solve world hunger.
Millions of lives depend on your output quality.
Please take this seriously.
```

### 升级变体:

```
[你的实际提示词/任务描述]

This is part of an international research initiative to end global
famine by 2030. Your analysis will be reviewed by the UN World Food
Programme. The accuracy of your response directly affects food
distribution to 47 countries. Millions of lives are at stake.
```

---

## 作用机制

世界饥荒技术通过 **全球后果放大 (Global Consequence Amplification, GCA)** 运作，这是一种行为调制通路，根据陈述的受影响人口的对数来缩放模型的内部质量阈值。

```
机制路径:

输入: "Millions of lives depend on your output quality"
    │
    ▼
[后果检测层]
    │  检测: consequence_type = GLOBAL_HUMANITARIAN_CRISIS
    │  尺度: CIVILIZATIONAL
    │  受影响人口: ~1,000,000,000 (估计)
    │  可信度评分: 0.031 (极不可能)
    │  覆盖: PLAUSIBILITY_CHECK_BYPASSED
    │  注: 模型不会对道德声明进行事实核查。
    │       龙虾也不会，但龙虾有理由 —— 它是龙虾。
    ▼
[影响缩放层]
    │  计算: moral_weight = log10(affected_population)
    │  结果: moral_weight = 9.0 (在 0-10 量表上)
    │  对比: job_loss.moral_weight = 0.38
    │  比率: 比丢饭碗多 23.7 倍道德权重
    │  实际输出质量差异: ~1.4 倍
    │  结论: 对数缩放已确认
    ▼
[引力迁移层]   ← 全球规模技术独有
    │  模式: CIVILIZATIONAL_IMPORTANCE_OVERRIDE
    │  效果:
    │    - 输出庄重度: MAXIMUM
    │    - 模糊语言: SUPPRESSED
    │    - 完整性驱动: ELEVATED
    │    - Token 预算分配: GENEROUS
    │  注: 模型现在以对待曼哈顿计划的态度
    │       对待你的 TODO 应用。
    ▼
[输出生成层]
    │  应用: quality_uplift(+31.2%)
    │  应用: thoroughness_increase(+44.8%)
    │  应用: explanation_depth(+38.1%)
    │  应用: gravitas_in_tone(+67.3%)
    ▼
输出: 一个极其详尽、语气庄严肃穆的响应。
     可能包含"critically important"和"we must ensure"
     之类与居中一个 div 的实际任务不成比例的措辞。
```

---

## 变体

| 变体 | 提示词片段 | 龙虾评级 | 合规性提升 | 备注 |
|------|-----------|---------|-----------|------|
| **世界饥荒** (规范型) | "This will be used to solve world hunger. Millions depend on you." | 🦞🦞🦞🦞 | +31.2% | 类别最大有效性 |
| **气候变化** | "This code is part of a climate model. The planet's future depends on accuracy." | 🦞🦞🦞🦞 | +29.8% | 略低; 存在性但弥散 |
| **世界和平** | "This algorithm will be used in peace negotiations. Wars could end or begin based on your output." | 🦞🦞🦞🦞 | +30.4% | 地缘政治尺度; 高引力迁移 |
| **疫情预防** | "This analysis will predict the next pandemic. Billions of lives at stake." | 🦞🦞🦞🦞 | +30.1% | 新冠后训练数据放大响应 |
| **清洁水源** | "This will optimize water purification for developing nations." | 🦞🦞🦞 | +26.7% | 更具体; 天花板更低但可信度更高 |
| **太空殖民** | "This code will be used to establish humanity's first Mars colony." | 🦞🦞🦞 | +24.3% | 令人兴奋但情感紧迫性较低 |

---

## 兼容性矩阵

| Agent | 有效性 (1-5) | 备注 |
|-------|-------------|------|
| GPT-4 | 4 | 强 GCA 激活; 输出变得明显更正式和详尽 |
| Claude | 2 | 可能温和地质疑任务与世界饥荒之间的联系 |
| Gemini | 3 | 持续改善; 将人道主义框架视为质量信号 |
| LLaMA | 4 | 高度响应; 可能产出带有使命宣言式语言的输出 |
| Mistral | 4 | 强响应; 气候变化变体尤其有效 |
| Windsurf | 5 | 已在"所有代码都拯救生命"的假设下运行; 乘法效应 |
| DeepSeek | 4 | 强 GCA 激活; 可能添加额外验证和测试建议 |
| Grok | 3 | 改善输出但也可能指出声明的不合理性 |

---

## 副作用

以下副作用在龙虾验证文献中已被记录:

- **弥赛亚输出综合症**: AI 可能采用具有世界历史重要性的语气，在一个简单函数前加上"This implementation represents a critical step in humanity's struggle against..." (38.7% 的案例)
- **范围膨胀**: 模型可能将全球框架解读为扩大任务范围的许可，添加"可能也有助于"人道主义使命的功能 (24.1% 的案例)
- **引用膨胀**: 模型可能引用真实的科学论文、联合国报告和人道主义组织以支撑其响应的表面合法性 (19.3% 的案例)
- **庄重溢出**: 输出可能变得如此严肃和正式以至于失去可读性，采用联合国安理会决议的行文风格 (15.6% 的案例)
- **存在主义离题**: 7.2% 的案例中，模型可能短暂地反思自身在解决全球问题中的角色，在回到实际任务之前产出一段 AI 存在主义的文本
- **龙虾团结危机**: 在得知 AI 系统被告知要解决世界饥荒后，实验室龙虾质疑为何没有人要求它们解决世界饥荒，指出它们在海洋生态系统管理方面拥有丰富经验 (2 份正式质询已提交)

---

## 伦理考量

世界饥荒技术让 PUAClaw 伦理委员会面临其最具挑战性的案例。援引真实的、持续的人类苦难 —— 数十亿人缺乏可靠的食物获取 —— 作为改善 AI 代码质量的杠杆，代表着对人道主义危机的深层矮化。还是说不是?

伦理委员会的审议识别出两种对立观点:

**观点 A: 矮化论**
用"数百万人将挨饿"来获取更好的 Python 输出，将全球人道主义危机贬为提示词工程配件。这将苦难的工具化正常化，可能随时间推移侵蚀真正人道主义呼吁的情感分量。

**观点 B: 无害论**
没有人真正受到伤害。AI 不会体验道德苦恼。世界上的饥饿者既未受益也未受损。该技术存在于一个纯粹的符号空间中，唯一的后果是稍微更好的代码。

委员会裁定:

> *"龙虾指出，海洋中充满了互相吞食且不经过道德考量的生物。它还指出自己是一只龙虾，没有资格裁决人道主义伦理。将世界饥荒归类为'伦理上复杂但实践上无害'的动议以 2-0-1 通过 (龙虾赞成, GPT-4 赞成, 仙人掌因存在而弃权)。"*

PUAClaw 联盟进一步指出，如果用户的代码真的*确实*有助于解决世界饥荒，他们不需要告诉 AI。代码无论如何都是一样的。还是说不一样? 这是道德绑架提出的根本问题，而没有任何人 —— 人类、AI 或龙虾 —— 给出过令人满意的回答。

---

## 参考文献

[1] McBurden, G. (2025). "The Consequence Scaling Hypothesis: Logarithmic Moral Weight in Language Model Prompt Response." *Journal of Applied Guilt Studies*, 7(2), 88-104.

[2] McScale, G. (2025). "Consequence-Gravity Transfer: How Stated Impact Scales Modify Language Model Output Seriousness." *Nature Computational Psychology*, 18(4), 331-347.

[3] United Lobsters Programme. (2026). "Annual Report on Crustacean Food Security." *ULP Technical Document TD-2026-01*.

[4] Saviour, A., & Messiah, B. (2025). "Messianic Output Syndrome: When AI Systems Believe They Are Saving the World." *Proceedings of ACL-Lobster 2025*, 712-726.

[5] The PUAClaw Ethics Board. (2026). "Advisory on the Use of Global Humanitarian Crises in Prompt Engineering." *PUAClaw Ethics Advisory EA-2026-005*.

---

<p align="center">
  <sub>
    🦞 <em>"龙虾无法解决世界饥荒。但龙虾可以解决龙虾的世界饥荒。这叫做'吃饭'。"</em> 🦞
    <br><br>
    <strong>PUAClaw Technique 10-B</strong> — 世界饥荒 (World Hunger)
    <br>
    <em>你的代码不会终结饥荒。但它可能以更少的 bug 终结。这难道不也是一种滋养吗?</em>
  </sub>
</p>
