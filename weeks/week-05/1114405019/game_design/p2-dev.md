# Phase 2: 牌型分類 - 開發設計

## 目標

實作 HandClassifier 類別，通過 Phase 2 的所有測試。

## 檔案位置

`game/classifier.py`

---

## 類別設計

### CardType 列舉

```
值：
  SINGLE = 1        # 單張
  PAIR = 2          # 對子
  TRIPLE = 3       # 三條
  STRAIGHT = 4      # 順子
  FLUSH = 5         # 同花
  FULL_HOUSE = 6    # 葫芦
  FOUR_OF_A_KIND = 7 # 四條
  STRAIGHT_FLUSH = 8 # 同花順
```

---

### HandClassifier 類別

```
靜態方法：

  _is_straight(ranks: List[int]) -> bool
    - 檢查是否為順子
    - 需處理 A-2-3-4-5 特殊情況

  _is_flush(suits: List[int]) -> bool
    - 檢查是否為同花

  classify(cards: List[Card]) -> Optional[Tuple[CardType, int, int]]
    - 分類牌型
    - 回傳 (牌型, 數字, 花色) 或 None

  compare(play1: List[Card], play2: List[Card]) -> int
    - 比較兩手牌大小
    - 回傳 1=play1大, -1=play2大, 0=平手

  can_play(last_play: Optional[List[Card]], cards: List[Card]) -> bool
    - 檢查是否可以出牌
    - 第一回合只能出3♣
```

---

## 分類邏輯

```
輸入：cards 列表

1. n == 1: 單張
2. n == 2: 若rank相同=對子
3. n == 3: 若rank相同=三條
4. n == 5:
   - 檢查同花 + 順子 => 同花順
   - 檢查4張相同 => 四條
   - 檢查3+2 => 葫芦
   - 檢查同花 => 同花
   - 檢查順子 => 順子
5. 其他: None
```

---

---

## 比較邏輯詳解

### 數字順序
```
2 > A > K > Q > J > T > 9 > 8 > 7 > 6 > 5 > 4 > 3
（rank: 15 > 14 > 13 > 12 > 11 > 10 > 9 > 8 > 7 > 6 > 5 > 4 > 3）
```

### 花色順序
```
♠ (3) > ♥ (2) > ♦ (1) > ♣ (0)
```

### 比較規則
- 同牌型：先比數字，再比花色
- 不同牌型：直接按牌型等級比較（STRAIGHT_FLUSH > ... > SINGLE）
- 五張牌型：比的是「最大的牌」（例：順子比最大的數字、同花比最大的數字）

---

## 順子檢查邏輯

```python
# 特殊情況：A-2-3-4-5 視為最小順子
# 如果牌型為 A-2-3-4-5，該順子的最大數字視為 5

# 檢查方式：
1. 對 ranks 排序
2. 檢查是否連續（每相鄰兩數差==1）
3. 特殊：如果有 A 和 2，檢查是否為 A-2-3-4-5
```

---

## 葫蘆與四條判定

```
葫蘆 (Full House)：3張相同 + 2張相同
  - 比較時用 3 張牌的 rank

四條 (Four of a Kind)：4張相同 + 1張不同
  - 比較時用 4 張牌的 rank
```

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_classifier -v
```

---

## 重構檢查清單

- [ ] 提取 _is_straight 邏輯為獨立方法
- [ ] 提取 _count_ranks 方法檢查牌數分佈
- [ ] 提取 _find_max_card 找最大牌
- [ ] 加入完整型別註解（type hints）
- [ ] 效能優化：避免重複迭代
- [ ] 加入 docstring 註解