# UVA 948: Fibonaccimal Base
# 將給定的十進位數字轉換為 Fibonaccimal Base 表示法
# Fibonaccimal Base 使用斐波那契數列作為基數，每個位數為 0 或 1，且不允許連續兩個 1

import sys

def generate_fibonacci(limit):
    # 生成斐波那契數列，直到超過 limit
    fib = []
    a, b = 1, 2
    while a <= limit:
        fib.append(a)
        a, b = b, a + b
    return fib[::-1]  # 從大到小

def fibonaccimal_base(n):
    if n == 0:
        return "0"
    fib = generate_fibonacci(n)
    result = []
    for f in fib:
        if n >= f:
            result.append('1')
            n -= f
        else:
            result.append('0')
    # 移除前導零
    return ''.join(result).lstrip('0') or '0'

def main():
    input = sys.stdin.read
    data = input().split()
    index = 0
    T = int(data[index])
    index += 1
    for _ in range(T):
        n = int(data[index])
        index += 1
        print(fibonaccimal_base(n))

if __name__ == "__main__":
    main()</content>
<parameter name="filePath">c:\Users\yiteng\Downloads\0318\2026-python\weeks\week-04\solutions\solution_948.py