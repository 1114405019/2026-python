# AI_LOG — 6/11 進位計數

## 我問 AI 什麼

「我要用 Python unittest 測試函式 count_carries(a: int, b: int) -> int，規格：回傳直式加法 a+b 的進位次數；a 或 b 為負數時 raise ValueError("operands must be non-negative")。輸入範圍 0 ≤ a, b < 10,000,000,000。請幫我列出至少 3 個 test case，要包含連鎖進位的 edge case 和例外案例。」

## AI 給了什麼

AI 給了 4 個測試：123+456→0、555+555→3、999+1→3、a=-1 應 raise ValueError。連鎖進位案例有，但只測了 a 為負，沒測 b 為負或兩者都負，也沒測 a=0 或 b=0 的邊界。

## 我改了什麼

1. 補了 `test_invalid_negative_b` 與 `test_invalid_both_negative`：題目說「a 或 b 為負」，AI 只測了 a<0，我加了 b<0 和兩者都負的案例，確保 `or` 條件兩邊都被覆蓋。
2. 補了 `test_edge_zero` 和 `test_edge_one_zero`：a=b=0 不應有進位；a=0,b=999 也不應觸發進位（999 本身不與任何東西相加），確認邊界不會 crash。
3. 加了 `test_single_carry`（123+594→1）：驗證「只有一位進位」的中間情況，AI 沒提供只有局部進位的案例。
