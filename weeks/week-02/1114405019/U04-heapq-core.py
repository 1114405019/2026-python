# U04. heap 為何能高效拿 Top-N（1.4）
"""
heap 為何能高效拿 Top-N

heapq 模組實現了最小堆算法，能夠在 O(log n) 時間內插入元素，
並在 O(1) 時間內訪問最小元素，這使得它非常適合尋找 Top-N 元素。
"""

import heapq

# 基礎用法
print("=== 基礎用法 ===")

# 創建堆
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"原始數據: {numbers}")

# 轉換為堆（原地修改）
heapq.heapify(numbers)
print(f"堆化後: {numbers}")

# 添加元素
heapq.heappush(numbers, 7)
print(f"添加7後: {numbers}")

# 移除並返回最小元素
smallest = heapq.heappop(numbers)
print(f"移除最小元素 {smallest}, 剩餘: {numbers}")

# 查看最小元素（不移除）
print(f"當前最小: {numbers[0]}")

# 進階應用
print("\n=== 進階應用 ===")

# 找到最大的 N 個元素
data = [1, 8, 3, 7, 2, 9, 4, 6, 5, 10]
k = 3

# 方法1: 使用 nlargest
largest = heapq.nlargest(k, data)
print(f"最大的 {k} 個元素: {largest}")

# 方法2: 使用 nsmallest + 負數（找最大）
largest_manual = [-x for x in heapq.nsmallest(k, [-x for x in data])]
print(f"手動找最大 {k} 個: {largest_manual}")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 成績排行榜
class ScoreManager:
    def __init__(self, top_n=5):
        self.scores = []
        self.top_n = top_n

    def add_score(self, student, score):
        heapq.heappush(self.scores, (score, student))
        # 保持只有 top_n 個
        if len(self.scores) > self.top_n:
            heapq.heappop(self.scores)

    def get_top_scores(self):
        # 返回從高到低的排序
        return sorted(self.scores, reverse=True)

manager = ScoreManager(top_n=3)

scores_data = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 88),
    ("Eve", 95),
    ("Frank", 82)
]

for student, score in scores_data:
    manager.add_score(student, score)

print("前3名成績:")
for score, student in manager.get_top_scores():
    print(f"  {student}: {score}")

# 案例2: 實時銷售排行
class SalesTracker:
    def __init__(self, top_products=5):
        self.sales = []
        self.top_products = top_products

    def record_sale(self, product, amount):
        # 使用負數使最大堆變最小堆
        heapq.heappush(self.sales, (-amount, product))
        if len(self.sales) > self.top_products:
            heapq.heappop(self.sales)

    def get_top_products(self):
        return [(-amount, product) for amount, product in sorted(self.sales, reverse=True)]

tracker = SalesTracker(top_n=3)

sales_data = [
    ("筆記本電腦", 25000),
    ("手機", 15000),
    ("平板電腦", 12000),
    ("鍵盤", 2000),
    ("滑鼠", 800),
    ("顯示器", 8000),
    ("耳機", 3000),
    ("充電器", 1500)
]

for product, amount in sales_data:
    tracker.record_sale(product, amount)

print("\n銷售排行榜:")
for amount, product in tracker.get_top_products():
    print(f"  {product}: ${amount:,}")

# 案例3: 系統監控 - 最高CPU使用率
class SystemMonitor:
    def __init__(self, max_records=10):
        self.cpu_usage = []
        self.max_records = max_records

    def record_cpu(self, timestamp, usage):
        heapq.heappush(self.cpu_usage, (-usage, timestamp, usage))
        if len(self.cpu_usage) > self.max_records:
            heapq.heappop(self.cpu_usage)

    def get_peak_usage(self, n=5):
        # 返回最高的 n 個記錄
        peaks = heapq.nsmallest(n, self.cpu_usage)
        return [(-usage, timestamp, usage) for usage, timestamp, original_usage in peaks]

monitor = SystemMonitor(max_records=5)

# 模擬CPU使用率數據
cpu_data = [
    ("10:00", 45.2),
    ("10:05", 67.8),
    ("10:10", 23.1),
    ("10:15", 89.5),
    ("10:20", 34.7),
    ("10:25", 92.3),
    ("10:30", 56.4),
    ("10:35", 78.9)
]

for timestamp, usage in cpu_data:
    monitor.record_cpu(timestamp, usage)

print("\nCPU使用率峰值:")
peaks = monitor.get_peak_usage(3)
for usage, timestamp, _ in peaks:
    print(f"  {timestamp}: {usage:.1f}%")

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. heapq.heapify() 將列表轉換為堆，O(n) 時間
2. heapq.heappush() 添加元素，O(log n) 時間
3. heapq.heappop() 移除最小元素，O(log n) 時間
4. heapq.nlargest(n, iterable) 找最大的 n 個元素
5. heapq.nsmallest(n, iterable) 找最小的 n 個元素
6. 最小堆: 預設是最小堆，要找最大值需使用負數
7. 適用場景: Top-N 查找、優先隊列、實時排行榜
8. 記憶體效率: 不需要排序整個數據集
"""

import heapq

nums = [5, 1, 9, 2]
h = nums[:]
heapq.heapify(h)
# h[0] 永遠是最小值（這是 heap 的核心性質）
m = heapq.heappop(h)  # 每次 pop 都拿到目前最小
