# 自訂測試案例表

| 測試類型 | 測資輸入 | 預期輸出 | 實際輸出 | 結果 | 對應測試函式 | 關鍵修改點 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1. 一般情況** (Task 1) | `5 3 5 2` | dedupe: `5 3 2` | dedupe: `5 3 2` | PASS | `tests/test_task1.py::test_normal_case` | 確認去重邏輯正確運作。 |
| **2. 邊界情況** (Task 3) | 空輸入 (0筆紀錄) | `[]`, `None`, `0` | `[]`, `None`, `0` | PASS | `tests/test_task3.py::test_empty_log` | 在函式開頭加上 `if not logs: return` 提早結束。 |
| **3. 同分排序** (Task 2) | `amy 88 20`, `bob 88 19`, `ian 88 19` | `bob`, `ian`, `amy` | `bob`, `ian`, `amy` | PASS | `tests/test_task2.py::test_ranking_logic` | 將 lambda 排序條件精確設定為 `(-score, age, name)`。 |
| **4. 反例/陷阱** (Task 1) | `2 4 6 8` (全偶數) | evens: `2 4 6 8` | evens: `2 4 6 8` | PASS | `tests/test_task1.py::test_normal_case` | 確保 list comprehension `x % 2 == 0` 能完整保留原陣列。 |
| **5. 最易出錯** (Task 3) | 兩位 user 次數相同 | 依名字字母序排列 | 依名字字母序排列 | PASS | `tests/test_task3.py::test_log_summary` | 在 Counter 排序時加上第二條件 `x[0]` 確保名稱升序。 |