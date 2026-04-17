# UVA 10019: Funny Encryption Method - 簡易版
# 十進位 1 數 + 二進位 1 數

import sys

T = int(input())
for _ in range(T):
    n = int(input())
    dec = str(n).count('1')
    bin_ones = bin(n).count('1')
    print(dec + bin_ones)</content>
<parameter name="filePath">c:\Users\yiteng\Downloads\0318\2026-python\weeks\week-04\solutions\solution_10019-easy.py