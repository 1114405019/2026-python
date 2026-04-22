# Week 03（115/03/09－115/03/15）

- 主題：字串處理：正規表達式、文字解析、加密與頻率
- 解題：[100](./QUESTION-100.md) | [118](./QUESTION-118.md) | [272](./QUESTION-272.md) | [299](./QUESTION-299.md) | [490](./QUESTION-490.md)
- 作業：完成 5 題並提交到 `weeks/week-03/solutions/<student-id>/`
- 進階作業（pygame）：[HOMEWORK.md](./HOMEWORK.md)

---

## 解題清單

| # | 題名 | 難度 | 題目檔 |
|---|------|------|------|
| 100 | UVA 100 | ⭐ | [QUESTION-100.md](./QUESTION-100.md) |
| 118 | UVA 118 | ⭐ | [QUESTION-118.md](./QUESTION-118.md) |
| 272 | UVA 272 | ⭐ | [QUESTION-272.md](./QUESTION-272.md) |
| 299 | UVA 299 | ⭐ | [QUESTION-299.md](./QUESTION-299.md) |
| 490 | UVA 490 | ⭐ | [QUESTION-490.md](./QUESTION-490.md) |


## Pygame MVP 功能清單

- 支援 `L/R/F` 指令操作機器人
- `scent` 會記錄掉落前的位置與方向
- 越界時顯示 `LOST` 並保留當前座標
- `N` 鍵可重置新機器人，保留已記錄的 scent
- `C` 鍵可清除所有 scent
- HUD 顯示機器人座標、方向、LOST 狀態與 scent 數量

## 資料結構說明

`scent` 選擇使用 `set`，原因如下：

- `set` 可以快速判斷同一個位置與方向是否已經標記過
- 除去重複記錄，避免重複 scent 相同資料
- 查詢速度為 O(1)，適合多次前進判斷是否應該忽略危險指令

## Gameplay 截圖

![gameplay](assets/gameplay.png)


## AI 使用方式

1. 讀 {問題說明} 設計一版針對該問題的 python unit-test 程式，並加上繁體中文的註解放到 {指定目錄} 中
2. 幫我寫一版 python 程式，並跑完測試，並保留測試紀錄
3. 幫我加上繁體中文的註解說明
4. 有更簡單、更容易記憶的方式來寫這個程式，在檔名後加上 `-easy`
5. 幫我加上繁體中文的詳細註解說明

## 今天任務

因為 CPE 是要當場打程式設計出來，所以請手動把簡單版本程式在 `week-#/solutions/{學號}` 中打一遍你的程式，並進行測試。

以下是送出標準
- 參考 [GITHUB_WORKFLOW](GITHUB_WORKFLOW.md) 將程式 PR 出來
- 內容 (2 程式、1 測試 及 LOG 資料)要包括：
   - AI 教你的簡單版本，有中文註解
   - 你手打的程式
   - 測試程式
   - 你手打程式的測試 LOG 記錄