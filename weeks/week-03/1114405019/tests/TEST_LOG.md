# TEST_LOG

## 測試指令

```
python -m unittest test_robot_core.py -v
```

## 第一次測試（Red）

- 目的：模擬故意少寫一個旋轉邏輯造成失敗。
- 結果摘要：
  - `test_rotate_four_times_right_returns_to_north` 失敗
  - 其餘測試可能通過，但整體狀態判定為 FAIL
- 失敗原因：`R` 連續執行 4 次後，機器人未回到 `N`，表示旋轉環節存在 bug。

## 第二次測試（Green）

- 目的：確認目前實作是否通過全部 12 個測試。
- 結果摘要：
  - 12 個測試全部通過
  - `OK`
- 核心通過項目：方向旋轉、邊界判定、LOST 行為、scent 方向區分、LOST 後停止執行。
