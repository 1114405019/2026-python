#!/usr/bin/env python3
"""
UVA 10170 - The Hotel with Infinite Rooms (簡單版本)

問題描述：
房間從 S 開始，每個房間 k 有 k 個客人，找出第 D 個客人住的房間。

解題邏輯：
1. 從房間 S 開始
2. 減去當前房間的客人數，直到 <= 當前房間
3. 當前房間即為答案
"""

import sys

def main():
    try:
        for line in sys.stdin:
            S, D = map(int, line.split())
            room = S
            guests = D
            while guests > room:
                guests -= room
                room += 1
            print(room)
    except EOFError:
        pass

if __name__ == "__main__":
    main()