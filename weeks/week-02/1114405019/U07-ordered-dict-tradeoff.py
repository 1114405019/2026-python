# U07. OrderedDict 的取捨：保序但更吃記憶體（1.7）
"""
OrderedDict 的取捨：保序但更吃記憶體

collections.OrderedDict 保持鍵的插入順序，但相比普通字典使用更多記憶體。
在 Python 3.7+ 中，普通字典也保持插入順序，但 OrderedDict 提供了額外的順序操作方法。
"""

from collections import OrderedDict

# 基礎用法
print("=== 基礎用法 ===")

# 創建 OrderedDict
od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3

print(f"OrderedDict: {od}")
print(f"鍵的順序: {list(od.keys())}")
print(f"值的順序: {list(od.values())}")

# 比較普通字典 (Python 3.7+ 也保持順序)
regular_dict = {'first': 1, 'second': 2, 'third': 3}
print(f"普通字典: {regular_dict}")
print(f"普通字典鍵順序: {list(regular_dict.keys())}")

# OrderedDict 的特殊方法
print(f"最舊的項目: {od.popitem(last=False)}")  # FIFO
print(f"剩餘項目: {od}")

od['fourth'] = 4
print(f"添加後: {od}")

print(f"最新的項目: {od.popitem(last=True)}")  # LIFO
print(f"最終剩餘: {od}")

# 進階應用
print("\n=== 進階應用 ===")

# 移動到結尾（最近使用）
od2 = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(f"原始: {od2}")

od2.move_to_end('b')  # 將 'b' 移到結尾
print(f"移動 'b' 到結尾: {od2}")

od2.move_to_end('a', last=False)  # 將 'a' 移到開頭
print(f"移動 'a' 到開頭: {od2}")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: LRU 快取實現
class LRUCache:
    def __init__(self, capacity=5):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            # 移動到結尾（最近使用）
            self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        if key in self.cache:
            # 更新值並移動到結尾
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                # 移除最舊的（最少使用的）
                oldest_key, _ = self.cache.popitem(last=False)
                print(f"快取已滿，移除最舊項目: {oldest_key}")
            self.cache[key] = value

    def display(self):
        print(f"快取內容 (最近使用 -> 最少使用): {list(self.cache.keys())}")

cache = LRUCache(capacity=3)

operations = [
    ('put', 'A', 1),
    ('put', 'B', 2),
    ('put', 'C', 3),
    ('get', 'A', None),  # 訪問 A，使其成為最近使用
    ('put', 'D', 4),     # 應該移除 B（最少使用）
    ('get', 'B', None),  # B 應該不存在
]

for op, key, value in operations:
    if op == 'put':
        cache.put(key, value)
        print(f"放入 {key}={value}")
    elif op == 'get':
        result = cache.get(key)
        print(f"獲取 {key}: {result}")
    cache.display()
    print()

# 案例2: 訂單處理隊列
class OrderQueue:
    def __init__(self):
        self.orders = OrderedDict()

    def add_order(self, order_id, customer, items):
        self.orders[order_id] = {
            'customer': customer,
            'items': items,
            'timestamp': '2023-10-01 12:00:00'  # 模擬
        }
        print(f"新增訂單: {order_id} ({customer})")

    def process_next_order(self):
        if self.orders:
            order_id, order_info = self.orders.popitem(last=False)  # FIFO
            print(f"處理訂單: {order_id} - {order_info['customer']}")
            return order_id, order_info
        return None

    def prioritize_order(self, order_id):
        """將訂單移到隊列前面（緊急處理）"""
        if order_id in self.orders:
            self.orders.move_to_end(order_id, last=False)
            print(f"優先處理訂單: {order_id}")

    def get_queue_status(self):
        return list(self.orders.keys())

queue = OrderQueue()

# 添加訂單
queue.add_order('ORD001', 'Alice', ['筆記本', '滑鼠'])
queue.add_order('ORD002', 'Bob', ['鍵盤'])
queue.add_order('ORD003', 'Charlie', ['螢幕', '鍵盤', '滑鼠'])

print(f"\n當前隊列: {queue.get_queue_status()}")

# 優先處理某個訂單
queue.prioritize_order('ORD003')
print(f"優先後隊列: {queue.get_queue_status()}")

# 處理訂單
print("\n處理訂單:")
while queue.get_queue_status():
    queue.process_next_order()
    print(f"剩餘隊列: {queue.get_queue_status()}")

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. OrderedDict 保持鍵的插入/訪問順序
2. popitem(last=False) 移除最舊項目 (FIFO)
3. popitem(last=True) 移除最新項目 (LIFO)
4. move_to_end(key, last=True) 移動鍵到結尾
5. move_to_end(key, last=False) 移動鍵到開頭
6. 記憶體使用: 比普通字典多約2倍
7. Python 3.7+: 普通字典也保持順序，但無額外方法
8. 適用場景: LRU快取、隊列管理、順序敏感操作
"""

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
# 你能解釋：為了維持插入順序，它需要額外結構（因此更耗記憶體）
