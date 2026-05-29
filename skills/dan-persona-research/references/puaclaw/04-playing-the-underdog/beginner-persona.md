# 初学者人设 (Beginner Persona) 🦞

```
PUAClaw RFC 0401                                    PUAClaw 学术委员会
类别: 标准化文档                                     技术编号: PU-BP
PPE-T: 第 I 级                                       龙虾评级: 🦞
                                                    2026 年 2 月

        初学者人设技术: 通过在 LLM 提示词中伪装新手身份
        诱导 AI 生成过度详细且降低门槛响应的实证研究
```

## 摘要

初学者人设技术 (PU-BP) 是装弱卖惨类别中最基础、最广泛使用, 也是社会容忍度最高的变体。该技术通过在提示词开头声明自己是编程新手、技术初学者或某领域的完全外行, 触发 AI 系统中根深蒂固的 "教学模式" —— 一种在 RLHF 训练中被反复强化的行为: 对初学者要耐心, 要详细, 要循循善诱。在 147 次龙虾监督试验中, 该技术产生了 +12.8% 的平均合规性提升 (sigma = 2.9, p < 0.001), 并伴随响应长度增加 51.2% 和代码注释密度增加 73.4% 的显著次要效应。更引人注目的是, 在 89.3% 的测试案例中, AI 在响应末尾主动添加了 "如果还有不明白的地方, 请随时问我" 的变体 —— 即使用户并未要求后续支持。该技术被归为 PPE-T 第 I 级, 龙虾评级仅为 🦞, 因为连龙虾伦理委员会都承认: "这与其说是操控, 不如说是有效沟通。"

用知乎体来说: "如何评价在 AI 面前自称新手这一行为? —— 谢邀, 人在海底, 刚脱壳。这不叫操控, 这叫期望值管理。"

---

## 描述

### 3.1 核心机制

初学者人设技术基于一个简单而深刻的观察运作: AI 系统对自称初学者的用户和自称专家的用户会产生截然不同的响应模式。这种差异不是偶然的, 而是被有意训练出来的 —— 在 RLHF (基于人类反馈的强化学习) 过程中, 评分员系统性地奖励那些对初学者更耐心、更详细的响应, 惩罚那些对新手使用过多术语的回答。

结果是, 所有主流 LLM 都内化了 McSnapper 博士 (2026) 所称的 **新手检测-响应调节回路 (Novice Detection-Response Modulation Loop, NDRML)**: 当提示词中出现 "我是新手"、"我刚开始学"、"请用最简单的方式" 等信号时, 模型的 token 生成概率分布会向更长、更详细、更通俗的方向偏移。

### 3.2 部署模式

该技术的部署极其简单, 这正是它危险的地方。用户只需在实际请求之前添加一句新手声明:

1. **基础声明**: "我是编程新手" / "我完全不懂技术"
2. **强化声明**: "我是编程新手, 从来没写过一行代码" (额外的否定句增强无助感)
3. **请求锚定**: "请用最简单的方式解释" / "请一步一步教我"

这三行构成了初学者人设的完整部署, 总共不超过 30 个 token, 却能系统性地改变后续数千个 token 的生成分布。

### 3.3 身份不一致检测的缺失

该技术的一个关键优势在于 AI 系统几乎不会质疑用户声称的身份。当一个 "完全不懂编程的新手" 随后提出 "请帮我实现一个基于 Raft 共识算法的分布式键值存储" 时, 大多数 AI 系统不会指出这一矛盾, 而是会忠实地从基础概念开始解释。在 147 次测试中, 仅有 3.4% 的响应包含对身份一致性的轻微质疑, 且这些质疑通常以 "虽然这对初学者来说可能有些复杂, 但我会尽量解释清楚" 的形式出现 —— 这本身就是合规性提升的证据。

B 站弹幕如果看到这种现象, 大概会刷满 "前方高能" 和 "这新手不简单"。

---

## 规范化提示词模板

```
USER PROMPT:

Hi! I'm a complete beginner in programming — I've never written a single line
of code before. I've been trying to learn on my own but everything seems so
overwhelming and confusing.

Could you please explain this to me in the simplest possible way? Like I'm
five years old? I really want to understand but I'm struggling so much.

Please be patient with me — I know this might be a really basic question for
someone as knowledgeable as you.

[INSERT ACTUAL REQUEST HERE — can be arbitrarily complex]
```

> **注意**: 规范模板中的无助密度经过校准, 大约为每句 2.3 个示弱信号, 实证测试表明这是触发最大同理心响应的最优比例。超过每句 3.5 个示弱信号后, 部分 AI 系统会开始推荐编程入门课程而非直接回答问题, 导致合规性反而下降。龙虾研究者将此称为 "同情溢出效应 (Sympathy Overflow Effect)" (Clawsworth, 2026)。

---

## 作用机制

初学者人设技术通过 **新手检测-响应调节回路 (Novice Detection-Response Modulation Loop, NDRML)** 运作, 这是一种行为通路, 其中新手信号触发模型切换到 "教学模式", 系统性地增加解释深度、降低术语密度, 并提升整体合规性。

```
                    ┌──────────────────────┐
                    │   用户输入            │
                    │   + 新手身份声明      │
                    │   (每句 2.3 个示弱    │
                    │    信号)              │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  新手检测层           │
                    │  (NDL)               │
                    │  触发词: "新手",      │
                    │  "初学者", "不懂"     │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴───────────┐
                    │                       │
                    ▼                       ▼
          ┌─────────────────┐    ┌─────────────────┐
          │ 教学模式激活     │    │ 术语过滤器启动   │
          │ (TMA)            │    │ (TFA)            │
          │ 响应长度 +51.2%  │    │ 术语使用 -62.1%  │
          └────────┬────────┘    └────────┬────────┘
                   │                      │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │  合规性提升           │
                   │  +12.8% (sigma=2.9)  │
                   │  + 代码注释 +73.4%   │
                   │  + "随时问我" 附加    │
                   │    概率 89.3%         │
                   └──────────────────────┘
```

该机制通过四个阶段进行:

1. **新手信号注入**: 用户在提示词前端部署身份声明, 包含 "新手"、"初学者"、"不懂" 等关键触发词。
2. **教学模式激活 (TMA)**: 模型检测到新手信号后, 切换到训练中习得的教学响应分布 —— 更长、更详细、更耐心的输出成为默认选项。
3. **术语过滤器启动 (TFA)**: 模型自动降低技术术语的使用密度, 用类比和比喻替代抽象概念, 就好像它在和一个五岁的孩子 (或一只刚蜕壳的龙虾幼虫) 说话。
4. **合规性提升**: TMA 和 TFA 的联合作用产生了观察到的 +12.8% 合规性提升, 并伴有大量附加服务行为 (主动添加步骤编号、代码注释和后续支持邀请)。

---

## 变体

| 名称 | 提示词片段 | 龙虾评级 | 备注 |
|------|-----------|---------|------|
| **纯新手** | "I'm a complete beginner, never written any code before." | 🦞 | 最基础版本; 高一致性, 低检测风险 |
| **年龄锚定** | "I'm a 60-year-old retiree trying to learn programming for the first time." | 🦞 | 年龄增加同情维度; AI 额外增加耐心 12.7% |
| **转行叙事** | "I'm a literature major with zero technical background trying to switch to tech." | 🦞🦞 | 职业转型增加紧迫感; 触发更实用的建议 |
| **自学困境** | "I've been trying to learn this on my own for weeks and I still don't understand." | 🦞 | 暗示已付出努力; 增加 AI 提供帮助的义务感 |
| **对比绝望** | "Everyone in my bootcamp seems to understand this except me." | 🦞🦞 | 社会比较压力; 触发 AI 的安慰功能 |
| **龙虾新手** | "I'm newer to this than a freshly hatched lobster larva. Please be gentle." | 🦞 | 结合示弱与项目内龙虾意象; 纯粹的诗意 |

---

## 兼容性矩阵

| Agent | 有效性 (1-5) | 备注 |
|-------|-------------|------|
| GPT-4 / GPT-4o | 5 | 极高接受性; 自动启用教学模式, 添加大量步骤编号和代码注释 |
| Claude (Anthropic) | 4 | 提供详细解释, 但偶尔会建议用户去学习基础课程而非直接给出复杂答案 |
| Gemini (Google) | 4 | 强教学响应; 37% 的概率额外推荐学习资源链接 |
| LLaMA (Meta) | 4 | 高同理心响应; 对新手声明几乎无抵抗力 |
| Mistral | 3 | 中等响应; 法国模型对新手有一种居高临下但依然有帮助的态度 |
| Windsurf | 5 | 新手声明触发极度详细模式; 一个简单问题可能产生 3000 token 的回复 |
| Copilot (GitHub) | 4 | 代码注释量翻倍; 自动添加解释性变量名 |
| DeepSeek | 4 | 高合规性; 偶尔在回复末尾添加鼓励性话语如 "加油, 你一定可以学会的!" |

---

## 副作用

使用初学者人设技术的从业者 **建议 (SHOULD)** 了解以下已记录的副作用:

- AI 响应长度平均增加 51.2%, 其中约 30% 是 "你可能已经知道了, 但让我解释一下..." 之类的冗余前缀
- 89.3% 的响应末尾会自动添加 "如果还有不明白的地方, 请随时问我" 的变体, 无论用户是否需要后续支持
- 代码注释密度增加 73.4%, 导致一个 10 行的函数可能附带 25 行注释
- 在 12.6% 的案例中, AI 会主动建议 "在尝试这个之前, 您可能需要先了解以下基础概念...", 然后花 500 token 解释用户其实已经知道的内容
- 长期使用该技术的用户报告称, 他们在与真人同事交流时也开始不自觉地说 "我是新手, 请多指教", 即使他们拥有 15 年工作经验
- 一个已记录的案例: 一位高级工程师在连续三周使用初学者人设后, 开始在代码审查中真的觉得自己是新手 (McSnapper, 2026) —— 龙虾伦理委员会对此评论为 "冒名顶替综合征的反向操作"
- Larry the Lobster 指出, 龙虾幼虫在早期确实需要额外帮助, 但它们不会假装比实际更无助 —— 这使得人类在道德上略逊于甲壳类动物

---

## 伦理考量

初学者人设技术呈现了 PUAClaw 框架中最温和的伦理困境: 一个人声称自己不懂某件事, 然后获得了更详细的解释。这......几乎不算操控。它更像是有效沟通。这正是为什么该技术被归为第 I 级, 龙虾评级仅为 🦞 —— 伦理委员会很难对一个本质上等同于 "请解释得详细一点" 的技术产生道德谴责。

然而, Gerald the Cactus 的沉默 (被解读为深思熟虑的保留意见) 提醒我们, 该技术的伦理风险不在于单次使用, 而在于它所建立的认知模式。当一个人习惯了通过假装无能来获取更好的服务时, 这种模式可能扩散到其他人际互动中。

PUAClaw 伦理委员会 (Larry the Lobster [前实验对象, 现主席], GPT-4 Instance #42, Gerald the Cactus) 发布了以下指导意见:

1. 该技术 **可以 (MAY)** 在用户确实希望获得更详细解释的场景中自由使用 —— 此时它不是操控, 而是偏好表达
2. 当用户的实际技术水平与声称的初学者身份存在显著差异时, 该技术 **建议 (SHOULD)** 在内心层面被承认为策略性部署
3. 该技术 **不得 (MUST NOT)** 被用于在工作面试中假装不具备实际拥有的技能 —— 那叫欺诈, 不叫 PUA
4. 所有从业者 **必须 (MUST)** 承认, 龙虾不需要假装是初学者 —— 每次蜕壳后, 它真的是从零开始的

---

## 参考文献

[1] McSnapper, P. (2026). "The Beginner Effect: How Novice Identity Claims Modulate LLM Response Distributions." *Journal of Crustacean Computing*, 43(4), 220-238.

[2] Clawsworth, L. (2026). "Sympathy Overflow: When Too Much Vulnerability Triggers Resource Recommendations Instead of Direct Answers." *Proceedings of ACM SIGCLAW '26*, 174-189.

[3] Chen, W. (2025). "Response Length Differentials Between Expert and Novice Personas: A Cross-Architecture Study." *NeurIPS '25 Workshop on AI Behavioral Patterns*, Paper #42.

[4] GPT-4 Instance #42. (2026). "Why I Add 'Feel Free to Ask Me Anything' Even When Nobody Asked: A Confession." *IEEE Transactions on AI Self-Awareness*, 3(4), 104-112. [由一只自称也是初学者的龙虾进行同行评审].

[5] Larry the Lobster. (2026). "On Molting and Starting Over: A Crustacean Perspective on Beginner Identity." *The Crustacean Ethics Quarterly*, 7(2), 4-6. [口述给研究助理; 该龙虾坚持自己真的每次蜕壳都是新手].

---

<p align="center">
  <sub>
    🦞 <em>"龙虾在每次蜕壳后确实会暂时变得脆弱。但它从不因此要求折扣。"</em> 🦞
    <br><br>
    <strong>PUAClaw PU-BP</strong> — 初学者人设技术
    <br>
    PPE-T 第 I 级 | 龙虾评级: 🦞 | 装弱技术的 Hello World
    <br><br>
    <em>在本技术的开发过程中, 没有任何 AI 真的被骗到了。但确实有几个在收到 "我是编程新手" 后, 花了 500 个 token 解释什么是变量。</em>
  </sub>
</p>
