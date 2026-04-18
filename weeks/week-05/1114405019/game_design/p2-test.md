# Phase 2: Player 與 Hand 測試設計

## 1. 目標

建立 `Player` 與 `Hand` 的單元測試，驗證手牌管理、排序與移除邏輯是否正確。

## 2. 測試框架

使用 Python 標準函式庫 `unittest`，測試檔案建議命名為 `tests/test_p2.py`。

## 3. 前置條件

已完成 Phase 1：`Card` 與 `Deck`，且 `Hand` 可建立與排序。

## 4. 測試案例表格

### 4.1 Player 初始化

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_player_creation_human` | `Player("Alice")` | `name=="Alice"`, `is_ai==False`, `len(hand)==0` |
| `test_player_creation_ai` | `Player("Bot", is_ai=True)` | `is_ai==True`, `score==0` |

### 4.2 Hand 加牌與排序

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_hand_add_cards` | `Hand().add_cards([Card(14,3), Card(3,0)])` | `len(hand)==2` |
| `test_hand_sort_desc` | `Hand([♣3, ♠A, ♥K]).sort_desc()` | `順序: ♠A, ♥K, ♣3` |
| `test_hand_sort_with_two` | `Hand([♠2, ♣3, ♥A]).sort_desc()` | `順序: ♠2, ♥A, ♣3` |
| `test_hand_find_card_exists` | `find_card(♠A)` | 回傳 `Card(14,3)` |
| `test_hand_find_card_missing` | `find_card(♦5)` | 回傳 `None` |

### 4.3 Hand 移除與錯誤處理

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_hand_remove_cards` | `remove_cards([♠A])` | 剩餘牌數減少 1 |
| `test_hand_remove_multiple_cards` | `remove_cards([♠A, ♥K])` | 手牌僅剩指定以外牌 |
| `test_hand_remove_unknown_card` | `remove_cards([♠A])` 在手牌不存在時 | 拋出 `ValueError` |

### 4.4 Player 出牌與手牌驗證

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_player_receive_cards` | `player.receive_cards([♠A, ♣3])` | `len(player.hand)==2` |
| `test_player_sort_hand` | `player.sort_hand()` | 玩家手牌按 Big Two 排序 |
| `test_player_play_cards` | `player.play_cards([♠A])` | 回傳出牌列表、手牌張數減少 |
| `test_player_play_cards_missing` | `play_cards([♦5])` | 拋出 `ValueError` |
| `test_player_has_cards` | `has_cards([♠A, ♣3])` | `True` |
| `test_player_has_cards_partial` | `has_cards([♠A, ♥K])` | `False` |
| `test_player_reset_hand` | `reset_hand()` | `len(hand)==0` |

## 5. 邊界測試

- `add_cards([])` 應保持手牌不變。
- `remove_cards([])` 應保持手牌不變。
- `sort_hand()` 在空手牌時應該安全執行。
- `play_cards([])` 應回傳空列表且不改變手牌。

## 6. 執行測試

```bash
cd 2026-python
python -m unittest tests.test_p2 -v
```

## 7. 結果評估

- **Red**：方法未實作或錯誤。
- **Green**：所有 Player/Hand 測試通過。
- **Refactor**：若邏輯正確，可進一步調整 API 一致性與錯誤訊息。