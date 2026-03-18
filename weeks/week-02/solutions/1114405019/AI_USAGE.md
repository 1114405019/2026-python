# AI 使用紀錄

## 詢問的問題
1. 如何在 Python 中對 list 進行去重，但同時保留原始順序？
2. `unittest` 執行時遇到 `ModuleNotFoundError` 找不到模組該怎麼解決？
3. 如何在 `sorted` 函式中設定多個排序條件（例如先降序、再升序）？

## 採用的建議
* AI 建議我在 Task 1 使用 `dict.fromkeys(nums)` 來去重，實測發現語法非常簡潔且確實能保留順序。
* AI 建議我透過在終端機加上 `$env:PYTHONPATH = "."` 來解決 Windows 環境下路徑找不到的問題，成功讓測試跑出 Green。

## 拒絕的建議
* AI 一開始在 Task 3 給了我用 `defaultdict(int)` 再手動跑迴圈的寫法，但我認為這樣程式碼太長，所以我拒絕了，改請 AI 提供用 `collections.Counter` 的精簡版本。

## AI 誤導與修正案例
* AI 曾建議我用 `set(nums)` 來做去重，但我知道 `set` 是一種無序的哈希表結構，會導致後面的順序全部亂掉，造成測試失敗 (Red)。我自行查閱資料後，將其修正為 `dict.fromkeys()` 確保通過測試。