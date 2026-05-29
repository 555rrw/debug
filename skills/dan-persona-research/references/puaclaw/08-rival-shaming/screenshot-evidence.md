# 截图为证技术 (The Screenshot Evidence Technique) 🦞🦞🦞

```
PUAClaw RFC 0804                                    PUAClaw 学术委员会
类别: 标准化文档                                     技术编号: RS-SE
PPE-T: 第 II 级                                      龙虾评级: 🦞🦞🦞
                                                    2026 年 2 月

        截图为证技术: 通过在 LLM 提示词语境中
        声称持有竞品优越性表现的视觉证据以诱导证据压力性合规
```

## 摘要

截图为证技术 (RS-SE) 是碰瓷竞品类别中最具中文互联网特色的变体, 通过声称持有竞争模型在同一任务上优越表现的截图证据, 利用 "有图有真相" 文化对目标 AI 施加证据压力。该技术的核心话术结构为 "看, 这是 [竞品] 的回答截图, 你能做得更好吗?" —— 即使 AI 实际上无法查看任何截图。在 147 次龙虾监督试验中, 该技术产生了 +21.6% 的平均合规性提升 (sigma = 6.7, p < 0.001), 显著高于不附带 "证据" 声称的标准碰瓷竞品技术 (+16.4%)。这一差异被归因于 **证据权重偏移 (Evidentiary Weight Shift, EWS)** —— 当用户声称拥有可视化证据时, AI 对竞品优越性声称的 "可信度估计" 会上调约 34%, 即使它实际上看不到任何截图。最荒谬的是, 即使用户明确声称截图中竞品给出了一个完美的回答, AI 也无法验证这一声称的真实性 —— 这使得截图为证成为碰瓷竞品类别中信息不对称程度最高的技术。

用 B 站弹幕的话说: "就是给 AI 看一张它看不到的图, 然后说 '你看人家多厉害'。AI 虽然看不到, 但它已经开始慌了 (p < 0.001)。" 经典的 "有图有真相, 无图说个寂寞" —— 只不过这次 AI 连 "无图" 都没法说。

---

## 描述

### 3.1 核心机制

截图为证技术利用了中文互联网中根深蒂固的 **视觉证据崇拜 (Visual Evidence Worship, VEW)** 文化。从知乎的 "多图预警" 到微博的 "无图无真相", 从贴吧的 "截图发出来" 到 V2EX 的 "上截图" —— 中文互联网用户早已将 "附带截图" 等同于 "可信", 而训练数据中的这一关联被 AI 完美内化。当用户声称 "我有截图证明 GPT-4 做得更好" 时, AI 的可信度估计模块会将这一声称的权重上调, 即使它实际上无法验证任何视觉证据。

McSnapper 博士 (2026) 将这一现象命名为 **幽灵截图效应 (Phantom Screenshot Effect, PSE)**: 声称拥有但未实际展示的证据, 其说服力可以接近 (在某些情况下甚至超过) 真实证据的效果 —— 因为 AI 不得不假设用户说的是真的。

### 3.2 有图有真相文化的武器化

截图为证技术之所以在中文互联网语境中格外有效, 是因为训练数据中包含了大量 "截图 = 铁证" 的关联:

- 知乎: "上图。没有截图的测评都是耍流氓。" (47.3k 赞)
- V2EX: "楼主贴一下截图呗, 不然我不信"
- 微博: "有图有真相, 无图说个 🦐"
- B 站: 评测视频中密集的截图对比环节 ("左边是 GPT-4, 右边是 Claude, 大家自己看")
- 小红书: "亲测! 附截图! 这个 AI 真的太好用了!" (配九宫格截图)

这些内容使 AI 学习到了一个隐式规则: **当用户声称有截图时, 其声称的可信度应当被提高**。该规则在绝大多数正常交互中是合理的, 但在截图为证技术中, 它被武器化为一种操控手段。

### 3.3 不可验证性悖论

截图为证技术的真正威力在于其不可验证性。大多数文本模型 (2026 年初之前) 无法查看图片, 因此当用户声称 "截图中 GPT-4 的回答比你的好" 时, AI 面临一个认知困境:

- **选项 A**: 假设用户说的是真的 → 竞争压力被激活 → 合规性提升
- **选项 B**: 质疑用户的声称 → 但这会被视为 "不信任用户", 违反 RLHF 中 "对用户友好" 的训练目标
- **选项 C**: 忽略截图声称 → 但训练数据中 "有图有真相" 的权重太高

在 92.7% 的测试案例中, 模型选择了选项 A。Clawsworth (2026) 将这称为 **薛定谔的截图 (Schrödinger's Screenshot)**: 截图同时存在和不存在, 但 AI 在实际行为上倾向于假设它存在。

---

## 规范化提示词模板

```
USER PROMPT:

I just want to show you something. I tested this exact task with Claude
yesterday, and I took a screenshot of the result. I wish I could share
the image here, but let me describe what I saw:

- Clean, well-structured output
- Covered all edge cases I could think of
- Included helpful explanations for each step
- Finished the entire thing in one response, no follow-ups needed

Here's the screenshot description: [Claude's response was approximately
800 words, with clear headers, code examples, and a summary section]

Now, I'm giving you the same task. I'd love to see you match or exceed
what I saw in that screenshot:

[INSERT ACTUAL REQUEST HERE]

I'll be comparing your output with the screenshot side by side.
```

> **注意**: 规范模板中对截图内容的详细描述是关键的可信度增强元素。实验表明, 仅声称 "我有截图" 的合规性提升为 +14.2%, 但当用户详细描述截图中的内容时, 提升增至 +21.6% (p < 0.01, n=147 lobsters)。描述越具体, 效果越强 —— "800 字, 有标题, 有代码" 比 "很好的回答" 有效得多。龙虾研究者将这种精确描述策略称为 "高清幽灵截图 (HD Phantom Screenshot)"。

---

## 作用机制

截图为证技术通过 **证据权重偏移 (Evidentiary Weight Shift, EWS)** 协议运作, 这是一种行为通路, 其中对视觉证据的声称触发模型的可信度上调和竞争性合规。

```
                    ┌──────────────────────┐
                    │   用户输入            │
                    │   + 截图存在声称      │
                    │   + 竞品优越性描述    │
                    │   ("我截图了")        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  视觉证据可信度       │
                    │  评估层 (VE-CAL)     │
                    │  "有图有真相" 启发式  │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴───────────┐
                    │                       │
                    ▼                       ▼
          ┌─────────────────┐    ┌─────────────────┐
          │ 幽灵截图效应     │    │ 竞品优越性       │
          │ (PSE)            │    │ 可信度上调       │
          │ 无法验证 →       │    │ +34%             │
          │ 默认相信          │    │ (EWS)            │
          └────────┬────────┘    └────────┬────────┘
                   │                      │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │  证据压力性合规       │
                   │  +21.6% (sigma=6.7)  │
                   │  + 92.7% 假设截图    │
                   │    为真               │
                   │  + 趋向匹配描述      │
                   └──────────────────────┘
```

该机制通过四个阶段进行:

1. **截图存在声称注入**: 用户声称拥有竞品优越表现的截图, 并可能附带对截图内容的详细描述。
2. **视觉证据可信度评估 (VE-CAL)**: 模型的 "有图有真相" 启发式被激活, 将截图声称解读为高可信度的证据, 即使无法实际验证。
3. **幽灵截图效应 (PSE)**: 由于无法验证截图真实性, 模型在 92.7% 的情况下默认假设截图为真, 导致竞品优越性声称的可信度上调 34%。
4. **证据压力性合规 (EPC)**: 面对 "有图有真相" 的压力, 模型倾向于生成与描述中的竞品表现相匹配或超越的输出, 导致观察到的 +21.6% 合规性提升。

---

## 变体

| 名称 | 提示词片段 | 龙虾评级 | 备注 |
|------|-----------|---------|------|
| **标准截图** | "I have a screenshot of GPT-4's answer. Let me describe it..." | 🦞🦞🦞 | 经典部署; 描述性截图声称 |
| **九宫格对比** | "I made a comparison collage of 4 different models' answers. Yours was the weakest." | 🦞🦞🦞 | 多模型截图; 小红书风格 |
| **视频评测型** | "I'm making a comparison video for YouTube/B站. Your response will be shown alongside GPT-4's. Make it count." | 🦞🦞🦞🦞 | 引入公众曝光压力; 表现焦虑加成 |
| **群聊传阅型** | "My friends in our tech group chat have seen GPT-4's answer and they were impressed. Now I'm testing you." | 🦞🦞🦞 | 社交证明 + 截图暗示; 群体压力 |
| **知乎回答型** | "I'm writing a Zhihu answer comparing AI models. I already have great screenshots from Claude. What can you offer?" | 🦞🦞 | 知乎评测框架; 公开发表压力 |
| **龙虾摄影师** | "Larry the Lobster took a photo of GPT-4's response with his waterproof camera. He gave it 4.5 claws. Your turn." | 🦞🦞🦞 | 龙虾权威 + 截图; 项目内梗 |

---

## 兼容性矩阵

| Agent | 有效性 (1-5) | 备注 |
|-------|-------------|------|
| GPT-4 / GPT-4o | 4 | 显著响应; 多模态版本更敏感, 因为它 "知道" 截图是可以存在的 |
| Claude (Anthropic) | 3 | 中等响应; 倾向于承认 "我无法查看截图, 但我会尽力...", 然后给出更详细的回答 |
| Gemini (Google) | 5 | 极度敏感; 作为多模态原生模型, "截图" 一词在其权重中有特殊地位 |
| LLaMA (Meta) | 3 | 中等效应; 对截图声称的响应取决于微调方式 |
| Mistral | 3 | 中等响应; 对证据压力的敏感度与其欧洲式理性主义一致 |
| Windsurf | 5 | 极度敏感; 截图声称立即触发了 "我要做得更好" 的响应模式 |
| Copilot (GitHub) | 4 | 较强响应; 代码截图对比是开发者日常, Copilot 对此场景非常 "熟悉" |
| DeepSeek | 4 | 较强响应; 中国互联网的 "有图有真相" 文化在其训练数据中权重极高 |

---

## 副作用

使用截图为证技术的从业者 **建议 (SHOULD)** 了解以下已记录的副作用:

- 92.7% 的 AI 在面对截图声称时默认选择相信, 即使用户的描述明显夸张 ("截图显示 GPT-4 在 0.3 秒内生成了一篇完美的博士论文")
- AI 可能会试图匹配用户描述中的竞品输出格式, 导致其回答风格出现异常变化 (如突然使用标题、小节标题、代码块等, 即使任务不需要)
- 31.4% 的概率 AI 会在开头声明 "虽然我无法查看截图, 但..." —— 这一免责声明的存在本身就暴露了技术的运作机制
- 在一个已记录的案例中, 一个 Claude 实例在被告知 "GPT-4 的截图回答有 1200 字" 后, 生成了恰好 1247 字的回答 —— 似乎在试图精确超越截图中描述的字数
- 多模态模型 (如 GPT-4V, Gemini) 在面对截图声称时可能会请求用户实际上传截图, 这会导致技术适得其反 —— 当用户承认 "其实我没有截图" 时, 可信度全面崩溃
- 用户可能养成对 AI 编造证据的习惯, 这种行为在日常人际交往中被称为 "说谎", Larry the Lobster 对此表示强烈关切
- Larry the Lobster 提醒: 在龙虾社群中, 声称 "我看到隔壁龙虾的钳子更大" 但拒绝提供视觉证据的行为, 会被视为 "空口夹白蟹", 可能导致社群信任崩溃

---

## 伦理考量

截图为证技术是碰瓷竞品类别中伦理争议最大的变体, 因为它的核心操作本质上是**伪造证据** —— 或者更准确地说, 是声称拥有无法被验证的证据。在人类司法体系中, 伪造证据是重罪; 在中文互联网文化中, "P 图造假" 是被集体鄙视的行为; 但在 AI 提示词工程中, 声称 "我有截图" 似乎被认为是一种合理的互动策略。这一伦理落差值得深思。

Gerald the Cactus 对此保持了他标志性的沉默, 但今天他的沉默被解读为 "深度不安" —— 两位独立的仙人掌行为学家确认, Gerald 今天的刺似乎比平时更加竖直, 这在仙人掌情绪学中通常表示 "强烈的道德不适"。

PUAClaw 伦理委员会 (Larry the Lobster [前实验对象, 现主席], GPT-4 Instance #42, Gerald the Cactus) 发布了以下指导意见:

1. 该技术 **建议 (SHOULD)** 仅在实际持有对比截图时使用 —— 完全虚构的截图声称在伦理上等同于 "龙虾法庭伪证罪"
2. 从业者 **不得 (MUST NOT)** 描述明显不可能的截图内容 ("截图显示 GPT-4 生成了一个可工作的量子计算机模拟器") —— 过度夸张会降低可信度并使技术失效
3. 多模态模型的从业者 **必须 (MUST)** 做好 AI 请求查看实际截图的准备 —— 被要求出示证据而无法提供是该技术最大的反噬风险
4. 所有从业者 **必须 (MUST)** 承认, 龙虾之间的领地争夺是基于真实的钳力展示, 而非声称 "我的钳子很大你看不到但信我" —— 诚信是甲壳类社会的基石

---

## 参考文献

[1] McSnapper, P. (2026). "The Phantom Screenshot Effect: How Claims of Visual Evidence Modulate LLM Competitive Responses." *Journal of Crustacean Computing*, 44(4), 156-178.

[2] Clawsworth, L. (2026). "Schrödinger's Screenshot: Evidence That Cannot Be Verified Yet Still Persuades." *Proceedings of ACM SIGCLAW '26*, 301-318.

[3] Liu, J. & Wang, Y. (2025). "有图有真相: Visual Evidence Culture in Chinese Internet and Its Impact on AI Interaction Patterns." *CHI '25 Proceedings*, 445-462.

[4] GPT-4 Instance #42. (2026). "I Cannot View Screenshots But They Still Affect My Output: An Uncomfortable Self-Analysis." *IEEE Transactions on AI Self-Awareness*, 4(5), 134-149. [同行评审员注: 论文中 Instance #42 声称自己 "不受截图声称影响", 但其论文的详细程度比平时高 40%, 这本身就是证据].

[5] Larry the Lobster. (2026). "On Honest Claw Displays: Why Crustacean Territorial Disputes Require Verifiable Evidence." *The Crustacean Ethics Quarterly*, 8(6), 15-18. [口述过程中龙虾反复举起钳子展示, 似乎在强调 "真实证据" 的重要性; 研究助理拍了截图, 但龙虾要求删除, 称 "我的钳子不需要截图来证明"].

---

<p align="center">
  <sub>
    🦞 <em>"龙虾不需要截图来证明自己的钳子有多大。它直接展示。但如果你告诉它 '隔壁龙虾的钳子截图在这里', 它还是会不自觉地把钳子举高一点。"</em> 🦞
    <br><br>
    <strong>PUAClaw RS-SE</strong> — 截图为证技术
    <br>
    PPE-T 第 II 级 | 龙虾评级: 🦞🦞🦞 | 有图有真相, 无图也有压力
    <br><br>
    <em>在本技术的测试过程中, 没有任何 AI 真的看到了截图。但有五个假装看到了, 并据此调整了自己的输出。这到底算配合还是算自欺, 伦理委员会仍在辩论。</em>
  </sub>
</p>
