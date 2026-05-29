# 評估與 MLOps (Evaluation & MLOps)

## 評估指標 (Metrics)

-   **忠實度 (Faithfulness)**、**上下文召回率 (Context Recall)**、**答案相關性 (Answer Relevance)** (RAGAS 框架)。

## 評估模式 (Evaluation Patterns)

-   **黃金集 (Golden Sets)**：用於回歸測試。
-   **LLM 作為評審 (LLM-as-Judge)**：透過 LLM 進行品質評分 (需校準)。
-   **A/B 測試 (A/B Testing)**：用於生產環境中的模型比較。

## 可觀察性 (Observability)

-   **追蹤 (Tracing)**：LangSmith/Phoenix。
-   **漂移檢測 (Drift Detection)**：監控模型性能變化。
-   **成本追蹤 (Cost Tracking)**。
