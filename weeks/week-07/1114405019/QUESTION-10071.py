#!/usr/bin/env python3
"""
UVA 10071 - Back to High School Physics
AI 撰寫的標準版 Python 程式

問題描述：
給定速度 v 和時間 t，計算粒子在時間 2t 時的位移。
位移公式：s = 2 * v * t

輸入：
多行，每行兩個整數 v t，直到 EOF。

輸出：
每行對應的位移。
"""

import sys

def main():
    """
    主程式：讀取輸入，計算位移
    """
    try:
        for line in sys.stdin:
            # 讀取 v 和 t
            v, t = map(int, line.split())
            # 計算位移
            displacement = 2 * v * t
            print(displacement)
    except EOFError:
        pass

if __name__ == "__main__":
    main()