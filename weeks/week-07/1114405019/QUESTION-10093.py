#!/usr/bin/env python3
"""
UVA 10093 - An Easy Problem!
AI 撰寫的標準版 Python 程式

問題描述：
給定一個字串，找出最小的基數 b (2<=b<=62) 使得該字串在基數 b 下是有效的數字。

輸入：
多行，每行一個字串，直到 EOF。

輸出：
每行對應的最小基數，或 "such number is impossible!"
"""

import sys

def char_to_value(c):
    """將字元轉為數值"""
    if c.isdigit():
        return int(c)
    elif c.isupper():
        return ord(c) - ord('A') + 10
    elif c.islower():
        return ord(c) - ord('a') + 36
    else:
        return -1  # 無效

def find_min_base(number):
    """找出最小基數"""
    if number == "1":
        return "such number is impossible!"
    
    if len(number) > 1 and number[0] == '0':
        return "such number is impossible!"
    
    max_val = 0
    for c in number:
        val = char_to_value(c)
        if val == -1:
            return "such number is impossible!"
        max_val = max(max_val, val)
    
    base = max_val + 1
    if base < 2:
        base = 2
    return base

def main():
    """主程式"""
    try:
        for line in sys.stdin:
            number = line.strip()
            if number:  # 跳過空行
                result = find_min_base(number)
                print(result)
    except EOFError:
        pass

if __name__ == "__main__":
    main()