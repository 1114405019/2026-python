# Big Two Card Game

一個完整的 Big Two 撲克牌遊戲實作，包含圖形介面和 AI 對手。

## 遊戲規則

- 4 位玩家（1 人 + 3 AI）
- 52 張牌，每人 13 張
- 遊戲從持有 3♣ 的玩家開始
- 支援 8 種牌型：單張、對子、三條、順子、同花、葫蘆、四條、同花順
- 輪流出牌，必須大過上家或過牌
- 三人連續過牌後重置回合
- 最先出完牌的玩家獲勝

## 專案結構

```
bigtwo/
├── main.py              # 遊戲入口
├── ui/
│   ├── __init__.py
│   ├── app.py          # 主應用程式
│   ├── render.py       # 渲染器
│   └── input.py        # 輸入處理
└── game/
    ├── __init__.py
    ├── models.py       # 資料模型 (Card, Deck, Hand, Player)
    ├── classifier.py   # 牌型分類與比較
    ├── finder.py       # 有效出牌搜尋
    ├── ai.py          # AI 策略
    └── game.py        # 遊戲邏輯控制器
```

## 系統需求

- Python 3.8+
- Pygame 2.0+

## 安裝與運行

1. 確保已安裝 Pygame：
```bash
pip install pygame
```

2. 運行遊戲：
```bash
cd bigtwo
python main.py
```

## 操作說明

### 滑鼠操作
- **點擊卡牌**：選中/取消選中要出的牌
- **Play 按鈕**：出牌
- **Pass 按鈕**：過牌
- **New Game 按鈕**：重新開始（遊戲結束後）

### 鍵盤操作
- **Enter**：出牌
- **P**：過牌
- **R**：重新開始
- **ESC**：退出遊戲

## 開發資訊

### Phase 完成狀態
- ✅ Phase 1: 資料模型 (39 測試通過)
- ✅ Phase 2: 牌型分類 (31 測試通過)
- ✅ Phase 3: 出牌搜尋 (18 測試通過)
- ✅ Phase 4: AI 策略 (9 測試通過)
- ✅ Phase 5: 遊戲流程 (17 測試通過)
- ✅ Phase 6: 圖形介面 (2 測試通過)

### 總測試數量
- **97 個測試全部通過**

### 主要組件

#### 資料模型 (models.py)
- `Card`: 單張牌，支援比較和排序
- `Deck`: 牌堆，支援洗牌和發牌
- `Hand`: 手牌，支援排序和移除
- `Player`: 玩家，包含名稱和手牌

#### 牌型分類 (classifier.py)
- 支援 8 種牌型辨識
- 牌型比較邏輯
- 出牌規則驗證

#### 出牌搜尋 (finder.py)
- 從手牌中尋找所有有效的出牌組合
- 支援遊戲規則約束

#### AI 策略 (ai.py)
- 貪婪策略：優先考慮牌型、點數、剩餘牌數、黑桃加分
- 自動選擇最佳出牌

#### 遊戲控制器 (game.py)
- 完整的遊戲流程控制
- 回合管理、勝利判定
- 整合所有遊戲組件

#### 圖形介面 (ui/)
- `Renderer`: 負責畫面渲染
- `InputHandler`: 處理用戶輸入
- `BigTwoApp`: 主應用程式，整合遊戲和UI

## 測試

運行所有測試：
```bash
python -m unittest discover tests -v
```

## 授權

此專案為學習用途。