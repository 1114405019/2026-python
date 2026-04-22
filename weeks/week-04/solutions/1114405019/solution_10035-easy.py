# UVA 10035: Primary Arithmetic - 簡易版
# 從右到左加，記進位

import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    if a == 0 and b == 0: break
    carry = 0
    count = 0
    while a or b:
        if (a % 10 + b % 10 + carry) >= 10:
            count += 1
            carry = 1
        else:
            carry = 0
        a //= 10
        b //= 10
    if count == 0:
        print("No carry operation.")
    elif count == 1:
        print("1 carry operation.")
    else:
        print(f"{count} carry operations.")</content>
<parameter name="filePath">c:\Users\yiteng\Downloads\0318\2026-python\weeks\week-04\solutions\solution_10035-easy.py