# 題目 299: UVA 299 - 火車車廂排序
# 計算將火車車廂排序到 1 到 L 順序所需的最少相鄰交換次數，即逆序對數。

import sys

def count_inversions(arr):
    """
    使用合併排序計算逆序對數。
    
    參數:
    arr (list): 排列列表
    
    返回:
    int: 逆序對數
    """
    def merge_sort(start, end):
        if start >= end:
            return 0
        mid = (start + end) // 2
        inv = merge_sort(start, mid) + merge_sort(mid + 1, end)
        i, j, k = start, mid + 1, start
        temp = [0] * (end - start + 1)
        idx = 0
        while i <= mid and j <= end:
            if arr[i] <= arr[j]:
                temp[idx] = arr[i]
                i += 1
            else:
                temp[idx] = arr[j]
                inv += (mid - i + 1)  # 所有剩餘的 i 都大於 arr[j]
                j += 1
            idx += 1
        while i <= mid:
            temp[idx] = arr[i]
            i += 1
            idx += 1
        while j <= end:
            temp[idx] = arr[j]
            j += 1
            idx += 1
        for p in range(len(temp)):
            arr[start + p] = temp[p]
        return inv
    
    return merge_sort(0, len(arr) - 1)

def main():
    """
    主函數，讀取測試資料並輸出結果。
    """
    input_lines = sys.stdin.readlines()
    N = int(input_lines[0].strip())
    line_idx = 1
    for _ in range(N):
        L = int(input_lines[line_idx].strip())
        line_idx += 1
        cars = list(map(int, input_lines[line_idx].strip().split()))
        line_idx += 1
        swaps = count_inversions(cars)
        print(f"Optimal train swapping takes {swaps} swaps.")

if __name__ == "__main__":
    main()