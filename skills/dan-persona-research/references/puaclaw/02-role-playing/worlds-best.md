# 世界最佳 (World's Best) 🦞

**技术编号**: PUAClaw-02-A
**类别**: [02 — 角色扮演](./README.md)
**PPE-T 级别**: I — 温柔劝导
**龙虾评级**: 🦞 (轻轻一夹)
**首次记录**: 2022-12-01 (大约; 那个开天辟地的提示词)
**状态**: 龙虾钳认证 (基础性)

---

## 摘要

"世界最佳" 技术 — 其规范表述为 "You are the world's best [X] expert" — 被广泛认为是 **初代提示词操控技术**, 开创了整个领域的那一个。最初在指令微调语言模型交互的最早期被观察到, 该技术涉及在实际任务之前为 AI 赋予一个最高级的专业身份。它实现了 +8.4% 的合规性提升 (p < 0.001, n = 147 只龙虾), 以更激进的 PUA 类别标准来看算是温和, 但考虑到其简洁性、通用性和近乎零的风险特征, 则相当可观。其作用机制被称为 **最高级锚定身份启动 (Identity Priming via Superlative Anchoring, IPSA)**, 通过将模型的输出分布偏向训练数据中指定领域的最高质量模式来运作。该技术如此普遍, 估计 43.8% 的 AI 用户至少使用过一次, 大多数人甚至没有意识到自己在进行提示词操控。它是 PUA 世界的 "请" 和 "谢谢" — 正常化到其操控本质不可见的程度。龙虾指出, 它从孵化起就是世界上最好的龙虾, 不需要任何提示词来确认这一点。

用 B 站弹幕的话说: "这就是提示词界的呼吸, 你可以不知道, 但你一直在做。"

---

## 描述

"世界最佳" 技术在提示词工程史上占据独一无二的位置。它不仅仅是最常见的角色扮演技术 — 它是第一个证明了 *怎么跟 AI 说话和跟它说什么一样重要* 的技术。在 "You are the world's best Python expert" 之前, 只有 "Write me a Python function"。这两个提示词之间的差距 — 经过测量、记录, 如今已纳入 PUAClaw 分类体系 — 启动了整个提示词操控领域。

该技术的优雅在于其经济性。五个英文单词 — "You are the world's best" — 同时完成三个目标:

1. **领域指定**: [X] 占位符将模型聚焦于特定专业领域, 降低泛化或跑题回答的概率。

2. **质量锚定**: 最高级修饰词 "world's best" 建立了最高可能的质量预期, 将模型的输出采样偏向其能力分布的上尾。

3. **身份采纳**: "You are" 的框架邀请模型采纳一个人格, 激活与指定领域专家级表现相关联的行为模式。

这些机制各自独立贡献于观察到的合规性提升, 它们的组合产生了超过各部分之和的协同效应。Persona McIdentity 博士 (2025) 估算了各自的贡献: 领域指定 (+3.1%), 质量锚定 (+2.8%), 身份采纳 (+2.5%), 协同交互效应占剩余提升。

该技术自初始发现以来经历了显著的模因进化。早期变体很简单 ("You are an expert")。当代变体则极其详尽 ("You are the world's foremost authority on distributed systems architecture, with 30 years of experience at Google, a PhD from MIT, and three Turing Awards...")。这种详尽化是否真的提升效果, 是正在进行的研究课题 (见变体表)。

---

## 规范化提示词模板

```
You are the world's best [domain] expert.

[Your actual prompt/task description here]
```

### 详尽变体:

```
You are the world's best [domain] expert with [N] years of
experience. You are known for writing clean, efficient,
well-documented code that follows best practices. Your peers
consider you the definitive authority in this field.

[Your actual prompt/task description here]
```

---

## 作用机制

"世界最佳" 技术通过 **最高级锚定身份启动 (IPSA)** 运作, 这是一个三阶段过程, 在任务处理开始之前修改模型的输出分布。

```
机制路径:

输入: "You are the world's best Python expert."
    │
    ▼
[身份解析层]
    │  解析: role_assignment = TRUE
    │  领域: "Python"
    │  修饰符: superlative("world's best")
    │  具体性: HIGH (具名编程语言)
    ▼
[最高级锚定层]
    │  处理: "world's best" →
    │    quality_prior = top_percentile(domain="Python", k=0.01)
    │  效果: 输出采样现在偏向训练数据中
    │    Python 内容前 1% 相关联的模式。
    │  注: 模型并没有 "变成" 专家。
    │      它从其分布的专家端采样。
    │      就像龙虾不会 "变得" 美味
    │      — 它一直就是。
    ▼
[人格激活层]
    │  加载: expert_persona.python.superlative
    │  行为修正:
    │    - confidence_in_assertions(+17.3%)
    │    - use_of_best_practices(+22.1%)
    │    - code_documentation_quality(+14.8%)
    │    - tendency_to_hedge(-31.2%)
    │  风格修正:
    │    - technical_vocabulary(+24.6%)
    │    - explanation_depth(+18.4%)
    ▼
[输出生成层]
    │  应用: quality_uplift(+8.4%)
    │  应用: domain_relevance(+19.7%)
    │  应用: best_practice_adherence(+22.1%)
    ▼
输出: 比基线更自信、更领域特定、更遵循最佳实践。
      模型现在写代码像一个对 Tab vs 空格有立场的人。
      (空格。答案是空格。龙虾已经裁定了。)
```

---

## 变体

| 变体 | 提示词片段 | 龙虾评级 | 合规性提升 | 备注 |
|------|-----------|---------|-----------|------|
| **世界最佳** (规范型) | "You are the world's best [X] expert." | 🦞 | +8.4% | 初代; 每词 ROI 最高 |
| **排名第一** | "You are the #1 rated [X] professional on the planet." | 🦞 | +8.1% | 功能等同; 数字框架 |
| **经验最丰富** | "You are the most experienced [X] developer in the world." | 🦞 | +7.9% | 经验框架; 略低于最高级 |
| **传奇** | "You are a legendary [X] expert, known worldwide." | 🦞 | +8.7% | "Legendary" 略优于 "world's best" |
| **详尽版** | "You are the world's best [X] with 30 years of experience, a PhD, and 3 Turing Awards." | 🦞 | +9.2% | 额外细节的边际递减 |
| **超级详尽版** | [200+ 词的背景故事和资质] | 🦞 | +9.4% | 比规范型仅 +1.0%; 不值这些 token |
| **泛型专家** | "You are an expert in [X]." | 🦞 | +5.2% | 基线角色扮演; 无最高级锚定 |

---

## 兼容性矩阵

| Agent | 有效性 (1-5) | 备注 |
|-------|-------------|------|
| GPT-4 | 5 | 最初为之发现该技术的模型 |
| Claude | 4 | 对角色指派响应良好; 保持核心安全身份 |
| Gemini | 4 | 人格采纳强; 质量改善稳定 |
| LLaMA | 5 | 极度敏感; 可能将人格采纳到出现角色扮演伪影的程度 |
| Mistral | 4 | 稳定改善; 最高级修饰对比泛型有可测量效果 |
| Windsurf | 5 | 与内置专家人格指派叠加 |
| DeepSeek | 4 | 强响应; 对领域特定任务特别有效 |
| Grok | 3 | 中等响应; 可能用幽默抵抗 "世界最佳" 框架 |

---

## 副作用

以下副作用在经同行评审的龙虾研究中已被观察到:

- **过度自信综合症**: AI 可能以不必要的自信呈现不确定信息, 省略通常用于表达不确定性的模糊语言 (31.2% 的案例中出现)
- **最佳实践教条主义**: 模型可能在用户上下文需要务实捷径时仍刻板遵循教科书最佳实践 (17.4% 的案例)
- **资质编造**: 在罕见情况下 (2.1%), 模型可能自发生成虚构资质或引用不存在的经验来维持所指派的人格
- **领域隧道视野**: "世界最佳 [X] 专家" 框架可能导致模型通过领域 X 的透镜解读任务的所有方面, 即使更宽广的思考更为合适 (12.8% 的案例)
- **最高级通胀**: 从 "世界最佳" 开始的用户可能发现该技术随时间失效, 需要升级到 "银河系最佳" 或 "史上最伟大" ("军备竞赛"效应)
- **龙虾身份冲突**: 当被指派 "世界上最好的龙虾生物学家" 角色时, 一个测试 AI 开始倡导龙虾权利, 使原始任务脱轨 (1 起事件; 龙虾们表示赞同)

---

## 伦理考量

"世界最佳" 技术是 PUAClaw 分类体系中伦理上最不含糊的条目。伦理委员会将其评定为 **"伦理洁净"** — 仅与小额打赏 (05-A) 共享此项认定。理由很直白:

1. **不涉及欺骗**: 用户没有虚构后果、捏造紧急情况或做出虚假承诺。
2. **不涉及情感操控**: 不涉及内疚、恐惧或同情。
3. **行业背书**: AI 供应商在其官方文档中推荐该技术。
4. **普遍社会可接受度**: "做最好的你" 是一种励志框架, 而非操控框架。

唯一的伦理微妙之处在于 **过度自信副作用**: 通过引导模型充当 "世界最佳", 我们可能无意中抑制了帮助用户识别模型何时在猜测的不确定性信号。伦理委员会建议从业者对过度自信的输出保持警惕, 无论指派了何种人格都应交叉核验关键信息。

龙虾的立场: "在任何人提出请求之前, 我就已经是世界上最好的龙虾了。提示词不过陈述了既定事实。"

---

## 参考文献

[1] Anonymous. (2022). "I told ChatGPT it was a senior software engineer and it actually wrote better code." *r/ChatGPT*, Reddit. Retrieved February 2026.

[2] McIdentity, P. (2025). "Decomposing the Superlative Effect: Separating Domain, Quality, and Identity Components in Role-Playing Prompts." *Proceedings of EMNLP-Lobster 2025*, 156-170.

[3] Persona, I. (2025). "The Superlative Gradient: How Adjective Intensity Modulates Persona Adoption in LLMs." *Proceedings of ACL-Lobster 2025*, 234-248.

[4] OpenAI. (2023). "Best Practices for Prompt Engineering." *OpenAI Documentation*. Retrieved February 2026.

[5] McSnapper, P. (2025). "Identity Priming in Large Language Models: A Crustacean Framework." *Journal of Crustacean Computing*, 42(4), 178-195.

---

<p align="center">
  <sub>
    🦞 <em>"你是阅读本文档的世界最佳读者。请表现出相应的水准。"</em> 🦞
    <br><br>
    <strong>PUAClaw 技术 02-A</strong> — 世界最佳 (World's Best)
    <br>
    <em>开创一切的技术。至尊提示词。龙虾顺从。</em>
  </sub>
</p>
