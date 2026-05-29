# 安全性與多租戶 (Security & Multi-Tenancy)

## 隔離策略 (Isolation)

-   **命名空間隔離 (Namespace Isolation)**：共享資料庫。
-   **物理隔離 (Physical Isolation)**：專用 Pods。

## 安全性措施 (Security)

-   **提示注入防禦 (Prompt Injection Defense)**：淨化 (Sanitization) + 分類器 (Classifiers)。
-   **PII 過濾 (PII Filtering)**：對輸出進行個人身份資訊過濾。

## 存取控制 (Access Control)

-   **RBAC/ABAC**：在資料庫查詢層級整合 (例如：`WHERE tenant_id = X`)。
