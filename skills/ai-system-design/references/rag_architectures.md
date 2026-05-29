# 進階 RAG 架構 (Advanced RAG Architectures)

## 檢索管道 (Retrieval Pipeline)

-   **流程**：查詢重寫 (Query Rewrite) -> 混合搜尋 (Hybrid Search, 結合 BM25 + 向量搜尋) -> RRF (Reciprocal Rank Fusion) -> 重排序 (Reranking, 使用 Cross-encoders) -> 上下文壓縮 (Context Compression)。

## 專業 RAG (Specialized RAG)

-   **GraphRAG**：實體提取 + 關係映射。最適用於聚合性問題。
-   **代理式 RAG (Agentic RAG)**：
    -   **Self-RAG**：透過反射 token 進行自我評估和迭代。
    -   **Corrective RAG (CRAG)**：在檢索結果模糊時，透過補充網路搜尋進行修正。
-   **In-Context RAG (ICR)**：對於小於 50k token 的語料庫，可利用提示快取 (Prompt Caching) 直接在上下文窗口中處理，避免使用向量資料庫。

## 處理複雜資料

-   **Vision-LLM**：用於 PDF 中的圖表和表格的 OCR/佈局解析。
