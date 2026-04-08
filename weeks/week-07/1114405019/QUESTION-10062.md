# 題目 10062

**題名**: UVA 10062

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a055)
- [Yui Huang 題解](https://yuihuang.com/zj-a055/)

## 題目敘述

有 N 頭（2 ≤ N ≤ 80,000）乳牛，每頭乳牛都有一個在 1 到 N 範圍內的獨特編號。
牠們在晚餐前去附近的「飲水站」喝了太多啤酒，一時判斷失準。
排隊吃晚飯時，牠們沒有依照編號從小到大的正確順序排列。
不幸的是，農夫 FJ 無法直接幫牠們排序，而且他的觀察能力也不太好。
他沒有記錄每頭乳牛的編號，而是統計了一個奇怪的數據：對於隊伍中的每頭乳牛，他知道在該乳牛前面、編號比它小的乳牛有幾頭。
請根據這份資料，告訴 FJ 乳牛的正確排列順序。

## 輸入說明

- 第 1 行：一個整數 N。
- 第 2 至 N 行：共 N-1 行，每行描述該位置的乳牛前面、編號比它小的乳牛數量。
  第一頭乳牛前面沒有任何乳牛，因此不列出。
  第 2 行描述第 2 個位置的乳牛前面編號較小的牛數；第 3 行描述第 3 個位置的情形，以此類推。

## 輸出說明

- 共 N 行，每行輸出該位置乳牛的編號。
  第 1 行為隊伍第 1 個位置的乳牛編號，第 2 行為第 2 個位置，以此類推。

---

## 解題思路

這題要求從每個位置前方較小編號的牛數，重建整個隊伍排列。由於乳牛編號為 1~N 的全排列，第 i 個位置的描述等同於該位置上的編號在剩餘可選編號中的「第 k 小」元素。

我們可從最後一個位置往前重建，使用 Fenwick tree（Binary Indexed Tree）維護目前還可用的編號集合。對於位置 i，從樹中查找第 counts[i] + 1 個可用編號，並將其移除。這樣整體時間為 O(N log N)，空間 O(N)。

## 解題代碼

```python
import sys


def build_fenwick(n):
    bit = [0] * (n + 1)
    for i in range(1, n + 1):
        j = i
        while j <= n:
            bit[j] += 1
            j += j & -j
    return bit


def fenwick_find(bit, k):
    idx = 0
    step = 1 << (len(bit).bit_length() - 1)
    while step:
        nxt = idx + step
        if nxt < len(bit) and bit[nxt] < k:
            k -= bit[nxt]
            idx = nxt
        step >>= 1
    return idx + 1


def fenwick_add(bit, idx, val):
    while idx < len(bit):
        bit[idx] += val
        idx += idx & -idx


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    counts = [0] * (n + 1)
    for i in range(2, n + 1):
        if len(data) > i - 1:
            counts[i] = int(data[i - 1])

    bit = build_fenwick(n)
    result = [0] * (n + 1)
    for i in range(n, 1, -1):
        pos = fenwick_find(bit, counts[i] + 1)
        result[i] = pos
        fenwick_add(bit, pos, -1)

    result[1] = fenwick_find(bit, 1)
    sys.stdout.write("\n".join(str(result[i]) for i in range(1, n + 1)))


if __name__ == "__main__":
    main()
```

## 測試用例

```
輸入:
4
0
1
1

輸出:
4
1
3
2
```
