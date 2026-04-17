# U03. deque(maxlen=N) 為何能保留最後 N 筆（1.3）
"""
deque(maxlen=N) 為何能保留最後 N 筆

collections.deque 是一個雙端隊列，當設置 maxlen 參數時，
它會自動維護固定大小，當新元素加入時自動移除最舊的元素。
"""

from collections import deque

# 基礎用法
print("=== 基礎用法 ===")

# 創建有限大小的 deque
recent_items = deque(maxlen=3)
print(f"初始 deque: {recent_items}")

# 添加元素
recent_items.append(1)
recent_items.append(2)
recent_items.append(3)
print(f"添加3個元素: {recent_items}")

# 添加第4個元素，自動移除最舊的
recent_items.append(4)
print(f"添加第4個: {recent_items} (自動移除最舊的1)")

recent_items.append(5)
print(f"添加第5個: {recent_items} (自動移除最舊的2)")

# 從左側添加
recent_items.appendleft(10)
print(f"從左添加: {recent_items} (移除最右邊的5)")

# 進階應用
print("\n=== 進階應用 ===")

# 實現移動平均
def moving_average(values, window_size):
    """計算移動平均"""
    window = deque(maxlen=window_size)
    averages = []

    for value in values:
        window.append(value)
        avg = sum(window) / len(window)
        averages.append(avg)

    return averages

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
averages = moving_average(data, 3)
print(f"原始數據: {data}")
print(f"移動平均 (窗口=3): {[f'{avg:.2f}' for avg in averages]}")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 最近的用戶活動
class RecentActivityTracker:
    def __init__(self, max_activities=5):
        self.activities = deque(maxlen=max_activities)

    def add_activity(self, activity):
        self.activities.append(activity)
        print(f"新增活動: {activity}")
        print(f"最近活動: {list(self.activities)}")

    def get_recent(self, n=None):
        if n is None:
            return list(self.activities)
        return list(self.activities)[-n:]

tracker = RecentActivityTracker(max_activities=3)

activities = [
    "用戶登入",
    "查看首頁",
    "瀏覽產品",
    "加入購物車",
    "結帳",
    "訂單確認"
]

for activity in activities:
    tracker.add_activity(activity)
    print()

# 案例2: 聊天室最新訊息
class ChatRoom:
    def __init__(self, max_messages=10):
        self.messages = deque(maxlen=max_messages)

    def add_message(self, user, message):
        self.messages.append(f"{user}: {message}")

    def get_recent_messages(self, count=5):
        return list(self.messages)[-count:]

chat = ChatRoom(max_messages=4)

messages = [
    ("Alice", "大家好！"),
    ("Bob", "歡迎來到聊天室"),
    ("Charlie", "今天天氣真好"),
    ("Alice", "是的，很適合出去玩"),
    ("David", "我剛完成一個專案"),
    ("Eve", "恭喜！"),
    ("Frank", "有人想討論 Python 嗎？")
]

print("聊天室訊息歷史:")
for user, msg in messages:
    chat.add_message(user, msg)

print(f"\n最近的訊息:")
for msg in chat.get_recent_messages():
    print(f"  {msg}")

# 案例3: 網路請求記錄
class RequestLogger:
    def __init__(self, max_requests=100):
        self.requests = deque(maxlen=max_requests)

    def log_request(self, ip, endpoint, status):
        request_info = {
            'ip': ip,
            'endpoint': endpoint,
            'status': status,
            'timestamp': '2023-10-01 12:00:00'  # 模擬時間戳
        }
        self.requests.append(request_info)

    def get_failed_requests(self):
        return [req for req in self.requests if req['status'] >= 400]

    def get_recent_requests(self, count=10):
        return list(self.requests)[-count:]

logger = RequestLogger(max_requests=5)

# 模擬請求日誌
requests_data = [
    ('192.168.1.1', '/api/users', 200),
    ('192.168.1.2', '/api/login', 401),
    ('192.168.1.1', '/api/data', 200),
    ('192.168.1.3', '/api/admin', 403),
    ('192.168.1.2', '/api/users', 200),
    ('192.168.1.4', '/api/error', 500),
    ('192.168.1.1', '/api/logout', 200)
]

for ip, endpoint, status in requests_data:
    logger.log_request(ip, endpoint, status)

print("\n最近的請求:")
for req in logger.get_recent_requests():
    print(f"  {req['ip']} -> {req['endpoint']} [{req['status']}]")

failed = logger.get_failed_requests()
print(f"\n失敗的請求 ({len(failed)} 個):")
for req in failed:
    print(f"  {req['ip']} -> {req['endpoint']} [{req['status']}]")

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. deque(maxlen=N) 創建固定大小的雙端隊列
2. 自動維護大小: 當超過 maxlen 時，自動移除最舊元素
3. 高效操作: append() 和 appendleft() 都是 O(1)
4. 適用場景: 最近記錄、緩衝區、移動窗口計算
5. 記憶體效率: 不需要手動管理大小
6. 雙端操作: 支持從兩端添加/移除元素
7. 線程安全: 但需要外部同步以確保線程安全
"""

from collections import deque

q = deque(maxlen=3)
for i in [1, 2, 3, 4, 5]:
    q.append(i)
# 結果只剩 [3, 4, 5]
