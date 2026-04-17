# R04. heapq：高效能 Top-N 元素查找
# ============================================================================
# heapq 模組提供堆積隊列演算法，專門用於高效能的 Top-N 查找
# 堆積是一種特殊的樹狀結構，能在 O(log n) 時間內插入和刪除元素
# nlargest() 和 nsmallest() 是最常用的函數，用於查找最大/最小 N 個元素
# ============================================================================

import heapq

## 1. 基礎 Top-N 查找
# --------------------------------------------------------------------------
# nlargest() 和 nsmallest() 是最簡單的方式獲取 Top-N 元素

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(f"原始數列：{nums}")

# 獲取最大的 3 個元素
largest_3 = heapq.nlargest(3, nums)
print(f"最大的 3 個：{largest_3}")

# 獲取最小的 3 個元素
smallest_3 = heapq.nsmallest(3, nums)
print(f"最小的 3 個：{smallest_3}")

## 2. 使用 key 函數的自訂排序
# --------------------------------------------------------------------------
# 可以指定 key 參數來自訂比較基準

# 範例：股票投資組合，按價格排序
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'GOOG', 'shares': 200, 'price': 98.5},
    {'name': 'MSFT', 'shares': 75, 'price': 234.56},
]

# 按價格找最便宜的股票
cheapest = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])
print(f"最便宜的股票：{cheapest[0]}")

# 按股數找最多的股票
most_shares = heapq.nlargest(2, portfolio, key=lambda s: s['shares'])
print(f"持有股數最多的 2 支股票：{[s['name'] for s in most_shares]}")

## 3. 手動堆積操作
# --------------------------------------------------------------------------
# heapq 也提供手動操作堆積的方法

# 將列表轉換為堆積
heap = list(nums)
heapq.heapify(heap)
print(f"轉換為堆積：{heap}")

# 彈出最小元素
min_val = heapq.heappop(heap)
print(f"彈出最小值：{min_val}, 剩餘堆積：{heap}")

# 推入新元素
heapq.heappush(heap, 0)
print(f"推入 0 後：{heap}")

# 推入並彈出（更高效）
heapq.heappushpop(heap, 50)
print(f"推入 50 並彈出最小值後：{heap}")

## 4. 實現優先隊列
# --------------------------------------------------------------------------
# 使用 heapq 可以實現優先隊列

class PriorityQueue:
    """簡單的優先隊列實現"""

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        """推入元素和優先級"""
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        """彈出最高優先級的元素"""
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        return len(self._queue) == 0

# 測試優先隊列
pq = PriorityQueue()
pq.push('任務 A', 3)  # 優先級 3
pq.push('任務 B', 1)  # 優先級 1
pq.push('任務 C', 2)  # 優先級 2

print("按優先級處理任務：")
while not pq.is_empty():
    task = pq.pop()
    print(f"處理：{task}")

## 5. Top-N 的高階應用
# --------------------------------------------------------------------------
# 合併多個排序列表
def merge_sorted_lists(*lists):
    """合併多個已排序的列表"""
    return list(heapq.merge(*lists))

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
list3 = [0, 9, 10]
merged = merge_sorted_lists(list1, list2, list3)
print(f"合併排序列表：{merged}")

# 查找第 N 大的元素
def find_nth_largest(nums, n):
    """查找第 n 大的元素"""
    if n <= 0 or n > len(nums):
        return None
    return heapq.nlargest(n, nums)[-1]

nums = [3, 1, 4, 1, 5, 9, 2, 6]
third_largest = find_nth_largest(nums, 3)
print(f"第 3 大的元素：{third_largest}")

## 6. 效能比較與注意事項
# --------------------------------------------------------------------------
# heapq 的 nlargest/nsmallest 在大多數情況下比 sorted() 更高效

import time
import random

# 生成測試資料
test_data = [random.randint(0, 10000) for _ in range(10000)]

# 使用 heapq.nlargest
start = time.time()
result_heapq = heapq.nlargest(100, test_data)
heapq_time = time.time() - start

# 使用 sorted
start = time.time()
result_sorted = sorted(test_data, reverse=True)[:100]
sorted_time = time.time() - start

print(".4f")
print(".4f")
print(".2f")

# 驗證結果正確性
assert result_heapq == result_sorted, "結果不一致！"

## 7. 實際應用：實時 Top-K 統計
# --------------------------------------------------------------------------
# 在資料流中維護 Top-K 元素

class TopKTracker:
    """實時追蹤 Top-K 元素"""

    def __init__(self, k):
        self.k = k
        self.heap = []

    def add(self, item):
        """新增元素到追蹤器"""
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, item)
        elif item > self.heap[0]:
            heapq.heapreplace(self.heap, item)

    def get_top_k(self):
        """獲取當前 Top-K 元素（降序）"""
        return sorted(self.heap, reverse=True)

# 測試 Top-K 追蹤器
tracker = TopKTracker(3)
stream_data = [5, 3, 8, 1, 9, 2, 7, 4, 6]
for num in stream_data:
    tracker.add(num)

print(f"資料流：{stream_data}")
print(f"Top-3 元素：{tracker.get_top_k()}")

# ============================================================================
# 語法重點總結：
# 1. nlargest/nsmallest 用於高效 Top-N 查找
# 2. key 參數支援自訂比較基準
# 3. heapify 將列表轉為堆積結構
# 4. heappush/heappop 用於堆積操作
# 5. 適用於優先隊列、排序合併等場景
# ============================================================================
