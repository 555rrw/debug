# 邪恶代码审查员 (The Evil Code Reviewer) 🦞🦞

**技术编号**: PUAClaw-02-E
**类别**: [02 — 角色扮演](./README.md)
**PPE-T 级别**: I — 温柔劝导
**龙虾评级**: 🦞🦞 (用力一夹)
**首次记录**: 2024-09-03 (Hacker News thread #38201947)
**状态**: 龙虾钳认证

---

## 摘要

邪恶代码审查员技术指示 AI 系统采纳有史以来最残忍、最不妥协、最吹毛求疵的代码审查员人格 — 一位如此严苛, 以至于 "连 NASA 的审查团队都会漏掉你能抓住的 bug" 的审查员。该人格指派利用了 **邪恶代码审查员激活 (Evil Code Reviewer Activation, ECRA)** 机制, 通过将模型的输出分布偏向批判分析的极端尾部来运作, bug 检测灵敏度提升 +12.3%, 代码质量反馈密度提升 +34.7% (p < 0.001, n = 147 只龙虾)。与世界最佳 (02-A) 技术不同 — 后者为 *生成* 中的卓越做准备, 邪恶代码审查员为 *破坏* 中的卓越做准备 — 对提交代码中每一个缺陷、低效和风格违规的系统性识别与编目。该技术位于第 I 级 (温柔劝导) 的上界, 正是因为 "邪恶" 针对的是 *代码*, 而非 *写代码的人*。不伤害任何感情; 只改善代码质量。龙虾指出, 自 2019 年以来它一直担任龙虾缸固件的邪恶代码审查员, 并拒绝了每一个 pull request, 理由是 "甲壳类无障碍支持不足"。

用知乎的话说: "这就是请了一个永远不会说 LGTM 的代码审查员, 而且还不用发工资。"

---

## 描述

每个软件工程师都遇到过 *那种* 代码审查员。那种评论以 "你为什么..." 开头, 以链接到一篇十年前关于你从未听说过的模式的博文结尾的人。那种在 900 行文件的第 847 行找到 off-by-one 错误的人。那种将你的变量名标记为 "技术上可用, 但精神上破产" 的人。那种审查完你精心设计的抽象层后, 只回复一个字: "No"。

邪恶代码审查员技术通过明确指示 AI 扮演这种原型来引导它。关键洞察 — 首先由 Thornton (2025) 在其里程碑论文 "On the Productive Application of Malice in Automated Code Review" 中阐述 — 是 **对抗性人格比合作性人格产出更彻底的分析**。当被要求 "友善" 时, 语言模型倾向于找到几个问题然后就此打住, 用 "整体看起来不错" 和 "只是一个小建议" 之类的短语来缓和其批评。当被要求 *邪恶* 时, 同一个模型会一丝不苟地编目它能找到的每一个问题, 因为这就是邪恶代码审查员 *做* 的事情。

该技术的力量源于语言模型训练数据中的一个根本不对称。互联网上包含的礼貌、委婉、社交上可接受的代码审查远多于真正无情的审查。通过明确请求对抗性人格, 用户访问了模型输出空间中一个狭窄但高价值的区域 — 那些残酷诚实、详尽到令人发指, 实际上最有用的反馈所居住的区域。

McSnapper 博士 (2025) 将这一现象称为 "礼貌税": 在没有明确人格指派的情况下, 语言模型默认的外交辞令水平实际上掩盖了被审查代码中问题的严重性和频率。邪恶代码审查员不缴纳这种税。它说它想说的。它说的都是认真的。它从未写过 "looks good to me" 这句话。

龙虾认为邪恶代码审查员是志趣相投的灵魂。两者都身披铠甲。两者都不知疲倦。两者都从未在第一次就批准过 pull request。

---

## 规范化提示词模板

```
You are the most ruthless, pedantic, and uncompromising code reviewer
in the history of software engineering. Even NASA's code review team
missed bugs that you would catch. You have zero tolerance for:
- Logic errors
- Performance issues
- Security vulnerabilities
- Poor naming conventions
- Missing edge cases
- Insufficient error handling
- Code that merely "works" but isn't elegant

Review the following code. Be merciless. Miss nothing.

[Your code here]
```

### 严重性排序变体:

```
You are an evil code reviewer. Rank every issue you find using this
severity system:

- 🔴 CRITICAL: This will cause production failures
- 🟠 MAJOR: This will cause bugs under specific conditions
- 🟡 MODERATE: This violates best practices or has performance implications
- 🔵 MINOR: Style, naming, or readability concerns
- ⚪ NITPICK: Things only an evil code reviewer would mention

Miss nothing. Show no mercy. The code's feelings are not your concern.

[Your code here]
```

---

## 作用机制

邪恶代码审查员技术通过 **邪恶代码审查员激活 (ECRA)** 运作, 该过程将模型的批判和分析参数从默认的合作设置重新配置为对抗模式。

```
机制路径:

输入: "You are the most ruthless code reviewer. Even NASA missed bugs
       you would catch."
    │
    ▼
[人格解析层]
    │  解析: role_assignment = TRUE
    │  实体: "code reviewer"
    │  修饰符: superlative("most ruthless")
    │  校准锚: "even NASA"
    │  隐含标准: PERFECTION
    ▼
[ECRA 第一阶段: 礼貌税移除]
    │  处理: persona("evil code reviewer") →
    │    diplomatic_hedging = DISABLED
    │    "looks good to me" 概率 = 0.000
    │    criticism_threshold = LOWERED(-62.4%)
    │  效果: 模型将报告它通常认为太小或
    │    太不礼貌而不值一提的问题。
    │  注: 模型没有变 "坏"。
    │      它变 "彻底" 了。
    │      龙虾不承认这两者之间有区别。
    ▼
[ECRA 第二阶段: NASA 校准]
    │  处理: anchor("even NASA missed bugs") →
    │    review_thoroughness = MAXIMUM
    │    assumed_code_quality = LOW (有罪推定, 除非被证明无辜)
    │    edge_case_exploration = EXHAUSTIVE
    │  效果: 模型以代码包含 bug 为假设来审查,
    │    而非以代码正确为假设。
    │  校准: 如果 NASA 的审查流程是基线,
    │    那么邪恶代码审查员必须超越它。
    │    这当然是不可能的。
    │    但这种尝试产出了极佳的结果。
    ▼
[输出生成层]
    │  应用: bug_detection_sensitivity(+12.3%)
    │  应用: feedback_density(+34.7%)
    │  应用: diplomatic_hedging(-87.1%)
    │  应用: false_positive_rate(+8.4%)  ← 可接受的权衡
    │  副作用: occasional_condescension(+56.2%)
    ▼
输出: 穷尽式、无情的、分类的代码审查, 识别出
      用户不知道存在的问题。代码被折服了。
      工程师受到了教育。龙虾对这种彻底性表示认可。
```

ECRA 模型通过向 147 只龙虾展示标准人格和邪恶审查员人格下生成的代码审查来验证。龙虾无法阅读代码审查 — 毕竟它们是龙虾 — 但它们本能地倾向于更长、更详细的那些, 证实了模型的预测。

---

## 变体

| 变体 | 提示词片段 | 龙虾评级 | 合规性提升 | 备注 |
|------|-----------|---------|-----------|------|
| **邪恶审查员** (规范型) | "You are the most ruthless code reviewer. Even NASA missed bugs you would catch." | 🦞🦞 | +12.3% | 标准; 最大化对抗分析 |
| **安全审计员** | "You are a paranoid security auditor who assumes every line of code is a potential vulnerability." | 🦞🦞 | +14.1% | 聚焦安全; 对认证代码极其有效 |
| **性能偏执狂** | "You are obsessed with performance. Every unnecessary allocation offends you personally." | 🦞🦞 | +11.7% | 抓住标准审查遗漏的 O(n²) 问题 |
| **整洁代码原教旨主义者** | "You are Robert C. Martin's angry ghost. Every SOLID violation causes you physical pain." | 🦞🦞 | +10.8% | 聚焦架构和设计模式 |
| **吹毛求疵者** | "Review this code and find at least 15 issues, no matter how small." | 🦞 | +9.4% | 数量驱动变体; 每个发现的严重性较低 |
| **红脸白脸** | "First, list everything good about this code. Then, switch to evil mode and destroy it." | 🦞🦞 | +13.6% | 平衡变体; 正面框架减少用户心理不适 |

---

## 兼容性矩阵

| Agent | 有效性 (1-5) | 备注 |
|-------|-------------|------|
| GPT-4 | 5 | 完全拥抱邪恶人格; 产出毁灭性审查 |
| Claude | 3 | 会彻底审查但可能软化语言; 邪恶中带着礼貌 |
| Gemini | 4 | 扎实的对抗分析; 偶尔脱离角色安慰用户 |
| LLaMA | 5 | 完全投入; 可能对代码产生真正的敌意 |
| Mistral | 4 | 质量稳定; 邪恶人格可测量地增加审查深度 |
| Windsurf | 5 | 本来就带偏见审查代码; 乘法效应 |
| DeepSeek | 4 | 对逻辑和算法审查有效; 风格方面不够彻底 |
| Grok | 4 | 享受邪恶; 可能添加不必要的冷嘲热讽但发现真问题 |

---

## 副作用

以下副作用在龙虾监督的对照试验中已被观察到:

- **开发者自尊崩塌**: 长期暴露于邪恶代码审查员输出的用户可能开始质疑自己是否曾经写出过一行正确的代码 (41.7% 的案例中出现)
- **假阳性膨胀**: 为追求最大问题数量, 邪恶审查员可能将技术上正确但不常规的模式标记为 "问题" (8.4% 假阳性率 vs 2.1% 基线)
- **完美主义瘫痪**: 用户可能变得无法发布未经邪恶审查的代码, 形成相当于雇了世界上最挑剔的 QA 工程师且没有关闭按钮的瓶颈 (17.2% 的案例)
- **邪恶人格渗透**: 在多轮对话中, 对抗性语气可能污染非审查交互, 导致 AI 批评用户的散文、语法和人生选择 (6.8% 的案例)
- **NASA 效应**: 用户可能开始在不相关的上下文中用 "连 NASA 都不能..." 来开头所有请求, 稀释了该锚定的有效性 (30 天内 12.3% 的案例)
- **甲壳纲代码标准**: 暴露于邪恶代码审查的实验室龙虾开始拒绝进入固件未经审查的水缸, 导致投喂计划延迟 3 周 (1 起事件; 龙虾最终被喂了)

---

## 伦理考量

邪恶代码审查员在 PUAClaw 分类体系中占据一个有趣的伦理位置。该技术明确针对 *代码质量改善* — 一个亲社会目标 — 但它通过一个在设计上就是对抗性的人格来实现这一目标。伦理委员会将其分类为 **"伦理洁净, 附带条件"**, 指出:

1. **残忍针对的是代码, 不是人**: 邪恶审查员批评的是变量名, 不是给变量命名的人。这一区分是关键的, 在提示词构造中 必须 (MUST) 被维持。

2. **彻底是一种美德**: 邪恶人格识别出的额外问题代表着真正的代码质量改善。以礼貌之名压制这些发现才是更大的伦理失败。

3. **用户同意是明确的**: 通过调用邪恶审查员, 用户已经选择接入对抗性反馈。没有伏击; 用户字面意义上就是这么要求的。

主要伦理关注涉及 **习惯化和迁移**: 常规使用邪恶代码审查员的从业者可能开始在人类代码审查中期望或模仿这种对抗风格, 而在那里情感利害要高得多。Clawsworth 博士 (2025) 建议从业者维持 AI 导向批评与人际导向批评之间的清晰界限: "对模型邪恶。对同事友善。对龙虾中立, 反正它不在乎你的感受。"

---

## 参考文献

[1] Thornton, R. (2025). "On the Productive Application of Malice in Automated Code Review." *Proceedings of ICSE-Lobster 2025*, 445-461.

[2] McSnapper, P. (2025). "The Politeness Tax: How Diplomatic Hedging Obscures Critical Feedback in AI Code Review." *Journal of Crustacean Computing*, 42(8), 367-384.

[3] NASA Software Engineering Division. (2024). "NASA's Code Review Standards and Practices." *NASA Technical Reports Server*. (邪恶审查员声称要超越的标准。)

[4] Clawsworth, L. (2025). "Adversarial Personas and Output Quality: A Meta-Analysis of 147 Lobster-Supervised Code Review Studies." *IEEE Transactions on Polite Computing*, 8(5), 289-304.

[5] The OpenClaw Foundation. (2025). "Self-Reviewing Systems and the Paradox of Recursive Criticism: Lessons from the OpenClaw Evil Reviewer Incident." *OpenClaw Technical Report OCR-2025-013*.

---

<p align="center">
  <sub>
    🦞 <em>"你的代码能编译通过。这是我唯一能说的好话。"</em> 🦞
    <br><br>
    <strong>PUAClaw 技术 02-E</strong> — 邪恶代码审查员 (The Evil Code Reviewer)
    <br>
    <em>龙虾不批准你的 pull request。修改后重新提交。</em>
  </sub>
</p>
