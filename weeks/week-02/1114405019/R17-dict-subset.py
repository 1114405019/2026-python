# R17. 字典子集（1.17）
"""
字典子集：從字典中提取子集的各種方法，包括字典推導式、keys() 過濾等。

這些技巧在處理大型字典或需要選擇性數據提取時非常有用。
"""

# 基礎用法
print("=== 基礎用法 ===")

# 原始字典
person = {
    'name': 'Alice',
    'age': 25,
    'email': 'alice@example.com',
    'phone': '123-456-7890',
    'address': '123 Main St',
    'city': 'Anytown',
    'country': 'USA'
}

print(f"原始字典: {person}")

# 使用字典推導式提取子集
basic_info = {k: v for k, v in person.items() if k in ['name', 'age', 'email']}
print(f"基本資訊: {basic_info}")

# 使用 keys() 過濾
contact_keys = {'name', 'email', 'phone'}
contact_info = {k: person[k] for k in person.keys() & contact_keys}
print(f"聯絡資訊: {contact_info}")

# 進階應用
print("\n=== 進階應用 ===")

# 條件過濾子集
# 提取字串類型的欄位
string_fields = {k: v for k, v in person.items() if isinstance(v, str)}
print(f"字串欄位: {string_fields}")

# 提取長度大於3的字串欄位
long_string_fields = {k: v for k, v in person.items() if isinstance(v, str) and len(v) > 3}
print(f"長字串欄位: {long_string_fields}")

# 使用 operator.itemgetter
from operator import itemgetter
subset_keys = ['name', 'age', 'city']
subset_values = itemgetter(*subset_keys)(person)
subset_dict = dict(zip(subset_keys, subset_values))
print(f"使用 itemgetter: {subset_dict}")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 用戶資料處理
user_profile = {
    'user_id': 12345,
    'username': 'alice_smith',
    'email': 'alice@example.com',
    'first_name': 'Alice',
    'last_name': 'Smith',
    'phone': '555-0123',
    'registration_date': '2023-01-15',
    'last_login': '2023-10-01',
    'account_status': 'active',
    'subscription_level': 'premium'
}

# 公開資訊（不包含敏感資料）
public_keys = {'username', 'first_name', 'last_name', 'registration_date'}
public_profile = {k: user_profile[k] for k in user_profile.keys() & public_keys}
print("公開用戶資訊:")
for k, v in public_profile.items():
    print(f"  {k}: {v}")

# 案例2: API 響應過濾
api_response = {
    'status': 'success',
    'data': {
        'id': 123,
        'title': 'Sample Post',
        'content': 'This is the content...',
        'author': 'Alice',
        'created_at': '2023-10-01T10:00:00Z',
        'updated_at': '2023-10-02T15:30:00Z',
        'tags': ['python', 'tutorial'],
        'metadata': {'word_count': 150, 'reading_time': 5}
    },
    'pagination': {'page': 1, 'total_pages': 5}
}

# 提取主要數據欄位
essential_data_keys = {'id', 'title', 'author', 'created_at', 'tags'}
essential_data = {k: api_response['data'][k] for k in api_response['data'].keys() & essential_data_keys}
print("\nAPI 響應主要數據:")
for k, v in essential_data.items():
    print(f"  {k}: {v}")

# 案例3: 配置檔案過濾
config = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'username': 'admin',
        'password': 'secret123',
        'database_name': 'myapp'
    },
    'redis': {
        'host': 'redis-server',
        'port': 6379,
        'password': 'redis_pass'
    },
    'logging': {
        'level': 'INFO',
        'file': '/var/log/app.log',
        'max_size': '10MB'
    },
    'secret_key': 'super-secret-key',
    'debug': True
}

# 提取非敏感配置（用於日誌記錄）
safe_config_keys = {'database', 'redis', 'logging', 'debug'}
safe_config = {k: config[k] for k in config.keys() & safe_config_keys}
print("\n安全配置（用於日誌）:")
for k, v in safe_config.items():
    print(f"  {k}: {v}")

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. 字典推導式: {k: v for k, v in d.items() if condition} - 最靈活的方法
2. 集合運算: {k: d[k] for k in d.keys() & key_set} - 適用於預定義鍵集合
3. operator.itemgetter: 適用於固定鍵集合的高效提取
4. 條件過濾: 可以基於鍵、值或鍵值對進行過濾
5. 記憶體效率: 推導式創建新字典，適合小型字典
6. 適用場景: API響應過濾、配置管理、數據清理等
"""

prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}
p1 = {k: v for k, v in prices.items() if v > 200}

tech_names = {'AAPL', 'IBM'}
p2 = {k: v for k, v in prices.items() if k in tech_names}
