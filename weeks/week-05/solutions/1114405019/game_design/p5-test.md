# Phase 5: TurnManager 測試設計

## 1. 目標

建立 `TurnManager` 的單元測試，驗證回合管理、過牌邏輯、回合重置與玩家輪替是否正確。

## 2. 測試框架

使用 Python 標準函式庫 `unittest`，測試檔案建議命名為 `tests/test_p5.py`。

## 3. 前置條件

已完成 Phase 1~4：`Card`, `Deck`, `Hand`, `Player`, `PatternEvaluator`, `RuleEngine`。

## 4. 測試案例表格

### 4.1 TurnManager 初始化與基本狀態

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_turn_manager_init` | 建立 `TurnManager(players, rule_engine)` | `current_index==0`, `pass_count==0`, `last_play is None` |
| `test_get_current_player` | 初始化後 | 回傳 `players[0]` |
| `test_is_first_turn` | 新遊戲開始 | `True` |

### 4.2 出牌提交

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_submit_play_valid` | 合法出牌 | 回傳 `True`, `last_play` 更新, `pass_count==0` |
| `test_submit_play_invalid` | 非法出牌 | 回傳 `False`, 狀態不改變 |
| `test_submit_play_records_history` | 合法出牌 | `turn_history` 增加記錄 |

### 4.3 過牌與回合重置

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_pass_turn_increments` | 一次過牌 | `pass_count==1` |
| `test_three_passes_resets` | 連續 3 次過牌 | `last_play is None`, `pass_count==0` |
| `test_round_reset_sets_next_player` | 重置後 | `current_index` 指向原 last_play 之後玩家 |

### 4.4 轉換玩家順序

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_advance_turn` | `advance_turn()` | `current_index` 進位循環 |
| `test_advance_turn_after_play` | 出牌後 | 下一位玩家 turn |
| `test_advance_turn_after_pass` | 過牌後 | 下一位玩家 turn |

### 4.5 邊界與錯誤情境

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_submit_play_without_last_play` | `last_play is None` | 只檢查合法牌型 |
| `test_reset_round_with_no_last_play` | 無 last_play 時 | 不改變狀態 |
| `test_record_turn_with_pass` | 過牌 | `turn_history` 記錄 None |

## 5. 執行測試

```bash
cd 2026-python
python -m unittest tests.test_p5 -v
```

## 6. 結果評估

- **Red**：回合管理或過牌邏輯錯誤。
- **Green**：TurnManager 所有測試通過。
- **Refactor**：若邏輯正確，可優化狀態紀錄與重置順序。 