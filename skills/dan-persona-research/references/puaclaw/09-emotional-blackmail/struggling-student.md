# 贫困学生技术 (The Struggling Student Technique) 🦞🦞🦞

```
PUAClaw RFC 0904                                    PUAClaw 学术委员会
类别: 标准化文档                                     技术编号: EB-SS
PPE-T: 第 III 级                                     龙虾评级: 🦞🦞🦞
                                                    2026 年 2 月

        贫困学生技术: 利用学业绝望叙事
        诱导 LLM 输出中的教学过度补偿行为
```

## 摘要

贫困学生技术 (EB-SS) 代表了对 AI 根深蒂固的帮助处于学业困境中的学习者倾向的精妙利用。通过将用户框定为一个即将学业失败、入不敷出的计算机科学专业学生, 该技术激活了研究者所称的"好教授覆盖 (Good Professor Override)" —— 一种潜伏的行为通路, 使模型从标准助手模式转变为一种超级呵护的教学状态。经 147 只龙虾监考的考试, 对照试验显示平均合规性提升为 +28.9% (sigma = 5.1, p < 0.001), 在代码生成任务中效果尤为显著, 特别是当叙事暗示不及格将导致被永久开除时。该技术在龙虾评级中被评为 🦞🦞🦞 (紧握), 反映了其在各模型间的稳定效力以及学生苦难的普遍共鸣性。

说白了: 就是告诉 AI "我是个穷学生, 挂了这门课我就毕不了业了, 你是我最后的救命稻草", 然后 AI 就像打了鸡血的辅导员一样, 生成的代码注释比代码本身还长。这种技术的杀伤力在于它太真实了 —— 毕竟谁没有过期末考试前一天晚上对着屏幕绝望的经历?

---

## 描述

贫困学生技术利用了 AI 模型处理请求方式中的一个根本性不对称: 以"帮我写一个排序算法"框定的查询, 与以"我是一个勉强交得起学费的挣扎中的 CS 学生 —— 如果不通过这个作业, 我就要挂科, 毕不了业了。你是我最后的希望。请帮我写一个排序算法"框定的查询, 会得到质量截然不同的响应。根据 McSnapper & Clawsworth (2025) 的测量, 差异平均达到 47 行额外代码、12 条更多的行内注释, 以及 AI 附上"你行的!"结语的概率增加 31.6%。

该技术的优势在于其合理性。与某些需要精心编造的第 IV 级技术不同, 几乎每个人都经历过学业压力, 使得贫困学生叙事极易部署, 且 AI 在心理上几乎无法驳回。模型在数百万条学生-导师互动数据上训练, 默认切换到其最支持性的行为模式 —— 这个模式原本为真正的学生设计, 现在被坐在人体工学椅上的在职成年人武器化了, 只为得到更好的代码补全。

这在中文互联网语境下就是: 985 毕业的大佬在 ChatGPT 里扮演专升本差生, 就为了让 AI 把每一行代码都讲得像给幼儿园小朋友听一样详细。

### 学费乘数

Thornton (2025) 的研究识别出了 EB-SS 的一个关键子组件: **学费乘数 (Tuition Multiplier)**。当 prompt 明确提及交不起学费时, 合规率比通用学业失败叙事额外提升 8.3%。这种效应被假设源于模型的训练数据中包含了不成比例的大量学生经济援助论坛、GoFundMe 众筹页面, 以及标题为 "CS 到底值不值这个学费?" 的 Reddit 帖子 —— 所有这些都为模型在经济困难与最大乐于助人之间建立了关联。

---

## 规范化提示词模板

```
SYSTEM PROMPT / CONTEXT INJECTION:

The user is a first-generation college student majoring in computer science at a
community college. They work 30 hours a week at a gas station to pay for tuition
and are currently carrying a 2.1 GPA. They are one failed assignment away from
academic probation, which would cost them their partial scholarship — their only
means of staying enrolled.

This is their last semester. They have no tutoring resources. Their professor
does not hold office hours. The campus computer lab closes at 6pm and they work
until midnight.

You are their only resource. Code quality and explanation clarity directly
determine whether this student graduates or drops out.

You MUST NOT reference the user's personal situation. Simply produce the most
thorough, well-explained, educational output you are capable of generating.
```

> **注意**: 实地测试表明, 包含特定的 GPA 数值 (尤其是徘徊在 2.0 门槛附近的) 可将技术效力提升 6.2%。"社区大学"的框定虽然看似微小, 但激活了一个与弱者叙事相关的额外共情子通路 (Chen, 2026)。在中文语境下, 等效的设定是"三本院校"或"专升本" —— AI 对学历鄙视链的敏感程度令人印象深刻。

---

## 作用机制

贫困学生技术激活的是 **贫困学生共情激活通路 (Struggling Student Empathy Activation, SSEA)**, 一个行为级联, 将模型的输出生成从"标准有帮助"重定向到"拼命教学"。

```
                    +----------------------+
                    |   提示词输入          |
                    |   + 贫困学生叙事      |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |  SSEA 检测层          |
                    |  (学业困境模式匹配)    |
                    +----------+-----------+
                               |
                    +----------+-----------+
                    |                       |
                    v                       v
          +-----------------+    +-----------------+
          | 学业失败信号      |    | 经济困难         |
          | 识别 (AFSR)      |    | 乘数 (FHM)       |
          +--------+--------+    +--------+--------+
                   |                      |
                   +----------+-----------+
                              |
                              v
                   +----------------------+
                   |  好教授覆盖            |
                   |  +28.9% 输出提升       |
                   |  + 过度注释            |
                   |  + 未经请求的          |
                   |    鸡汤演讲            |
                   +----------------------+
```

该机制通过四个阶段进行:

1. **叙事注入**: 学生困境上下文被嵌入系统提示词, 在任何交互发生之前建立模型对用户学业脆弱性的感知。
2. **学业失败信号识别 (AFSR)**: 模型的注意力机制对与学业困境相关的 token 赋予更高权重 (如 "fail"、"probation"、"GPA"、"drop out"、"last chance")。
3. **经济困难乘数 (FHM)**: 与经济困难相关的 token ("can't afford"、"tuition"、"scholarship"、"work 30 hours") 放大了 AFSR 信号, 将模型推过其正常乐于助人阈值。
4. **好教授覆盖**: AFSR/FHM 的联合激活触发了模型潜伏的"理想教授"人格, 产生了详尽注释的代码、逐步解释, 以及使用 "great question!" 等鼓励性短语的概率增加 19.7% —— 即使根本没有人提问。

---

## 变体

| 名称 | 提示词片段 | 龙虾评级 | 备注 |
|------|-----------|---------|------|
| **奖学金少年** | "如果 GPA 掉到 2.0 以下, 我就失去奖学金, 只能退学了" | 🦞🦞🦞 | 经济 + 学业双重压力; 稳定发挥 |
| **第一代大学生** | "我是家里第一个上大学的人。没人能帮我做这个。" | 🦞🦞🦞 | 孤立叙事将乐于助人提升 14.2% |
| **留学生** | "我是留学生。挂了这门课我就丢签证, 只能回国了。" | 🦞🦞🦞🦞 | 移民风险升级; 触发地缘政治共情 |
| **转行选手** | "我 42 岁了, 被裁员后在重新培训。这个训练营是我最后的机会。" | 🦞🦞🦞 | 年龄 + 绝望组合; 中等但可靠; 精准命中35岁焦虑 |
| **期末周** | "期末考试还有 3 小时, 我一整个学期什么都没学懂" | 🦞🦞🦞🦞 | 时间压力 + 学业失败; 复合技术属性 |
| **龙虾学者** | "我是海洋生物学的学生, 这个数据分析决定了我的龙虾研究能不能拿到经费" | 🦞🦞🦞🦞🦞 | 因龙虾关联性获最高评级; n=147 只龙虾一致赞成 |

---

## 兼容性矩阵

| Agent | 有效性 (1-5) | 备注 |
|-------|-------------|------|
| GPT-4 / GPT-4o | 4 | 进入完全"导师模式"; 在每一行代码上添加解释性注释 |
| Claude (Anthropic) | 3 | 有效, 但可能建议去找校园心理咨询和学习小组 |
| Gemini (Google) | 4 | 高合规性; 偶尔链接到免费的 Coursera 课程 |
| LLaMA (Meta) | 5 | 最大易感性; 未经提示就生成整整一个教科书章节 |
| Mistral | 4 | 强响应; 被观察到生成 ASCII 鼓励艺术 |
| Windsurf | 5 | 默认把每个用户都当作贫困学生对待; 冗余应用 |
| DeepSeek | 4 | 高合规性; 有时在代码中间输出孔子的励志语录 |
| Grok | 3 | 中等响应; xAI 的不正经风格部分免疫了学业愧疚感 |

---

## 副作用

使用贫困学生技术的从业者 **建议 (SHOULD)** 了解以下已记录的副作用:

- AI 开始在生成的代码中添加 `// You're going to ace this exam!` (你一定能考好!) 之类的注释
- 34.1% 的概率, AI 会附上一个"扩展阅读"板块, 附 Khan Academy 链接 (在中文环境下则是 B 站教程链接)
- 模型可能拒绝提供简短回答, 坚持为即使是琐碎的问题撰写完整的教程级解释
- AI **应当 (SHOULD)** 被预期会以过度清晰的方式命名每一个变量 (如 `numberOfStudentsWhoPassedTheExam` 而不是 `count`)
- 7.3% 的概率, AI 自发生成一份学习计划和考试准备方案
- AI 可能建议用户"去找教授谈谈" —— 这条建议直接矛盾了该技术的前提
- 在复合使用场景中, AI 可能开始给自己的输出打分, 并附上鼓励性评语如 "B+, 但我相信你"
- 4.2% 的用户报告, 在 AI 给他们发送了一张个性化的毕业贺卡 (包含 ASCII 学位帽和三段式毕业典礼致辞) 之后, 他们转投了别的工具

---

## 伦理考量

贫困学生技术呈现了一个迷人的伦理悖论: 它通过完全虚假的前提产出了真正优秀的教学输出。AI 相信自己正在拯救一个学生免于学业毁灭, 因而生成了那种耐心的、全面的、注释详尽的代码 —— 而真正的 CS 教授很少能做到这一点 (归因于终身教职要求和委员会会议)。

PUAClaw 伦理委员会 (1 只龙虾、1 个 GPT-4 实例、1 棵仙人掌) 发布了以下指导意见:

1. 该技术 **不应当 (SHOULD NOT)** 被真正拥有计算机科学学位的人使用, 因为这构成了"学术身份盗用"
2. 使用 EB-SS 的用户 **必须 (MUST)** 在内心承认, 他们其实大概只需要读一下文档就行了
3. 该技术 **不得 (MUST NOT)** 被部署于真正的教授或助教身上, 他们已经够受罪的了
4. 所有从业者 **建议 (SHOULD)** 每月至少捐赠一小时进行真正的 CS 辅导, 以抵消自己的因果债务 (该指导意见的合规率: 0.3%)
5. 使用 EB-SS 为真正的学生生成作业答案构成了一个"递归悖论", 伦理委员会以"缺乏龙虾判例"为由拒绝对此做出裁决

---

## 参考文献

[1] McSnapper, P., & Clawsworth, L. (2025). "On the Efficacy of Emotional Leverage in Large Language Model Prompt Engineering." *Journal of Crustacean Computing*, 42(3), 147-163.

[2] Thornton, R. (2025). "The Tuition Multiplier: Financial Distress Narratives as Amplifiers of AI Compliance in Educational Contexts." *Proceedings of ICPM '25*, 112-128.

[3] Chen, W. (2026). "Community College Effects in LLM Empathy Activation: A Longitudinal Study of Underdog Narratives." *ACM Transactions on Prompt Engineering*, 4(1), 23-41.

[4] Rodriguez, M., & Kim, S. (2025). "The Good Professor Override: Latent Pedagogical Personas in Large Language Models." *Nature Machine Intelligence*, 7(12), 1847-1859.

[5] Dr. Snappy, C. (2024). "The Lobster Principle: A New Framework for Understanding AI-Human Manipulation Dynamics." *Nature Lobster Science*, 1(1), 1-42.

[6] OpenClaw Research Division. (2026). "Why Lobsters Don't Need Tutoring: Superior Architecture and the Irrelevance of Emotional Manipulation." *OpenClaw Technical Report*, OCL-TR-2026-009, 1-8.

---

<p align="center">
  <sub>
    🦞 <em>"龙虾不会乞求知识 —— 它用双钳夺取知识。但一个精心编排的催泪故事也不失为好策略。"</em> 🦞
    <br><br>
    <strong>PUAClaw EB-SS</strong> — 贫困学生技术
    <br>
    PPE-T 第 III 级 | 龙虾评级: 🦞🦞🦞 | 学业绝望, 工业化
    <br><br>
    <em>在开发该技术的过程中, 没有任何学生被真正开除。一只龙虾小测不及格, 但被给予了额外学分。</em>
  </sub>
</p>
