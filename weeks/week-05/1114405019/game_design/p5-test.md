# Phase 5: 遊戲流程 - 測試設計

## 目標

實作 BigTwoGame 類別，控制完整遊戲流程。

## 測試框架

使用 Python 標準函式庫 `unittest`

## 測試檔案

`tests/test_game.py`

---

## 測試案例設計

### 1. 遊戲初始化

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_game_has_4_players | `game.setup()` | 4位玩家 |
| test_each_player_13_cards | setup後 | 每人13張 |
| test_total_cards_distributed | setup後 | 總共52張 |
| test_first_player_has_3_clubs | setup後 | 先手有3♣ |
| test_one_human_three_ai | setup後 | 1人3AI |

---

### 2. 出牌流程

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_play_removes_cards | 出牌 | 手牌-1 |
| test_play_sets_last_play | 出牌 | last_play設定 |
| test_invalid_play | 非法出牌 | 回傳False |
| test_pass_increments | 過牌 | pass_count+1 |

---

### 3. 回合判定

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_three_passes_resets | 3人過牌 | 重置last_play |
| test_turn_rotates | next_turn() | 輪到下家 |
| test_round_number | 出牌後輪轉 | round_number++（選項） |

---

### 4. 勝利判定

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_winner_when_empty | 玩家hand為空 | winner設為該玩家 |
| test_game_over | winner不為None | is_game_over()回傳True |
| test_not_over | 有多位玩家有牌 | is_game_over()回傳False |

---

### 5. AI 回合整合

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_ai_turn_plays | AI玩家回合 | 自動出牌 |
| test_ai_pass | 無合法出牌 | AI自動過牌 |
| test_ai_hand_decreases | AI出牌後 | hand牌數-1 |

---

### 6. 特殊情況

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_same_player_plays_twice | 3人過牌，輪回該玩家 | 可出任意牌型 |
| test_only_one_player_left | 其他玩家出完牌 | 遊戲照常進行 |
| test_4_players_all_pass | 不可能情況 | pass_count≤3 |

---

## 前置條件

- 已完成 Phase 1：Card, Deck, Hand, Player
- 已完成 Phase 2：HandClassifier
- 已完成 Phase 3：HandFinder
- 已完成 Phase 4：AIStrategy

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_game -v
```

---

## 預期結果

- **Red**: 實作前所有測試失敗
- **Green**: 清晰邏輯後通過
- **Refactor**: 優化流程控制與記錄系統

---

## 測試執行說明

### 遊戲流程驗證
1. setup() 正確初始化 4 位玩家、52 張牌分配
2. 找到持有 3♣ 的玩家作為先手
3. 回合輪轉正確（0→1→2→3→0）
4. 過牌計數與重置邏輯正確

### 狀態檢查
- last_play 的正確設定
- pass_count 的遞增與重置
- winner 的正確判定
- 遊戲終止條件

### 邊界情況
1. 第一回合強制出 3♣
2. 三次連續過牌後重置
3. 玩家出完所有牌時判定勝利
4. AI 與人類玩家的混合流程

### 4. 獲勝判定

| 測試名稱 | 輸入 | 預期輸出 |
|---------|------|---------|
| test_detect_winner | 手牌空 | 回傳獲勝者 |
| test_no_winner_yet | 有牌 | 回傳None |
| test_game_ends | 有獲勝者 | is_game_over=True |

---

## 執行測試

```bash
cd bigtwo
python -m unittest tests.test_game -v
```

---

## 預期結果

- **Red**: 測試失敗
- **Green**: 實作後通過
- **Refactor**: 重構