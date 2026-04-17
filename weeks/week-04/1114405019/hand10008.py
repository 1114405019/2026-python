# UVA 10008 手打練習 - What's Cryptanalysis?
# 筆記：統計字母出現次數，大小寫一樣，按次數多到少排，次數一樣按字母 A-Z 排
# 用 Counter 超方便，記得轉小寫過濾字母

import sys
from collections import Counter

# 讀第一行 n
n = int(input())
# 讀 n 行，合起來轉小寫
text = ""
for _ in range(n):
    text += input().lower()

# 只留字母，統計
freq = Counter(c for c in text if c.isalpha())
# 排序：先次數降序，再字母升序
for char, count in sorted(freq.items(), key=lambda x: (-x[1], x[0])):
    # 輸出大寫字母和次數
    print(f"{char.upper()} {count}")</content>
<parameter name="filePath">c:\Users\yiteng\Downloads\0318\2026-python\weeks\week-04\solutions\hand10008.py