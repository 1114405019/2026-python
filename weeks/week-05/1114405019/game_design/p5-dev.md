# Phase 5: 遊戲流程 - 開發設計

## 目標

實作 BigTwoGame 類別，控制完整遊戲流程。

## 檔案位置

`game/game.py`

---

## 類別設計

### BigTwoGame 類別

```
屬性：
  deck: Deck
  players: List[Player] (4位)
  current_player: int (0-3)
  last_play: Optional[Tuple[List[Card], str]]
  pass_count: int
  winner: Optional[Player]
  round_number: int

方法：

  setup() -> None
    - 建立牌堆、洗牌
    - 發13張牌給每位玩家
    - 找3♣決定先手
    - 初始化遊戲狀態

  play(player: Player, cards: List[Card]) -> bool
    - 檢查合法性
    - 移除手牌
    - 設定last_play
    - 檢查獲勝

  pass_(player: Player) -> bool
    - 玩家過牌
    - pass_count+1

  next_turn() -> None
    - current_player = (current+1) % 4

  _is_valid_play(cards: List[Card]) -> bool
    - 使用HandClassifier.can_play

  check_round_reset() -> None
    - pass_count>=3 時重置

  check_winner() -> Optional[Player]
    - 回傳手牌為空的玩家

  is_game_over() -> bool
    - winner is not None

  get_current_player() -> Player

  ai_turn() -> bool
    - AI自動回合
    - 調用 AIStrategy.select_best()
```

---

## 遊戲流程詳解

### 初始化階段 (setup)
```
1. 建立 Deck，洗牌
2. 循環發牌：每位玩家得 13 張
3. 掃描找 3♣：
   - 持有 3♣ 的玩家作為先手
   - 設定 current_player
4. 初始化遊戲狀態：
   - last_play = None
   - pass_count = 0
   - round_number = 1
```

### 回合循環
```
while not is_game_over():
    1. 取得 current_player
    2. 取得合法出牌清單
    3. 如果 is_ai: 
        ai_turn() → 自動選擇最佳出牌
    4. 否則：
        等待玩家輸入（GUI 層處理）
    5. 檢查回合重置：
        if pass_count >= 3:
            last_play = None
            pass_count = 0
    6. 檢查勝利：
        if current_player.hand 為空:
            winner = current_player
    7. next_turn()
```

### 回合重置規則
```
當 3 位玩家連續過牌時：
- 重置 last_play 為 None
- 重置 pass_count 為 0
- 當前玩家可出任意牌型
```

### 勝利判定
```
條件：玩家的 hand 牌數 == 0
結果：設定 winner，遊戲結束
```

---

## 關鍵屬性說明

| 屬性 | 型別 | 說明 |
|------|------|------|
| deck | Deck | 剩餘牌堆 |
| players | List[Player] | 4 位玩家（含 1 個人類 + 3 個 AI） |
| current_player | int | 0-3，表示目前輪到誰 |
| last_play | Tuple | (出牌列表, 玩家名稱) 或 None |
| pass_count | int | 連續過牌次數 |
| winner | Player | 遊戲結束時的贏家 |
| round_number | int | 目前局數 |

---

## execute 流程（主迴圈）

```python
def execute(self):
    """執行完整遊戲至結束"""
    self.setup()
    
    while not self.is_game_over():
        player = self.get_current_player()
        valid_plays = self.get_valid_plays()
        
        if player.is_ai:
            cards = self.ai_turn()
            if cards:
                self.play(player, cards)
            else:
                self.pass_(player)
        else:
            # GUI 層獲取 cards，然後調用 self.play()
            pass
        
        self.check_round_reset()
        self.next_turn()
    
    return self.winner
```

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_game -v
```

---

## 重構檢查清單

- [ ] 提取回合邏輯到 _execute_turn() 方法
- [ ] 加入遊戲記錄（game_log）
- [ ] 支援暫停/恢復遊戲狀態
- [ ] 加入計分系統（多局遊戲）
- [ ] 實作觀看者模式（Spectator Pattern）
- [ ] 加入 docstring 文檔
- [ ] 性能優化：快取合法出牌