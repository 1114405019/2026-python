# 火車車廂排序，簡化版
# 算逆序對，用雙迴圈，記得交換次數

def count_inversions(arr):
    # 算逆序對數
    # arr 是列表
    # 返回逆序數
    inv = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv += 1
    return inv

# 測試
if __name__ == "__main__":
    print(count_inversions([1, 3, 2]))  # 1
    print(count_inversions([3, 1, 2]))  # 2