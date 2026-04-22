#!/usr/bin/env python3
"""
UVA 10093 - An Easy Problem! (簡單版本)

問題描述：
輸入字串，找出最小基數 b 使得字串在 b 進制下有效。

解題邏輯：
1. 如果字串 == "1" 或以 0 開頭且長度 >1，impossible
2. 否則，找出字串中最大 digit 值，b = max + 1
3. 如果 b < 2，b = 2
"""

import sys

def main():
    try:
        for line in sys.stdin:
            num = line.strip()
            if not num:
                continue
            if num == "1" or (len(num) > 1 and num[0] == '0'):
                print("such number is impossible!")
                continue
            max_digit = 0
            for c in num:
                if c.isdigit():
                    val = int(c)
                elif c.isupper():
                    val = ord(c) - ord('A') + 10
                elif c.islower():
                    val = ord(c) - ord('a') + 36
                else:
                    val = -1
                if val == -1:
                    print("such number is impossible!")
                    break
                max_digit = max(max_digit, val)
            else:
                base = max(max_digit + 1, 2)
                print(base)
    except EOFError:
        pass

if __name__ == "__main__":
    main()