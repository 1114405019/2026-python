# Phase 3: 牌型搜尋 - 測試設計

## 目標

實作 HandFinder 類別，找出所有可能的牌型組合。

## 測試框架

使用 Python 標準函式庫 `unittest`

## 測試檔案

`tests/test_finder.py`

---

## 測試案例設計

### 1. 單張搜尋

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
### 4. 五張牌型搜尋

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_find_straight | `[3♣,4♦,5♥,6♠,7♣,8♦]` | 至少1個順子 |
| test_find_flush | `[♣3,♣5,♣7,♣9,♣J,♠A]` | 至少1個同花 |
| test_find_fullhouse | `[♠A,♥A,♦A,♣2,♦2,♥K]` | 至少1個葫蘆 |
| test_find_fourkind | `[♠A,♥A,♦A,♣A,♦3]` | 至少1個四條 |

---

### 5. 合法出牌搜尋

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_valid_plays_first | last_play=None, hand | 只有3♣ |
| test_valid_plays_single | 上家單張, hand | 包括所有單張、對子、三條、五張 |
| test_valid_plays_pair | 上家對子, hand | 包括所有對子、三條、五張 |
| test_valid_plays_triple | 上家三條, hand | 包括所有三條、五張 |
| test_valid_plays_higher_strength | 上家對5, hand有對6對10 | 包括對6、對10但不含對5 |
| test_valid_plays_only_higher_rank | 上家♠A, hand有♠K,♥A | 只包括♥A（需比♠A大） |
| test_valid_plays_empty | 無可出牌 | 回傳空列表 |

---

## 前置條件

- 已完成 Phase 1：Card, Deck, Hand, Player
- 已完成 Phase 2：HandClassifier（分類、比較、合法性判定）

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_finder -v
```

---

## 預期結果

- **Red**: 實作前所有測試失敗
- **Green**: 清晰邏輯後通過
- **Refactor**: 優化組合與搜尋演算法

---

## 測試執行說明

### 組合數量驗證
某些測試需驗證組合數量，例：
- 4張相同 rank 的牌：C(4,2) = 6 種對子
- 找出所有三條組合：每個 rank 的三條組合只有 1 種

### 邊界情況重點
1. 手牌為空時的搜尋結果
2. 精確的牌型組合數計算
3. 多個相同 rank 時的組合生成
4. 順子的連續性檢查（包括 A-2-3-4-5 特殊情況）
| test_find_straight | 有順子牌型 | 有順子 |
| test_find_flush | 有同花牌型 | 有同花 |
| test_find_full_house | 有葫芦牌型 | 有葫芦 |
| test_find_four_of_a_kind | 有四條牌型 | 有四條 |
| test_find_straight_flush | 有同花順牌型 | 有同花順 |

---

### 5. 合法出牌搜尋

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_first_turn | hand有3♣, last=None | 只能出3♣ |
| test_with_last_single | last=單5 | 只回單張 |
| test_with_last_pair | last=對5 | 只回對子 |
| test_no_valid | 無法大於上家 | 空清單 |

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_finder -v
```

---

## 預期結果

- **Red**: 測試失敗
- **Green**: 實作後通過
- **Refactor**: 重構