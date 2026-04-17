#!/usr/bin/env python3
"""
UVA 10101 - Bangla Numbers (簡單版本)

問題描述：
格式化數字為孟加拉格式：從右每 2 位，然後最後 3 位。

解題邏輯：
1. 將數字轉字串
2. 從右開始組，每組 2 位，第一次組可能是 3 位
3. 用逗號連接
"""

import sys

def main():
    try:
        for line in sys.stdin:
            n = int(line.strip())
            s = str(n)
            if len(s) <= 3:
                print(s)
                continue
            result = []
            i = len(s)
            gl = 3 if i >= 3 else i
            result.append(s[i - gl:i])
            i -= gl
            while i > 0:
                gl = 2 if i >= 2 else i
                result.append(s[i - gl:i])
                i -= gl
            result.reverse()
            print(','.join(result))
    except EOFError:
        pass

if __name__ == "__main__":
    main()