# Phase 1: Card 與 Deck 單元測試設計

## 1. 目標

建立 `Card` 與 `Deck` 的單元測試，驗證 Big Two 基礎資料模型、牌權重以及發牌行為。

## 2. 測試框架

使用 Python 標準函式庫 `unittest`，測試檔案建議命名為 `tests/test_p1.py`。

## 3. 測試案例表格

### 3.1 Card 類別

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_card_creation` | 建立 `Card(rank=14, suit=3)` | `rank==14`, `suit==3` |
| `test_card_repr` | `repr(Card(14,3))` | `"♠A"` |
| `test_card_repr_ten` | `repr(Card(10,1))` | `"♦10"` |
| `test_card_rank_order` | `Card(15,0)` vs `Card(14,3)` | `2 > A` |
| `test_card_same_rank_suit_order` | `Card(14,3)` vs `Card(14,2)` | `♠ > ♥` |
| `test_card_same_rank_different_suits` | `Card(3,3)` vs `Card(3,0)` | `♠3 > ♣3` |
| `test_card_equality` | `Card(12,2) == Card(12,2)` | `True` |
| `test_card_hashable` | `set([Card(12,2), Card(12,2)])` | `len==1` |
| `test_card_sort_key` | `Card(15,1).to_sort_key()` | `(15,1)` |

### 3.2 Deck 類別

| 測試名稱 | 場景 | 期望結果 |
|---|---|---|
| `test_deck_initial_count` | 建立 `Deck()` | `len(deck.cards)==52` |
| `test_deck_unique_cards` | `set(deck.cards)` | `len==52` |
| `test_deck_complete_ranks` | 讀取所有牌的 `rank` | 包含 `3..15` |
| `test_deck_complete_suits` | 讀取所有牌的 `suit` | 包含 `0..3` |
| `test_deck_shuffle_changes_order` | `deck.shuffle(seed=42)` | 卡片順序改變，但集合相等 |
| `test_deck_shuffle_preserves_cards` | 洗牌前後 `set(deck.cards)` | 完整集合不變 |
| `test_deal_count_reduces_deck` | `deck.deal(5)` | 回傳 5 張，`remaining()==47` |
| `test_deal_zero_cards` | `deck.deal(0)` | 回傳空列表，`remaining()==52` |
| `test_deal_all_cards` | `deck.deal(52)` | 回傳 52 張，`remaining()==0` |
| `test_deal_more_than_available` | `deck.deal(60)` | 回傳剩餘 52 張，`remaining()==0` |
| `test_deal_multiple_rounds` | `deck.deal(5)` 再 `deal(3)` | `remaining()==44` |

## 4. 邊界與錯誤情境測試

- `deal(0)` 應回傳空列表，不應改變牌堆。
- `deal(count)` 若 `count > remaining()`，應回傳所有剩餘牌且不拋出例外。
- `shuffle(seed)` 應支援可重複的測試結果。
- `Card` 比較應在相同 `rank` 時正確應用花色權重。

## 5. 推薦測試內容

- 檢查 `Card` 的 `2` 是否為最大值。
- 檢查 `Deck` 是否含有完整 52 張且無重複。
- 檢查洗牌不改變牌的總集合。
- 檢查連續多次發牌後剩餘張數正常。

## 6. 執行測試

```bash
cd 2026-python
python -m unittest tests.test_p1 -v
```

---

## 7. 結果評估

- **Red**：尚未實作或失敗。
- **Green**：通過所有 Phase 1 測試。
- **Refactor**：若實作正確，進行類別邊界或排序邏輯優化。 