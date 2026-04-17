# 題目 100: UVA 100 - 3n+1 問題 (簡化版本)
# 這個簡化版本直接計算每個數字的 cycle length，沒有使用記憶化。
# 適合用來記憶基本邏輯。

def cycle_length(n):
    """
    計算數字 n 的 cycle length。
    
    參數:
    n (int): 輸入的正整數
    
    返回:
    int: n 的 cycle length
    """
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

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

# 範例使用
if __name__ == "__main__":
    # 測試範例
    print(find_max_cycle(1, 10))  # 應該是 20
    print(find_max_cycle(100, 200))  # 測試更大範圍