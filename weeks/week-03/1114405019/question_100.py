# 題目 100: UVA 100 - 3n+1 問題
# 這個程式解決了 3n+1 猜想問題，計算給定區間內所有數字的最大 cycle length。
# cycle length 定義為從該數字開始，根據規則生成序列直到 1 的長度。

import sys

# 使用字典來儲存已經計算過的 cycle length，以避免重複計算
memo = {}

def cycle_length(n):
    """
    計算數字 n 的 cycle length。
    
    參數:
    n (int): 輸入的正整數
    
    返回:
    int: n 的 cycle length
    """
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    if n % 2 == 0:
        memo[n] = 1 + cycle_length(n // 2)
    else:
        memo[n] = 1 + cycle_length(3 * n + 1)
    return memo[n]

def find_max_cycle(i, j):
    """
    在區間 [min(i,j), max(i,j)] 內找到最大的 cycle length。
    
    參數:
    i (int): 第一個數字
    j (int): 第二個數字
    
    返回:
    int: 區間內的最大 cycle length
    """
    min_val = min(i, j)
    max_val = max(i, j)
    max_cycle = 0
    for num in range(min_val, max_val + 1):
        max_cycle = max(max_cycle, cycle_length(num))
    return max_cycle

def main():
    """
    主函數，讀取標準輸入，處理每一行的測試資料。
    每行包含兩個整數 i 和 j，輸出 i, j 和區間內的最大 cycle length。
    """
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 2:
            continue  # 跳過無效行
        i, j = map(int, parts)
        max_cycle = find_max_cycle(i, j)
        print(f"{i} {j} {max_cycle}")

if __name__ == "__main__":
    main()