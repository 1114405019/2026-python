# Phase 3: 牌型搜尋 - 開發設計

## 目標

實作 HandFinder 類別，通過 Phase 3 的所有測試。

## 檔案位置

`game/finder.py`

---

## 類別設計

### HandFinder 類別

```
靜態方法：

  find_singles(hand: Hand) -> List[List[Card]]
    - 回傳 [[card1], [card2], ...]

  find_pairs(hand: Hand) -> List[List[Card]]
    - 使用 combinations 找相同 rank 的2張組合

  find_triples(hand: Hand) -> List[List[Card]]
    - 使用 combinations 找相同 rank 的3張組合

  find_fives(hand: Hand) -> List[List[Card]]
    - 找順子、同花、葫芦、四條、同花順

  _find_straight_from(hand: Hand, start_rank: int) -> Optional[List[Card]]
    - 從指定 rank 找順子

  get_all_valid_plays(hand: Hand, last_play: Optional[List[Card]]) -> List[List[Card]]
    - 根據上家的牌型，回傳所有合法出牌
```

---

## 演算法重點

### 找對子
```
1. 對每個 rank (3-14)
2. 找相同 rank 的牌
3. 使用 combinations(相同牌, 2) 產生所有組合
```

### 找順子
```
1. 對每個可能開始的 rank (3-11)
2. 檢查是否有 5 張連續的牌
3. 處理 A-2-3-4-5 特殊情況（從 A 開始）
4. 返回找到的所有順子組合
```

### 找五張牌型
```
優先級順序（從高到低）：
1. 同花順 (STRAIGHT_FLUSH)
2. 四條 (FOUR_OF_A_KIND)
3. 葫蘆 (FULL_HOUSE)
4. 同花 (FLUSH)
5. 順子 (STRAIGHT)
6. 無法組成五張牌型 => []
```

---

## 實作細節

### 組合生成
使用 `itertools.combinations()` 生成所有可能組合
- `find_pairs()`: combinations(hand, 2) 中符合條件者
- `find_triples()`: combinations(hand, 3) 中符合條件者
- `find_fives()`: 累積所有五張有效組合

### get_all_valid_plays 邏輯
```
if last_play is None:
    # 第一回合：只能出3♣
    return [[Card(rank=3, suit=0)]]
elif card_type(last_play) == SINGLE:
    # 上家單張：回傳所有單張、對子、三條、五張牌型
    return find_singles() + find_pairs() + find_triples() + find_fives()
elif card_type(last_play) == PAIR:
    # 上家對子：回傳所有對子、三條、五張牌型
    return find_pairs() + find_triples() + find_fives()
# ... 依此類推
```

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_finder -v
```

---

## 重構檢查清單

- [ ] 優化順子搜尋演算法（可考慮動態規劃）
- [ ] 減少重複計算（快取相同 rank 的牌）
- [ ] 考慮使用生成器（yield 而非 return list）
- [ ] 性能優化：提前終止不可能的搜尋
- [ ] 加入 docstring 文檔