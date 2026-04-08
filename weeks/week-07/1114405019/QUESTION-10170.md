# 題目 10170

**題名**: UVA 10170 — The Hotel with Infinite Rooms

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a163)
- [UVA Online Judge](https://uva.onlinejudge.org/external/10170.pdf)

## 題目敘述

HaluaRuti 城裡有一家奇特的旅館，擁有**無限多間房間**。

旅館的住宿規則如下：

- 同一時間只能有**一個旅行團**住宿。
- 每個旅行團**早上入住，傍晚退房**。
- 前一個旅行團退房的**隔天早上**，下一個旅行團入住。
- **每個旅行團的人數比前一個多 1 人**（起始旅行團除外，其人數為 S）。
- 一個有 **n 人**的旅行團，會住 **n 天**。

例如：若起始旅行團有 4 人，則第 1~4 天住 4 人團，第 5~9 天住 5 人團，以此類推。

給定起始旅行團的人數 **S** 和查詢天數 **D**，請找出**第 D 天住宿的旅行團有幾人**。

## 輸入說明

- 每行包含兩個整數 **S**（1 ≤ S ≤ 10000）和 **D**（1 ≤ D < 10¹⁵）。
- 所有輸入和輸出整數均小於 10¹⁵。
- 輸入直到 **EOF** 結束。

## 輸出說明

每行輸入對應一行輸出，為**第 D 天住宿的旅行團人數**。

---

## 解題思路

這題要求計算第 D 天住宿的人數。從起始團人數 S 開始，團的人數會依序增加 1 人，且每個團住的天數等於該團人數。

累計天數公式為從 S 開始的等差數列：T(k) = S + (S+1) + ... + k = k(k+1)/2 - (S-1)S/2。給定 D，求最小的 k 使 T(k) >= D，該 k 即為第 D 天的團人數。

## 解題代碼

```python
import sys


def find_group_size(start, day):
    offset = (start - 1) * start // 2
    target = day + offset
    lo = start
    hi = max(start, int((2 * target) ** 0.5) + 3)
    while lo < hi:
        mid = (lo + hi) // 2
        if mid * (mid + 1) // 2 >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo


def main():
    lines = sys.stdin.read().strip().split()
    if not lines:
        return
    out_lines = []
    for i in range(0, len(lines), 2):
        try:
            s = int(lines[i])
            d = int(lines[i + 1])
        except (IndexError, ValueError):
            break
        out_lines.append(str(find_group_size(s, d)))
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
```

## 測試用例

```
輸入:
4 1
5 6

輸出:
4
6
```
