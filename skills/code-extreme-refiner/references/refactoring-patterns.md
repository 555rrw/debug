# 程式碼精煉模式

本文件收錄了 `code-extreme-refiner` 技能在進行程式碼精煉時應用的常見模式，旨在協助 Agent 透過這些模式，在不犧牲功能與品質的前提下，將程式碼精簡化。

## 1. 提早回傳 (Early Return)

**描述**：在函數或方法開始時，優先處理特殊情況或無效輸入，並立即返回結果。這有助於減少巢狀 `if-else` 結構，使主邏輯更清晰。

**範例**：

**原始程式碼**：
```javascript
function processData(data) {
  if (data !== null && data !== undefined) {
    if (data.isValid) {
      // 處理有效數據
      return result;
    } else {
      // 處理無效數據
      return errorResult;
    }
  } else {
    return defaultResult;
  }
}
```

**精煉後**：
```javascript
function processData(data) {
  if (!data) return defaultResult; // 提早回傳無效數據
  if (!data.isValid) return errorResult; // 提早回傳無效數據
  // 處理有效數據
  return result;
}
```

## 2. 可選鏈 (Optional Chaining) - 適用於支援的語言

**描述**：允許在存取物件深層屬性時，如果路徑中的某個屬性為 `null` 或 `undefined`，則表達式會短路並返回 `undefined`，而不會拋出錯誤。這可以簡化多層次的 `null` 或 `undefined` 檢查。

**範例**：

**原始程式碼**：
```javascript
const userName = user && user.profile && user.profile.name;
```

**精煉後**：
```javascript
const userName = user?.profile?.name;
```

## 3. 空值合併運算符 (Nullish Coalescing Operator) - 適用於支援的語言

**描述**：當左側運算元為 `null` 或 `undefined` 時，返回右側運算元；否則返回左側運算元。這與 `||` 運算符不同，`||` 會在左側為任何假值（例如 `0`, `''`, `false`）時返回右側。

**範例**：

**原始程式碼**：
```javascript
const configValue = userConfig !== null && userConfig !== undefined ? userConfig : defaultValue;
// 或使用 || 運算符，但會將 0, '', false 視為預設值
const configValue = userConfig || defaultValue;
```

**精煉後**：
```javascript
const configValue = userConfig ?? defaultValue;
```

## 4. 條件式簡化與布林邏輯

**描述**：利用布林邏輯的特性，簡化複雜的條件判斷式，移除不必要的 `if-else` 結構。

**範例**：

**原始程式碼**：
```javascript
function isEligible(age, hasLicense) {
  if (age >= 18) {
    if (hasLicense === true) {
      return true;
    } else {
      return false;
    }
  } else {
    return false;
  }
}
```

**精煉後**：
```javascript
function isEligible(age, hasLicense) {
  return age >= 18 && hasLicense;
}
```

## 5. 函數式編程技巧 (Functional Programming Techniques)

**描述**：利用高階函數（如 `map`, `filter`, `reduce`）和不可變數據結構來處理集合，減少副作用，使程式碼更具表達性和簡潔性。

**範例**：

**原始程式碼**：
```javascript
const numbers = [1, 2, 3, 4, 5];
const evenNumbers = [];
for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] % 2 === 0) {
    evenNumbers.push(numbers[i] * 2);
  }
}
```

**精煉後**：
```javascript
const numbers = [1, 2, 3, 4, 5];
const evenNumbers = numbers.filter(num => num % 2 === 0).map(num => num * 2);
```

## 6. 移除不必要的抽象

**描述**：當抽象層次過多，反而增加了程式碼的複雜度和理解成本時，應考慮移除這些不必要的抽象，直接實現功能。

**範例**：

**原始程式碼**：
```javascript
class Calculator {
  constructor() {
    this.result = 0;
  }

  add(num) {
    this.result += num;
    return this;
  }

  getResult() {
    return this.result;
  }
}

const calc = new Calculator();
const finalResult = calc.add(5).add(10).getResult();
```

**精煉後**：
```javascript
function add(a, b) {
  return a + b;
}

const finalResult = add(add(0, 5), 10);
```

這些模式並非獨立存在，Agent 應根據具體情況靈活組合應用，以達到最佳的精煉效果。
