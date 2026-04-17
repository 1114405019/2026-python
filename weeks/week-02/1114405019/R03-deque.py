# R03. deque：高效能雙端隊列
# ============================================================================
# deque (double-ended queue) 是 collections 模組中的雙端隊列
# 相較於列表，deque 在兩端插入和刪除元素更高效
# 特別適用於實現隊列、棧等資料結構，以及滑動視窗等演算法
# ============================================================================

from collections import deque

## 1. 基礎 deque 操作
# --------------------------------------------------------------------------
# deque 支援在兩端高效地新增和移除元素

# 創建空的 deque
q = deque()
print(f"初始 deque：{q}")

# 在右端新增元素
q.append(1)
q.append(2)
print(f"新增元素後：{q}")

# 在左端新增元素
q.appendleft(0)
print(f"左端新增後：{q}")

# 移除右端元素
right = q.pop()
print(f"移除右端：{right}, 剩餘：{q}")

# 移除左端元素
left = q.popleft()
print(f"移除左端：{left}, 剩餘：{q}")

## 2. 固定長度 deque：自動丟棄舊元素
# --------------------------------------------------------------------------
# 設定 maxlen 參數可以創建固定大小的 deque
# 當超過長度時，自動丟棄最舊的元素

print("\n--- 固定長度 deque ---")
q_fixed = deque(maxlen=3)
for i in range(5):
    q_fixed.append(i)
    print(f"新增 {i} 後：{list(q_fixed)}")

# 實際應用：保留最後 N 個元素
recent_items = deque(maxlen=3)
recent_items.append(1)
recent_items.append(2)
recent_items.append(3)
print(f"當前項目：{list(recent_items)}")
recent_items.append(4)  # 自動丟掉最舊的 1
print(f"新增 4 後：{list(recent_items)}")

## 3. deque 的高階操作
# --------------------------------------------------------------------------
# deque 提供更多實用的方法

q = deque([1, 2, 3, 4, 5])
print(f"\n原始 deque：{list(q)}")

# 旋轉操作
q.rotate(2)  # 向右旋轉 2 位
print(f"右旋轉 2 位：{list(q)}")

q.rotate(-1)  # 向左旋轉 1 位
print(f"左旋轉 1 位：{list(q)}")

# 擴展操作
q.extend([6, 7])  # 在右端擴展
print(f"右端擴展：{list(q)}")

q.extendleft([0, -1])  # 在左端擴展（注意順序相反）
print(f"左端擴展：{list(q)}")

## 4. 應用場景：實現隊列和棧
# --------------------------------------------------------------------------
# 使用 deque 可以輕鬆實現各種資料結構

# 實現 FIFO 隊列
class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.popleft() if self._items else None

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

# 測試隊列
queue = Queue()
for i in range(3):
    queue.enqueue(i)
print(f"隊列大小：{queue.size()}")
while not queue.is_empty():
    print(f"出隊：{queue.dequeue()}")

# 實現 LIFO 棧
class Stack:
    def __init__(self):
        self._items = deque()

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop() if self._items else None

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

# 測試棧
stack = Stack()
for i in range(3):
    stack.push(i)
print(f"棧大小：{stack.size()}")
while not stack.is_empty():
    print(f"出棧：{stack.pop()}")

## 5. 效能比較：deque vs list
# --------------------------------------------------------------------------
# deque 在兩端操作上比 list 更高效

import time

# 測試在左端插入效能
n = 10000

# 使用 list
start = time.time()
lst = []
for i in range(n):
    lst.insert(0, i)
list_time = time.time() - start

# 使用 deque
start = time.time()
dq = deque()
for i in range(n):
    dq.appendleft(i)
deque_time = time.time() - start

print(".4f")
print(".4f")
print(".2f")

## 6. 實際應用：滑動視窗最大值
# --------------------------------------------------------------------------
# 使用 deque 實現 O(n) 時間複雜度的滑動視窗最大值演算法

def sliding_window_max(nums, k):
    """
    找出陣列中每個長度為 k 的滑動視窗的最大值
    參數：
        nums: 輸入陣列
        k: 視窗大小
    返回：每個視窗的最大值列表
    """
    if not nums or k == 0:
        return []

    result = []
    dq = deque()  # 儲存索引，維持遞減順序

    for i in range(len(nums)):
        # 移除視窗外的元素
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # 移除小於當前元素的元素（維持遞減）
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        dq.append(i)

        # 當視窗形成時，記錄最大值
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# 測試滑動視窗
test_array = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
max_values = sliding_window_max(test_array, k)
print(f"陣列：{test_array}")
print(f"視窗大小 {k} 的最大值：{max_values}")

# ============================================================================
# 語法重點總結：
# 1. deque 適用於頻繁的兩端操作
# 2. maxlen 參數實現固定大小隊列
# 3. rotate() 用於旋轉操作
# 4. 效能優於 list 在兩端插入/刪除
# 5. 常用於隊列、棧、滑動視窗演算法
# ============================================================================
