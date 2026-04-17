# R20. ChainMap 合併映射（1.20）
"""
ChainMap 合併映射：使用 collections.ChainMap 將多個字典合併為一個視圖。

ChainMap 提供了一種高效的方式來合併多個字典，並保持它們的獨立性。
"""

from collections import ChainMap

# 基礎用法
print("=== 基礎用法 ===")

# 創建多個字典
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 20, 'c': 30}
dict3 = {'c': 300, 'd': 400}

print(f"字典1: {dict1}")
print(f"字典2: {dict2}")
print(f"字典3: {dict3}")

# 使用 ChainMap 合併
combined = ChainMap(dict1, dict2, dict3)
print(f"合併後: {dict(combined)}")

# 訪問元素（前面的字典優先）
print(f"combined['a']: {combined['a']}")  # 來自 dict1
print(f"combined['b']: {combined['b']}")  # 來自 dict1（覆蓋 dict2）
print(f"combined['c']: {combined['c']}")  # 來自 dict2（覆蓋 dict3）
print(f"combined['d']: {combined['d']}")  # 來自 dict3

# 進階應用
print("\n=== 進階應用 ===")

# 模擬作用域鏈（類似於變數作用域）
global_scope = {'x': 10, 'y': 20}
local_scope = {'y': 200, 'z': 300}

# 局部作用域優先
scope_chain = ChainMap(local_scope, global_scope)
print(f"作用域鏈: {dict(scope_chain)}")
print(f"x (全域): {scope_chain['x']}")
print(f"y (局部覆蓋全域): {scope_chain['y']}")
print(f"z (局部): {scope_chain['z']}")

# 動態更新（ChainMap 是動態的）
local_scope['w'] = 400
print(f"新增局部變數後: {dict(scope_chain)}")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 配置管理
default_config = {
    'debug': False,
    'host': 'localhost',
    'port': 8080,
    'timeout': 30
}

user_config = {
    'host': 'production-server.com',
    'port': 80,
    'debug': True
}

environment_config = {
    'timeout': 60
}

# 合併配置（環境 > 用戶 > 預設）
config = ChainMap(environment_config, user_config, default_config)
print("應用配置:")
print(f"debug: {config['debug']}")
print(f"host: {config['host']}")
print(f"port: {config['port']}")
print(f"timeout: {config['timeout']}")

# 案例2: 多語言支援
english = {
    'hello': 'Hello',
    'goodbye': 'Goodbye',
    'thank_you': 'Thank you'
}

spanish = {
    'hello': 'Hola',
    'goodbye': 'Adiós',
    'thank_you': 'Gracias'
}

french = {
    'hello': 'Bonjour',
    'goodbye': 'Au revoir'
}

# 語言優先順序：法文 > 西班牙文 > 英文
translations = ChainMap(french, spanish, english)
print("\n翻譯系統:")
for key in ['hello', 'goodbye', 'thank_you']:
    print(f"{key}: {translations[key]}")

# 案例3: 資料庫連接池
import time

# 模擬不同優先級的資料庫配置
primary_db = {
    'host': 'primary.db.example.com',
    'port': 5432,
    'pool_size': 10
}

secondary_db = {
    'host': 'secondary.db.example.com',
    'port': 5432,
    'pool_size': 5
}

fallback_db = {
    'host': 'fallback.db.example.com',
    'port': 5432,
    'pool_size': 2,
    'retry_delay': 5
}

# 連接策略：主要 > 次要 > 後備
db_config = ChainMap(primary_db, secondary_db, fallback_db)

print("\n資料庫配置:")
print(f"主機: {db_config['host']}")
print(f"連接池大小: {db_config['pool_size']}")
print(f"重試延遲: {db_config.get('retry_delay', '未設定')}")

# 檢查所有可用的鍵
all_keys = set()
for d in db_config.maps:
    all_keys.update(d.keys())
print(f"所有可用配置: {sorted(all_keys)}")

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. ChainMap(*maps) 將多個字典合併為單一視圖
2. 鍵查找順序：從左到右，第一個找到的優先
3. 動態性：修改原始字典會反映到 ChainMap
4. 不可變性：ChainMap 本身不可修改，但可以創建新實例
5. maps 屬性：訪問底層字典列表
6. 適用場景：配置管理、作用域鏈、多語言支援
7. 效能：查找時間 O(n)，其中 n 是字典數量
8. 記憶體效率：不複製數據，只創建視圖
"""

from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)

c['x']
c['z']  # 取到 a 的 z
