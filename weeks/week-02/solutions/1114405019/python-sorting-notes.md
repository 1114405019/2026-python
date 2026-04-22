# Python 比較運算與 Key 函數排序深度解析

## 概述

本文深入探討 Python 中的比較運算、排序機制以及 `key` 函數的應用。通過分析 Tuple 的逐個元素比較原理、Lambda 表達式的實用性，以及排序演算法的時間複雜度，為開發者提供全面的技術洞見。

## 技術點分析：Tuple 逐個元素比較（Lexicographical Order）

Python 中的 Tuple 比較遵循 **字典序（Lexicographical Order）** 原理，這意味著比較是從左到右逐個元素進行的，直到找到第一個不相等的元素對。

### 基本原理

當比較兩個 Tuple 時，Python 會：
1. 比較第一個元素
2. 如果相等，繼續比較第二個元素
3. 依此類推，直到找到差異或其中一個 Tuple 結束

```python
# 範例：Tuple 比較
a = (1, 2)
b = (1, 3)
result = a < b  # True，因為 2 < 3

# 更複雜的範例
c = (1, 2, 4)
d = (1, 2, 3, 5)
result2 = c > d  # True，因為在第三個元素處 4 > 3
```

這種比較方式類似於字典中單詞的排序：先比較第一個字母，如果相同則比較第二個，以此類推。

## Lambda 應用：sorted() 與 min/max 中 key 參數的使用時機與優勢

`key` 參數允許我們指定一個函數來提取比較的鍵值，這在處理複雜數據結構時特別有用。

### 使用時機

- 當需要根據對象的特定屬性排序時
- 處理字典列表或自定義對象時
- 需要自定義排序邏輯時

### 優勢

- **靈活性**：可以使用任意函數作為鍵
- **效能**：鍵值只計算一次，避免重複計算
- **可讀性**：Lambda 表達式使代碼簡潔

```python
# 基本 key 排序
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
rows_sorted = sorted(rows, key=lambda r: r['uid'])

# min/max 搭配 key
smallest = min(rows, key=lambda r: r['uid'])
largest = max(rows, key=lambda r: r['uid'])
```

## 時間複雜度：Python Timsort 演算法

Python 的 `sorted()` 函數使用 **Timsort** 演算法，這是一種混合排序演算法，結合了插入排序和合併排序的特點。

### Big O 表示

Timsort 的時間複雜度為 **$O(n \log n)$**，其中：
- $n$ 是要排序的元素數量
- $\log n$ 表示比較操作的層次

這種複雜度在最壞情況下保證了高效的排序性能，使其適用於大多數實際應用場景。

## 擴充範例：多重條件排序

在實際應用中，經常需要根據多個條件進行排序。例如，先按用戶 ID 排序，再按名稱排序。

```python
# 多重條件排序範例
users = [
    {'uid': 3, 'name': 'Alice'},
    {'uid': 1, 'name': 'Bob'},
    {'uid': 2, 'name': 'Charlie'},
    {'uid': 1, 'name': 'Alice'}
]

# 先按 uid 升序，再按 name 升序
users_sorted = sorted(users, key=lambda u: (u['uid'], u['name']))

# 結果：
# [{'uid': 1, 'name': 'Alice'}, {'uid': 1, 'name': 'Bob'}, 
#  {'uid': 2, 'name': 'Charlie'}, {'uid': 3, 'name': 'Alice'}]
```

在這個範例中，`key=lambda u: (u['uid'], u['name'])` 創建了一個 Tuple 作為排序鍵，Python 會先比較 `uid`，如果相等再比較 `name`。

## 相關概念補充

### 容器操作與推導式

Python 的列表推導式提供了一種簡潔的方式來創建列表：

```python
nums = [1, -2, 3, -4]
positives = [n for n in nums if n > 0]  # [1, 3]

pairs = [('a', 1), ('b', 2)]
lookup = {k: v for k, v in pairs}  # {'a': 1, 'b': 2}
```

### 生成器表達式

生成器表達式類似於列表推導式，但返回一個生成器，可以節省內存：

```python
squares_sum = sum(n * n for n in nums)  # 計算平方和
```

### 模組與類別基礎

```python
from collections import deque

q = deque(maxlen=2)
q.append(1)
q.append(2)
q.append(3)  # 自動丟掉最舊的元素

class User:
    def __init__(self, user_id):
        self.user_id = user_id

u = User(42)
```

### 例外處理

```python
def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False
```

### Big-O 複雜度提示

- `list.append()` 通常是 $O(1)$
- 列表切片操作是 $O(n)$

## 結論

掌握 Python 的比較運算和排序機制，能夠幫助開發者編寫更高效、更可讀的代碼。通過理解 Tuple 的字典序比較、善用 `key` 參數，以及認識排序演算法的複雜度，可以在處理數據時做出更好的設計決策。