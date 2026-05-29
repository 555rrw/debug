# 代理式系統與工具 (Agentic Systems & Tools)

## MCP (Model Context Protocol) 2.0

-   **功能**：OAuth 2.1 認證、可串流 HTTP、動態資源發現。
-   **作用**：解決「工具過多」問題，實現標準化的工具/資源整合。

## 代理式編碼 (Agentic Coding)

-   **CLAUDE.md Manifest**：用於注入專案上下文，指導代理編碼行為。
-   **編碼循環**：Scaffold-Implement-Verify (支架-實作-驗證) 模式。

## 電腦使用 (Computer-Use)

-   **功能**：基於螢幕截圖的 GUI 控制 (模擬滑鼠、鍵盤輸入)。
-   **安全性**：沙盒化 (Sandboxing) 環境 + 螢幕截圖驗證。

## 框架 (Frameworks)

-   **LangGraph**：用於有狀態的代理循環編排。
-   **DSPy**：透過可優化模組而非手動提示來編程 LLM。
-   **Pydantic AI**：用於結構化輸出和模型驗證。
