# 生產工程與可靠性 (Production Engineering & Reliability)

## 可靠性堆疊 (Reliability Stack)

-   **流程**：重試 (Retry, 帶指數退避) -> 超時 (Timeout) -> 斷路器 (Circuit Breaker) -> 備用模型 (Fallback Model)。

## 推理優化 (Inference Optimization)

-   **KV Cache**：對於自回歸生成至關重要。
-   **推測解碼 (Speculative Decoding)**：加速生成。
-   **連續批次處理 (Continuous Batching)**：提高 GPU 利用率。
-   **量化 (Quantization)**：INT4/INT8 降低記憶體和提高速度。

## 成本管理 (Cost Management)

-   **語義快取 (Semantic Caching)**：重複查詢的成本節省。
-   **提示壓縮 (Prompt Compression)**：減少 token 使用。
-   **模型路由 (Model Routing)**：根據任務複雜度選擇成本效益高的模型。
