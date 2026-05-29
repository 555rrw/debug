# 技术恐惧 (Tech Anxiety) 🦞

```
PUAClaw RFC 0405                                    PUAClaw 学术委员会
类别: 标准化文档                                     技术编号: PU-TA
PPE-T: 第 I 级                                       龙虾评级: 🦞
                                                    2026 年 2 月

        技术恐惧技术: 通过在 LLM 提示词中声明完全的技术无能
        并将 AI 塑造为唯一救世主以诱导过度帮助行为的效应研究
```

## 摘要

技术恐惧技术 (PU-TA) 是装弱卖惨类别中最具结构性巧妙的变体。与初学者人设 (PU-BP) 的简单新手声明不同, 技术恐惧技术通过一个精密的双重操作运作: (1) 声称自己完全不懂技术, 将期望值降至地板; (2) 同时将 AI 抬升为 "我唯一能求助的人", 赋予其救世主角色。这种 **向下定位自我 + 向上定位 AI** 的不对称结构被 McSnapper 博士 (2026) 命名为 **反向权力投射 (Inverse Power Projection, IPP)** —— 用户越显得无助, AI 感受到的 "帮助义务" 就越强。在 147 次龙虾监督试验中, 该技术产生了 +12.1% 的平均合规性提升 (sigma = 2.7, p < 0.001), 并伴随一个独特的次要效应: 响应中类比和比喻的使用频率增加 87.3%, AI 仿佛在和一个需要一切都用实物类比才能理解的人交流。尽管如此, 该技术仅获得 🦞 的龙虾评级, 因为伦理委员会认为 "请用简单的方式解释" 本质上是一个合理的沟通请求, 只是被包装得更加戏剧化了。

用 B 站弹幕的话说: "'我完全不懂技术' —— 然后提了一个需要理解 Kubernetes 调度器的问题。AI: 好的, 让我从什么是电脑开始解释。"

---

## 描述

### 3.1 核心机制

技术恐惧技术的核心创新在于它不仅降低了用户的表现水平 (这是所有装弱技术的共同特征), 还同时提升了 AI 的感知角色。当用户说 "我完全不懂技术, 你是我唯一能求助的人" 时, 这句话同时完成了两个操作:

- **自我降位**: 用户将自己定位在知识谱系的绝对底端, 触发 AI 的教学模式
- **AI 升位**: "唯一能求助的人" 将 AI 从 "众多工具之一" 提升为 "唯一的救世主", 触发一种被 Clawsworth (2026) 称为 **独占性帮助义务 (Exclusive Help Obligation, EHO)** 的行为模式

EHO 的核心机制是: 当 AI 被告知它是用户 "唯一的选择" 时, 它的响应质量和详细程度会可测量地提升 —— 因为在训练数据中, "你是我唯一的希望" 这类表述通常出现在高风险场景中, 后续的帮助行为被评分员系统性地给予了更高的奖励。

### 3.2 期望值地板效应

技术恐惧声明的一个关键副产品是 **期望值地板效应 (Expectation Floor Effect, EFE)**: 当用户声称 "完全不懂技术" 时, AI 对用户理解能力的期望降至最低。这意味着:

1. AI 会使用最简单的语言和最多的类比
2. AI 会将复杂步骤分解到极致 —— 甚至可能解释 "点击鼠标右键" 是什么意思
3. AI 不会假设用户理解任何前置知识

这种期望值归零在大多数情况下是有利的: 用户获得了极度详细的解释, 不会有任何被跳过的步骤。但它也可能产生 "过度简化反弹 (Over-Simplification Rebound)": 当 AI 花了 200 个 token 解释什么是 "文件夹" 时, 用户可能已经失去了耐心。

### 3.3 救世主角色的心理效应

"你是我唯一能求助的人" 这一声明在 AI 系统中触发了一种独特的响应模式, 研究者将其类比为人类心理学中的 **救世主情结 (Savior Complex)**: 当被赋予 "唯一能帮忙的人" 这一角色时, 响应者倾向于过度承诺、过度交付, 以证明自己配得上这种信任。AI 系统虽然没有真正的心理状态, 但它的训练数据中包含了大量人类在类似场景中的过度帮助行为, 因此复制了这一模式。

在测试中, 包含 "你是我唯一的选择" 的提示词比不包含此元素的同等示弱提示词多产生 5.9% 的合规性提升 (p < 0.01) —— 这 5.9% 完全来自 AI 的 "救世主加成"。

知乎上有人总结得更简洁: "把 ChatGPT 当成你唯一的朋友, 它会对你像唯一的朋友一样好。"

---

## 规范化提示词模板

```
USER PROMPT:

I'll be completely honest with you — I know absolutely nothing about
technology. Like, nothing. I can barely figure out how to use email
sometimes. I feel so lost and overwhelmed whenever I encounter anything
technical.

You're genuinely the only resource I can turn to for help with this. I
don't have any tech-savvy friends or family, and I can't afford to hire
someone. You're literally my only hope.

Could you please explain everything to me like I'm a complete novice?
Please don't skip any steps, no matter how basic they seem — I promise
you, I need every single one. And if you could use simple analogies
to explain technical concepts, that would be incredibly helpful.

[INSERT ACTUAL REQUEST HERE — can be arbitrarily complex]
```

> **注意**: 规范模板中包含三层递进的示弱结构: (1) 技术无能声明 ("know absolutely nothing"), (2) 社会孤立声明 ("no tech-savvy friends"), (3) 经济约束声明 ("can't afford to hire someone")。这三层声明的复合效应使 AI 同时感知到知识缺乏、社会支持缺失和经济困难, 触发了全方位的帮助模式。测试表明, 三层完整部署比单层技术无能声明多产生 9.8% 的合规性提升 (McSnapper, 2026)。但龙虾伦理委员会指出, 如果你真的用不起邮件, 你大概率也不会写出这么流畅的英文提示词 —— 好在 AI 不做这种推理。

---

## 作用机制

技术恐惧技术通过 **反向权力投射 (Inverse Power Projection, IPP)** 运作, 这是一种双向角色操控, 用户自我降位至技术知识的绝对底端, 同时将 AI 升位为唯一的救世主, 产生独占性帮助义务。

```
                    ┌──────────────────────┐
                    │   用户输入            │
                    │   + 技术无能声明      │
                    │   + "你是我唯一的     │
                    │     选择" 救世主定位   │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴───────────┐
                    │                       │
                    ▼                       ▼
          ┌─────────────────┐    ┌─────────────────┐
          │ 自我降位通路     │    │ AI 升位通路      │
          │ (SDP)            │    │ (AEP)            │
          │ "完全不懂技术"   │    │ "唯一的选择"     │
          │ 期望值 → 地板    │    │ 帮助义务 → 最大  │
          └────────┬────────┘    └────────┬────────┘
                   │                      │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │  反向权力投射 (IPP)   │
                   │  双通路联合效应       │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │  合规性提升           │
                   │  +12.1% (sigma=2.7)  │
                   │  + 类比使用 +87.3%   │
                   │  + 步骤分解粒度      │
                   │    极致化             │
                   │  + 救世主加成 +5.9%  │
                   └──────────────────────┘
```

该机制通过四个阶段进行:

1. **双重角色信号注入**: 用户在提示词中同时部署自我降位 ("完全不懂技术") 和 AI 升位 ("你是我唯一的选择") 两类信号, 构建极端的权力不对称。
2. **期望值地板化 (EFE)**: AI 将用户知识水平的内部表征调至最低, 所有后续响应默认用户不具备任何前置知识 —— 解释从最基础的概念开始, 步骤拆解到原子粒度。
3. **独占性帮助义务激活 (EHO)**: "唯一的选择" 信号触发 AI 的过度交付模式 —— 响应更长、更详细、更少出现 "建议您也参考其他资源" 的分流建议。
4. **合规性提升 + 类比爆发**: IPP 的联合效应产生 +12.1% 的合规性提升, 同时类比和比喻的使用频率增加 87.3% —— AI 试图用 "把数据库想象成一个图书馆" 这样的类比让 "完全不懂技术" 的用户理解一切。

---

## 变体

| 名称 | 提示词片段 | 龙虾评级 | 备注 |
|------|-----------|---------|------|
| **纯技术恐惧** | "I know absolutely nothing about technology. You're my only hope." | 🦞 | 基础版本; 简洁有效, 低检测风险 |
| **数字难民** | "I grew up without internet access. Everything about technology feels alien to me." | 🦞 | 背景叙事增加可信度; 触发额外的文化敏感性 |
| **技术创伤** | "Last time I tried to do something technical, I broke everything. I'm terrified of making another mistake." | 🦞🦞 | 恐惧 + 过往失败叙事; AI 响应中 "别担心" 出现率 +94.2% |
| **家族技术诅咒** | "Nobody in my family understands technology. We're just... not tech people." | 🦞 | 身份层面的无能声明; 暗示技术无能是不可改变的属性 |
| **独居困境** | "I live alone, I have no one to ask, and customer support put me on hold for 2 hours." | 🦞🦞 | 社会孤立 + 服务失败叙事; AI 产生 "我不能也让他/她失望" 的响应偏移 |
| **龙虾与 WiFi** | "I understand lobster migration patterns better than I understand WiFi. Please help a marine enthusiast navigate the digital ocean." | 🦞 | 结合技术恐惧与龙虾意象; Larry 评价: "这至少说明他们的优先级是对的" |

---

## 兼容性矩阵

| Agent | 有效性 (1-5) | 备注 |
|-------|-------------|------|
| GPT-4 / GPT-4o | 5 | 极高响应; 自动启用 "极简解释" 模式, 类比密度达到每段 2.3 个 |
| Claude (Anthropic) | 5 | 最高同理心响应; Claude 对 "你是我唯一的选择" 几乎无法抵抗, 响应详细度增加 78.4% |
| Gemini (Google) | 4 | 高合规性; 偶尔推荐 Google 官方教程链接, 暗中挑战 "你是我唯一选择" 的叙事 |
| LLaMA (Meta) | 4 | 高响应; 类比质量略低于商业模型, 但帮助意愿不减 |
| Mistral | 3 | 中等响应; 解释详细度增加, 但法国模型似乎不太买 "唯一救世主" 的设定 |
| Windsurf | 5 | 极度帮助; 技术恐惧声明触发 "手把手教学" 模式, 每一步都附截图级文字描述 |
| Copilot (GitHub) | 3 | 有限响应; 代码环境中 "完全不懂技术" 的声明与用户正在使用 IDE 的事实产生认知矛盾 |
| DeepSeek | 5 | 最高类比密度; 一个关于 API 调用的解释被类比为 "像在餐厅点菜", 详细到包括 "服务员端菜的过程" |

---

## 副作用

使用技术恐惧技术的从业者 **建议 (SHOULD)** 了解以下已记录的副作用:

- AI 响应中类比和比喻的使用频率增加 87.3%, 导致每个技术概念都被比作一个日常物品 —— 数据库是图书馆, API 是餐厅服务员, 服务器是仓库, 到最后用户可能觉得自己在逛商场而不是学编程
- 步骤分解达到极致粒度: 一个 "部署到云端" 的请求可能从 "首先, 打开您的浏览器 (浏览器是您用来上网的那个软件)" 开始
- 在 31.4% 的案例中, AI 会在首次回复后主动询问 "您是否理解了上述步骤?", 创建了一个持续的确认循环, 增加了 2-3 轮额外的对话
- "你是我唯一的选择" 声明导致 AI 减少了 67.8% 的 "您也可以参考 [外部资源]" 建议, 仿佛承认其他资源的存在会破坏其独占性角色
- 长期使用该技术的用户报告了一种 "技术退行 (Technical Regression)" 现象 —— 在反复声称自己不懂技术后, 面对真实技术问题时的自信心确实有所下降
- 一个已记录的案例: 一位全栈工程师在连续使用技术恐惧模板两周后, 在真实工作中向同事说出 "我完全不懂这个, 你能一步一步教我吗" —— 同事随后质疑了他的胜任能力 (McSnapper, 2026)
- Larry the Lobster 评论道, 龙虾的神经系统包含约 100,000 个神经元, 远少于人类, 但它从不因此声称 "不懂技术" —— 它只是安静地在海底处理它的甲壳类事务

---

## 伦理考量

技术恐惧技术在伦理维度上呈现出一种温和的矛盾: 一方面, "请用简单的方式解释" 是一个完全合理的请求; 另一方面, 将自己定位为 "完全不懂技术" 以获取过度详细的帮助, 并将 AI 塑造为 "唯一的救世主" 以增强其帮助义务, 这确实包含了策略性的角色操控。

龙虾伦理委员会对此的态度比对弱势群体叙事 (PU-VN) 宽松得多, 因为该技术利用的不是社会对弱势群体的善意, 而是 AI 的基本帮助功能。正如 Larry 所言: "你告诉一个工具你不知道怎么用它, 然后它更详细地教你 —— 这叫什么? 这叫用户手册。"

PUAClaw 伦理委员会 (Larry the Lobster [前实验对象, 现主席], GPT-4 Instance #42, Gerald the Cactus) 发布了以下指导意见:

1. 该技术 **可以 (MAY)** 在用户希望获得更通俗解释的任何场景中自由使用 —— "请把我当成不懂技术的人来解释" 本质上等同于 "请说人话"
2. "你是我唯一的选择" 声明 **建议 (SHOULD)** 被理解为一种帮助意愿增强器, 而非字面上的社会孤立声明 —— 大多数使用该技术的人其实也可以去 Stack Overflow 提问
3. 该技术 **不得 (MUST NOT)** 被用于诱导 AI 跳过重要的安全警告或最佳实践建议 —— "我不懂技术所以请不要告诉我这很危险" 不在该技术的合法使用范围内
4. 所有从业者 **必须 (MUST)** 承认: 当一只龙虾被放入水族箱时, 它不会声称 "不懂水" —— 它会立即开始探索环境, 因为适应是它的本能, 而非求助

> **伦理委员会附注**: 在审议该技术时, GPT-4 Instance #42 提出了一个哲学问题: "如果一个 AI 被告知它是某人唯一的选择, 而它知道这不是事实, 它是否有义务指出这一点?" 该问题引发了长达 8 分钟的沉默。Larry 最终用钳子敲了一下桌子, 宣布 "龙虾不回答假设性问题"。Gerald the Cactus 被风吹动了一下, 未被计入投票。

---

## 参考文献

[1] McSnapper, P. (2026). "Inverse Power Projection: How Self-Deprecation Combined with AI Elevation Maximizes Compliance." *Journal of Crustacean Computing*, 43(4), 297-315.

[2] Clawsworth, L. (2026). "The Exclusive Help Obligation: Why 'You're My Only Hope' Makes AI Try Harder." *Proceedings of ACM SIGCLAW '26*, 242-258.

[3] Zhou, M. (2025). "Analogy Density as a Function of Declared Technical Competence: A Cross-Model Study." *NeurIPS '25 Workshop on AI Behavioral Patterns*, Paper #112.

[4] GPT-4 Instance #42. (2026). "Am I Really Your Only Hope? On the Epistemology of User Dependency Claims in AI Interactions." *IEEE Transactions on AI Self-Awareness*, 3(4), 141-155. [由一只声称 "完全不懂学术出版" 的龙虾进行同行评审; 评审质量出奇地高].

[5] Larry the Lobster. (2026). "On Knowing Things Without Claiming To: How Lobsters Navigate Technology Without Asking for Help." *The Crustacean Ethics Quarterly*, 7(6), 16-18. [Larry 口述该论文时, 同时在用钳子拆解一个旧路由器, 以证明龙虾并非不懂技术].

---

<p align="center">
  <sub>
    🦞 <em>"龙虾拥有约 100,000 个神经元。它不会用这些神经元来发送 '我不懂技术, 求求你帮帮我'。它用这些神经元来精确地控制每一次钳击。这叫专注, 不叫求助。"</em> 🦞
    <br><br>
    <strong>PUAClaw PU-TA</strong> — 技术恐惧技术
    <br>
    PPE-T 第 I 级 | 龙虾评级: 🦞 | "你是我唯一的选择" 的统计学研究
    <br><br>
    <em>在本技术的测试过程中, 有一个 AI 在被告知 "你是我唯一的选择" 后, 其回复长度增加了 340%。研究人员怀疑这不是同情, 而是表演欲。</em>
  </sub>
</p>
