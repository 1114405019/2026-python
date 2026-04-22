# Phase 4: RuleEngine 測試設計

## 1. 目標

建立 `RuleEngine` 的單元測試，驗證合法出牌邏輯與同牌型比較是否正確。

## 2. 測試框架

使用 Python 標準函式庫 `unittest`，測試檔案建議命名為 `tests/test_p4.py`。

## 3. 前置條件

已完成 Phase 1~3：`Card`, `Deck`, `Hand`, `Player`, `PatternEvaluator`。

## 4. 測試案例表格

### 4.1 合法性判斷

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_is_legal_play_single_first_turn` | `last_play=None`, `play=[♣3]`, `is_first_turn=True` | `True` |
| `test_is_legal_play_non_first_single` | `last_play=None`, `play=[♠A]` | `True` |
| `test_is_legal_play_first_turn_invalid` | `last_play=None`, `play=[♠A]`, `is_first_turn=True` | `False` |
| `test_is_legal_play_same_type_higher` | `last_play=[♣5]`, `play=[♦6]` | `True` |
| `test_is_legal_play_same_type_lower` | `last_play=[♣K]`, `play=[♥Q]` | `False` |
| `test_is_legal_play_different_type_same_size` | `last_play=[♣3,♦3]`, `play=[♣4,♦4]` | `True` |
| `test_is_legal_play_different_type_invalid` | `last_play=[♣3,♦3]`, `play=[♣4,♦4,♥4]` | `False` |

### 4.2 比較函數

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_compare_plays_single_rank` | `play_a=[♠A]`, `play_b=[♠K]` | `1` |
| `test_compare_plays_single_suit` | `play_a=[♠A]`, `play_b=[♥A]` | `1` |
| `test_compare_plays_pair` | `play_a=[♣A,♦A]`, `play_b=[♣K,♦K]` | `1` |
| `test_compare_plays_straight` | `play_a=[♣4,♦5,♥6,♠7,♣8]`, `play_b=[♣3,♦4,♥5,♠6,♣7]` | `1` |
| `test_compare_plays_same_strength` | `play_a=[♠A]`, `play_b=[♥A]` | `1` |
| `test_compare_plays_equal` | 同樣牌型同樣大小 | `0` |

### 4.3 邊界與錯誤情境

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_invalid_play_unclassified` | `play=[♠A,♥K,♣3]` | `False` |
| `test_compare_different_pattern_types` | `play_a=[♠A]`, `play_b=[♣3,♦3]` | 可以比較，但依應用可回傳 `-1` 或 `TypeError`（建議選擇一致處理） |
| `test_play_requires_same_card_count` | `last_play=[♣3,♦3]`, `play=[♣4]` | `False` |

## 5. 執行測試

```bash
cd 2026-python
python -m unittest tests.test_p4 -v
```

## 6. 結果評估

- **Red**：牌型比較或合法性規則錯誤。
- **Green**：RuleEngine 所有測試通過。
- **Refactor**：若邏輯正確，可優化錯誤訊息與比較簽章。 