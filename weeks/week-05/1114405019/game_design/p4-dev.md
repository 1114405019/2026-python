# Phase 4: AI 策略 - 開發設計

## 目標

實作 AIStrategy 類別，使用貪心演算法選擇最佳出牌。

## 檔案位置

`game/ai.py`

---

## 類別設計

### AIStrategy 類別

```
常數：
  TYPE_SCORES = {
    SINGLE: 1, PAIR: 2, TRIPLE: 3,
    STRAIGHT: 4, FLUSH: 5, FULL_HOUSE: 6,
    FOUR_OF_A_KIND: 7, STRAIGHT_FLUSH: 8
  }
  
  EMPTY_HAND_BONUS = 10000
  NEAR_EMPTY_BONUS = 500
  SPADE_BONUS = 5

靜態方法：

  score_play(cards: List[Card], hand: Hand, is_first: bool = False) -> float
    評分公式：
    score = 牌型×100 + 數字×10 + 剩餘加分
    
    - 牌型分數 × 100
    - 數字分數 × 10  
    - 剩1張: +10000
    - 剩≤3張: +500
    - ♠牌: +5/張

  select_best(valid_plays: List[List[Card]], hand: Hand, is_first: bool = False) -> Optional[List[Card]]
    貪心策略：
    1. 第一回合: 只能選3♣
    2. 其他: 選分數最高者
```

---

---

## 評分邏輯詳解

### 基礎評分
```
score = TYPE_SCORE[card_type] * 100 + rank_score * 10
```

其中：
- `TYPE_SCORE[]` 為牌型分數（SINGLE=1, ..., STRAIGHT_FLUSH=8）
- `rank_score` 為牌的數字值（3-15）

### 加分項目
```
1. 剩餘牌數加分：
   - 剩 1 張: +10000 分（最優先）
   - 剩 2-3 張: +500 分
   - 剩 4+ 張: +0 分

2. 黑桃加分：
   - 每張黑桃 +5 分
   - 適度鼓勵出高花色牌

3. 第一回合特殊：
   - 強制選擇 3♣（一律出此牌）
```

### 完整評分範例
```
出牌：[♠A, ♥A]（對A），剩 11 張
- 牌型分：2 * 100 = 200
- 數字分：14 * 10 = 140
- 黑桃加分：1 * 5 = 5（♠A）
- 剩餘加分：0（≥4張）
- 總分：200 + 140 + 5 = 345

出牌：[♠3]（單♠3），剩 1 張
- 牌型分：1 * 100 = 100
- 數字分：3 * 10 = 30
- 黑桃加分：1 * 5 = 5
- 剩餘加分：10000（剩 1 張）
- 總分：100 + 30 + 5 + 10000 = 10135（優先度極高）
```

---

## 貪心策略說明

該 AI 採用**局部最優**策略：
- 每回合選擇分數最高的出牌
- 不考慮對手狀態
- 簡單高效，適合教學演示

> **改進方向**：可加入博弈論（minimax）或蒙特卡洛樹搜尋（MCTS）提升 AI 難度

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_ai -v
```

---

## 重構檢查清單

- [ ] 提取分數常數為類別屬性
- [ ] 實作更複雜的讓牌策略
- [ ] 加入對手分析（監控對手剩餘牌數）
- [ ] 考慮加入隨機性（破壞預測性）
- [ ] 性能優化
- [ ] 加入 docstring 文檔