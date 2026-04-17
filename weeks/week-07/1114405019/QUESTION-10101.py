#!/usr/bin/env python3
"""
UVA 10101 - Bangla Numbers
AI 撰寫的標準版 Python 程式

問題描述：
將數字格式化為孟加拉語數字表示：從右開始，每 2 位一組，然後最後一組 3 位。

輸入：
多行，每行一個非負整數。

輸出：
每行對應的格式化數字。
"""

import sys

def format_bangla_number(n):
    """格式化孟加拉數字"""
    s = str(n)
    if len(s) <= 3:
        return s
    
    result = []
    i = len(s)
    # 第一組從右，長度 3
    group_len = 3 if i >= 3 else i
    result.append(s[i - group_len:i])
    i -= group_len
    # 後續組長度 2
    while i > 0:
        group_len = 2 if i >= 2 else i
        result.append(s[i - group_len:i])
        i -= group_len
    result.reverse()
    return ','.join(result)

def main():
    """主程式"""
    try:
        for line in sys.stdin:
            num = int(line.strip())
            formatted = format_bangla_number(num)
            print(formatted)
    except EOFError:
        pass

if __name__ == "__main__":
    main()