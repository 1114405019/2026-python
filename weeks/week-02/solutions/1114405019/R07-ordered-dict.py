# R07. OrderedDict：保持插入順序的字典
# ============================================================================
# OrderedDict 是 collections 模組中的有序字典
# 記住元素的插入順序，在迭代時按插入順序返回
# 在 Python 3.7+ 中，普通 dict 也保持插入順序，但 OrderedDict 提供額外方法
# 適用於需要預測性迭代順序的場景
# ============================================================================

from collections import OrderedDict
import json

## 1. 基礎 OrderedDict 用法
# --------------------------------------------------------------------------
# OrderedDict 記住插入順序

print("=== 基礎 OrderedDict ===")
od = OrderedDict()
od['foo'] = 1
od['bar'] = 2
od['baz'] = 3

print(f"OrderedDict 內容：{od}")
print(f"鍵的順序：{list(od.keys())}")
print(f"值的順序：{list(od.values())}")
print(f"鍵值對的順序：{list(od.items())}")

# 比較普通字典（Python 3.7+ 也保持順序）
regular_dict = {'foo': 1, 'bar': 2, 'baz': 3}
print(f"普通字典：{regular_dict}")
print(f"順序是否相同：{list(od.keys()) == list(regular_dict.keys())}")

## 2. JSON 序列化保持順序
# --------------------------------------------------------------------------
# OrderedDict 在 JSON 序列化時保持順序

print("\n=== JSON 序列化 ===")
data = OrderedDict([
    ('name', 'Alice'),
    ('age', 30),
    ('city', 'New York'),
    ('job', 'Engineer')
])

json_str = json.dumps(data, indent=2)
print("JSON 輸出：")
print(json_str)

# 解析回來仍然保持順序
parsed = json.loads(json_str, object_pairs_hook=OrderedDict)
print(f"解析後的類型：{type(parsed)}")
print(f"解析後的內容：{parsed}")

## 3. OrderedDict 的特殊方法
# --------------------------------------------------------------------------
# OrderedDict 提供額外的順序操作方法

print("\n=== OrderedDict 特殊方法 ===")
od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# move_to_end(key, last=True) - 將鍵移到末尾或開頭
od.move_to_end('b')  # 移到末尾
print(f"將 'b' 移到末尾：{od}")

od.move_to_end('d', last=False)  # 移到開頭
print(f"將 'd' 移到開頭：{od}")

# popitem(last=True) - 彈出最後一個或第一個項目
last_item = od.popitem()  # 預設彈出最後一個
print(f"彈出最後項目：{last_item}, 剩餘：{od}")

first_item = od.popitem(last=False)  # 彈出第一個
print(f"彈出第一項目：{first_item}, 剩餘：{od}")

## 4. 實際應用：LRU 快取
# --------------------------------------------------------------------------
# 使用 OrderedDict 實現簡單的 LRU 快取

class LRUCache:
    """簡單的 LRU 快取實現"""

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """獲取快取項目"""
        if key not in self.cache:
            return None
        # 將訪問的項目移到末尾（最近使用）
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """存入快取項目"""
        if key in self.cache:
            # 更新現有項目，移到末尾
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # 新增項目
            self.cache[key] = value
            self.cache.move_to_end(key)
            # 如果超過容量，移除最舊的
            if len(self.cache) > self.capacity:
                removed_key, _ = self.cache.popitem(last=False)
                print(f"快取滿載，移除最舊項目：{removed_key}")

    def __str__(self):
        return f"LRUCache({dict(self.cache)})"

# 測試 LRU 快取
print("\n=== LRU 快取測試 ===")
cache = LRUCache(3)

cache.put('A', 1)
print(f"存入 A: {cache}")

cache.put('B', 2)
print(f"存入 B: {cache}")

cache.put('C', 3)
print(f"存入 C: {cache}")

cache.get('A')  # 訪問 A，將其移到末尾
print(f"訪問 A: {cache}")

cache.put('D', 4)  # 超過容量，移除最舊的 B
print(f"存入 D: {cache}")

## 5. 排序與重新排列
# --------------------------------------------------------------------------
# OrderedDict 可以用於排序字典

print("\n=== 排序應用 ===")
# 創建無序字典
unsorted = {'zebra': 1, 'apple': 2, 'banana': 3, 'cherry': 4}

# 按鍵排序
sorted_by_key = OrderedDict(sorted(unsorted.items(), key=lambda x: x[0]))
print(f"按鍵排序：{sorted_by_key}")

# 按值排序
sorted_by_value = OrderedDict(sorted(unsorted.items(), key=lambda x: x[1]))
print(f"按值排序：{sorted_by_value}")

# 自訂排序
sorted_custom = OrderedDict(sorted(unsorted.items(),
                                  key=lambda x: (len(x[0]), x[0])))
print(f"自訂排序（長度+字母）：{sorted_custom}")

## 6. OrderedDict vs 普通 dict 的比較
# --------------------------------------------------------------------------
# 在 Python 3.7+ 中，普通 dict 也保持插入順序

print("\n=== OrderedDict vs 普通 dict ===")

# 記憶體使用比較
import sys

od_test = OrderedDict([(f'key{i}', i) for i in range(100)])
dict_test = {f'key{i}': i for i in range(100)}

print(f"OrderedDict 記憶體：{sys.getsizeof(od_test)} bytes")
print(f"普通 dict 記憶體：{sys.getsizeof(dict_test)} bytes")

# 功能比較
print(f"都有順序：{list(od_test.keys()) == list(dict_test.keys())}")
print(f"OrderedDict 有 move_to_end：{hasattr(od_test, 'move_to_end')}")
print(f"普通 dict 有 move_to_end：{hasattr(dict_test, 'move_to_end')}")

## 7. 實際應用：配置檔案解析
# --------------------------------------------------------------------------
# 使用 OrderedDict 保持配置項目的順序

def parse_config(config_lines):
    """解析配置檔案，保持順序"""
    config = OrderedDict()
    for line in config_lines:
        line = line.strip()
        if line and not line.startswith('#'):
            key, value = line.split('=', 1)
            config[key.strip()] = value.strip()
    return config

config_text = [
    "# 資料庫配置",
    "db_host=localhost",
    "db_port=5432",
    "db_name=myapp",
    "# 快取配置",
    "cache_host=redis-server",
    "cache_port=6379"
]

parsed_config = parse_config(config_text)
print(f"\n解析的配置：")
for key, value in parsed_config.items():
    print(f"  {key} = {value}")

# ============================================================================
# 語法重點總結：
# 1. OrderedDict 記住插入順序
# 2. move_to_end() 重新排列順序
# 3. popitem(last=True/False) 控制彈出方向
# 4. 適用於 LRU 快取、配置解析等
# 5. Python 3.7+ 普通 dict 也保持順序
# ============================================================================
