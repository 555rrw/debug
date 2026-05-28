# 程式碼精煉範例

本文件收錄了 `code-extreme-refiner` 技能的程式碼精煉範例，展示了如何將臃腫的程式碼轉換為極致精煉、可讀性高且功能等效的版本。這些範例將作為 Agent 學習和參考的基準。

## 範例一：資料清理 / 判斷狀態 (JavaScript)

### 原始程式碼 (臃腫版本)

這是一個典型的巢狀 `if-else` 結構，導致程式碼難以閱讀和維護。

```javascript
function getUserStatus(user) {
  if (user === null || user === undefined) {
    return "unknown";
  }

  if (user.active === true) {
    if (user.banned === true) {
      return "banned";
    } else {
      if (user.emailVerified === true) {
        return "active";
      } else {
        return "pending";
      }
    }
  } else {
    if (user.banned === true) {
      return "banned";
    } else {
      return "inactive";
    }
  }
}
```

### 精煉後程式碼 (極致精煉版本)

此版本採用了「提早回傳 (Early Return)」模式，優先處理最明確、最優先的條件，大大減少了巢狀層次，提升了可讀性。

```javascript
function getUserStatus(user) {
  if (!user) return "unknown";
  if (user.banned) return "banned";
  if (!user.active) return "inactive";
  return user.emailVerified ? "active" : "pending";
}
```

### 核心差異與精煉原則

*   **消除巢狀**：原始版本中多層次的 `if-else` 巢狀結構被完全消除。
*   **提早回傳 (Early Return)**：精煉版優先處理了 `user` 為空、`user.banned` 為真、`user.active` 為假等明確條件，並立即返回結果，避免了不必要的後續判斷。
*   **布林簡寫**：利用 JavaScript 的真值/假值特性，將 `user === null || user === undefined` 簡化為 `!user`，將 `user.banned === true` 簡化為 `user.banned`。
*   **三元運算子**：最後的判斷 `user.emailVerified ? "active" : "pending"` 簡潔地表達了兩種狀態的選擇。

**精煉目標**：在保持功能完全正常的情況下，使程式碼更簡潔、可讀，並清除因過度巢狀和冗餘判斷造成的技術債。
