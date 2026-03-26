# Phase 6: GUI - 測試設計

## 目標

實作 Pygame GUI，提供視覺化遊戲介面。

## 測試方式

整合測試 + 手動測試

## 測試檔案

`tests/test_ui.py`

---

## 測試案例設計

### 1. 渲染測試

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_card_render | Card(♠A) | surface寬度>0 |
| test_hand_render | Hand有3張牌 | surface正常 |

---

### 2. 整合測試

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_game_init | BigTwoApp() | 4位玩家 |
| test_card_selection | 點擊座標 | 正確轉換 |
| test_button_click | 點擊按鈕區 | 正確回應 |

---

### 3. E2E 測試

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_complete_flow | 模擬完整遊戲 | 遊戲正確結束 |

---

### 3. E2E 測試

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_complete_flow | 模擬完整遊戲 | 遊戲正確結束 |
| test_ui_updates_per_turn | 每回合更新 | 畫面正確刷新 |
| test_manual_play_flow | 人類點擊出牌 | 卡牌移除，狀態更新 |

---

## 前置條件

- 已完成 Phase 1~5 的所有功能
- 已安裝 Pygame：`pip install pygame`
- 支援 Python 3.8+

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_ui -v
```

---

## 測試方式說明

### 自動化測試（unittest）
使用 mock 隔離 pygame 依賴：
```python
from unittest.mock import Mock, patch
import pygame

# Mock pygame.display.set_mode
with patch('pygame.display.set_mode'):
    app = BigTwoApp()
    app.render()
```

### 手動測試清單
1. **啟動遊戲**
   - 能否順利開啟視窗
   - 初始顯示是否正確（4位玩家、手牌分佈）

2. **選牌與出牌**
   - 點擊卡牌是否正確高亮
   - 出牌按鈕是否有回應
   - 選牌清除功能是否正常

3. **遊戲流程**
   - AI 是否自動出牌
   - 過牌功能是否正常
   - 遊戲終止時是否顯示贏家

4. **視覺效果**
   - 卡牌渲染是否清晰
   - 顏色選擇是否符合預期
   - 介面是否美觀合理

---

## 預期結果

- **Red**: 實作前所有測試失敗
- **Green**: 清晰邏輯後通過
- **Refactor**: 優化渲染效能與視覺設計

---

## 性能目標

- **幀率**: 至少 60 FPS（分配允許）
- **回應時間**: 滑鼠點擊 ≤ 100ms 回應
- **記憶體**: 運行時 ≤ 200MB

---

## 持續改進方向

1. **視覺增強**
   - 卡牌翻轉動畫
   - 出牌飛行效果
   - 玩家頭像與統計資訊

2. **互動優化**
   - 鍵盤快捷鍵支援
   - 觸控設備支援
   - 視窗大小自適應

3. **功能擴展**
   - 遊戲暫停/恢復
   - 回合記錄與回放
   - 多局遊戲積分系統
   - 網路對戰模式