# 遊戲資料庫 API 參考

## RAWG API
- **官網**: https://rawg.io/apidocs
- **主要端點**:
  - `/games`: 搜尋與列表
  - `/games/{id}`: 詳細資訊
  - `/platforms`: 平台列表
  - `/genres`: 類型列表
- **限制**: 免費版每月 20,000 次請求。

## IGDB API (Twitch)
- **官網**: https://api-docs.igdb.com/
- **驗證方式**: OAuth2 (Client ID & Client Secret)
- **主要端點**:
  - `/games`: 遊戲主體
  - `/involved_companies`: 開發商與發行商
  - `/release_dates`: 發行日期
- **查詢語言**: 使用專屬的 Apicalypse 語法。

## Steam Web API
- **官網**: https://steamcommunity.com/dev
- **常用端點**:
  - `GetAppList`: 獲取所有遊戲 ID
  - `appdetails`: 獲取特定遊戲細節 (https://store.steampowered.com/api/appdetails?appids={id})
