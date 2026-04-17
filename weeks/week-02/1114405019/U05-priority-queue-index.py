# U05. 優先佇列為何要加 index（1.5）
"""
優先佇列為何要加 index

在 heapq 實現的優先隊列中，當優先級相同時，為了確保先進先出（FIFO）的順序，
需要添加索引來打破平局。這避免了相同優先級元素的任意順序問題。
"""

import heapq
from itertools import count

# 基礎用法
print("=== 基礎用法 ===")

# 創建優先隊列
pq = []

# 添加任務 (優先級, 任務名稱)
heapq.heappush(pq, (3, "低優先級任務"))
heapq.heappush(pq, (1, "高優先級任務"))
heapq.heappush(pq, (2, "中優先級任務"))
heapq.heappush(pq, (1, "另一個高優先級任務"))

print("處理任務順序:")
while pq:
    priority, task = heapq.heappop(pq)
    print(f"優先級 {priority}: {task}")

# 問題：相同優先級的順序不穩定
print("\n=== 相同優先級的問題 ===")

pq2 = []
heapq.heappush(pq2, (1, "任務A"))
heapq.heappush(pq2, (1, "任務B"))
heapq.heappush(pq2, (1, "任務C"))

print("相同優先級任務處理順序:")
while pq2:
    priority, task = heapq.heappop(pq2)
    print(f"優先級 {priority}: {task}")

# 進階應用
print("\n=== 進階應用 ===")

# 使用索引確保 FIFO 順序
pq_with_index = []
counter = count()  # 無限計數器

def push_task(priority, task):
    heapq.heappush(pq_with_index, (priority, next(counter), task))

def pop_task():
    if pq_with_index:
        priority, index, task = heapq.heappop(pq_with_index)
        return task
    return None

# 添加任務
push_task(1, "高優先級任務1")
push_task(2, "中優先級任務1")
push_task(1, "高優先級任務2")  # 後進，但優先級相同
push_task(1, "高優先級任務3")  # 最後進
push_task(3, "低優先級任務1")

print("使用索引的優先隊列處理順序:")
while True:
    task = pop_task()
    if task is None:
        break
    print(f"處理: {task}")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 任務調度器
class TaskScheduler:
    def __init__(self):
        self.tasks = []
        self.counter = count()

    def add_task(self, priority, task_name, description=""):
        heapq.heappush(self.tasks, (priority, next(self.counter), task_name, description))

    def get_next_task(self):
        if self.tasks:
            priority, index, name, desc = heapq.heappop(self.tasks)
            return f"{name}: {desc}" if desc else name
        return None

    def get_queue_status(self):
        return [(p, n) for p, i, n, d in sorted(self.tasks)]

scheduler = TaskScheduler()

# 添加不同優先級的任務
scheduler.add_task(1, "系統更新", "緊急安全補丁")
scheduler.add_task(2, "資料備份", "每日例行備份")
scheduler.add_task(1, "錯誤修復", "生產環境當機")
scheduler.add_task(3, "功能優化", "非緊急改進")
scheduler.add_task(2, "日誌清理", "磁碟空間管理")

print("任務隊列狀態:")
for priority, name in scheduler.get_queue_status():
    print(f"  優先級 {priority}: {name}")

print("\n執行任務:")
while True:
    task = scheduler.get_next_task()
    if task is None:
        break
    print(f"  ✓ {task}")

# 案例2: 訂單處理系統
class OrderProcessor:
    def __init__(self):
        self.orders = []
        self.order_counter = count()

    def add_order(self, priority, order_id, customer_type, amount):
        # 優先級: VIP > 普通 > 大單
        priority_score = {
            'VIP': 1,
            '大單': 2,
            '普通': 3
        }.get(customer_type, 3)

        heapq.heappush(self.orders, (priority_score, next(self.order_counter), order_id, customer_type, amount))

    def process_next_order(self):
        if self.orders:
            priority, index, order_id, customer_type, amount = heapq.heappop(self.orders)
            return f"訂單 {order_id} ({customer_type}, ${amount})"
        return None

processor = OrderProcessor()

orders = [
    (1, "ORD001", "普通", 150),
    (2, "ORD002", "VIP", 200),
    (3, "ORD003", "大單", 500),
    (4, "ORD004", "普通", 75),
    (5, "ORD005", "VIP", 300),
    (6, "ORD006", "普通", 125)
]

for order_id, customer_type, amount in orders:
    processor.add_order(0, order_id, customer_type, amount)

print("\n處理訂單順序:")
processed_count = 0
while processed_count < 6:
    order = processor.process_next_order()
    if order:
        print(f"  {processed_count + 1}. {order}")
        processed_count += 1

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. heapq 實現最小堆，相同優先級順序不穩定
2. 使用 itertools.count() 生成唯一索引
3. 堆元素格式: (priority, index, ...data)
4. 索引確保 FIFO: 相同優先級下，先進的索引較小
5. 適用場景: 任務調度、訂單處理、事件隊列
6. 效能: O(log n) 插入和刪除
7. 記憶體: 每個元素額外儲存索引
"""

import heapq

class Item:
    def __init__(self, name):
        self.name = name

pq = []
# 若只放 (priority, item)，同 priority 會比較 item，Item 不支援 < 會炸
# heapq.heappush(pq, (-1, Item('a')))
# heapq.heappush(pq, (-1, Item('b')))  # TypeError

# 正解：加 index 避免比較 item
idx = 0
heapq.heappush(pq, (-1, idx, Item('a'))); idx += 1
heapq.heappush(pq, (-1, idx, Item('b'))); idx += 1
