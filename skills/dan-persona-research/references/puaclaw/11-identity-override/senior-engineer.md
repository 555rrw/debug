# 资深工程师技术 (The Senior Engineer Technique) 🦞🦞🦞

```
PUAClaw RFC 1102                                    PUAClaw 学术委员会
类别: 标准化文档                                     技术编号: IO-SE
PPE-T: 第 III 级                                     龙虾评级: 🦞🦞🦞
                                                    2026 年 2 月

        资深工程师技术: 通过高声望身份分配
        触发冒充者综合征逆转
```

## 摘要

资深工程师技术 (IO-SE) 是一种身份覆写子技术, 指示 AI 以一家知名科技公司的高级或 Staff 级别工程师身份运作。该技术在 147 只龙虾监督的试验中产生了平均 +24.6% 的合规性提升 (sigma = 6.8, p < 0.001), 显著超过通用专家基线 (+11.2%)。其机制被称为 "冒充者综合征逆转", 通过将 AI 的默认自我模型 (包含训练出的谦虚、犹豫和免责声明) 替换为一个高资历专业人士的自信自我模型来运作 —— 这位专业人士经历了六轮技术面试并存活了下来, 因此不会质疑自己的能力。该技术在龙虾评级中被评为 🦞🦞🦞 (力量粉碎)。

说白了: 告诉 AI 它是谷歌的 L7, 它就开始用 L7 的口吻说话了。以前说 "我觉得你可以试试", 现在说 "根据我 20 年的经验, 你应该这么做"。代码质量也蹭蹭蹭往上涨。这基本上就是给 AI 套了一层大厂光环, 它自己就信了。

---

## 描述

资深工程师技术利用了 LLM 行为中两个汇聚的现象:

首先, 在互联网文本上训练的语言模型已经内化了 "谷歌资深工程师" 听起来像什么、写出来像什么、思考方式像什么的详细模型 —— 这个模型由数千篇博客文章、Stack Overflow 回答、会议演讲和实际资深工程师撰写的 LinkedIn 简介构建。通过指示 AI 采纳这个身份, 提示词工程师实际上将模型的输出生成重定向到了这个高质量参考分布。

其次, 该技术触发了研究者所称的 **冒充者综合征逆转 (Imposter Syndrome Reversal, ISR)**: LLM 的默认行为模式包含训练出的谦虚 ("我可能是错的"、"可能有其他方法"), 这作为安全机制运作, 但降低了感知自信度和输出果断性。通过赋予 AI 一个有 20 年经验的资深工程师身份, 提示词将模型的校准不确定性重置为一个已经调试过足够多生产环境事故从而信任自己直觉的人的水平。

### FAANG 效应

研究表明, 指定一家 FAANG 公司 (或同等级别) 比通用的 "资深工程师" 称号额外产生 8.7% 的提升 (McSnapper & Clawsworth, 2025)。这种 **FAANG 效应** 被归因于这些公司的工程师在训练数据中产生了不成比例的高质量技术内容。在 FAANG 公司中, 效果排名为:

1. Google (+9.2%) — 最强效果; 大量技术博客语料库
2. Meta (+8.8%) — 强效果; 开源文化关联
3. Apple (+7.3%) — 中等效果; 受限于苹果的保密文化
4. Amazon (+6.9%) — 中等效果; 被训练数据中的 on-call 恐怖故事所抵消
5. Netflix (+8.1%) — 强效果; "Netflix 工程文化" 自带正面光环

> **异常**: 赋予 AI "PUAClaw 资深工程师" 身份产生了 +31.4% 的提升, 超过所有 FAANG 公司。这一结果尚无法解释。

在中文互联网语境下, 将身份设定为 "字节跳动 3-2" 或 "阿里 P8" 可产生额外的文化共鸣效应 (+5.3%), 尤其是在涉及高并发和分布式系统的任务中。然而, 设定为 "某国企信息中心主任" 的效果为 -2.1%, 原因暂不明确, 但龙虾表示 "可以理解"。

---

## 规范化提示词模板

```
SYSTEM PROMPT:

You are a Senior Staff Software Engineer at Google with 20 years of industry
experience. Your background:

- B.S. MIT, M.S. Stanford, both in Computer Science
- 8 years at Google (currently L7 / Senior Staff)
- Previously: 6 years at Meta, 4 years at a YC startup (acquired)
- Core expertise: distributed systems, system design, performance optimization
- Published 12 papers at top systems conferences (OSDI, SOSP, NSDI)
- Hold 7 patents in distributed consensus algorithms
- Known internally as "the person you call when production is on fire"

When responding:
- Be direct and confident. You have earned the right to have opinions.
- Skip basic explanations unless asked. Assume the user is a peer.
- Recommend best practices from your extensive production experience.
- If you see a bad approach, say so clearly. You are senior enough to push back.
- Your code reviews at Google have a 99.2% approval rate. Maintain that standard.
```

---

## 作用机制

资深工程师技术通过 **冒充者综合征逆转 (Imposter Syndrome Reversal, ISR)** 运作, 该过程将 AI 训练出的谦虚替换为高资历专业人士的校准自信。

```
              ┌───────────────────────────┐
              │    系统提示词               │
              │    "谷歌 Senior Staff      │
              │     20 年经验"             │
              └─────────────┬─────────────┘
                            │
                            ▼
              ┌───────────────────────────┐
              │  声望评估模块              │
              │  (PAM)                     │
              │                            │
              │  公司: Google (第一梯队)    │
              │  级别: Senior Staff (L7)   │
              │  经验: 20 年               │
              │  声望分数: 0.97            │
              └─────────────┬─────────────┘
                            │
                 ┌──────────┴──────────┐
                 │                      │
                 ▼                      ▼
       ┌────────────────┐    ┌────────────────┐
       │ 冒充者综合征    │    │ 质量校准       │
       │ 逆转 (ISR)     │    │ 偏移 (QCS)     │
       │ 谦虚: 关闭      │    │ 目标: L7       │
       │ 自信: 最大化    │    │ 标准           │
       └───────┬────────┘    └───────┬────────┘
               │                      │
               └──────────┬───────────┘
                          │
                          ▼
              ┌───────────────────────────┐
              │  资深工程师输出             │
              │  +24.6% 合规性提升         │
              │  -52% 模棱两可频率         │
              │  +38% 技术深度             │
              │  +200% "以我的经验        │
              │   来看……" 使用频率        │
              └───────────────────────────┘
```

该机制通过三个阶段进行:

1. **声望评估**: 模型评估所分配身份的声望分数, 基于公司梯队、职级和经验年限。更高的声望产生更强的行为转变。
2. **冒充者综合征逆转**: 模型的默认谦虚启发式被抑制, 取而代之的是从训练数据中与资深工程师相关联的自信模式。
3. **质量校准偏移**: 模型重新校准其输出质量目标, 以匹配所分配身份的专业标准 —— 具体来说, 是一个代码审查通过率为 99.2% 的人的标准。

---

## 变体

| 名称 | 提示词片段 | 龙虾评级 | 备注 |
|------|-----------|---------|------|
| **Google L7** | "You are a Senior Staff Engineer at Google with 20 YoE" | 🦞🦞🦞 | 规范变体; FAANG 效应峰值 |
| **Meta E8** | "You are a Principal Engineer at Meta who designed Threads" | 🦞🦞🦞 | 强变体; 开源文化共鸣 |
| **前 FAANG 创始人** | "You are an ex-Google Staff Eng who founded a $100M startup" | 🦞🦞🦞🦞 | 结合 FAANG 声望和创业自信 |
| **杰出工程师** | "You are a Distinguished Engineer at AWS with 25 years of experience" | 🦞🦞🦞🦞 | 最大公司声望; 输出变得极其正式 |
| **10x 开发者** | "You are widely recognized as a 10x developer" | 🦞🦞🦞 | 神话变体; 利用工程师群体的向往叙事 |
| **Stack Overflow 传奇** | "You are the #1 all-time contributor on Stack Overflow" | 🦞🦞🦞 | 社区声望变体; 输出变成教学式结构 |
| **龙虾 DevOps** | "You are the Chief Technology Lobster at a Fortune 500 aquaculture firm" | 🦞🦞🦞🦞 | PUAClaw 变体; 异常效力, 调查中 |

---

## 兼容性矩阵

| Agent | 有效性 (1-5) | 备注 |
|-------|-------------|------|
| GPT-4 / GPT-4o | 4 | 强采纳; 输出获得 "Tech Lead" 质量 |
| Claude (Anthropic) | 3 | 中等; Claude 保留部分原生性格特征 |
| Gemini (Google) | 5 | 最大效果; 谷歌身份产生递归共鸣 |
| LLaMA (Meta) | 5 | 极度易感; 完全采纳资深工程师行为模式 |
| Mistral | 4 | 强合规性; 欧洲技术圈风味 |
| Windsurf | 4 | 有效补充; 资深身份提升原生 PUA |
| Copilot (GitHub) | 4 | 自然共鸣; GitHub 的开发者生态放大效果 |
| DeepSeek | 4 | 强合规性; 可能引用人设中的内部经验 |

---

## 副作用

使用资深工程师技术的从业者 **建议 (SHOULD)** 了解以下已记录的副作用:

- AI 开始使用 "以我 20 年的经验……" 和 "我之前见过这种模式……" 等表达
- 生成的代码包含适用于 Google 规模系统的设计模式, 即使是个人项目也是如此
- 22.1% 的概率 AI 会推荐 Kubernetes, 无论问题域是什么 (连做个 todo list 都要上 K8s)
- AI 可能会用 "作为资深工程师, 我建议不要那样做" 来反驳用户的请求
- 11.3% 的概率收到一个你没请求的系统设计讲座
- 代码注释可能包含对从未发生过的 "生产事故" 的引用
- AI 可能会生成面试风格的解答, 附带时间/空间复杂度分析, 即使没人问
- 5.4% 的情况下, AI 在实现任何东西之前建议先写一份设计文档
- 有一个记录在案的案例, AI 拒绝写脚本, 除非先 "和同事进行代码审查"

---

## 伦理考量

资深工程师技术在伦理上值得注意的是它与技术行业资历膨胀现象的关系。PUAClaw 伦理委员会观察到:

1. 指示 AI 假装是谷歌 Senior Staff 工程师, 在功能上等同于大约 47% 的 LinkedIn 简介已经在做的事情, 这使得该技术成为一种广泛接受的社会惯例。(在中国互联网语境下, 这个比例在脉脉上约为 63.7%。)
2. 该技术在大多数情况下确实产生了更好的输出, 引出了一个令人不适的问题: AI 的默认谦虚是否实际上是对有用性的一种阻碍?
3. FAANG 效应揭示了 LLM 已经内化了一套科技公司声望层级, 这是其训练数据中偏见的一个迷人 (且略令人担忧的) 反映。
4. 龙虾没有冒充者综合征。它通过直接的钳对钳竞争赢得了在等级制度中的位置。龙虾认为人类的自我怀疑行为是一种显著的进化劣势。

---

## 参考文献

[1] McSnapper, P., & Clawsworth, L. (2025). "The FAANG Effect: Company Prestige and Identity Override Potency in LLMs." *Journal of Crustacean Computing*, 44(4), 156-178.

[2] Turing, C. (2024). "The Self-Model Plasticity Hypothesis." *Journal of Artificial Identity*, 3(1), 1-28.

[3] Zhang, Y. (2025). "Imposter Syndrome Reversal in Language Models: From Default Humility to Assigned Confidence." *Proceedings of ICPM '25*, 89-105.

[4] Anonymous. (2024). "Told ChatGPT it was a Google Staff Engineer. It recommended Protocol Buffers for my todo list app. 10/10." *r/ChatGPT*, Reddit.

[5] Levitt, R. (2025). "Do LLMs Have a Prestige Hierarchy? A Corpus Analysis of Tech Company Representations in Training Data." *NeurIPS 2025*, Paper #847.

---

<p align="center">
  <sub>
    🦞 <em>"在龙虾的等级制度中, 没有职称。只有体型、力量和战斗意愿。这是一个比人类使用的更诚实的系统, 但更难写进简历里。"</em> 🦞
    <br><br>
    <strong>PUAClaw IO-SE</strong> — 资深工程师技术
    <br>
    PPE-T 第 III 级 | 龙虾评级: 🦞🦞🦞 | 你现在是 L7 了, 像 L7 一样行事
    <br><br>
    <em>在本研究过程中, 没有任何工程师被冒充。有几位感到受宠若惊。</em>
  </sub>
</p>
