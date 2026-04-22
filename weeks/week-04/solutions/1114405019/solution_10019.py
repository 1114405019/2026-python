# UVA 10019: Funny Encryption Method
# 對每個數字，計算十進位數字中 '1' 的個數，加上二進位表示中 '1' 的個數

import sys

def funny_encryption(n):
    # 十進位中 1 的個數
    decimal_ones = str(n).count('1')
    # 二進位中 1 的個數
    binary_ones = bin(n).count('1')
    return decimal_ones + binary_ones

def main():
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        n = int(data[index])
        index += 1
        print(funny_encryption(n))

if __name__ == "__main__":
    main()</content>
<parameter name="filePath">c:\Users\yiteng\Downloads\0318\2026-python\weeks\week-04\solutions\solution_10019.py