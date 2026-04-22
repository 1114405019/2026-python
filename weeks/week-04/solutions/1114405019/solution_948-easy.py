# UVA 948: Fibonaccimal Base - 簡易版
# 邏輯：生成斐波那契數，貪婪從大到小減

import sys

def fib_base(n):
    if n == 0: return "0"
    fib = [1, 2]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    fib.reverse()
    res = ""
    for f in fib:
        if n >= f:
            res += "1"
            n -= f
        else:
            res += "0"
    return res.lstrip("0") or "0"

for line in sys.stdin:
    print(fib_base(int(line.strip())))</content>
<parameter name="filePath">c:\Users\yiteng\Downloads\0318\2026-python\weeks\week-04\solutions\solution_948-easy.py