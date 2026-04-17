"""heapq

1. 取得最大/最小前 N 筆
2. 支援可比對元素與 key 函式
3. heapify 與 heappop 操作最小堆
"""

import heapq

# 直接使用 nlargest/nsmallest 取得前 N 筆元素
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.nlargest(3, nums)
heapq.nsmallest(3, nums)

# 對字典列表使用 key 參數，以 price 欄位做比較
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
]
heapq.nsmallest(1, portfolio, key=lambda s: s['price'])

# 將 list 轉換成堆後，可用 heappop 取出最小值
heap = list(nums)
heapq.heapify(heap)
heapq.heappop(heap)
