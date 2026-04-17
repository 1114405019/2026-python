# UVA 948 手打練習 - Fibonaccimal Base
# 筆記：斐波那契基數，把數字拆成斐波那契數的和，不能重複用同一個
# 從最大的斐波那契數開始，看能不能減，減了就記 1，沒減就 0

import sys

def fib_base(n):
    # 如果是 0 直接回傳 0
    if n == 0: return "0"
    # 先做出斐波那契數列，從 1,2 開始，加到超過 n
    fib = [1, 2]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    # 反轉，從大到小
    fib.reverse()
    # 初始化結果字串
    res = ""
    # 對每個斐波那契數
    for f in fib:
        if n >= f:
            res += "1"  # 能減就減，記 1
            n -= f
        else:
            res += "0"  # 不能減，記 0
    # 去掉前導零，如果全零就回 0
    return res.lstrip("0") or "0"

# 讀輸入，每行一個數字，轉換輸出
for line in sys.stdin:
# 讀取輸入，每一行一個數字，轉換輸出
    for line in sys.stdin:
        if line.strip():
            print(fib_base(int(line.strip())))