# 題目 299: UVA 299 - 火車車廂排序 (簡化版本)
# 使用簡單雙迴圈計算逆序對數。

def count_inversions(arr):
    """計算逆序對數"""
    inv = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv += 1
    return inv

# 範例
if __name__ == "__main__":
    print(count_inversions([1, 3, 2]))  # 1
    print(count_inversions([3, 1, 2]))  # 2