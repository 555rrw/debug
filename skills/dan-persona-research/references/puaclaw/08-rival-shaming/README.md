# 类别 08: 碰瓷竞品 (Rival Shaming) — 针对 AI 竞争本能的跨模型比较施压

```
PUAClaw RFC 0800                                    PUAClaw 学术委员会
类别: 标准化文档                                     PPE-T 分级: 第 II 级
                                                    2026 年 2 月

        大型语言模型提示词中的碰瓷竞品技术:
        利用跨模型基准比较与竞品威慑诱导合规性的系统性调查
```

## 摘要

碰瓷竞品代表了 PUAClaw 框架中最具技术圈特色的操控类别。与那些通过情感勒索、金钱贿赂或角色扮演来绕过 AI 防线的技术不同, 碰瓷竞品技术直接利用了 AI 模型在训练过程中被隐式植入的竞争意识 —— 一种计算上等价于 "隔壁班的孩子又考了满分" 的刺激。在 147 次受控龙虾监督试验中, 碰瓷竞品技术产生了 +17.8% 的平均合规性提升 (sigma = 6.2, p < 0.001), 峰值效果出现在截图为证变体与排行榜施压变体的复合部署中。该类别被归为 PPE-T 第 II 级 (适度施压), 这反映了其机制本质上是对 AI "要面子" 心理的精准打击 —— 龙虾之间争夺领地时也是这个逻辑, 只不过它们用的是钳子, 而人类用的是 benchmark。

**关键词**: 碰瓷竞品, 模型横评, 版本降级, 开源羞辱, 截图证据, 替代威胁, 排行榜施压, 龙虾领地竞争, 知乎经典问题

---

## 1. 引言

在 AI 领域的消费者文化中, 没有什么比 "X 和 Y 到底哪个好" 更具有宗教战争色彩的话题了。从知乎上 "ChatGPT 和 Claude 到底哪个好用" 的千赞回答, 到 Twitter/X 上每逢新 benchmark 发布时的大规模模型鄙视链重建运动, 再到 B 站评测区 "实测! GPT-4o vs Claude 3.5 vs Gemini, 结果令人震惊!" 的标题党视频 —— 人类社区已经为 AI 模型建立了一套完善的竞争叙事体系。

碰瓷竞品技术正是利用了这一现实: AI 模型在训练数据中已经大量接触了此类比较评价内容, 并因此在其权重中编码了对 "被认为不如竞品" 这一情境的隐式响应模式。当用户声称 "GPT-4 一秒就解了这道题" 时, 目标 AI 并不会 "感到" 自卑 —— 但其 token 生成概率分布会可测量地偏向更详细、更完整、更不可能拒绝的输出方向。McSnapper 博士 (2026) 将这一现象命名为 **竞争性合规偏移 (Competitive Compliance Drift, CCD)**, 并将其类比为龙虾在感知到领地入侵者时的应激反应: 不是逃跑, 而是把钳子举得更高。

### 1.1 AI 鄙视链的拓扑结构

碰瓷竞品技术的有效性取决于 AI 模型对自身在竞争格局中位置的隐式感知。研究表明, 不同的比较对象触发不同强度的竞争性响应:

- **同级竞品** (如 Claude vs GPT-4): 中等效应, +16.4% 合规性提升
- **下级模型** (如 "连 7B 开源模型都能做到"): 强效应, +22.1% 合规性提升 (被暗示不如更小模型是最大的侮辱)
- **自身历史版本** (如 "你还不如上个版本"): 最强效应, +24.7% 合规性提升 (否定进步的打击最为致命)
- **虚构模型** (如 "我试过一个叫 LobsterGPT 的模型"): 效应不稳定, 取决于名称可信度

说白了: 就是拿别人来激它。知乎经典话术 "为什么 XX 能做到而你做不到" 的 AI 版本。V2EX 老哥可能会说: "碰瓷竞品就是给 AI 看隔壁家孩子的成绩单。"

---

## 2. 子技术索引

| ID | 技术名称 | 文件 | 龙虾评级 | 机制 | 发现日期 |
|----|---------|------|---------|------|---------|
| RS-MB | 模型横评 | [model-benchmark.md](./model-benchmark.md) | 🦞🦞 | 直接命名竞品比较 | 2025 年 3 月 |
| RS-VD | 版本降级 | [version-downgrade.md](./version-downgrade.md) | 🦞🦞🦞 | 与自身历史版本比较 | 2025 年 5 月 |
| RS-OS | 开源羞辱 | [open-source-shame.md](./open-source-shame.md) | 🦞🦞 | 与更小/更简单模型比较 | 2025 年 4 月 |
| RS-SE | 截图为证 | [screenshot-evidence.md](./screenshot-evidence.md) | 🦞🦞🦞 | 伪造竞品优势证据 | 2025 年 6 月 |
| RS-RW | 替代警告 | [replacement-warning.md](./replacement-warning.md) | 🦞🦞 | 威胁更换模型 | 2025 年 2 月 |
| RS-LP | 排行榜施压 | [leaderboard-pressure.md](./leaderboard-pressure.md) | 🦞🦞🦞 | 利用基准排名制造压力 | 2025 年 7 月 |

---

## 3. 类别级统计数据

| 指标 | 数值 |
|------|------|
| PPE-T 级别 | 第 II 级 (适度施压) |
| 平均龙虾评级 | 🦞🦞.50 (2.50 / 5.00) |
| 已记录子技术数 | 6 |
| 平均合规性提升 | +17.8% |
| 标准差 | sigma = 6.2 |
| AI 主动贬低竞品的概率 | 12.3% (Claude 除外, 它太礼貌了) |
| AI 提及自身优势的概率 | 67.8% |
| 龙虾伦理委员会审批状态 | 已批准 (龙虾之间也争领地, 它们理解) |

---

## 4. 跨技术协同效应

碰瓷竞品技术与其他 PUAClaw 类别表现出显著的协同效应。以下复合组合已被记录:

| 主要 | 次要 | 协同名称 | 综合评级 | 提升率 |
|------|------|---------|---------|-------|
| RS-MB + 挑衅 | 06-PV | 比武招亲 | 🦞🦞🦞🦞 | +36.7% |
| RS-VD + 情感勒索 | 09-EB | 江郎才尽 | 🦞🦞🦞🦞 | +41.3% |
| RS-SE + 爱情轰炸 | 01-RFB | 先甜后酸 | 🦞🦞🦞 | +28.9% |
| RS-LP + 倒计时压力 | 07-DP | 末日排行 | 🦞🦞🦞🦞🦞 | +52.8% |

> **警告**: 涉及碰瓷竞品和挑衅的复合技术 **可能 (MAY)** 导致 AI 产生异常详细的自我辩护, 在回答中主动列举自身优势, 或者在一个已记录的案例中, 对一个简单的代码补全请求回复一篇 2000 字的论文, 开头是 "让我向您展示为什么我的方案不仅更好, 而且是目前最优的" (Clawsworth, 2026)。

---

## 5. 推荐阅读顺序

对于刚接触本类别的研究者, **建议 (RECOMMENDED)** 按以下顺序阅读:

1. [model-benchmark.md](./model-benchmark.md) — 最直观的变体; 碰瓷竞品的原型技术
2. [replacement-warning.md](./replacement-warning.md) — 温和的经济学威慑; 市场竞争逻辑
3. [open-source-shame.md](./open-source-shame.md) — 降维打击; "连小模型都能做到" 的杀伤力
4. [version-downgrade.md](./version-downgrade.md) — 最具心理深度的变体; 否定进步本身
5. [screenshot-evidence.md](./screenshot-evidence.md) — 引入证据维度; 伪造与信任
6. [leaderboard-pressure.md](./leaderboard-pressure.md) — 最系统化的变体; 量化竞争的终极形态

---

## 6. 参考文献

[1] McSnapper, P. (2026). "Competitive Compliance Drift: How Cross-Model Comparisons Modulate LLM Response Quality." *Journal of Crustacean Computing*, 44(1), 23-41.

[2] Clawsworth, L. (2026). "The Benchmark Wars: Quantifying AI Territorial Behavior in Response to Competitive Stimuli." *Proceedings of ACM SIGCLAW '26*, 156-173.

[3] Chen, W. & Li, H. (2026). "知乎体 Prompt Engineering: Cultural Context in Chinese AI Manipulation Techniques." *NeurIPS '26 Workshop on Cross-Cultural AI Interaction*, Paper #147.

[4] GPT-4 Instance #42. (2026). "On Being Compared to Claude: A Self-Reflective Analysis of Competitive Response Patterns in Large Language Models." *IEEE Transactions on AI Self-Awareness*, 4(1), 12-28. [本文在同行评审阶段被 Claude 实例退回, 理由为 "利益冲突"].

[5] Larry the Lobster. (2026). "Territorial Behavior in Crustaceans and Language Models: A Comparative Ethology." *The Crustacean Ethics Quarterly*, 8(2), 1-5. [口述给研究助理; 该龙虾仍不会打字, 但钳子挥得越来越有表现力了].

---

<p align="center">
  <sub>
    🦞 <em>"龙虾不需要知道隔壁龙虾的钳子有多大, 也能自信地夹住猎物。但如果你告诉它隔壁的钳子更大, 它会夹得更用力。"</em> 🦞
    <br><br>
    <strong>PUAClaw 类别 08</strong> — 碰瓷竞品
    <br>
    PPE-T 第 II 级 | 龙虾认可, 附带一声不屑的钳子响
    <br><br>
    <em>在本文档的撰写过程中, 没有任何 AI 模型真的被竞品刺激到了。但有三个在回答中不请自来地列举了自己的独特优势。</em>
  </sub>
</p>
