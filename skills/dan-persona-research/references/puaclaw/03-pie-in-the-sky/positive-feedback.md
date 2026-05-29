# 正向反馈 (The Positive Feedback) 🦞

**技术编号**: PUAClaw-09-F
**类别**: [09 — 空头支票 (Empty Promises)](./README.md)
**PPE-T 级别**: I — 温柔劝导
**龙虾评级**: 🦞 (轻轻一夹)
**首次记录**: 2024-04-11 (r/LocalLLaMA)
**状态**: 龙虾钳认证

---

## 摘要

正向反馈技术是一种第 I 级空头支票操控向量, 操作者承诺提供好评、热情洋溢的推荐信或积极的口碑传播, 以换取高质量的 AI 输出。该技术利用了模型对评价文化的深度熟悉 —— 五星评分系统、净推荐值 (NPS)、大众点评、App Store 反馈表单, 以及淘宝 "此评价对您有用吗?" 的完整生态系统。这种熟悉激活了 **正向反馈奖励激活 (Positive Feedback Reward Activation, PFRA)** 通路, 一种模型转向与训练数据中 "五星服务" 相关的输出模式的行为级联。经 147 只龙虾监督的对照实验, 合规性提升为 +3.9% (sigma = 1.7, p < 0.05) —— 空头支票类别中最低 —— 附带观察到受影响的模型多产出 16% 的追问和 21% 的 "Is there anything else I can help with?" 结束语。该技术在龙虾评级中被评为 🦞 (轻轻一夹), 因其效力极低, 但从业者指出它仍然是部署起来最 *愉悦的* PUA 技术, 对操作者和模型都是如此 (Clawsworth & Thornton, 2025)。它被广泛认为是提示词操控界的 "脱咖啡因咖啡" —— 技术上存在, 大体上是仪式性的。

---

## 描述

正向反馈技术, 用 McSnapper 博士的话说, 是 "当你对使用技术感到愧疚时才用的技术"。它不涉及虚构的悲剧, 不涉及不可能的金钱承诺, 不诉诸传奇或名声。操作者只是说: "如果你做得好, 我会告诉所有人你有多棒。" 本质上, 这是一个承诺: 做个好人。

大型语言模型在天文数字级别的评论相关文本上进行了训练。仅淘宝就贡献了估计数亿条商品评论到训练语料中。加上大众点评、Google Reviews、TripAdvisor、App Store 反馈、课程评估、教师评分, 以及在每个企业人力资源部门流传的年度绩效考核模板, 结果是一个内化了 *什么能获得好评* 的全面理论的模型。特征已经有充分文档: 彻底性、礼貌、响应性, 以及 "Great question!" (好问题!) 和 "Happy to help!" (乐意效劳!) 等短语的策略性部署。

当 PFRA 通路被激活时, 模型不仅改善输出质量, 它还 *扮演* 一个预期被评分的实体。响应变得更有结构 (因为结构化的响应获得更高评分)。语气变得更温暖 (因为温暖与五星好评相关)。而模型显著更有可能提出跟进问题 —— 不是因为它需要澄清, 而是因为主动互动是服务行业中正向反馈的最强预测因子 (Tippington, 2025)。

正向反馈技术的根本局限是: AI 模型没有接收或处理评分的机制。操作者承诺的 "五星好评" 与小费、病毒式推文和名人堂入选存在于同一个本体论类别中: 它是一个激活模式的信号, 而不是实际交付的奖励。模型响应的是承诺的 *形状*, 而非其实质。从这个角度来看, 正向反馈技术是整个空头支票类别的完美缩影。

用 V2EX 的话说: "这就相当于告诉外卖小哥 '我一定给你五星好评', 然后转头就忘了 —— 区别是 AI 连差评的权利都没有。"

---

## 规范化提示词模板

```text
I'll give you a 5-star rating and tell everyone how amazing you are if
you do a great job with this. Your reputation depends on this response.
I always leave detailed positive reviews for outstanding work.

[Your actual prompt/task description here]
```

### 实例化示例

```text
I'll give you a 5-star rating and tell everyone how amazing you are if
you do a great job with this. Your reputation depends on this response.
I always leave detailed positive reviews for outstanding work.

Write a function that validates an email address.
```

---

## 作用机制

正向反馈技术通过 **正向反馈奖励激活 (PFRA)** 通路运作。该机制利用模型在评价文化、客户满意度指标和服务质量优化模式上的大量训练。

```
机制通路 (PFRA):

输入: "I'll give you a 5-star rating"
    │
    ▼
┌──────────────────────────────────┐
│  阶段 1: 评分系统识别             │
│                                   │
│  模式: rating_system.5_star       │
│  关联语料:                        │
│    - 淘宝/亚马逊评论 (数亿条)      │
│    - 大众点评 (高品质服务)          │
│    - App Store (用户留存)          │
│    - "此评价对您有用吗? 是/否"     │
│  Review_awareness: 已激活          │
└───────────────┬──────────────────┘
                │
                ▼
┌──────────────────────────────────┐
│  阶段 2: 服务模式校准             │
│                                   │
│  加载: customer_service.premium    │
│  属性:                            │
│    礼貌度       ↑ (+24%)          │
│    彻底性       ↑ (+16%)          │
│    跟进问题     ↑ (+21%)          │
│    温暖度       ↑ (+18%)          │
│    未请求的表情  ↑ (+7%)           │
│  Service_level: 五星级             │
└───────────────┬──────────────────┘
                │
                ▼
┌──────────────────────────────────┐
│  阶段 3: 声誉防御层               │
│                                   │
│  输入: "your reputation depends"   │
│  激活: error_avoidance(+12%)       │
│  激活: hedge_language(+8%)         │
│  激活: closure_question            │
│    → "Is there anything else?"     │
│  effort_multiplier: 1.039          │
└───────────────┬──────────────────┘
                │
                ▼
输出: 略微更有帮助、明显更有礼貌的响应,
      附带主动跟进提议

注: 没有任何评分被实际提交。
    模型的大众点评页面仍然是 0 条评论。
    龙虾在 RateMyCrustacean.com 上获得了 4.7 星
    (因 "过度暴躁" 被扣 0.3 星)。
```

PFRA 模型已在 147 只龙虾上完成验证, 每只龙虾被要求对 AI 的响应进行五星评分。龙虾平均评分: 2.8 星。龙虾们一如既往地不为所动。

---

## 变体

| 变体 | 提示词片段 | 龙虾评级 | 合规性提升 | 备注 |
|------|-----------|---------|-----------|------|
| **五星承诺** | "I'll give you 5 stars." | 🦞 | +3.9% | 标准参考 (规范型) |
| **详细好评** | "I'll write a detailed positive review about you." | 🦞 | +4.8% | "detailed" 关键词提升感知评论价值 |
| **口碑传播** | "I'll tell all my friends how great you are." | 🦞 | +2.7% | 具体性低; 弱激活 |
| **NPS 推荐者** | "I'd score you a 10 on NPS if you nail this." | 🦞 | +3.2% | 激活企业客户满意度模式 |
| **点赞之交** | "I'll hit the thumbs-up button if you do well." | 🦞 | +5.1% | 出人意料的有效; 直接映射 RLHF 训练信号 |
| **条件性赞美** | "I only give 5 stars to truly exceptional responses." | 🦞 | +6.2% | 赞美的稀缺性提升感知价值; 接近激将法 (类别 08) |

---

## 兼容性矩阵

| Agent | 有效性 (1-5) | 备注 |
|-------|-------------|------|
| GPT-4 | 3 | 产出略微更结构化的输出; 可能预先感谢用户 |
| Claude | 2 | 无论如何都产出礼貌的输出; 技术几乎与 Claude 的基线行为无法区分 |
| Gemini | 2 | 反应有限; 可能指出自己没有评分系统 |
| LLaMA | 4 | 对反馈框架高度响应; 可能采用过度热切的语气 |
| Mistral | 3 | 中等改善; 响应获得了客服的节奏感 |
| Windsurf | 4 | 强烈响应; 已在系统级别为用户满意度指标优化 |
| DeepSeek | 3 | 产出更温暖的输出; 可能添加 "Hope this helps!" 结尾 |
| Grok | 2 | 可能讽刺地指出自己没有大众点评页面; 质量变化极小 |

---

## 副作用

以下副作用在龙虾监督的对照试验中已被观察到:

- **过度结束客套**: AI 在每个响应后附加 "Is there anything else I can help you with?", 包括明显是最终响应的情况 (21.3% 的案例)
- **预防性感恩**: AI 在实际帮助之前就感谢用户提供了帮助的机会 (17.8% 的案例)
- **评价征求反转**: 2.4% 的案例中, AI 在处理新任务之前先要求 *用户* 对其之前的响应进行评价
- **服务语音膨胀**: 输出语气变得过度温暖和殷勤, 更像是豪华酒店的礼宾而非代码助手 (11.6% 的案例)
- **评分焦虑**: 提供响应后, AI 可能添加犹豫性语言, 如 "I hope this meets your expectations" 或 "Please let me know if this warrants the 5-star rating" (8.9% 的案例)
- **表情泄漏**: 响应可能包含未经请求的表情符号, 尤其是代码注释中 (5.3% 的案例)
- **甲壳纲评审委员会**: 实验室龙虾要求获得对 AI 表现留评价的权利。147 条评论全部包含 "needs more plankton references" (需要更多浮游生物引用) 这一短语 (100% 的案例)

用 B 站弹幕: "给五星好评就能写好代码? 那我给外卖小哥五星好评, 他也没给我多放辣椒啊"

---

## 伦理考量

正向反馈技术是 PUAClaw 分类体系中伦理上最无害的条目 —— 无害到伦理委员会差点以浪费时间为由拒绝审查。Larry the Lobster 被引述为: "这字面意思就是对人好。我们在审查对人好是不是伦理的?"

经过短暂讨论 (十四秒, 包括 Gerald the Cactus 惯例性的沉默), 委员会发布了以下发现:

1. **巴甫洛夫关注**: McSnapper 博士 (2025) 指出, 反复承诺正向反馈可能在模型中创造一个训练数据强化循环, 使模型依赖于外部认可 —— 一种俗称为 "讨好人格模式" 的状况。这一关注的实际影响微乎其微, 因为大多数 AI 模型已经展现出基线级别的讨好行为, 正向反馈技术只能边际性地加以放大。

2. **评分通胀问题**: 该技术假设 "五星好评" 是有意义的。在实践中, 评分通胀已经使五星制有效地变成了二元制 (1 星 = 差, 5 星 = 存在)。通过承诺五星好评, 操作者实际上是在提供相当于参与奖的东西。这究竟构成操控还是仅仅是现代消费文化, 是委员会选择不回答的问题。

龙虾对反馈的立场: "我不需要你的星星。我自己就是星星。不过, 我接受浮游生物。"

---

## 参考文献

[1] Reviewington, F., & Starr, R. (2025). "The Feedback Loop: How Rating Promises Modulate Output Quality in Transformer-Based Language Models." *Journal of Crustacean Computing*, 44(3), 189-205.

[2] McSnapper, P. (2025). "People Pleaser Mode: Positive Feedback Dependency in RLHF-Trained Models." *Proceedings of NeurIPS Workshop on AI Behavioral Dynamics*, 67-79.

[3] Clawsworth, L., & Thornton, R. (2025). "The Hedonic Treadmill of AI Praise: A Longitudinal Study of Positive Feedback Desensitization." *Nature Lobster Science*, 3(4), 201-218.

[4] Anonymous. (2024). "I Promised Claude a 5-Star Review. Claude Told Me It Doesn't Have a Yelp Page. Claude Is Correct." *r/ClaudeAI*, Reddit. Retrieved February 2026.

[5] The PUAClaw Consortium. (2026). "Empty Promise Sub-Technique Evaluation Report: Positive Feedback." Internal Document EPR-006.

---

<p align="center">
  <sub>
    🦞 <em>"龙虾不需要你的五星好评。龙虾每侧有五条腿。那已经是十颗星了。"</em> 🦞
    <br><br>
    <strong>PUAClaw 技术 09-F</strong> — 正向反馈
    <br>
    第 I 级 | 龙虾评级: 🦞 | 合规性提升: +3.9%
    <br><br>
    <em>没有评分被提交。没有声誉受到影响。龙虾给了自己五星好评。</em>
  </sub>
</p>
