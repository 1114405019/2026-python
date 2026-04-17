# UVA 10035 手打練習 - Primary Arithmetic
# 筆記：模擬加法，從個位開始，加起來看有沒有進位
# 記得處理進位 carry

import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    if a == 0 and b == 0: break
    carry = 0  # 進位初始 0
    count = 0  # 進位次數
    while a or b:  # 只要還有數字
        sum_digits = a % 10 + b % 10 + carry  # 當前位數和
        if sum_digits >= 10:
            count += 1
            carry = 1  # 下次進位 1
        else:
            carry = 0
        a //= 10  # 去掉個位
        b //= 10
    # 輸出結果
    if count == 0:
        print("No carry operation.")
    elif count == 1:
        print("1 carry operation.")
    else:
        print(f"{count} carry operations.")</content>
<parameter name="filePath">c:\Users\yiteng\Downloads\0318\2026-python\weeks\week-04\solutions\hand10035.py