#!/usr/bin/env python3
"""
UVA 10170 - The Hotel with Infinite Rooms
AI 撰寫的標準版 Python 程式

問題描述：
找出第 D 個客人住的房間號，房間從 S 開始，每個房間 k 有 k 個客人。

輸入：
多行，每行 S D。

輸出：
每行對應的房間號。
"""

import sys

def find_room(S, D):
    """找出第 D 個客人住的房間"""
    current_room = S
    guests_needed = D
    while guests_needed > current_room:
        guests_needed -= current_room
        current_room += 1
    return current_room

def main():
    """主程式"""
    try:
        for line in sys.stdin:
            S, D = map(int, line.split())
            room = find_room(S, D)
            print(room)
    except EOFError:
        pass

if __name__ == "__main__":
    main()