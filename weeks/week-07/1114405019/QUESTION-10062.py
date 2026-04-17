#!/usr/bin/env python3
"""
UVA 10062 - Tell me the frequencies!
AI 撰寫的標準版 Python 程式

問題描述：
給定一行文字，找出其中 ASCII 字元的頻率。
頻率應按升序排列，相同頻率時按 ASCII 值降序排列。

輸入：
多行文字，每行包含可列印 ASCII 字元 (32-126)。
輸入以 EOF 結束。

輸出：
對於每行輸入，輸出字元的 ASCII 值、空格、頻率。
字元按頻率升序排序，相同頻率按 ASCII 降序。
"""

import sys
from collections import Counter

def process_line(line):
    """
    處理單行輸入，計算字元頻率並格式化輸出

    Args:
        line (str): 輸入行

    Returns:
        list: 格式化的輸出行列表
    """
    if not line.strip():  # 跳過空行
        return []

    # 使用 Counter 計算每個字元的頻率
    freq = Counter(line)

    # 排序：先按頻率升序，相同頻率按 ASCII 值降序
    # key=lambda x: (x[1], -ord(x[0]))
    # x[1] 是頻率，x[0] 是字元
    sorted_chars = sorted(freq.items(), key=lambda x: (x[1], -ord(x[0])))

    # 格式化輸出：ASCII值 空格 頻率
    result = []
    for char, count in sorted_chars:
        ascii_val = ord(char)
        result.append(f"{ascii_val} {count}")

    return result

def main():
    """
    主程式：讀取標準輸入，處理每一行，直到 EOF
    """
    try:
        # 讀取所有輸入
        for line in sys.stdin:
            # 移除行尾的換行符
            line = line.rstrip('\n')
            # 處理這行
            output_lines = process_line(line)
            # 輸出結果
            for output_line in output_lines:
                print(output_line)
    except EOFError:
        pass  # EOF 正常結束

if __name__ == "__main__":
    main()