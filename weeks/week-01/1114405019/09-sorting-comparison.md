# Python 比較運算與排序深度解析

## 概述

本文深入探討 Python 中的比較運算、排序機制以及 `key` 函數的應用。通過分析 Tuple 的逐個元素比較原理、Lambda 表達式的實用性，以及排序演算法的時間複雜度，為開發者提供全面的技術洞見。

## 語法解析

### 比較運算符

Python 支持標準比較運算符：`<`, `<=`, `>`, `>=`, `==`, `!=`

對於序列類型（如 Tuple、List），比較遵循字典序（Lexicographical Order）：
- 從左到右逐個元素比較
- 遇到第一個不相等元素時決定結果
- 如果一個序列是另一個的前綴，較短的序列較小

### sorted() 函數

```python
sorted(iterable, key=None, reverse=False)
```

- `iterable`：要排序的可迭代對象
- `key`：用於提取比較鍵的函數
- `reverse`：是否降序排序

### key 參數與 Lambda

`key` 參數接受一個函數，該函數對每個元素調用一次，返回用於比較的值：

```python
sorted(data, key=lambda x: x['attribute'])
```

Lambda 表達式提供簡潔的匿名函數定義。

## 比較表格

| 方法 | 適用場景 | 靈活性 | 效能 | 內存使用 |
|------|----------|--------|------|----------|
| 基本 sorted() | 簡單類型排序 | 低 | 高 | 中等 |
| key 參數排序 | 複雜對象排序 | 高 | 中等 | 中等 |
| 多重條件排序 | 多字段排序 | 很高 | 中等 | 中等 |
| min/max + key | 查找極值 | 高 | 高 | 低 |
| 手動比較 | 自定義邏輯 | 最高 | 低 | 低 |

## Big O 複雜度分析

### 時間複雜度

- **Timsort (sorted() 預設)**：$O(n \log n)$ 最壞情況
  - $n$：元素數量
  - $\log n$：比較層次
- **key 函數應用**：$O(n)$ 鍵值計算 + $O(n \log n)$ 排序
- **Tuple 比較**：$O(k)$ 其中 $k$ 為比較的元素數（通常 $k \ll n$）
- **min/max 掃描**：$O(n)$ 線性掃描

### 空間複雜度

- **基本排序**：$O(n)$ 創建新列表
- **key 排序**：$O(n)$ 鍵值存儲 + $O(n)$ 結果
- **原地排序 (list.sort())**：$O(1)$ 額外空間

## 技術點分析：Tuple 逐個元素比較

Python 中的 Tuple 比較遵循字典序原理：

```python
a = (1, 2)
b = (1, 3)
result = a < b  # True，因為 2 < 3

c = (1, 2, 4)
d = (1, 2, 3, 5)
result2 = c > d  # True，因為在第三個元素處 4 > 3
```

## Lambda 應用實例

```python
# 基本 key 排序
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
rows_sorted = sorted(rows, key=lambda r: r['uid'])

# min/max 搭配 key
smallest = min(rows, key=lambda r: r['uid'])
largest = max(rows, key=lambda r: r['uid'])
```

## 擴充範例：多重條件排序

```python
users = [
    {'uid': 3, 'name': 'Alice'},
    {'uid': 1, 'name': 'Bob'},
    {'uid': 2, 'name': 'Charlie'},
    {'uid': 1, 'name': 'Alice'}
]

# 先按 uid 升序，再按 name 升序
users_sorted = sorted(users, key=lambda u: (u['uid'], u['name']))
```

## 效能最佳實踐

- 使用 `key` 參數避免重複計算
- 對於大數據集，考慮原地排序 `list.sort()`
- 多重條件排序使用 Tuple 鍵值
- 理解 Timsort 的自適應特性

## 結論

掌握 Python 的比較運算和排序機制，能夠幫助開發者編寫更高效、更可讀的代碼。通過理解字典序比較、善用 `key` 參數，以及認識排序演算法的複雜度，可以在處理數據時做出更好的設計決策。