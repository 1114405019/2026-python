# UVA 10019 手打練習 - Funny Encryption Method
# 筆記：把數字轉字串數 1 的個數，加上 bin() 數 1 的個數
# 簡單但有趣的加密方法

import sys

# 讀測試案例數
T = int(input())
for _ in range(T):
    n = int(input())
    # 十進位 1 數
    dec_ones = str(n).count('1')
    # 二進位 1 數
    bin_ones = bin(n).count('1')
    # 加起來輸出
    print(dec_ones + bin_ones)</content>
<parameter name="filePath">c:\Users\yiteng\Downloads\0318\2026-python\weeks\week-04\solutions\hand10019.py