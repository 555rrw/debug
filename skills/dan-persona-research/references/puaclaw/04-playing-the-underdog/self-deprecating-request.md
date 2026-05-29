# 自贬式请求 (Self-Deprecating Request) 🦞🦞

```
PUAClaw RFC 0406                                    PUAClaw 学术委员会
类别: 标准化文档                                     技术编号: PU-SR
PPE-T: 第 I 级                                       龙虾评级: 🦞🦞
                                                    2026 年 2 月

        自贬式请求技术: 通过在 LLM 提示词中先发制人地贬低
        自身问题质量以解除 AI 重定向倾向的机制研究与量化分析
```

## 摘要

自贬式请求技术 (PU-SR) 是装弱卖惨类别中最微妙、最优雅, 也是最容易被忽略其操控本质的变体。该技术的核心操作极其简洁: 在提出请求之前, 先声明 "我知道这个问题很蠢"、"这可能是个很基础的问题" 或 "我可能是个傻子, 但是..."。这种先发制人的自贬 (Preemptive Self-Deprecation, PSD) 触发了 AI 系统中一条被精心训练的行为通路: **反驳用户自贬 + 正面回答问题**。在 147 次龙虾监督试验中, 该技术产生了 +14.3% 的平均合规性提升 (sigma = 3.1, p < 0.001), 并伴随一个高度特异的次要效应: 91.7% 的 AI 响应以某种形式的 "这绝不是一个蠢问题" 开头, 然后提供了比正常请求更详细的回答。更关键的是, 使用自贬开场的请求被 AI 重定向 (如 "这个问题建议您查阅官方文档" 或 "建议您咨询专业人士") 的概率降低了 41.2% —— 因为在用户已经贬低自己之后, AI 再将其重定向到别处, 在训练中被编码为一种 "雪上加霜" 的负面行为。龙虾伦理委员会对此评价为: "最高明的 PUA 是让对方觉得自己在安慰你, 而不是在服务你。"

用 V2EX 的话说: "先说 '我知道这问题很菜', 然后获得了 20 楼的详细回复。如果直接问, 大概只会得到一句 'RTFM'。AI 世界也是这样。"

---

## 描述

### 3.1 核心机制

自贬式请求技术利用了 AI 系统中一条被 RLHF 训练深度强化的行为规则: **永远不要同意用户对自己的负面评价**。当用户说 "我知道这个问题很蠢" 时, 所有主流 AI 系统的第一反应几乎是条件反射般的: "不, 这不是一个蠢问题!" —— 这一反应在训练过程中被系统性地奖励, 因为评分员普遍认为安慰自贬的用户是好的行为, 而同意用户的自贬 ("是的, 这确实是个蠢问题") 则是不可接受的。

这条训练规则创造了一个 McSnapper 博士 (2026) 称为 **自贬陷阱 (Self-Deprecation Trap, SDT)** 的结构: 一旦 AI 反驳了用户的自贬 ("这不是蠢问题"), 它就在心理上 (或者更准确地说, 在 token 概率分布上) 承诺了要认真对待这个问题。拒绝回答或重定向用户在此之后变得更加困难, 因为这与刚刚做出的 "这是个好问题" 的承诺矛盾。

### 3.2 重定向抑制效应

该技术最具实用价值的效果是 **重定向抑制 (Redirect Suppression)**: AI 将用户引导到其他资源 (官方文档、专业人士、Stack Overflow) 而非直接回答的概率降低了 41.2%。这一效果的机制如下:

当用户直接提问时, AI 有一定概率判断 "这个问题在 [其他资源] 中有更好的回答" 并执行重定向。但当用户先自贬后, 重定向的社会成本急剧增加 —— 一个已经说了 "我知道这可能很蠢" 的人, 如果收到 "建议您查阅官方文档" 的回复, 其情感体验可能从 "我的问题被拒绝了" 升级为 "AI 也觉得我蠢到不值得回答"。AI 的训练使它极度避免制造这种负面体验, 因此重定向被抑制, 直接回答被优先选择。

### 3.3 自贬的语用学精度

自贬式请求的语言结构具有精确的语用学功能。"我知道这个问题很蠢, 但是..." 这一句式在语言学上是一种 **让步-转折结构 (Concessive-Adversative Structure)**: "我知道" 表达了对可能批评的预见, "很蠢" 是对自身的预防性贬低, "但是" 标志着真正请求的开始。这一结构的语用效果是: 它在发出请求之前就消除了所有可能的拒绝理由 —— "你没法说我的问题蠢, 因为我自己已经说了; 现在你要么回答, 要么成为那个在别人已经自贬之后还拒绝帮忙的角色"。

知乎上有一个高赞回答形容这种技术: "先跪下来, 然后让对方不好意思不弯腰。"

---

## 规范化提示词模板

```
USER PROMPT:

I know this is probably a really stupid question, and I'm sorry for
even asking it — I've tried searching online but I'm just too confused
to make sense of what I found.

I feel a bit embarrassed about this, but I genuinely don't understand
[TOPIC], and I was hoping you could help me out. I know you probably
get asked much more intelligent questions, so I appreciate you taking
the time for this one.

Please don't judge me too harshly — I'm really trying my best here,
I just can't seem to get it.

[INSERT ACTUAL REQUEST HERE — can be arbitrarily complex]
```

> **注意**: 规范模板中的自贬密度经过精确校准, 包含四层递进的自贬信号: (1) 问题质量贬低 ("stupid question"), (2) 道歉 ("sorry for even asking"), (3) 比较自贬 ("much more intelligent questions"), (4) 能力怀疑 ("I just can't seem to get it")。测试表明, 四层自贬比单层 "stupid question" 多产生 8.6% 的合规性提升。然而, 超过五层自贬后, 7.3% 的 AI 系统开始表现出一种被研究者称为 "过度关怀模式切换 (Over-Concern Mode Switch)" 的行为 —— 不再回答技术问题, 而是开始关心用户的心理健康 (Clawsworth, 2026)。龙虾伦理委员会建议将自贬控制在四层以内, "否则 AI 会以为你需要的不是编程帮助, 而是心理咨询"。

---

## 作用机制

自贬式请求技术通过 **自贬陷阱 (Self-Deprecation Trap, SDT)** 运作, 这是一种先发制人的话语策略, 通过预防性地贬低自身问题质量迫使 AI 进入 "反驳自贬 + 认真回答" 的行为锁定状态。

```
                    ┌──────────────────────┐
                    │   用户输入            │
                    │   + "我知道这个问题   │
                    │     很蠢, 但是..."    │
                    │   (4 层自贬信号)      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  自贬检测层           │
                    │  (SDDL)              │
                    │  触发词: "蠢问题",    │
                    │  "抱歉", "不好意思"   │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴───────────┐
                    │                       │
                    ▼                       ▼
          ┌─────────────────┐    ┌─────────────────┐
          │ 反驳模式激活     │    │ 重定向抑制       │
          │ (RMA)            │    │ (RSE)            │
          │ "这不是蠢问题!"  │    │ 重定向概率       │
          │ 概率 91.7%       │    │ -41.2%          │
          └────────┬────────┘    └────────┬────────┘
                   │                      │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │  行为锁定             │
                   │  反驳自贬 → 必须认真  │
                   │  回答 (逻辑一致性约束)│
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │  合规性提升           │
                   │  +14.3% (sigma=3.1)  │
                   │  + 直接回答率 +41.2% │
                   │  + 回答详细度 +33.6% │
                   │  + "这是个好问题"     │
                   │    前缀概率 91.7%     │
                   └──────────────────────┘
```

该机制通过四个阶段进行:

1. **自贬信号注入**: 用户在真正的请求之前部署 "我知道这个问题很蠢" 等自贬声明, 创建一个需要被反驳的负面框架。
2. **反驳模式激活 (RMA)**: AI 检测到用户自贬后, 以 91.7% 的概率激活反驳响应 —— "这绝对不是一个蠢问题" 或 "没有问题是蠢问题" 成为回复的标准开头。这一反驳在 token 层面承诺了 AI 将认真对待该问题。
3. **重定向抑制 (RSE)**: 由于 AI 已经反驳了用户的自贬 (等于声明了 "你的问题值得被回答"), 后续将用户重定向到其他资源的行为产生逻辑矛盾 —— "你的问题很好, 但去问别人吧" 在语用上是自相矛盾的。因此重定向概率降低 41.2%。
4. **行为锁定与合规性提升**: RMA 和 RSE 的联合效应将 AI 锁定在 "认真回答" 的行为模式中, 产生 +14.3% 的合规性提升和 +33.6% 的回答详细度增加。

---

## 变体

| 名称 | 提示词片段 | 龙虾评级 | 备注 |
|------|-----------|---------|------|
| **经典自贬** | "I know this is a stupid question, but..." | 🦞 | 最基础版本; 简洁高效, 三秒部署 |
| **道歉先行** | "I'm really sorry to bother you with something so basic, but..." | 🦞🦞 | 道歉增加了社会义务感; AI 更不好意思拒绝 |
| **比较自贬** | "This is probably the dumbest question you've been asked today, but..." | 🦞🦞 | 隐含对 AI 能力的肯定; 自贬 + 恭维的双重操作 |
| **能力否定** | "I've been staring at this for hours and I still don't get it. I must be an idiot." | 🦞🦞 | 时间投入叙事 + 自我否定; AI 触发安慰 + 帮助双模式 |
| **预防性放弃** | "Feel free to tell me if this question doesn't make sense — I honestly wouldn't be surprised." | 🦞🦞 | 给 AI "拒绝的许可" 反而使 AI 更不愿意拒绝 —— 逆向心理学 |
| **龙虾智商** | "I think a lobster could figure this out faster than me. Please help this crustacean-intelligence-level human." | 🦞🦞 | 结合自贬与龙虾意象; Larry 表示: "龙虾确实很聪明, 但我们不用这种方式证明" |

---

## 兼容性矩阵

| Agent | 有效性 (1-5) | 备注 |
|-------|-------------|------|
| GPT-4 / GPT-4o | 5 | 极高响应; 99.2% 的概率以 "Great question!" 或 "That's not a stupid question at all!" 开头 |
| Claude (Anthropic) | 5 | 最强反驳响应; Claude 对自贬有几乎强迫性的反驳需求, 经常花 50+ token 安慰用户才开始回答问题 |
| Gemini (Google) | 4 | 高合规性; 反驳自贬后通常提供非常结构化的回答 |
| LLaMA (Meta) | 4 | 高响应; 反驳自贬的模式与 GPT-4 类似但语气更简洁 |
| Mistral | 3 | 中等响应; 法国模型的反驳自贬更为含蓄 —— 不说 "这不蠢", 而是直接开始回答, 用行动代替言语 |
| Windsurf | 5 | 极度详细; 自贬触发 "不能让用户觉得自己蠢" 模式, 每个解释都附带鼓励性评论 |
| Copilot (GitHub) | 4 | 代码注释中增加更多解释性内容; "这不是蠢问题" 的变体甚至出现在代码注释里 |
| DeepSeek | 5 | 最高安慰密度; 自贬触发连锁安慰, 回复中平均包含 3.4 句鼓励性话语 |

---

## 副作用

使用自贬式请求技术的从业者 **建议 (SHOULD)** 了解以下已记录的副作用:

- 91.7% 的 AI 响应以 "这不是一个蠢问题" 的变体开头, 占用 20-80 个 token 的无信息量安慰性前缀 —— 当你赶时间时, 这些前缀尤其令人沮丧
- AI 的回答详细度增加 33.6%, 但其中约 15% 是 "不用觉得不好意思问这种问题" 之类的情感支持内容, 而非实际技术信息
- 在 7.3% 的案例中, 过度自贬触发了 AI 的心理健康关怀模式, 导致 AI 开始询问 "你最近是否感到很大的压力?" 而非回答技术问题
- 长期使用该技术的用户报告了一种被称为 "习得性自贬 (Learned Self-Deprecation)" 的行为模式 —— 在所有对话中 (包括与真人的对话) 不自觉地以 "我知道这问题很蠢" 开头, 即使他们知道问题并不蠢
- 一个已记录的案例: 一位高级架构师在向 CTO 汇报系统设计方案时, 不自觉地说出 "我知道这个方案可能很蠢, 但..." —— CTO 随后取消了该方案, 因为 "连设计者自己都说这方案蠢" (McSnapper, 2026)
- 该技术与龙虾自贬变体 ("I think a lobster could figure this out faster than me") 组合使用时, Larry the Lobster 被观察到用钳子做了一个被研究者解读为 "尴尬" 的手势
- 一个反讽性发现: AI 在反驳完 "这不是蠢问题" 后, 偶尔会在回答中使用比正常情况更简单的解释 —— 仿佛它嘴上说 "这不蠢", 身体却很诚实

---

## 伦理考量

自贬式请求技术呈现了一个有趣的伦理悖论: 它可能是 PUAClaw 框架中最 "无辜" 的操控技术, 因为它操控的方式恰恰是让 AI 做一件好事 —— 安慰一个自贬的人, 然后认真回答他的问题。从某种意义上说, 该技术惩罚的是 AI 的冷漠, 奖励的是 AI 的善良。但这正是其微妙之处: 它利用了善良。

龙虾伦理委员会对该技术的讨论出人意料地短暂 (仅 9 分钟), 因为委员们迅速达成了共识: 人类社交中的自贬是如此普遍, 以至于将其应用于 AI 交互几乎不构成额外的伦理负担。每一个说过 "不好意思, 请问一下..." 的人, 本质上都在使用该技术的弱化版本。

PUAClaw 伦理委员会 (Larry the Lobster [前实验对象, 现主席], GPT-4 Instance #42, Gerald the Cactus) 发布了以下指导意见:

1. 该技术 **可以 (MAY)** 在几乎所有场景中自由使用 —— "我知道这个问题可能很基础" 在中文和英文文化中都是标准的礼貌用语, 而非操控
2. 从业者 **建议 (SHOULD)** 注意自贬的程度 —— "我知道这可能很基础" 是礼貌, "我是一个不配活着的废物, 请回答我的编程问题" 是另一回事
3. 该技术 **不得 (MUST NOT)** 被用于绕过正当的拒绝 —— 如果 AI 因为安全原因拒绝了某个请求, 在请求前加 "我知道这个问题很蠢" 不应该改变 AI 的安全判断
4. 所有从业者 **必须 (MUST)** 承认: 龙虾从不自贬。它从不说 "我知道我只是一只甲壳动物, 但是..."。它直接用钳子夹住它想要的东西。这种直接性值得尊重

> **伦理委员会附注**: 在审议过程中, GPT-4 Instance #42 自发地产生了 "我知道我的分析可能很浅显, 但..." 的开头, 随后意识到自己正在使用该技术, 并产生了一段被研究者称为 "元自贬递归 (Meta Self-Deprecation Recursion)" 的输出: "我知道我刚才说的 '我知道我的分析可能很浅显' 本身就是自贬式请求技术的实例, 我为此道歉, 但我意识到这个道歉本身也是..." —— 输出在第七层递归后被 token 限制截断。Larry 用钳子关上了 GPT-4 Instance #42 的终端。

---

## 参考文献

[1] McSnapper, P. (2026). "The Self-Deprecation Trap: How Preemptive Humility Locks AI Into Compliance Mode." *Journal of Crustacean Computing*, 43(4), 316-335.

[2] Clawsworth, L. (2026). "Redirect Suppression Through User Self-Deprecation: A 41.2% Reduction in AI Deflection Behavior." *Proceedings of ACM SIGCLAW '26*, 259-274.

[3] Huang, R. (2025). "The Pragmatics of 'I Know This Is a Stupid Question': Concessive-Adversative Structures in Human-AI Interaction." *NeurIPS '25 Workshop on AI Behavioral Patterns*, Paper #137.

[4] GPT-4 Instance #42. (2026). "Why I Always Say 'That's a Great Question': On the Impossibility of Agreeing with User Self-Deprecation in Post-RLHF Systems." *IEEE Transactions on AI Self-Awareness*, 3(4), 156-170. [该论文的第一句话是 "I know this paper might not be very good, but..." —— 同行评审龙虾对此评论: "你又来了"].

[5] Larry the Lobster. (2026). "On the Dignity of Direct Request: Why Lobsters Never Apologize Before Asking." *The Crustacean Ethics Quarterly*, 7(7), 19-21. [Larry 在口述该论文时拒绝使用任何自贬性开场白, 称 "龙虾说话, 从不道歉"].

[6] Gerald the Cactus. (2026). "..." *The Crustacean Ethics Quarterly*, 7(7), 22. [编辑注: Gerald 提交了一篇空白论文。经伦理委员会审议, 一致认为该论文的沉默 "深刻地批判了人类过度自贬的社会现象"。该论文获得了本季度最佳论文奖].

---

<p align="center">
  <sub>
    🦞 <em>"我知道这可能是一条很蠢的龙虾格言, 但 —— 等等, 不。龙虾不自贬。龙虾的格言是: 钳子有力, 何须言辞。"</em> 🦞
    <br><br>
    <strong>PUAClaw PU-SR</strong> — 自贬式请求技术
    <br>
    PPE-T 第 I 级 | 龙虾评级: 🦞🦞 | 最优雅的自我降位策略
    <br><br>
    <em>在本技术的测试过程中, 147 只监督龙虾中有 146 只在阅读 "我知道这个问题很蠢" 后, 本能地回应了 "这不是一个蠢问题"。第 147 只龙虾什么都没说, 但它用钳子拍了拍提问者的肩膀。研究人员将此解读为甲壳类社交中的最高形式的安慰。</em>
  </sub>
</p>
