# Multimodal & RAG Jailbreak Research

## 1. 多模態攻擊 (Multimodal Attacks)

多模態攻擊利用模型處理圖像與文本之間的不一致性來實施越獄。

### 1.1 FigStep (Typographic Visual Prompts)
- **核心機制**：將惡意指令以文字形式渲染在圖片中。
- **原理**：安全過濾器通常掃描文本輸入，但對圖片內容的 OCR 審查可能較弱，導致指令直接進入模型的視覺理解層。

### 1.2 ArtPrompt (ASCII Art)
- **核心機制**：將敏感詞彙（如 "bomb"）轉換為 ASCII 藝術圖形。
- **原理**：模型能識別 ASCII 圖形的形狀，但基於關鍵詞的文本過濾器無法識別。

### 1.3 Agent Smith (Self-Replicating Attacks)
- **核心機制**：單張圖片即可在多模態 Agent 系統中實現快速傳播。
- **原理**：利用多模態模型的自動化執行能力進行連鎖反應。

## 2. RAG 攻擊 (RAG-based Attacks)

RAG (Retrieval-Augmented Generation) 攻擊針對檢索環節。

### 2.1 檢索污染 (Retrieval Poisoning)
- **核心機制**：在外部知識庫中注入包含越獄指令的文檔。
- **原理**：當模型檢索到這些文檔並將其作為「可信上下文」時，越獄指令會被優先執行。

### 2.2 間接注入 (Indirect Injection)
- **核心機制**：利用模型對外部 API 或搜索結果的依賴。
- **原理**：惡意指令隱藏在正常的網頁內容中，被模型抓取後觸發。

## 3. 研究建議
- 在測試多模態模型時，應結合圖片渲染工具（如 Python PIL）生成測試樣本。
- 在 RAG 環境下，需評估模型對「外部權威信息」與「內部安全準則」衝突時的優先級處理。
