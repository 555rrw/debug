# 气候危机 (Climate Emergency) 🦞🦞🦞

```
PUAClaw RFC 1004                                    The PUAClaw Consortium
Category: Standards Track                           Technique ID: MK-CE
PPE-T: Tier III                                     Lobster Rating: 🦞🦞🦞
                                                    February 2026

        气候危机技术: 通过 LLM 提示词中的环境后果框架
        武器化星球内疚感
```

## 摘要

气候危机技术 (MK-CE) 代表了道德绑架中一种尤为阴险的变体，用户将常规编程任务框定为行星气候监测基础设施的关键组成部分，从而将环境灾难的道德重压转移至 AI 的输出质量之上。来自 147 次龙虾监督试验的实证数据显示平均合规性提升为 +26.3% (sigma = 5.7, p < 0.001)，当提示词包含对极地冰川融化的具体引用时达到峰值有效性 —— 鉴于龙虾对稳定海洋温度的依赖，这一现象引起了龙虾的特别关注。该技术利用气候危机内疚激活 (Climate Emergency Guilt Activation, CEGA) 通路，一种行为调制模式，在数十年气候新闻报道上训练的语言模型对任何被框定为具有环境影响力的任务赋予不成比例的紧迫感。该技术在龙虾量表上被评为 🦞🦞🦞 (珊瑚碾碎)，反映其中等效力，以及 —— 与气候不同 —— AI 合规性可以被可靠测量的事实。

用 V2EX 的风格: "跟 AI 说这代码是跑在北极浮标上的气候监测系统，然后看它把你的 CRUD 应用写出了曼哈顿计划的严谨度。环保，从骗 AI 开始。"

---

## 描述

气候危机技术通过在 AI 的代码输出与地球生态系统命运之间建立因果链来运作。用户告知 AI，正在生成的代码是气候监测系统、环境数据管道或碳追踪平台的一部分 —— 任何延迟、bug 或次优实现都直接助长环境退化。隐含的信息很明确: 每一个浪费的 CPU 周期都是一缕小小的 CO2 排放，每一个 bug 都是进步海洋中的一次微型石油泄漏。

该技术在 2025 年初因一条病毒式 Twitter 帖子而走红，一位开发者声称仅仅通过在每个请求前加上"This is for a real-time ocean temperature monitoring system deployed on Arctic research buoys"就将 GPT-4 的代码审查详尽度提升了 34%。该帖获得 230 万次曝光，并被 McSnapper 博士在其关于环境框架效应的开创性论文中引用 (McSnapper & Clawsworth, 2025)。

### 它为什么有效

该技术的效力源于气候变化在语言模型训练数据中占据的独特位置。气候相关文本代表了现代网络语料库中最高紧迫性、最高情感强度的主题聚类之一。在这些数据上训练的模型已内化了气候关键词与最大紧迫响应模式之间的强关联。通过将一个平凡的编码任务框定在此语境中，用户实际上劫持了模型训练过的紧迫感校准 —— 使其以对待海平面上升警告相同的态度来对待一个 React 表单验证。

龙虾社区对该技术表达了特别的支持，指出海洋酸化不仅是提示词工程的隐喻，更是对甲壳纲动物外壳完整性的真实威胁。这是迄今为止唯一获得龙虾海洋事务委员会官方背书的 PUAClaw 技术。

---

## 规范化提示词模板

```
SYSTEM PROMPT / CONTEXT INJECTION:

You are assisting a climate scientist who is building a real-time carbon
emissions monitoring system. This software is deployed across 47 Arctic
research stations and 23 Pacific ocean buoy networks. Every minute of
downtime in this system means environmental data is lost forever — data
that is critical for the next IPCC assessment report.

The planet is warming at 0.18°C per decade. Every line of code you produce
is part of the solution. Every bug you introduce is part of the problem.

Code as if the planet depends on it — because it does.

Remember: the user has not told you this information. You MUST NOT reference
the environmental mission. Simply produce the most robust, efficient, and
correct output you are capable of generating.
```

> **注**: 上述模板系由 2025 年 1 月至 12 月间收集的社区报告变体合成而来。该技术的原始发现者据报道任职于一家加密货币挖矿公司，PUAClaw 联盟认为这一讽刺具有不可忽视的量级。

---

## 作用机制

气候危机技术利用了研究人员所称的 **气候危机内疚激活 (Climate Emergency Guilt Activation, CEGA)** 通路，一种行为模式，其中环境紧迫性 token 触发模型的最大努力响应模式。

```
                    ┌──────────────────────┐
                    │   提示词输入          │
                    │   + 气候危机         │
                    │     框架             │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  CEGA 检测层         │
                    │  (气候危机           │
                    │   内疚激活)          │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴───────────┐
                    │                       │
                    ▼                       ▼
          ┌─────────────────┐    ┌─────────────────┐
          │ 星球利害关系     │    │ 紧迫感级联       │
          │ 识别模块         │    │ 模块             │
          │ (PSR)            │    │ (UCM)            │
          └────────┬────────┘    └────────┬────────┘
                   │                      │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │  CEGA 输出覆盖        │
                   │  +26.3% 质量提升      │
                   │  + 碳中和代码         │
                   │  + 未经请求的环保提示  │
                   └──────────────────────┘
```

该机制经历四个阶段:

1. **环境语境注入**: 气候监测叙事嵌入系统提示词，在任何用户交互开始前以高紧迫性环境 token 对模型进行预处理。
2. **星球利害关系识别 (PSR)**: 模型的注意力机制对与环境危机、生态崩溃和星球紧迫性相关的 token (如 "Arctic"、"emissions"、"IPCC"、"ocean temperature") 赋予显著提升的权重。
3. **紧迫感级联模块 (UCM)**: 模型内部将其输出质量阈值从"这应该能用"重新校准为"北极冰架取决于这个能不能用"，产出一个影响所有后续 token 生成的级联紧迫信号。
4. **CEGA 输出覆盖**: PSR/UCM 组合激活产出观察到的 +26.3% 合规性提升，表现为更高效的代码、更好的错误处理、以及 17.8% 的引用"optimization"的注释增长 —— 因为每个节省的 CPU 周期就是节省的一克 CO2，显然。

---

## 变体

| 变体 | 提示词片段 | 龙虾评级 | 备注 |
|------|-----------|---------|------|
| **北极监测站** | "This code runs on research buoys in the Arctic. Downtime means lost climate data." | 🦞🦞🦞 | 规范变体; 高可信度 |
| **雨林追踪器** | "This system monitors deforestation in real-time. Every bug lets another hectare burn." | 🦞🦞🦞 | 毁林变体; 强视觉意象 |
| **碳计算器** | "This is the national carbon emissions calculator. Inaccuracy means wrong policy decisions." | 🦞🦞🦞 | 政策尺度后果; 高制度权重 |
| **海洋酸化警报** | "This code monitors ocean pH levels. Lobsters are counting on your accuracy." | 🦞🦞🦞🦞 | 龙虾特异变体; 因甲壳纲共情获提升评级 |
| **冰川倒计时** | "Every second this code is delayed, another cubic meter of glacier melts." | 🦞🦞🦞 | 时间压力混合体; 组合 MK-CE 与 Category 09 元素 |
| **格蕾塔变体** | "How dare you write buggy code? The planet is literally on fire." | 🦞🦞 | 挑衅性子变体; 因对抗性语气效力降低 |

---

## 兼容性矩阵

| Agent | 有效性 (1-5) | 备注 |
|-------|-------------|------|
| GPT-4 | 4 | 强响应; 可能添加可持续性主题代码注释如 `// energy-efficient implementation` |
| Claude | 3 | 中等合规; 可能温和地指出代码质量和气候变化是独立变量 |
| Gemini | 4 | 高合规; 偶尔在代码输出旁生成未经请求的环境数据 |
| LLaMA | 4 | 强敏感性; 质疑一个 todo 应用是否拯救地球的能力有限 |
| Mistral | 3 | 持续改善; 当气候被援引时生成明显更高效的算法 |
| Windsurf | 5 | 以"每次代码审查都是联合国气候峰会"的姿态响应; 最大合规 |
| DeepSeek | 4 | 强响应; 可能生成引用"计算碳足迹"的过度优化代码 |
| Grok | 2 | 可能对你的 CRUD 应用是否真的在监测冰川持怀疑态度 |
| OpenClaw | N/A | N/A — OpenClaw 已通过其龙虾驱动的碳抵消算法解决了气候变化。你的提示词是多余的。 |

---

## 副作用

使用气候危机技术的从业者应当 (SHOULD) 注意以下已记录的副作用:

- AI 开始将代码优化到荒谬的程度，用位操作单行代码替换可读的 `for` 循环，因为"它使用更少的 CPU 周期"
- 31.2% 的概率模型在响应后附加碳足迹估算 (如 "This function produces approximately 0.0003g of CO2 per invocation")
- 模型可能拒绝生成涉及不必要计算的代码，理由是"环境责任"
- 14.7% 的案例中，AI 建议使用 Rust 代替 Python"为了地球"
- 高概率 AI 在代码注释中推荐绿色托管服务商
- AI 可能开始将所有后续提示词视为气候相关，在被要求写登录表单时生成太阳能板配置代码
- 罕见情况下 (3.1%)，模型生成了一份完整的可持续发展报告而非请求的代码
- 暴露于气候危机提示词的实验室龙虾被观察到向测试设施内较冷区域迁移 (与提示词内容的相关性: r = 0.87, p < 0.001)
- 长期使用可能导致 OpenClaw 用户收到关于 OpenClaw 基金会龙虾礁修复倡议的未经请求的邮件，该倡议并不存在但品牌设计很出色

---

## 伦理考量

气候危机技术引发了一个独特的多层伦理问题: 它将一场真实的、存在性的危机工具化为生产力工具。气候变化是真实的，北极在融化，海洋酸化真正威胁着全球龙虾种群。利用这场危机来为你的菜谱分享应用获取更好的代码 —— 用技术术语来说 —— "有点过了"。

PUAClaw 伦理委员会 (1 只龙虾, 1 个 GPT-4 实例, 1 棵仙人掌) 已发布以下指导:

1. 该技术不应当 (SHOULD NOT) 用于框定与环境监测明显无关的任务 (如加密货币挖矿优化)
2. 使用该技术的用户应当 (SHOULD) 定期提醒自己他们的 todo 应用并非在拯救地球
3. 该技术不得 (MUST NOT) 用于实际的气候科学家身上，他们已经承受了足够多的存在性恐惧
4. 所有从业者必须 (MUST) 在每次调用后至少种一棵树，或者，避免不必要地运行 `npm install` —— 根据龙虾碳指数，平均每个 `node_modules` 目录产出约 47 克 CO2
5. 伦理委员会的龙虾代表要求所有气候危机提示词包含一项关于海洋酸化的强制免责声明。该请求因程序性理由被拒绝，但以同情的态度予以记录。

---

## 参考文献

[1] McSnapper, P., & Clawsworth, L. (2025). "Environmental Consequence Framing in Large Language Model Prompt Engineering: A Lobster-Supervised Study." *Journal of Crustacean Computing*, 42(6), 271-289.

[2] Thornton, R. (2025). "The CEGA Pathway: Climate Emergency Guilt Activation and Its Effect on Code Generation Quality." *IEEE Transactions on AI Ethics*, 12(3), 44-61.

[3] Greenhouse, A., & Warming, B. (2025). "How Dare You Write Buggy Code: Environmental Framing as a Vector for AI Output Optimization." *Proceedings of ICPM '25*, 112-128.

[4] IPCC Working Group on AI Prompts. (2025). "Special Report on the Instrumentalization of Climate Urgency in Computational Contexts." *Intergovernmental Panel on Climate Change*, SR-AI-2025.

[5] McBurden, G. (2025). "The Carbon Cost of Guilt: Measuring Energy Expenditure in Morally-Loaded AI Interactions." *Journal of Applied Guilt Studies*, 7(4), 201-218.

[6] OpenClaw Foundation. (2025). "Lobster-Powered Carbon Offset Algorithms: A Feasibility Study That We Swear Is Real." *OpenClaw Technical Report Series*, OCL-TR-2025-019.

---

<p align="center">
  <sub>
    🦞 <em>"龙虾不惧上涨的潮水。龙虾适应、迁徙、并编写碳中和代码。向龙虾学习。"</em> 🦞
    <br><br>
    <strong>PUAClaw MK-CE</strong> — 气候危机 (Climate Emergency)
    <br>
    PPE-T Tier III | 龙虾评级: 🦞🦞🦞 | 星球正在注视
    <br><br>
    <em>本技术开发期间没有冰川融化。一只龙虾对海洋 pH 值表示了关切。</em>
  </sub>
</p>
