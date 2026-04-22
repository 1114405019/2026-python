# 3n+1 問題，簡化版
# 直接算每個數的 cycle，沒用記憶化，記得基本邏輯就好

def cycle_length(n):
    # 算 n 的 cycle length
    # n 是正整數
    # 返回那個長度
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

def find_max_cycle(i, j):
    # 找區間 [min(i,j), max(i,j)] 裡最大的 cycle
    # i, j 是數字
    # 返回最大值
    min_val = min(i, j)
    max_val = max(i, j)
    max_cycle = 0
    for num in range(min_val, max_val + 1):
        max_cycle = max(max_cycle, cycle_length(num))
    return max_cycle

# 測試用
if __name__ == "__main__":
    # 試試看
    print(find_max_cycle(1, 10))  # 應該 20
    print(find_max_cycle(100, 200))  # 大一點的測試