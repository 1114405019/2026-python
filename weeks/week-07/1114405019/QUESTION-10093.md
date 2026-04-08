# 題目 10093

**題名**: UVA 10093

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a086)
- [Yui Huang 題解](https://yuihuang.com/zj-a086/)

## 題目敘述

司令部的將軍們打算在 **N×M 的網格地圖**上部署炮兵部隊。

地圖的每一格可能是：
- **山地**（用 `H` 表示）：不能部署炮兵
- **平原**（用 `P` 表示）：每格最多可部署一支炮兵部隊

一支炮兵部隊的**攻擊範圍**為：沿橫向左右各兩格，沿縱向上下各兩格（攻擊範圍不受地形影響）。

為了**防止誤傷**，任何兩支炮兵部隊之間不能互相攻擊（即任何一支炮兵部隊都不在其他支炮兵部隊的攻擊範圍內）。

請問在整個地圖區域內，**最多能部署多少支炮兵部隊**？

## 輸入說明

- 第一行包含兩個正整數 **N** 和 **M**，以空格分隔（**N ≤ 100，M ≤ 10**）。
- 接下來的 N 行，每行含有連續的 M 個字元（`P` 或 `H`），表示地圖各列的地形。

## 輸出說明

輸出一個整數 **K**，表示最多能部署的炮兵部隊數量。

---

## 解題思路

這題可以用狀態壓縮動態規劃求解。每一列的佈置由一個長度 M 的位元遮罩表示，位元 1 代表該格可放炮兵且實際放置了炮兵。對於同一列，炮兵之間不能在水平方向上相隔 1 或 2 格，因此列遮罩必須滿足此條件。

另外，炮兵的攻擊範圍在縱向可達上下兩列，因此一列的佈置必須和前一列、前兩列在同一列位置上沒有重疊。用 DP 將上一列和上兩列的狀態一同記錄起來，就能求出最大值。

## 解題代碼

```python
import sys


def count_bits(x):
    return bin(x).count("1")


def is_valid_row(mask):
    return (mask & (mask << 1)) == 0 and (mask & (mask << 2)) == 0


def main():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    first = data[0].strip().split()
    if len(first) < 2:
        return
    n = int(first[0])
    m = int(first[1])
    grid = [line.strip() for line in data[1:1 + n]]

    row_masks = []
    for row in grid:
        mask = 0
        for j, ch in enumerate(row):
            if ch == "P":
                mask |= 1 << j
        row_masks.append(mask)

    all_valid = [mask for mask in range(1 << m) if is_valid_row(mask)]
    dp = {(0, 0): 0}

    for r in range(n):
        available = [mask for mask in all_valid if (mask & row_masks[r]) == mask]
        new_dp = {}
        for (prev, prev2), value in dp.items():
            for cur in available:
                if (cur & prev) != 0 or (cur & prev2) != 0:
                    continue
                key = (cur, prev)
                new_dp[key] = max(new_dp.get(key, -1), value + count_bits(cur))
        dp = new_dp

    answer = max(dp.values()) if dp else 0
    sys.stdout.write(str(answer))


if __name__ == "__main__":
    main()
```

## 測試用例

```
輸入:
2 3
PPP
PHP

輸出:
2
```
