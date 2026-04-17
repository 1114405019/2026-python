"""優先佇列

1. 以 heapq 實作 priority queue
2. 透過負 priority 轉為最大優先順序
3. 使用 index 維持相同 priority 的先後順序
"""

import heapq

class PriorityQueue:
    # 初始化內部堆與索引；索引保證相同 priority 時維持插入順序
    def __init__(self):
        self._queue = []
        self._index = 0

    # push 時以 (-priority, index, item) 儲存，heapq 依 tuple 比較順序排序
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    # pop 取出優先權最高的項目，回傳原始資料項目
    def pop(self):
        return heapq.heappop(self._queue)[-1]
