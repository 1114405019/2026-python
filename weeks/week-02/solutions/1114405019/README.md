# Week 02 作業 (1114405019)

## 完成題目
- Task 1: Sequence Clean
- Task 2: Student Ranking
- Task 3: Log Summary

## 執行與測試方式
* Python 版本：Python 3.11 (或以上)
* 程式執行指令範例：`python task1_sequence_clean.py`
* 測試執行指令：`$env:PYTHONPATH = "."; python -m unittest discover -s tests -p "test_*.py" -v`

## 資料結構選擇理由
* **Task 1**: 使用 `dict.fromkeys()` 來去重，因為它在 Python 3.7+ 保證維持插入順序，比用 `set` 再排序更直接且效能更好。
* **Task 2**: 直接使用內建的 `list` 與 `tuple`，配合 `sorted` 的多條件 `lambda` 排序，語法簡潔且能完美處理同分同齡的狀況。
* **Task 3**: 使用 `collections.Counter`，因為它是專門用來計數的資料結構，比起 `defaultdict(int)` 能少寫很多行程式碼，且內建 `most_common()` 找最大值非常方便。

## 遇到的錯誤與修正方式
* **錯誤**：在執行 `test_task1.py` 時遇到 `ModuleNotFoundError`，因為 Python 找不到上一層目錄的模組。
* **修正**：在測試檔案開頭加入 `sys.path.append(...)` 強制將父目錄加入環境變數，或是在執行時加上 `$env:PYTHONPATH = "."` 解決。

## TDD (Red → Green → Refactor) 摘要
* **Task 1**: 先寫了包含去重與排序的測試 (Red)，接著實作 `dict.fromkeys` 與 `sorted` (Green)，最後優化變數命名使回傳值更清晰 (Refactor)。
* **Task 2**: 先準備了包含同分、同齡的邊界測資 (Red)，接著寫出多條件的 `lambda x: (-x[1], x[2], x[0])` (Green)，確認穩定排序無誤。
* **Task 3**: 先寫了空紀錄與一般紀錄的測試 (Red)，接著導入 `Counter` 完成統計與次數降序邏輯 (Green)，再拆分出找全域最常見動作的邏輯 (Refactor)。