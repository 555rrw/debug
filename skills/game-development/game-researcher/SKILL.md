---
name: game-researcher
description: 查詢成功遊戲案例、爬取遊戲資料庫（如 RAWG, IGDB, Steam），並分析遊戲機制與市場趨勢，以輔助遊戲設計與製作。當使用者需要研究特定類型遊戲、尋找靈感或分析競爭對手時使用。
---

# Game Researcher

此技能協助 Manus 成為專業的遊戲研究員。透過存取全球領先的遊戲資料庫，你可以獲取詳細的遊戲中繼資料、評分、玩家評論及市場表現，並將其轉化為可執行的遊戲設計建議。

## 核心工作流程

### 1. 遊戲資料查詢與檢索
當需要獲取遊戲資訊時，優先考慮以下來源：
- **RAWG API**: 適用於獲取遊戲基本資訊、評分、相似遊戲推薦及跨平台資料。
- **IGDB (Twitch)**: 適用於深入的遊戲分類、開發者關係及詳細的發行日期。
- **SteamDB/Steam Web API**: 適用於分析 PC 遊戲的在線人數、價格變動及玩家標籤。

### 2. 成功案例分析
分析一款「成功」遊戲時，應關注：
- **核心玩法 (Core Loop)**: 玩家重複執行的主要動作。
- **獲利模式 (Monetization)**: 是買斷制、內購 (IAP) 還是訂閱制？
- **玩家反饋**: 從 Metacritic 或 Steam 評論中提取優點與痛點。
- **市場定位**: 該遊戲填補了哪個市場空白？

### 3. 遊戲製作輔助
利用蒐集到的資料：
- **競品對照表**: 建立功能對比矩陣。
- **機制拆解**: 參考成功案例設計數值平衡或關卡結構。
- **趨勢預測**: 根據近期熱門標籤建議遊戲方向。

## 推薦工具與 API 使用指南

### RAWG API 快速參考
- **搜尋遊戲**: `GET https://api.rawg.io/api/games?search={query}&key={YOUR_API_KEY}`
- **熱門遊戲**: `GET https://api.rawg.io/api/games?ordering=-added&key={YOUR_API_KEY}`
- **特定年份高分作品**: `GET https://api.rawg.io/api/games?dates={year}-01-01,{year}-12-31&ordering=-rating&key={YOUR_API_KEY}`

### IGDB 查詢範例 (使用 POST)
- **獲取前 10 名遊戲**: `fields name, rating; limit 10; sort rating desc;`
- **搜尋特定遊戲**: `search "Game Title"; fields *;`

## 輸出格式規範
當為使用者提供研究報告時，應包含：
1. **概覽表格**: 包含遊戲名稱、類型、評分及主要發行平台。
2. **核心特色分析**: 以條列方式總結該遊戲成功的關鍵。
3. **對使用者的建議**: 針對使用者正在開發的遊戲提供具體改進建議。
