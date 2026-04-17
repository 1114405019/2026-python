"""deque

1. 限定長度自動丟棄最舊元素
2. append/appendleft/pop/popleft 基本操作
3. 雙端佇列適合雙向資料處理
"""

from collections import deque

# 使用 maxlen 建立定長 deque，超出容量時自動丟掉最舊元素
q = deque(maxlen=3)
q.append(1); q.append(2); q.append(3)
q.append(4)  # 自動丟掉最舊的 1

# deque 也支援從左右兩端新增與移除元素
q = deque()
q.append(1); q.appendleft(2)
q.pop(); q.popleft()
