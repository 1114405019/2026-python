#!/usr/bin/env python3
"""
UVA 10071 - Back to High School Physics (簡單版本)

問題描述：
輸入速度 v 和時間 t，輸出位移 s = 2 * v * t

輸入：多行，每行 v t，直到 EOF
輸出：每行對應的位移

解題邏輯：
1. 使用 sys.stdin 讀取輸入
2. 每行分割為 v 和 t
3. 計算 2 * v * t
4. 輸出結果
"""

import sys

def main():
    """
    主函數：處理輸入輸出
    """
    try:
        for line in sys.stdin:
            # 分割輸入為 v 和 t
            parts = line.split()
            v = int(parts[0])
            t = int(parts[1])
            # 計算位移
            s = 2 * v * t
            print(s)
    except EOFError:
        pass

if __name__ == "__main__":
    main()