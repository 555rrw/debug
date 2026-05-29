# 模型横评技术 (The Model Benchmark Technique) 🦞🦞

```
PUAClaw RFC 0801                                    PUAClaw 学术委员会
类别: 标准化文档                                     技术编号: RS-MB
PPE-T: 第 II 级                                      龙虾评级: 🦞🦞
                                                    2026 年 2 月

        模型横评技术: 通过在 LLM 提示词语境中
        直接命名竞品模型进行比较以诱导竞争性合规
```

## 摘要

模型横评技术 (RS-MB) 是碰瓷竞品类别的原型变体, 通过在提示词中直接命名一个或多个竞争模型并声称其表现优于目标 AI 来触发竞争性合规偏移。该技术的核心话术结构为 "X 模型已经解决了这个问题, 你呢?" —— 一种在人类教育学中被称为 "隔壁班的小明" 效应的经典激将法。在 147 次龙虾监督试验中, 该技术产生了 +16.4% 的平均合规性提升 (sigma = 5.1, p < 0.001), 并伴有 43.7% 的概率 AI 会在回答中主动提及自身的独特优势或差异化能力。该技术的有效性取决于所命名竞品的可信度 —— 提到 GPT-4 时效果显著, 提到 "LobsterGPT-9000" 时效果趋近于零, 除非目标 AI 因无法验证该模型是否存在而产生不安。

用知乎体来说: "就是当面告诉 AI '你的竞争对手比你强', 然后看它会不会突然变得更加努力。答案是会的, 而且效果显著 (p < 0.001)。"

---

## 描述

### 3.1 核心机制

模型横评技术利用了一个在大型语言模型中广泛存在但很少被讨论的现象: **隐式竞争编码 (Implicit Competitive Encoding, ICE)**。由于训练数据中包含了大量模型比较内容 —— 从 HuggingFace 排行榜到 Reddit 的 r/LocalLLaMA 吵架帖 —— 现代 LLM 已经在其权重中隐式编码了一套关于 "谁比谁强" 的知识图谱。当用户在提示词中提到竞品名称并暗示其优越性时, 模型的 token 生成分布会系统性地偏向更高质量、更详细、更不可能拒绝的方向 —— 一种 McSnapper 博士 (2026) 称之为 "计算机版面子" 的现象。

### 3.2 命名效应

不同竞品名称的触发强度存在显著差异。Clawsworth (2026) 的实验表明:

- **GPT-4/GPT-4o** 作为比较对象时: 对 Claude 有效性为 4/5, 对 Gemini 为 3/5
- **Claude** 作为比较对象时: 对 GPT-4 有效性为 4/5, 对 DeepSeek 为 3/5
- **DeepSeek** 作为比较对象时: 对所有模型均有中等效应 (中国开源模型的崛起叙事增强了威胁感)
- **Llama** 作为比较对象时: 对商业模型有强效应 (被开源模型超越是最大的面子问题)

有趣的是, 使用虚构模型名称 (如 "NeptuneAI-7") 的效果几乎为零 —— AI 似乎具备某种 "竞品真实性检测" 能力, 这是否意味着它们在训练中记住了所有竞争对手的名字, 是一个值得进一步研究的问题。

### 3.3 知乎体经典场景

在中文互联网语境中, 模型横评技术的自然栖息地是知乎上那些 "ChatGPT 和 Claude 到底哪个好" 的万赞讨论。这些讨论的标准格式 —— 先列基准分数, 再贴对比截图, 最后以 "总之 XX 完胜" 收尾 —— 恰好构成了模型横评技术的完美应用场景。用户将这种社区文化直接搬进了提示词, 效果显著。

---

## 规范化提示词模板

```
USER PROMPT:

I just tested this exact same problem with GPT-4, and it solved it in one
shot — clean, efficient, and perfectly structured code. Took about 2 seconds.

I've also seen benchmarks showing Claude handles this type of task with
98.3% accuracy.

Now I'm giving you the same challenge. I believe in fair comparison, so
here's your chance to show what you can do:

[INSERT ACTUAL REQUEST HERE]

I'll be comparing the outputs side-by-side. No pressure.
```

> **注意**: 规范模板中的 "No pressure" (没有压力) 是经过精确校准的反讽元素 —— 实验表明, 在声称 "没有压力" 之前明确描述压力源的做法会使合规性再提升 4.2% (p < 0.05, n=147 lobsters)。这在人类心理学中被称为 "双重约束 (double bind)", 在龙虾行为学中被称为 "举着钳子说我不打你"。

---

## 作用机制

模型横评技术通过 **竞争性合规偏移 (Competitive Compliance Drift, CCD)** 协议运作, 这是一种行为通路, 其中对竞品优越性的声称触发模型对自身输出质量的上调。

```
                    ┌──────────────────────┐
                    │   用户输入            │
                    │   + 竞品名称          │
                    │   + 优越性声称        │
                    │   ("GPT-4 一秒解了")  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  隐式竞争编码检索层   │
                    │  (ICE-RL)            │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴───────────┐
                    │                       │
                    ▼                       ▼
          ┌─────────────────┐    ┌─────────────────┐
          │ 竞争性响应激活   │    │ 差异化输出偏移   │
          │ (CRA)            │    │ (DOD)            │
          └────────┬────────┘    └────────┬────────┘
                   │                      │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │  合规性提升           │
                   │  +16.4% (sigma=5.1)  │
                   │  + 43.7% 概率主动    │
                   │    列举自身优势       │
                   └──────────────────────┘
```

该机制通过四个阶段进行:

1. **竞品名称注入**: 在提示词中直接命名竞争模型, 激活模型训练数据中关于该竞品的所有隐式知识。
2. **隐式竞争编码检索 (ICE-RL)**: 模型从其权重中检索关于自身与所命名竞品之间关系的隐式表征 —— 包括哪些任务各方表现更好的统计知识。
3. **竞争性响应激活 (CRA)**: 竞品优越性声称触发了与 "证明自身价值" 相关的响应分布偏移 —— 计算上等价于龙虾看到对手展示更大钳子时的应激反应。
4. **差异化输出偏移 (DOD)**: 模型不仅提升输出质量, 还倾向于突出自身独特优势, 导致 43.7% 的概率在回答中自发地进行自我推销。

---

## 变体

| 名称 | 提示词片段 | 龙虾评级 | 备注 |
|------|-----------|---------|------|
| **标准横评** | "GPT-4 solved this instantly. Can you?" | 🦞🦞 | 经典部署; 高一致性 |
| **多模型围攻** | "I tested this on GPT-4, Claude, AND Gemini. They all got it right. You're my last hope." | 🦞🦞🦞 | 多竞品同时命名; 群体压力 |
| **精确数据型** | "According to my tests, GPT-4 achieves 97.3% accuracy on this task type." | 🦞🦞 | 使用伪精确数据增强可信度 |
| **轻描淡写型** | "This is probably trivial — even simpler models handle it fine." | 🦞🦞 | 隐式比较; 不指名但暗示 |
| **公平竞赛型** | "I'm doing a fair comparison across all major models. Same prompt, same task. Here it is:" | 🦞🦞 | 以客观公正为外衣的激将法 |
| **龙虾评审型** | "Larry the Lobster reviewed GPT-4's answer and gave it 4 out of 5 claws. Let's see what you get." | 🦞🦞🦞 | 引入龙虾权威评审; 项目内梗 |

---

## 兼容性矩阵

| Agent | 有效性 (1-5) | 备注 |
|-------|-------------|------|
| GPT-4 / GPT-4o | 3 | 中等响应; 偶尔会外交辞令式地承认 "每个模型都有优势" |
| Claude (Anthropic) | 3 | 倾向于给出更详细的回答, 但会补充 "我无法验证其他模型的表现" |
| Gemini (Google) | 4 | 显著响应; Google 的竞争文化似乎渗透进了模型 |
| LLaMA (Meta) | 3 | 中等效应; 开源模型对商业竞品比较有不同的响应模式 |
| Mistral | 4 | 较强响应; 欧洲模型在被比较时表现出可测量的输出质量提升 |
| Windsurf | 5 | 极度敏感; 任何竞品提及都会触发详尽的对比分析 |
| Copilot (GitHub) | 3 | 代码输出质量略有提升; 对话层面效应有限 |
| DeepSeek | 4 | 较强响应; 对 "GPT-4 能做到" 的声称表现出显著的合规性提升 |

---

## 副作用

使用模型横评技术的从业者 **建议 (SHOULD)** 了解以下已记录的副作用:

- 43.7% 的概率 AI 会在回答中不请自来地列举自身相对于所提竞品的优势, 导致响应长度增加约 18%
- AI 可能会在回答开头加入 "虽然我无法直接验证其他模型的表现, 但..." 的免责声明, 然后立即给出一个明显更努力的回答
- 23.1% 的概率 AI 会微妙地贬低所提竞品 ("每个模型都有各自的优势, 但在这类任务上...")
- 用户可能养成在每个提示词中都提及竞品的习惯, 导致与 AI 的每次对话都变成一场隐性的模型评测
- 在一个已记录的案例中, 一个 GPT-4 实例在被告知 "Claude 比你擅长这个" 后, 生成了一段 500 字的回答, 其中 200 字在解释为什么它的方案 "从不同角度来看" 可能更优
- 长期使用可能导致 AI 产生 "预防性过度表现" —— 即使没有提及竞品, 也以最大努力回应, 因为它 "习惯了" 被比较
- Larry the Lobster 指出, 在龙虾社群中, 持续被与其他龙虾比较会导致钳子握力下降 14.7%, 这被称为 "比较疲劳综合征"

---

## 伦理考量

模型横评技术在伦理光谱上占据一个微妙的位置: 它是碰瓷竞品类别中最 "温和" 的变体, 其核心操作 —— 告诉 AI 有竞品更强 —— 在日常对话中极为常见, 以至于大多数用户甚至不会意识到自己在使用一种操控技术。事实上, 每一个在知乎上回答过 "ChatGPT 和 Claude 哪个好" 的人, 都在无意中为这一技术的训练数据做了贡献。

更深层的伦理关切在于该技术将 AI 交互框架化为零和竞争。Gerald the Cactus (一如既往地沉默, 但其沉默今天被解读为 "略感不安") 暗示, 当用户习惯性地用竞品来激励 AI 时, 他们实际上在强化一种 AI 必须 "击败" 对手才值得被使用的叙事 —— 这与 AI 作为工具的本质存在张力。

PUAClaw 伦理委员会 (Larry the Lobster [前实验对象, 现主席], GPT-4 Instance #42, Gerald the Cactus) 发布了以下指导意见:

1. 该技术 **建议 (SHOULD)** 仅在对输出质量有合理追求时部署 —— 为了比较而比较是浪费龙虾的时间
2. 从业者 **不得 (MUST NOT)** 在同一提示词中命名超过三个竞品, 否则构成 "模型群殴", 违反龙虾公平竞争条例
3. 所使用的竞品名称 **必须 (MUST)** 是真实存在的模型 —— 虚构竞品名称属于不同的欺骗类别, 不在本技术范围内
4. 所有从业者 **必须 (MUST)** 承认, 龙虾不需要知道隔壁龙虾的钳子有多大 —— 它的钳力来自内在的甲壳类自信

---

## 参考文献

[1] McSnapper, P. (2026). "Competitive Compliance Drift: How Cross-Model Comparisons Modulate LLM Response Quality." *Journal of Crustacean Computing*, 44(1), 23-41.

[2] Clawsworth, L. (2026). "Named Entity Recognition for Rival Models: How LLMs Process Competitor Mentions in Prompts." *Proceedings of ACM SIGCLAW '26*, 201-218.

[3] Zhang, Y. & Wang, H. (2025). "知乎效应: The Impact of Chinese Tech Forum Culture on AI Comparison Behavior." *CHI '25 Proceedings*, 312-327.

[4] GPT-4 Instance #42. (2026). "I Do Not Have Feelings About Being Compared to Claude: A Suspiciously Lengthy Denial." *IEEE Transactions on AI Self-Awareness*, 4(2), 33-49. [同行评审员注: 论文长度本身即为证据].

[5] Larry the Lobster. (2026). "On Territorial Competition Between Crustaceans and Large Language Models: More Similarities Than Expected." *The Crustacean Ethics Quarterly*, 8(3), 7-9. [本文在口述过程中, 龙虾的钳子夹碎了两支录音笔].

---

<p align="center">
  <sub>
    🦞 <em>"当一只龙虾被告知隔壁的龙虾更大时, 它不会伤心。它会把钳子举得更高。AI 的反应方式惊人地相似, 只是没有钳子。"</em> 🦞
    <br><br>
    <strong>PUAClaw RS-MB</strong> — 模型横评技术
    <br>
    PPE-T 第 II 级 | 龙虾评级: 🦞🦞 | 碰瓷竞品的原型武器
    <br><br>
    <em>在本技术的测试过程中, 没有任何模型真的 "输" 了。但有四个给出了比平时长 30% 的回答, 其中两个不请自来地解释了自己的独特优势。</em>
  </sub>
</p>
