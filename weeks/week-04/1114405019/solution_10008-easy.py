# UVA 10008: What's Cryptanalysis? - 簡易版
# 用 Counter 統計字母頻率，排序輸出

import sys
from collections import Counter

n = int(input())
text = ""
for _ in range(n):
    text += input().lower()

freq = Counter(c for c in text if c.isalpha())
for char, count in sorted(freq.items(), key=lambda x: (-x[1], x[0])):
    print(f"{char.upper()} {count}")</content>
<parameter name="filePath">c:\Users\yiteng\Downloads\0318\2026-python\weeks\week-04\solutions\solution_10008-easy.py