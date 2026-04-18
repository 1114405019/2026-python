# AI_USAGE

## 問題紀錄

1. 拆解 UVA 118 規格
   - 我問如何把 UVA 118 的文字規則轉成機器人模擬邏輯。
   - 你回應要把機器人狀態、地圖邊界、scent 記錄與指令處理分開設計。

2. 產生 `robot_core.py` 雛形
   - 我要求撰寫純邏輯核心，不能依賴 pygame，方便測試。
   - 你提供了 `RobotManager` 類別、`execute_command()` 方法與 `scent` / `LOST` 判斷。

3. 修正 VS Code 找不到 tests 資料夾的 Import 錯誤
   - 我提醒要確認實際檔案位置與 import 路徑是否一致。
   - 幫我找出 `robot_game.py` 與 `test_robot_core.py` 實際存在於 `weeks/week-03/1114405019/` 目錄下，並建議避免錯誤路徑。

## 為何要把邏輯與介面分離

- 邏輯與介面分離可以讓核心行為專注於規則實作，不被視覺框架綁死。
- 這樣測試更容易：`robot_core.py` 可以用純 `unittest` 驗證，不需要啟動 pygame。
- 當介面改變（例如從 pygame 換成文字或網頁）時，核心邏輯仍可重複使用。
- 也能避免 `pygame` 對執行環境的依賴影響測試穩定性。
