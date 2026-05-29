# 學術 API 參考

## arXiv API
- **用途**：獲取物理、數學、電腦科學等領域的開放獲取論文。
- **限制**：每秒請求不宜過多，建議間隔 1 秒。
- **欄位**：
  - `title`: 論文標題
  - `summary`: 摘要
  - `pdf_url`: PDF 下載連結
  - `published`: 發布日期

## Semantic Scholar API (預留)
- **用途**：獲取更廣泛的學術引文數據。
- **網址**：`https://api.semanticscholar.org/v1/paper/{id}`

## Canva 整合建議
- 目前透過生成結構化的 JSON 資料，讓使用者可以利用 Canva 的「批量建立」功能或匯入 PPT 檔案來完成設計。
- 支援的欄位：`Header`, `Content`, `Image_Description`
