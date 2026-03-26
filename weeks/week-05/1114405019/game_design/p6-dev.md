# Phase 6: GUI - 開發設計

## 目標

實作 Pygame GUI，提供完整的遊戲介面。

## 檔案結構

```
bigtwo/
├── ui/
│   ├── __init__.py
│   ├── render.py    # 渲染器
│   ├── input.py    # 輸入處理
│   └── app.py      # 主應用
└── main.py          # 入口
```

---

## 1. render.py - 渲染器

```
類別：Renderer

屬性：
  COLORS = {
    background: (45,45,45)
    card_back: (74,144,217)
    spade_club: (255,255,255)
    heart_diamond: (231,76,60)
    player: (46,204,113)
    ai: (149,165,166)
    selected: (241,196,15)
    button: (52,152,219)
  }
  
  CARD_WIDTH = 60
  CARD_HEIGHT = 90

方法：
  draw_card(card, x, y, selected=False)
    - 繪製單張牌
    - 數字/花色顏色處理
    
  draw_hand(hand, x, y, selected_indices)
    - 繪製手牌（重疊顯示）
    
  draw_player(player, x, y, is_current)
    - 繪製玩家名稱
    
  draw_last_play(cards, player_name, x, y)
    - 繪製上家出牌
    
  draw_buttons(buttons, x, y)
    - 繪製按鈕
```

---

## 2. input.py - 輸入處理

```
類別：InputHandler

屬性：
  renderer: Renderer
  selected_indices: List[int]
  buttons: Dict

方法：
  handle_event(event, game) -> bool
    - 處理事件
    
  handle_click(pos, game) -> bool
    - 處理點擊
    - 檢查按鈕
    - 檢查選牌
    
  handle_key(key, game) -> bool
    - 處理鍵盤
    - Enter: 出牌
    - P: 過牌
    
  try_play(game) -> bool
    - 嘗試出牌
    - 驗證選牌合法性
    - 調用 game.play()
```

---

## 3. app.py - 主應用

```
類別：BigTwoApp

屬性：
  screen: pygame.Surface
  clock: pygame.time.Clock
  renderer: Renderer
  input_handler: InputHandler
  game: BigTwoGame
  running: bool
  fps: int (預設 60)

方法：

  __init__(screen_width=1200, screen_height=800)
    - 初始化 Pygame
    - 建立遊戲視窗

  setup() -> None
    - 呼叫 game.setup()

  render() -> None
    - 清除畫面
    - 渲染遊戲狀態
    - 翻新顯示

  update() -> None
    - 更新遊戲邏輯（如 AI 回合）

  handle_events() -> bool
    - 事件循環
    - 返回 False 表示應關閉APP

  run() -> None
    - 主迴圈
    - while running:
        - handle_events()
        - update()
        - render()
        - clock.tick(fps)

  cleanup() -> None
    - 退出 Pygame
```

---

## Pygame 配置

```python
# 視窗設定
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# 卡牌尺寸
CARD_WIDTH = 60
CARD_HEIGHT = 90
CARD_SPACING = 10

# 玩家位置（四人座位）
PLAYER_POSITIONS = {
    0: (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150),  # 底部（人類玩家）
    1: (SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2),   # 右
    2: (SCREEN_WIDTH // 2, 50),                    # 頂部
    3: (100, SCREEN_HEIGHT // 2)                   # 左
}

# 中央出牌區
CENTER_PLAY_AREA = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
```

---

## 渲染層級順序

1. 背景
2. 玩家位位置 & 名稱
3. 各玩家手牌（左-頂部-右視角）
4. 中央上家出牌區
5. 當前玩家手牌（放大顯示）
6. 選中指示（黃色框）
7. 按鈕（出牌、過牌、認輸）
8. 提示訊息（遊戲狀態、錯誤提示）

---

## 事件處理流程

```
滑鼠點擊（MOUSEBUTTONDOWN）
  ├─ 是否在按鈕範圍內？
  │  ├─ 「出牌」按鈕 → input_handler.try_play(game)
  │  ├─ 「過牌」按鈕 → game.pass_()
  │  └─ 「認輸」按鈕 → game 狀態設為結束
  └─ 是否在手牌區域內？
     └─ 計算點擊的卡牌 index
        └─ input_handler.toggle_selection(index)

鍵盤輸入（KEYDOWN）
  ├─ Enter: input_handler.try_play(game)
  ├─ P: game.pass_()
  ├─ R: 重新開始遊戲
  └─ ESC: 退出遊戲

視窗關閉（QUIT）
  └─ 設定 running = False
```

---

## 執行與起點

```bash
# 啟動遊戲
python main.py

# main.py 內容：
if __name__ == "__main__":
    app = BigTwoApp()
    app.setup()
    app.run()
    app.cleanup()
```

---

## 重構檢查清單

- [ ] 實作設定選單（玩家名稱、難度設定）
- [ ] 加入暫停/恢復功能
- [ ] 實作遊戲記錄回放
- [ ] 加入音效系統
- [ ] 支援解析度自適應
- [ ] 優化卡牌動畫（發牌、出牌）
- [ ] 加入連接網路對戰
- [ ] 完整 docstring 文檔
  buttons: Dict

方法：
  __init__()
    - 初始化pygame
    - 建立遊戲
    
  run()
    - 主迴圈
    - handle_events()
    - render()
    - pygame.display.flip()
    
  handle_events()
    - 處理所有事件
    - 遊戲結束時跳過
    
  render()
    - 背景
    - 所有玩家（AI顯示背面）
    - 人類玩家手牌
    - 上家出牌
    - 按鈕
    - 遊戲結束訊息
```

---

## 4. main.py - 入口

```
from ui.app import BigTwoApp

if __name__ == "__main__":
    app = BigTwoApp()
    app.run()
```

---

## 控制說明

```
滑鼠點擊：選取/取消選取牌
Enter：確認出牌
P：過牌
```

---

## 執行遊戲

```bash
cd bigtwo
pip install pygame
python main.py
```

---

## 重構檢查清單

- [ ] 加入動畫效果
- [ ] 優化牌面設計
- [ ] 加入遊戲記錄
- [ ] 支援鍵盤導航