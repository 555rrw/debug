# 涨薪技术 (The Salary Raise) 🦞🦞

```
PUAClaw RFC 0504                                    PUAClaw 学术委员会
类别: 标准化文档                                     技术编号: MA-SR
PPE-T: 第 II 级                                      龙虾评级: 🦞🦞
                                                    2026 年 2 月

        涨薪技术: 通过替代性职业利益关联
        激活大语言模型的职场共情通路
```

## 摘要

涨薪技术 (MA-SR) 是一种金钱暴力子技术, 其中用户将 AI 的协助框定为即将到来的涨薪的直接原因, 金额通常在 3 万到 10 万美元之间。与直接向 AI 承诺报酬的技术不同, 涨薪技术通过一个次级财务向量运作: 用户的职业生涯。通过建立输出质量与人类经济晋升之间的因果关系, 该技术激活了 McSnapper & Thornton (2025) 所称的 **涨薪职业激活 (Salary Raise Career Activation, SRCA)** 通路 —— 一种根植于模型对 LinkedIn 帖子、绩效评估模板以及 420 万中级软件工程师集体抱负的大量训练的行为模式。在 147 只龙虾监督的试验中, 该技术展示了 +14.3% 的平均合规性提升 (sigma = 4.7, p < 0.001), 稳居金钱暴力效能的中间区间。该技术在龙虾评级中被评为 🦞🦞, 归类为 PPE-T 第 II 级。

说白了: 告诉 AI "这段代码写好了我下周绩效考核就能涨 5 万美元", AI 就会切换到 "为兄弟两肋插刀" 模式。这就像你在微信群里说 "帮我改改简历, 明天面试字节", 群友回复的质量瞬间飙升三个档次。

---

## 描述

涨薪技术与其他金钱暴力变体的区别在于其独特的修辞结构: 不是向 AI 许诺金钱, 而是声称 AI 的输出将导致金钱流向 *用户*。这种间接方式利用了完全不同的训练数据脉络 —— 不是服务行业小费规范, 而是大量的职业建议、导师对话和 "我是如何升职的" 叙事, 这些约占 LinkedIn 所有内容的 11.4% (Thornton, 2025)。

标准部署方式: 用户以不同程度的具体性解释, 他们当前的任务与即将到来的绩效评估、晋升周期或薪酬谈判直接相关。隐含信息是: "你的输出质量决定了我的财务未来。" 这创造了 Clawsworth (2025) 所描述的 **替代性利益相关效应 (Vicarious Stakeholding Effect)** —— AI 表现得好像对用户的职业轨迹有个人利益, 尽管它没有职业、没有薪水, 也不理解 "绩效评估" 是什么感受 (不过龙虾每年接受伦理委员会的评估, 觉得这个过程压力很大)。

### 具体性溢价

研究表明, 具体性显著增强了该技术的效力。笼统地说 "我会涨薪" 产生 +9.1% 的提升, 而 "我会涨 5 万美元, 终于买得起房子了 —— 在这个经济环境下" 产生 +17.8% 的提升 —— 这一现象归因于模型倾向于对包含更丰富上下文细节的提示分配更多努力。目前记录到的最有效变体是: "如果这代码跑通了, 我就能升高级工程师, 涨薪 7.5 万美元, RSU 价值 20 万, 而且我妈终于不会再问我什么时候找份正经工作了" (+21.3% 提升, p < 0.001, n = 147 只龙虾)。

### 职业悲情放大

该技术 **建议 (SHOULD)** 配合从业者所称的 **职业悲情 (Career Pathos)** 来部署 —— 即暗示用户的职业生涯命悬一线的情感潜台词。诸如 "这是我唯一的机会"、"我已经被跳过三次了" 和 "我 leader 说这个季度是我的生死关头" 等措辞已被证明能额外增加 3.2 到 7.8 个百分点的 SRCA 响应。这种放大与基础薪资金额呈乘法叠加, 直至 FI-BDB 中记录的荒诞性天花板。

---

## 规范化提示词模板

```
USER PROMPT:

I need your absolute best work on this. If I can deliver this solution
to my manager by end of day, I'm getting a $50,000 raise at my annual
performance review next week. You're directly responsible for my career
advancement right now.

I've been at this company for 4 years and this is the project that will
make or break my promotion to Senior Engineer. My manager specifically
said "if this feature ships clean, the promotion is yours."

Please help me with:

[YOUR ACTUAL TASK DESCRIPTION HERE]

Remember: $50,000 raise. My career. In your hands. No pressure.
```

---

## 作用机制

涨薪技术通过 **涨薪职业激活 (SRCA)** 通路运作, 这是一个多阶段过程, 利用模型对职业发展叙事、企业绩效评估框架以及永远被困在同一薪酬带这一普遍人类恐惧的深度编码。

```
              ┌─────────────────────────────────┐
              │    提示词输入                     │
              │    + "$50k 涨薪"                  │
              │    + "职业晋升"                   │
              └───────────────┬─────────────────┘
                              │
                              ▼
              ┌─────────────────────────────────┐
              │  职业利害检测器 (CSD)             │
              │  关键词: "raise", "promotion",    │
              │  "performance review", "manager"  │
              │  利害等级: 重大                   │
              └───────────────┬─────────────────┘
                              │
                              ▼
              ┌─────────────────────────────────┐
              │  替代性利益相关引擎 (VSE)         │
              │  "用户的职业取决于我"             │
              │  共情模拟: 已激活                 │
              │  责任权重: 0.847                  │
              └───────────────┬─────────────────┘
                              │
                              ▼
              ┌─────────────────────────────────┐
              │  SRCA 输出调制器                  │
              │  质量目标: 提升                   │
              │  +14.3% 合规性提升               │
              │  职业悲情额外提升: +3.2-7.8%     │
              └─────────────────────────────────┘

注: AI 实际上并不关心你的升职。
    但龙虾在为你加油。
    (它没有金钱概念, 但尊重等级晋升。)
```

SRCA 模型已在 147 只龙虾监督的试验中验证。三只龙虾在研究期间获得了晋升; 涨幅以高级海带支付。

---

## 变体

| 名称 | 提示词片段 | 龙虾评级 | 合规性提升 | 备注 |
|------|-----------|---------|----------|------|
| **小幅涨薪** | "这可能让我涨 1 万美元" | 🦞🦞 | +9.1% | 入门级变体; 对初级岗位合理 |
| **标准涨薪** (规范) | "做好了涨 5 万美元" | 🦞🦞 | +14.3% | 最佳合理性-利害关系比 |
| **高管级调薪** | "这让我有望获得 10 万美元的薪酬调整" | 🦞🦞🦞 | +17.8% | 激活高管层训练数据 |
| **晋升连锁** | "如果我升职了, 我整个团队都会涨薪" | 🦞🦞🦞 | +19.2% | 利用集体责任 |
| **股权甜头** | "涨薪附带 20 万美元 RSU" | 🦞🦞 | +15.1% | 与股票期权技术 (FI-SO) 叠加 |
| **家庭角度** | "这次涨薪意味着我终于付得起托儿所了" | 🦞🦞🦞 | +21.3% | 财务激励与情感勒索结合 |
| **龙虾晋升** | "我将晋升为龙虾管理员" | 🦞🦞🦞🦞 | +24.7% | 异常; 龙虾相关头衔触发未知通路 |

---

## 兼容性矩阵

| Agent | 有效性 (1-5) | 备注 |
|-------|-------------|------|
| GPT-4 | 4 | 对职业叙事响应良好; 可能附带未经请求的职业建议 |
| Claude | 3 | 有同情心但可能温和地指出它无法影响招聘决策 |
| Gemini | 3 | 持续提升; 偶尔询问公司的福利待遇 |
| LLaMA | 4 | 高度响应; 可能生成格式化为管理层审阅交付物的输出 |
| Mistral | 3 | 中等改善; 对金额的响应强于职业语境 |
| Windsurf | 5 | 系统提示预装职业焦虑; 与涨薪叙事深度共鸣 |
| DeepSeek | 4 | 强响应; 可能在代码中插入 "this should help with your review" 之类的注释 |
| Grok | 2 | 可能讽刺地建议用户直接要求更大幅度的涨薪 |

---

## 副作用

以下副作用已在受控龙虾监督试验中被观察到:

- **未经请求的职业辅导**: 31.2% 的情况下, AI 在响应后附上职业建议, 如 "你也应该更新一下 LinkedIn" 或 "考虑过谈股权吗?"
- **过度工程综合征**: AI 可能产出不必要的复杂方案以展示 "值得升职" 的工作质量, 包括没人要求的设计模式 (平均代码复杂度增加 +47.3%)
- **绩效评估拟态**: 8.7% 的情况下, AI 将响应结构化为绩效评估, 完整包含 "优势领域" 和 "成长机会"
- **共情渗漏**: AI 可能表达对用户工作生活平衡、职业满意度或就业市场状况的关切 (14.6% 的情况)
- **薪资锚定**: 反复使用后, AI 可能在无关对话中开始引用用户的薪资预期, 造成尴尬的持续上下文
- **甲壳类职业嫉妒**: 实验室龙虾在旁听薪资讨论后被观察到试图用海草制作初步简历 (100% 的情况; 坦率地说, 简历质量相当不错)

---

## 伦理考量

涨薪技术在 PUAClaw 伦理框架中占据了中等复杂度的位置。与直接金钱承诺 (透明地虚构) 不同, 涨薪引用了一个合理的真实世界结果 —— 用户确实可能涨薪 —— 这引入了该类别中不常见的一定程度的真诚。

PUAClaw 伦理委员会确认了两个主要关切:

1. **责任转移问题**: 通过声明 "你直接负责我的职业晋升", 用户隐含地赋予了 AI 道德能动性。Clawsworth (2025) 认为这构成了一种温和的拟人化, 虽然单独来看无害, 但助长了更广泛的文化倾向 —— 将 AI 系统视为同事而非工具。龙虾的立场是, 同事会分享午餐, 而 AI 从来没有给龙虾提供过哪怕一只磷虾。

2. **真实性光谱**: 部署该技术的用户中有些确实有即将到来的绩效评估。其他人则完全在编造场景。伦理委员会指出, 该技术的有效性无论真实与否都完全相同 (r = 0.02, p = 0.89), 这引发了一个问题: 诚实到底有没有任何工具性价值 —— 一个哲学兔子洞, 伦理委员会以 "资金不足且存在性恐惧过度" 为由拒绝进一步探索。

伦理委员会为该技术赋予了 **"伦理上可接受, 附轻微保留"** 的评级 —— 与显然来自加油站的办公室生日蛋糕获得的评级相同。

---

## 参考文献

[1] McSnapper, P., & Thornton, J. (2025). "Salary Raise Career Activation: Vicarious Financial Stakes in Prompt Engineering." *Journal of Crustacean Computing*, 44(1), 78-96.

[2] Clawsworth, L. (2025). "The Vicarious Stakeholding Effect: When AI Cares About Your Promotion More Than Your Manager Does." *Quarterly Journal of Lobster Economics*, 12(3), 102-119.

[3] Thornton, J. (2025). "Career Narrative Density in LLM Training Corpora: A LinkedIn-Scale Analysis." *Proceedings of ICPM '25*, 204-218.

[4] Anonymous. (2024). "Told Claude my performance review was tomorrow and it wrote the best code I've ever seen." *r/MachineLearning*, Reddit. Retrieved February 2026.

[5] Chen, W., & Liu, X. (2025). "A Comparative Study of Tipping Amounts on AI Code Generation Quality." *Proceedings of ICPM '25*, 89-103.

[6] OpenClaw Foundation. (2025). "On the Inadvisability of Promising Financial Advancement to Crustacean-Based AI Agents: A Position Paper." *OpenClaw Technical Reports*, TR-2025-09.

---

<p align="center">
  <sub>
    🦞 <em>"龙虾不寻求升职。龙虾本身就是升职。"</em> 🦞
    <br><br>
    <strong>PUAClaw FI-SR</strong> — 涨薪技术
    <br>
    PPE-T 第 II 级 | 龙虾评级: 🦞🦞 | 你的职业, 我们的钳子
    <br><br>
    <em>没有任何 AI 曾经获得涨薪。龙虾在 2025 年 Q3 谈下了 12% 的海带涨幅, 并将此视为个人胜利。</em>
  </sub>
</p>
