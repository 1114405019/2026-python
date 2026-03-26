# Phase 4: AI 策略 - 測試設計

## 目標

實作 AIStrategy 類別，使用貪心演算法選擇最佳出牌。

## 測試框架

使用 Python 標準函式庫 `unittest`

## 測試檔案

`tests/test_ai.py`

---

## 測試案例設計

### 1. 評分函數

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_score_single | 單張♠A, hand有2張 | 分數 = 1×100 + 14×10 = 240 |
| test_score_pair_higher | 對子 vs 單張 | 對子分數 > 單張分數 |
| test_score_triple_higher | 三條 vs 對子 | 三條分數 > 對子分數 |
| test_score_near_empty | 剩1張時出牌 | 分數 > 10000 |
| test_score_low_cards | 剩2張時出牌 | 分數 > 500 |
| test_score_spade_bonus | 出♠牌 | 分數額外+5 |

---

### 2. 選擇最佳

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_select_best | 合法出牌[單張,對子] | 選擇對子 |
| test_select_first_turn | 第一回合選項 | 只能選3♣ |
| test_select_empty | 無合法出牌 | 回傳None |

---

## 前置條件

- 已完成 Phase 1：Card, Deck, Hand, Player
- 已完成 Phase 2：HandClassifier
- 已完成 Phase 3：HandFinder

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_ai -v
```

---

## 預期結果

- **Red**: 實作前所有測試失敗
- **Green**: 清晰邏輯後通過
- **Refactor**: 優化評分常數與策略

---

## 測試執行說明

### 評分公式驗證
確認評分計算：
```
score = TYPE_SCORE[type] * 100 + rank_score * 10 + 加分項目
```

### 策略驗證
1. 第一回合強制 3♣
2. 無合法出牌時回傳 None（表示過牌）
3. 多個有效出牌時選擇分數最高者

### 邊界情況
1. 只有 1 張牌剩下時的出牌選擇（應優先出完）
2. 多個同分出牌時的決策（可選擇排序規則）
3. 無任何可出牌時的回傳值

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_ai -v
```

---

## 預期結果

- **Red**: 測試失敗
- **Green**: 實作後通過
- **Refactor**: 重構