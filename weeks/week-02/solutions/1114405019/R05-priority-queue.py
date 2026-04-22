# R05. 優先隊列：任務調度與事件處理
# ============================================================================
# 優先隊列（Priority Queue）是一種特殊的隊列結構
# 元素按照優先級出隊，而不是先進先出
# 使用 heapq 實現高效能的優先隊列
# 應用於任務調度、事件處理、路徑尋找等場景
# ============================================================================

import heapq
from datetime import datetime, timedelta

## 1. 基礎優先隊列實現
# --------------------------------------------------------------------------
# 使用 heapq 實現優先隊列，優先級數字越大優先級越高

class PriorityQueue:
    """
    優先隊列實現
    使用負數優先級實現最大堆（Python heapq 預設是最小堆）
    """

    def __init__(self):
        self._queue = []  # 儲存 (-priority, index, item) 元組
        self._index = 0   # 用於處理相同優先級的插入順序

    def push(self, item, priority):
        """
        推入元素和優先級
        參數：
            item: 要儲存的元素
            priority: 優先級（數字越大優先級越高）
        """
        # 使用 (-priority, index, item) 確保優先級高的先出隊
        # index 確保相同優先級時先進先出
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        """
        彈出最高優先級的元素
        返回：儲存的元素（不含優先級資訊）
        """
        if self.is_empty():
            raise IndexError("優先隊列為空")
        return heapq.heappop(self._queue)[-1]

    def peek(self):
        """
        查看最高優先級的元素（不移除）
        返回：(item, priority) 元組
        """
        if self.is_empty():
            raise IndexError("優先隊列為空")
        neg_priority, _, item = self._queue[0]
        return item, -neg_priority

    def is_empty(self):
        """檢查隊列是否為空"""
        return len(self._queue) == 0

    def size(self):
        """返回隊列大小"""
        return len(self._queue)

    def clear(self):
        """清空隊列"""
        self._queue.clear()
        self._index = 0

## 2. 優先隊列的基本使用
# --------------------------------------------------------------------------

# 創建優先隊列
pq = PriorityQueue()

# 推入任務（任務名稱, 優先級）
tasks = [
    ("寫報告", 3),
    ("開會", 5),
    ("回郵件", 2),
    ("程式設計", 4),
    ("喝咖啡", 1)
]

print("推入任務到優先隊列：")
for task, priority in tasks:
    pq.push(task, priority)
    print(f"  推入：{task}（優先級 {priority}）")

print(f"\n隊列大小：{pq.size()}")

print("\n按優先級處理任務：")
while not pq.is_empty():
    task = pq.pop()
    print(f"  處理：{task}")

## 3. 進階應用：任務調度系統
# --------------------------------------------------------------------------
# 實現一個更完整的任務調度器

class TaskScheduler:
    """任務調度系統"""

    def __init__(self):
        self.pq = PriorityQueue()
        self.task_id = 0

    def add_task(self, task_name, priority, deadline=None):
        """
        新增任務
        參數：
            task_name: 任務名稱
            priority: 優先級 (1-10)
            deadline: 截止時間 (datetime 物件)
        """
        # 如果有截止時間，調整優先級
        adjusted_priority = priority
        if deadline:
            now = datetime.now()
            time_left = (deadline - now).total_seconds() / 3600  # 小時
            if time_left < 24:  # 24 小時內截止
                adjusted_priority += 2
            elif time_left < 72:  # 3 天內截止
                adjusted_priority += 1

        task = {
            'id': self.task_id,
            'name': task_name,
            'priority': priority,
            'adjusted_priority': adjusted_priority,
            'deadline': deadline,
            'created_at': datetime.now()
        }

        self.pq.push(task, adjusted_priority)
        self.task_id += 1
        return task['id']

    def get_next_task(self):
        """獲取下一個要處理的任務"""
        if self.pq.is_empty():
            return None
        return self.pq.pop()

    def get_pending_tasks(self):
        """獲取所有待處理任務（按優先級排序）"""
        # 注意：這會破壞原隊列，需要重新建構
        tasks = []
        while not self.pq.is_empty():
            tasks.append(self.pq.pop())
        # 重新推入
        for task in reversed(tasks):
            self.pq.push(task, task['adjusted_priority'])
        return tasks

# 測試任務調度器
scheduler = TaskScheduler()

# 新增任務
scheduler.add_task("專案會議", 8, datetime.now() + timedelta(hours=2))
scheduler.add_task("程式碼審查", 6, datetime.now() + timedelta(days=1))
scheduler.add_task("文件編寫", 4, datetime.now() + timedelta(days=3))
scheduler.add_task("測試部署", 7, datetime.now() + timedelta(hours=6))
scheduler.add_task("團隊建設", 3, None)  # 無截止時間

print("\n=== 任務調度系統測試 ===")
print("待處理任務：")
pending = scheduler.get_pending_tasks()
for task in pending:
    deadline_str = task['deadline'].strftime('%m-%d %H:%M') if task['deadline'] else '無'
    print(f"  {task['name']}（優先級：{task['priority']}，調整後：{task['adjusted_priority']}，截止：{deadline_str}）")

print("\n處理任務順序：")
while True:
    task = scheduler.get_next_task()
    if task is None:
        break
    print(f"  處理：{task['name']}")

## 4. 實際應用：事件驅動模擬
# --------------------------------------------------------------------------
# 使用優先隊列模擬事件驅動系統

class Event:
    """事件類別"""
    def __init__(self, time, event_type, data=None):
        self.time = time
        self.event_type = event_type
        self.data = data or {}

    def __str__(self):
        return f"Event({self.time}, {self.event_type}, {self.data})"

class EventSimulator:
    """事件驅動模擬器"""

    def __init__(self):
        self.event_queue = PriorityQueue()
        self.current_time = 0

    def schedule_event(self, delay, event_type, data=None):
        """安排事件"""
        event_time = self.current_time + delay
        event = Event(event_time, event_type, data)
        self.event_queue.push(event, -event_time)  # 時間越小優先級越高
        return event

    def run_simulation(self, max_time):
        """運行模擬"""
        print(f"\n開始模擬（最多 {max_time} 時間單位）...")

        while not self.event_queue.is_empty() and self.current_time < max_time:
            # 獲取下一個事件
            event = self.event_queue.pop()
            self.current_time = event.time

            print(f"時間 {self.current_time}: {event.event_type}")

            # 處理不同類型的事件
            if event.event_type == "customer_arrival":
                # 顧客到達，安排服務
                service_time = event.data.get('service_time', 5)
                self.schedule_event(service_time, "service_complete",
                                  {'customer_id': event.data['customer_id']})

            elif event.event_type == "service_complete":
                print(f"  顧客 {event.data['customer_id']} 服務完成")

# 測試事件模擬
simulator = EventSimulator()

# 安排初始事件
simulator.schedule_event(0, "customer_arrival", {'customer_id': 1, 'service_time': 3})
simulator.schedule_event(2, "customer_arrival", {'customer_id': 2, 'service_time': 5})
simulator.schedule_event(4, "customer_arrival", {'customer_id': 3, 'service_time': 2})

simulator.run_simulation(20)

## 5. 效能考量與最佳實踐
# --------------------------------------------------------------------------
# 優先隊列的效能分析

print("\n=== 效能測試 ===")
import time

# 測試大規模優先隊列操作
pq_test = PriorityQueue()
n = 10000

# 插入測試
start = time.time()
for i in range(n):
    pq_test.push(f"item_{i}", random.randint(1, 100))
insert_time = time.time() - start

# 彈出測試
start = time.time()
while not pq_test.is_empty():
    pq_test.pop()
pop_time = time.time() - start

print(f"插入 {n} 個元素：{insert_time:.4f} 秒")
print(f"彈出 {n} 個元素：{pop_time:.4f} 秒")
print(".4f")

# ============================================================================
# 語法重點總結：
# 1. 使用 (-priority, index, item) 元組實現最大堆
# 2. index 確保相同優先級的 FIFO 順序
# 3. 適用於任務調度、事件處理等場景
# 4. push/pop 操作時間複雜度為 O(log n)
# 5. 可以與 deadline 等因素結合調整優先級
# ============================================================================
