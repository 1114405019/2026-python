# Phase 3: PatternEvaluator 測試設計

## 1. 目標

建立 `PatternEvaluator` 的單元測試，驗證牌型分類、特徵萃取與合法性判斷。

## 2. 測試框架

使用 Python 標準函式庫 `unittest`，測試檔案建議命名為 `tests/test_p3.py`。

## 3. 前置條件

已完成 Phase 1 與 Phase 2：`Card`、`Deck`、`Hand`、`Player`、`Card` 比較與手牌管理。

## 4. 測試案例表格

### 4.1 PatternType 與 PatternResult

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_pattern_type_enum` | 讀取 `PatternType` | 包含 `SINGLE, PAIR, TRIPLE, STRAIGHT, FLUSH, FULL_HOUSE, FOUR_OF_A_KIND, STRAIGHT_FLUSH` |
| `test_pattern_result_signature` | `classify([♠A])` | `PatternResult(pattern_type=SINGLE, primary_rank=14, high_suit=3)` |

### 4.2 單張/對子/三條驗證

| 測試名稱 | 輸入 | 期望結果 |
|---|---|---|
| `test_is_single` | `[♠A]` | `True` |
| `test_is_pair` | `[♠A,♥A]` | `True` |
| `test_is_pair_diff_rank` | `[♠A,♠K]` | `False` |
| `test_is_triple` | `[♠A,♥A,♦A]` | `True` |
| `test_is_triple_invalid` | `[♠A,♥A,♣3]` | `False` |

### 4.3 5 張基本牌型分類

| 測試名稱 | 輸入 | 期望結果 |
|---|---|---|
| `test_is_flush` | `[♣3,♣5,♣7,♣9,♣J]` | `True` |
| `test_is_straight` | `[♣3,♦4,♥5,♠6,♣7]` | `True` |
| `test_is_straight_ace_two_low` | `[♣A,♦2,♥3,♠4,♣5]` | `True` |
| `test_is_full_house` | `[♠A,♥A,♦A,♣2,♦2]` | `True` |
| `test_is_four_of_a_kind` | `[♠A,♥A,♦A,♣A,♦3]` | `True` |
| `test_is_straight_flush` | `[♣3,♣4,♣5,♣6,♣7]` | `True` |

### 4.4 牌型判斷與特徵提取

| 測試名稱 | 輸入 | 期望結果 |
|---|---|---|
| `test_classify_single` | `[♠A]` | `SINGLE` |
| `test_classify_pair` | `[♠A,♥A]` | `PAIR` |
| `test_classify_triple` | `[♠A,♥A,♦A]` | `TRIPLE` |
| `test_classify_straight_flush` | `[♣3,♣4,♣5,♣6,♣7]` | `STRAIGHT_FLUSH` |
| `test_classify_ace_two_straight` | `[♣A,♦2,♥3,♠4,♣5]` | `STRAIGHT` |
| `test_classify_invalid_shape` | `[♠A,♥K,♦Q]` | `None` |

### 4.5 邊界與錯誤情境

| 測試名稱 | 輸入 | 期望結果 |
|---|---|---|
| `test_empty_cards` | `[]` | `False` / `None` |
| `test_invalid_five_card_sequence` | `[♣3,♦4,♥5,♠6,♣8]` | `False` / `None` |
| `test_duplicate_cards_invalid` | `[♠A,♠A]` | `False` / `None` |
| `test_pattern_signature_for_full_house` | `[♠A,♥A,♦A,♣2,♦2]` | `(FULL_HOUSE, 14, 2)` |

## 5. 執行測試

```bash
cd 2026-python
python -m unittest tests.test_p3 -v
```

## 6. 結果評估

- **Red**：類別未實作或模式判斷錯誤
- **Green**：所有 PatternEvaluator 測試通過
- **Refactor**：若判斷正確，可優化 `classify()` 與 `get_pattern_signature()` 的結構