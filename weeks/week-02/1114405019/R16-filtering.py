# R16. 過濾：推導式 / generator / filter / compress（1.16）
"""
過濾：使用列表推導式、生成器表達式、filter() 函數和 itertools.compress 進行數據過濾。

這些工具提供了不同的過濾方式，各有優缺點適用於不同場景。
"""

from itertools import compress

# 基礎用法
print("=== 基礎用法 ===")

# 原始數據
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"原始數據: {numbers}")

# 列表推導式過濾
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"偶數（列表推導式）: {even_numbers}")

# 生成器表達式過濾
even_gen = (x for x in numbers if x % 2 == 0)
print(f"偶數（生成器）: {list(even_gen)}")

# filter() 函數過濾
even_filter = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶數（filter）: {even_filter}")

# itertools.compress 過濾（使用布林遮罩）
mask = [x % 2 == 0 for x in numbers]
even_compress = list(compress(numbers, mask))
print(f"偶數（compress）: {even_compress}")

# 進階應用
print("\n=== 進階應用 ===")

# 多條件過濾
data = [
    {'name': 'Alice', 'age': 25, 'score': 85, 'active': True},
    {'name': 'Bob', 'age': 30, 'score': 92, 'active': False},
    {'name': 'Charlie', 'age': 22, 'score': 78, 'active': True},
    {'name': 'David', 'age': 28, 'score': 88, 'active': True}
]

# 使用列表推導式多條件過濾
active_high_scorers = [
    person for person in data
    if person['active'] and person['score'] >= 80
]
print("活躍且高分的人:")
for person in active_high_scorers:
    print(person)

# 使用 filter 和 lambda
young_active = list(filter(
    lambda p: p['age'] < 30 and p['active'],
    data
))
print("\n年輕且活躍的人:")
for person in young_active:
    print(person)

# compress 應用：根據另一個序列過濾
names = ['Alice', 'Bob', 'Charlie', 'David']
scores = [85, 92, 78, 88]
passing_mask = [score >= 80 for score in scores]
passing_students = list(compress(names, passing_mask))
print(f"\n及格學生: {passing_students}")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 檔案過濾
import os
files = ['document.txt', 'image.jpg', 'script.py', 'data.csv', 'readme.md']

# 過濾 Python 檔案
python_files = [f for f in files if f.endswith('.py')]
print(f"Python 檔案: {python_files}")

# 過濾圖片檔案
image_files = list(filter(lambda f: f.endswith(('.jpg', '.png', '.gif')), files))
print(f"圖片檔案: {image_files}")

# 案例2: 用戶數據過濾
users = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'verified': True},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com', 'verified': False},
    {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com', 'verified': True},
    {'id': 4, 'name': 'David', 'email': 'david@example.com', 'verified': False}
]

# 過濾已驗證用戶
verified_users = [u for u in users if u['verified']]
print("\n已驗證用戶:")
for user in verified_users:
    print(f"ID: {user['id']}, Name: {user['name']}")

# 使用 filter 過濾包含特定域名的郵箱
gmail_users = list(filter(lambda u: 'gmail.com' in u['email'], users))
print(f"\nGmail 用戶: {[u['name'] for u in gmail_users]}")

# 案例3: 銷售數據過濾
sales = [
    {'product': 'A', 'amount': 100, 'region': 'North'},
    {'product': 'B', 'amount': 150, 'region': 'South'},
    {'product': 'A', 'amount': 200, 'region': 'North'},
    {'product': 'C', 'amount': 50, 'region': 'East'},
    {'product': 'B', 'amount': 300, 'region': 'South'}
]

# 過濾高銷售額
high_sales = [s for s in sales if s['amount'] >= 150]
print("\n高銷售額記錄:")
for sale in high_sales:
    print(sale)

# 過濾特定地區
north_sales = list(filter(lambda s: s['region'] == 'North', sales))
print(f"\n北部地區銷售: {[s['amount'] for s in north_sales]}")

# 使用 compress 根據銷售額閾值過濾
threshold = 120
sales_mask = [s['amount'] > threshold for s in sales]
above_threshold = list(compress(sales, sales_mask))
print(f"\n超過 {threshold} 的銷售: {[s['amount'] for s in above_threshold]}")

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. 列表推導式: [expr for item in iterable if condition] - 創建新列表
2. 生成器表達式: (expr for item in iterable if condition) - 創建生成器，節省記憶體
3. filter(func, iterable): 返回滿足條件的元素迭代器
4. compress(data, selectors): 使用布林序列過濾數據
5. 列表推導式和 filter 返回具體類型，生成器表達式返回生成器
6. compress 適用於需要預先計算遮罩的情況
7. 選擇適當工具取決於數據大小和使用模式
"""

mylist = [1, 4, -5, 10]
[n for n in mylist if n > 0]
pos = (n for n in mylist if n > 0)

values = ['1', '2', '-3', '-', 'N/A']

def is_int(val):
    try:
        int(val); return True
    except ValueError:
        return False

list(filter(is_int, values))

from itertools import compress
addresses = ['a1', 'a2', 'a3']
counts = [0, 3, 10]
more5 = [n > 5 for n in counts]
list(compress(addresses, more5))
