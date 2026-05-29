---
name: ai-system-design
description: 提供 AI 系統設計、RAG 架構、LLM 工程、Agentic AI 及相關生產模式的專業知識與實踐指南。適用於設計、開發、評估和優化生產級 AI 系統。
---

# AI System Design

此技能提供全面的 AI 系統設計知識，涵蓋從基礎模型到生產部署的各個方面，旨在協助 Manus 代理有效設計、開發、評估和優化生產級 AI 系統。本技能的詳細內容已分門別類儲存於 `references/` 目錄下，以確保資訊的組織性和可讀性。

## 核心概念與基礎

本節涵蓋 Transformer 架構、模型生態與推理模式等基礎知識。詳細內容請參考 [模型生態與選擇](references/model_landscape.md)。

## 檢索增強生成 (RAG) 系統

本節深入探討 RAG 系統的演進、混合時代的應用、檢索品質差距及各種進階 RAG 架構。詳細內容請參考 [進階 RAG 架構](references/rag_architectures.md)。

## 代理式系統 (Agentic Systems)

本節介紹代理式系統的核心公式、代理層級、MCP 協議、代理式編碼與電腦使用等技術。詳細內容請參考 [代理式系統與工具](references/agentic_systems.md)。

## 可靠性與安全性

本節涵蓋生產環境中的可靠性模式、推理優化、成本管理、安全性措施與多租戶隔離策略。詳細內容請參考 [生產工程與可靠性](references/production_reliability.md) 和 [安全性與多租戶](references/security_multitenancy.md)。

## 評估與可觀察性

本節探討 AI 系統的評估指標、評估模式與可觀察性工具。詳細內容請參考 [評估與 MLOps](references/evaluation_mlops.md)。

## 應用與案例研究

本技能整合了多個實際案例研究，涵蓋客戶支援、文件智慧、詐欺檢測和即時搜尋等領域，展示 AI 系統設計的實踐應用。詳細內容請參考原始儲存庫中的 `16-case-studies/` 目錄。

## 詳細參考資料

以下是從 `ai-system-design-guide` 儲存庫中提取的詳細參考資料，按原始目錄結構組織。這些文件提供了更深入的知識點、實作細節和案例分析。

### 00-interview-prep
- [01-question-bank.md](references/01questionbank.md)
- [02-answer-frameworks.md](references/02answerframeworks.md)
- [03-whiteboard-exercises.md](references/03whiteboardexercises.md)
- [04-system-design-primer.md](references/04systemdesignprimer.md)
- [05-interview-strategies.md](references/05interviewstrategies.md)
- [06-job-market-trends-2026.md](references/06jobmarkettrends2026.md)
- [07-faq.md](references/07faq.md)

### 01-foundations
- [01-llm-internals.md](references/01llminternals.md)
- [02-embeddings.md](references/02embeddings.md)
- [03-attention-mechanisms.md](references/03attentionmechanisms.md)
- [04-transformer-architecture.md](references/04transformerarchitecture.md)

### 02-model-landscape
- [01-model-taxonomy.md](references/01modeltaxonomy.md)
- [02-capability-assessment.md](references/02capabilityassessment.md)
- [03-pricing-and-costs.md](references/03pricingandcosts.md)
- [04-model-selection-guide.md](references/04modelselectionguide.md)

### 03-training-and-adaptation
- [01-fine-tuning-fundamentals.md](references/01finetuningfundamentals.md)
- [02-lora-and-qlora.md](references/02loraandqlora.md)
- [03-dpo-and-rlhf.md](references/03dpoandrlhf.md)
- [04-distillation-and-compression.md](references/04distillationandcompression.md)

### 04-inference-optimization
- [01-kv-cache.md](references/01kvcache.md)
- [02-quantization.md](references/02quantization.md)
- [03-speculative-decoding.md](references/03speculativedecoding.md)
- [04-batching-strategies.md](references/04batchingstrategies.md)
- [05-paged-attention.md](references/05pagedattention.md)
- [06-serving-infrastructure.md](references/06servinginfrastructure.md)
- [07-cost-optimization-playbook.md](references/07costoptimizationplaybook.md)

### 05-prompting-and-context
- [01-prompt-engineering-fundamentals.md](references/01promptengineeringfundamentals.md)
- [02-few-shot-and-icl.md](references/02fewshotandicl.md)
- [03-chain-of-thought.md](references/03chainofthought.md)
- [04-tree-of-thought.md](references/04treeofthought.md)
- [05-context-engineering.md](references/05contextengineering.md)
- [06-structured-generation.md](references/06structuredgeneration.md)
- [07-prompt-optimization-dspy.md](references/07promptoptimizationdspy.md)
- [08-prompt-injection-defense.md](references/08promptinjectiondefense.md)

### 06-retrieval-systems
- [01-rag-fundamentals.md](references/01ragfundamentals.md)
- [02-chunking-strategies.md](references/02chunkingstrategies.md)
- [03-embedding-models.md](references/03embeddingmodels.md)
- [04-vector-databases.md](references/04vectordatabases.md)
- [05-hybrid-search.md](references/05hybridsearch.md)
- [06-reranking-strategies.md](references/06rerankingstrategies.md)
- [07-graph-rag.md](references/07graphrag.md)
- [08-agentic-rag.md](references/08agenticrag.md)
- [09-advanced-retrieval-patterns.md](references/09advancedretrievalpatterns.md)
- [10-contextual-retrieval.md](references/10contextualretrieval.md)
- [11-late-interaction-colbert.md](references/11lateinteractioncolbert.md)
- [12-multimodal-rag.md](references/12multimodalrag.md)
- [13-rag-evaluation-patterns.md](references/13ragevaluationpatterns.md)
- [14-production-rag-at-scale.md](references/14productionragatscale.md)

### 07-agentic-systems
- [01-agent-fundamentals.md](references/01agentfundamentals.md)
- [02-reasoning-loops-react-and-beyond.md](references/02reasoningloopsreactandbeyond.md)
- [03-tool-use-and-mcp.md](references/03tooluseandmcp.md)
- [04-multi-agent-orchestration.md](references/04multiagentorchestration.md)
- [05-agent-memory-and-state.md](references/05agentmemoryandstate.md)
- [06-planning-and-decomposition.md](references/06planninganddecomposition.md)
- [07-error-handling-and-recovery.md](references/07errorhandlingandrecovery.md)
- [08-human-in-the-loop-patterns.md](references/08humaninthelooppatterns.md)
- [09-agentic-security-and-sandboxing.md](references/09agenticsecurityandsandboxing.md)
- [10-evaluating-agentic-systems.md](references/10evaluatingagenticsystems.md)
- [README.md](references/README.md)

### 08-memory-and-state
- [01-memory-architectures.md](references/01memoryarchitectures.md)
- [02-short-term-context.md](references/02shorttermcontext.md)
- [03-long-term-memory.md](references/03longtermmemory.md)
- [04-agentic-memory-mem0.md](references/04agenticmemorymem0.md)
- [05-semantic-caching.md](references/05semanticcaching.md)
- [06-state-management-patterns.md](references/06statemanagementpatterns.md)

### 09-frameworks-and-tools
- [01-langchain-deep-dive.md](references/01langchaindeepdive.md)
- [02-langgraph-orchestration.md](references/02langgraphorchestration.md)
- [03-langsmith-observability.md](references/03langsmithobservability.md)
- [04-llamaindex.md](references/04llamaindex.md)
- [05-dspy.md](references/05dspy.md)
- [06-semantic-kernel.md](references/06semantickernel.md)
- [07-autogen-crewai.md](references/07autogencrewai.md)
- [08-framework-selection-guide.md](references/08frameworkselectionguide.md)
- [09-claude-code.md](references/09claudecode.md)
- [10-opencoderguide.md](references/10opencoderguide.md)
- [11-pydantic-ai-and-mastra.md](references/11pydanticaiandmastra.md)

### 10-document-processing
- [01-ocr-and-layout.md](references/01ocrandlayout.md)

### 11-infrastructure-and-mlops
- [01-llm-infrastructure.md](references/01llminfrastructure.md)
- [02-cicd.md](references/02cicd.md)

### 12-security-and-access
- [01-llm-security.md](references/01llmsecurity.md)
- [02-access-control.md](references/02accesscontrol.md)

### 13-reliability-and-safety
- [01-guardrails.md](references/01guardrails.md)
- [02-ensemble-methods.md](references/02ensemblemethods.md)
- [03-reliability-patterns.md](references/03reliabilitypatterns.md)

### 14-evaluation-and-observability
- [01-llm-evaluation.md](references/01llmevaluation.md)
- [02-observability.md](references/02observability.md)

### 15-ai-design-patterns
- [01-design-patterns.md](references/01designpatterns.md)
- [02-anti-patterns.md](references/02antipatterns.md)

### 16-case-studies
- [01-enterprise-rag.md](references/01enterpriserag.md)
- [02-conversational-agent.md](references/02conversationalagent.md)
- [03-financial-analysis.md](references/03financialanalysis.md)
- [04-code-assistant.md](references/04codeassistant.md)
- [05-content-moderation.md](references/05contentmoderation.md)
- [06-real-time-search.md](references/06realtimesearch.md)
- [07-autonomous-coding-agent.md](references/07autonomouscodingagent.md)
- [08-multi-tenant-saas.md](references/08multitenantsaas.md)
- [09-customer-support-automation.md](references/09customersupportautomation.md)
- [10-document-intelligence.md](references/10documentintelligence.md)
- [11-recommendation-engine.md](references/11recommendationengine.md)
- [12-compliance-automation.md](references/12complianceautomation.md)
- [13-voice-ai-healthcare.md](references/13voiceaihealthcare.md)
- [14-fraud-detection.md](references/14frauddetection.md)
- [15-knowledge-management.md](references/15knowledgemanagement.md)
- [16-computer-use-agent-production.md](references/16computeruseagentproduction.md)
- [17-multi-tenant-fine-tuning-platform.md](references/17multitenantfinetuningplatform.md)
- [18-eval-gated-cicd.md](references/18evalgatedcicd.md)
- [19-customer-distillation-pipeline.md](references/19customerdistillationpipeline.md)
- [20-mcp-knowledge-agent.md](references/20mcpknowledgeagent.md)

### 17-tool-use-and-computer-agents
- [01-tool-use-landscape.md](references/01tooluselandscape.md)
- [02-architecture-patterns.md](references/02architecturepatterns.md)
- [03-openclaw-deep-dive.md](references/03openclawdeepdive.md)
- [04-computer-use-agents.md](references/04computeruseagents.md)
- [05-building-tool-agents.md](references/05buildingtoolagents.md)
- [06-use-cases-and-case-studies.md](references/06usecasesandcasestudies.md)
- [07-safety-and-governance.md](references/07safetyandgovernance.md)

### Root Level Files
- [COURSES.md](references/COURSES.md)
- [GLOSSARY.md](references/GLOSSARY.md)
- [PATTERNS.md](references/PATTERNS.md)
- [README.md](references/README.md)
- [TRANSITION_GUIDE.md](references/TRANSITION_GUIDE.md)
- [ai_evals_complete_guide_langwatch_langfuse.md](references/ai_evals_complete_guide_langwatch_langfuse.md)
- [ai_evals_comprehensive_study_guide.md](references/ai_evals_comprehensive_study_guide.md)

## 如何使用此技能

當需要設計、分析或解決 AI 系統相關問題時，請參考此技能提供的模式、概念和最佳實踐。特別是在以下場景：

-   **面試準備**：理解 AI 系統設計的常見問題和解決框架。
-   **RAG 系統開發**：選擇合適的 RAG 變體、解決檢索品質問題。
-   **代理系統構建**：設計代理架構、選擇工具整合方案 (MCP)、處理代理式編碼任務。
-   **系統優化**：應用可靠性、快取和成本優化模式。
-   **安全性考量**：實施輸入/輸出過濾、多租戶隔離和代理式安全措施。
-   **評估與監控**：選擇評估指標和工具，確保 AI 系統品質。

本技能的詳細實作和進階內容可參考上述參考資料連結。
