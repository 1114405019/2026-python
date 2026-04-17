#!/usr/bin/env python3
"""
UVA 10062 - Tell me the frequencies! (簡單版本)

這個版本使用基本的字典來計算頻率，更容易理解和記憶。

問題描述：
給定一行文字，計算每個 ASCII 字元的出現頻率。
輸出格式：按頻率升序排列，相同頻率時按 ASCII 值降序。

輸入：多行文字，直到 EOF。
輸出：每行對應的頻率統計。

解題邏輯：
1. 讀取輸入：使用 sys.stdin 逐行讀取，直到 EOF。
2. 計算頻率：對每一行，使用字典記錄每個字元出現次數。
3. 排序：將字典轉為列表，按 (頻率, -ASCII值) 排序。
4. 輸出：格式化輸出 ASCII值 空格 頻率。
"""

import sys

def main():
    """
    主函數：讀取輸入並處理每一行

    這個函數負責：
    - 從標準輸入讀取資料
    - 處理每一行文字
    - 計算並輸出字元頻率
    """
    # 使用 try-except 來處理 EOF (End Of File)
    # 當輸入結束時，會引發 EOFError，我們捕獲它並正常結束程式
    try:
        # sys.stdin 是標準輸入物件，可以逐行讀取
        # for line in sys.stdin: 會自動處理多行輸入
        for line in sys.stdin:
            # line 包含換行符 \n，我們使用 rstrip('\n') 移除它
            # rstrip() 移除右側指定字元，預設移除空白字元
            line = line.rstrip('\n')

            # 如果行是空的（只有空白或換行），我們可以選擇跳過
            # not line 檢查字串是否為空
            if not line:
                continue

            # 初始化一個空字典來儲存字元頻率
            # 字典的鍵是字元，值是出現次數
            freq = {}

            # 遍歷字串中的每個字元
            for char in line:
                # 檢查字元是否已在字典中
                if char in freq:
                    # 如果已存在，頻率加一
                    freq[char] += 1
                else:
                    # 如果不存在，初始化為1
                    freq[char] = 1

            # 此時 freq 字典包含了所有字元的頻率
            # 例如：{'A': 3, 'B': 2, 'C': 1}

            # 將字典轉換為列表，方便排序
            # dict.items() 返回 (鍵, 值) 的元組列表
            char_list = list(freq.items())

            # 排序字元列表
            # key=lambda x: (x[1], -ord(x[0]))
            # x[1] 是頻率 (第一排序鍵，升序)
            # -ord(x[0]) 是 -ASCII值 (第二排序鍵，降序，因為負號)
            # ord() 函數返回字元的 ASCII 值
            char_list.sort(key=lambda x: (x[1], -ord(x[0])))

            # 輸出結果
            # 遍歷排序後的列表
            for char, count in char_list:
                # ord(char) 獲取 ASCII 值
                ascii_val = ord(char)
                # 使用 f-string 格式化輸出
                # f"{ascii_val} {count}" 會插入變數值
                print(f"{ascii_val} {count}")

    except EOFError:
        # 當到達檔案結尾時，會引發 EOFError
        # 我們捕獲異常並正常結束程式
        pass

# 這是 Python 的標準寫法
# 當腳本直接執行時，__name__ == "__main__"
# 如果被 import，__name__ 是模組名
if __name__ == "__main__":
    # 呼叫主函數開始執行
    main()