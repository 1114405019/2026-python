# 題目 10071

**題名**: UVA 10071

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a064)
- [Yui Huang 題解](https://yuihuang.com/zj-a064/)

## 題目敘述

給定一個整數集合 S，其元素均介於 -30000 到 30000 之間（含首尾）。
請計算满足条件的六元組數量：a + b + c + d + e = f，其中 a、b、c、d、e、f 均屬於 S（可重複使用）。

## 輸入說明

第一行包含一個整數 N（1 ≤ N ≤ 100），代表集合 S 的元素個數。
接下來的 N 行，每行一個整數，為 S 的元素。
所有數字均不重複。

## 輸出說明

輸出符合條件的六元組總數量。

---

## 解題思路

題目要求計算滿足 a + b + c + d + e = f 的六元組數量，且 a,b,c,d,e,f 都來自相同集合 S，允許重複使用。

最直接的做法是先計算所有 a+b+c 的出現次數，再計算所有 d+e 的出現次數。對於每個 f，將 d+e 的值與 f - (d+e) 對應的 a+b+c 次數相乘並累加即可。這樣的時間複雜度為 O(N^3 + N^2)，完全可接受。

## 解題代碼

```python
import sys
from collections import Counter


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    arr = [int(x) for x in data[1:1 + n]]
    sum3 = Counter()
    sum2 = Counter()

    for a in arr:
        for b in arr:
            for c in arr:
                sum3[a + b + c] += 1

    for d in arr:
        for e in arr:
            sum2[d + e] += 1

    total = 0
    for f in arr:
        for s2, count2 in sum2.items():
            total += count2 * sum3[f - s2]

    sys.stdout.write(str(total))


if __name__ == "__main__":
    main()
```

## 測試用例

```
輸入:
2
0
1

輸出:
6
```
