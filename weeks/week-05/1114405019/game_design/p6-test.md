# Phase 6: GameController 測試設計

## 1. 目標

建立 `GameController` 的單元測試與基本整合測試，驗證主遊戲流程、勝負判定與分數更新。

## 2. 測試框架

使用 Python 標準函式庫 `unittest`，測試檔案建議命名為 `tests/test_p6.py`。

## 3. 前置條件

已完成 Phase 1~5：`Card`, `Deck`, `Hand`, `Player`, `PatternEvaluator`, `RuleEngine`, `TurnManager`。

## 4. 測試案例表格

### 4.1 遊戲初始設定

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_setup_game_creates_players` | `GameController(['A','B'], [False, True])` | 兩位玩家建立 | 
| `test_setup_game_deals_cards` | `setup_game()` | 每位玩家獲得 13 張牌 |
| `test_setup_game_initial_turn` | `setup_game()` | `current_player` 為持有 `3♣` 的玩家 |

### 4.2 主流程執行

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_play_turn_valid` | 玩家合法出牌 | 回傳 `True`, 牌從手牌移除 |
| `test_play_turn_invalid` | 非法出牌 | 回傳 `False`, 狀態不變 |
| `test_handle_pass` | 玩家過牌 | 觸發 `TurnManager` 過牌行為 |
| `test_evaluate_winner` | 玩家手牌空 | 傳回 `winner`, `game_over=True` |

### 4.3 分數與重置

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_update_scores_on_win` | 勝者出完牌 | 分數更新 |
| `test_restart_game` | 完成一局後重新啟動 | `game_over=False`, 重新發牌 |

### 4.4 狀態查詢

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_get_game_state` | 遊戲進行中 | 回傳包含 `current_player`, `last_play`, `scores` |
| `test_is_game_over` | 有勝者 | `True` |
| `test_is_game_over_when_no_win` | 尚未分出勝負 | `False` |

### 4.5 邊界與整合情境

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_play_turn_after_game_over` | 遊戲結束後出牌 | 不接受新操作 |
| `test_ai_and_human_sequence` | 模擬 AI 與人類出牌流程 | 回合正確輪替 |
| `test_game_state_without_ui` | 非 UI 呼叫 | 正常回傳可序列化狀態 |

## 5. 執行測試

```bash
cd 2026-python
python -m unittest tests.test_p6 -v
```

## 6. 結果評估

- **Red**：主遊戲流程或勝負判定錯誤。
- **Green**：GameController 所有測試通過。
- **Refactor**：若流程正確，可進一步拆分 `play_turn()` 內部邏輯。 