# U09. groupby 為何一定要先 sort（1.15）
"""
groupby 為何一定要先 sort

itertools.groupby 要求輸入的序列必須按分組鍵排序，因為它依賴於連續的相同元素。
如果不排序，相同值的元素可能分散在序列中，導致分組不正確。
"""

from itertools import groupby

# 基礎用法
print("=== 基礎用法 ===")

# 未排序的數據
data = [('A', 1), ('B', 2), ('A', 3), ('B', 4), ('A', 5)]
print(f"原始數據: {data}")

# 不排序直接 groupby - 錯誤的分組
print("不排序的分組結果:")
for key, group in groupby(data, key=lambda x: x[0]):
    print(f"{key}: {list(group)}")

# 正確做法：先排序再分組
sorted_data = sorted(data, key=lambda x: x[0])
print(f"\n排序後: {sorted_data}")

print("正確的分組結果:")
for key, group in groupby(sorted_data, key=lambda x: x[0]):
    print(f"{key}: {list(group)}")

# 進階應用
print("\n=== 進階應用 ===")

# 多重排序鍵
complex_data = [
    ('A', 'X', 1),
    ('B', 'Y', 2),
    ('A', 'Y', 3),
    ('A', 'X', 4),
    ('B', 'X', 5),
    ('B', 'Y', 6)
]

print(f"複雜數據: {complex_data}")

# 按第一個鍵排序
sorted_by_first = sorted(complex_data, key=lambda x: x[0])
print("\n按第一個鍵分組:")
for key, group in groupby(sorted_by_first, key=lambda x: x[0]):
    print(f"{key}: {list(group)}")

# 按兩個鍵排序
sorted_by_both = sorted(complex_data, key=lambda x: (x[0], x[1]))
print("\n按兩個鍵分組:")
for key, group in groupby(sorted_by_both, key=lambda x: (x[0], x[1])):
    print(f"{key}: {list(group)}")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 日誌分析
logs = [
    ('ERROR', '2023-10-01 10:00:00', 'Database connection failed'),
    ('INFO', '2023-10-01 10:05:00', 'User login successful'),
    ('ERROR', '2023-10-01 10:10:00', 'Network timeout'),
    ('WARNING', '2023-10-01 10:15:00', 'Low disk space'),
    ('INFO', '2023-10-01 10:20:00', 'Data processed'),
    ('ERROR', '2023-10-01 10:25:00', 'Authentication failed'),
    ('INFO', '2023-10-01 10:30:00', 'Backup completed')
]

print("日誌數據:")
for log in logs:
    print(f"  {log[0]}: {log[2]}")

# 按日誌等級分組（需要先排序）
sorted_logs = sorted(logs, key=lambda x: x[0])
print("\n按日誌等級分組:")
for level, level_logs in groupby(sorted_logs, key=lambda x: x[0]):
    log_list = list(level_logs)
    print(f"{level} ({len(log_list)} 條):")
    for log in log_list:
        print(f"  {log[1]}: {log[2]}")

# 案例2: 學生成績分級
students = [
    ('Alice', 'A', 95),
    ('Bob', 'B', 85),
    ('Charlie', 'A', 92),
    ('David', 'C', 78),
    ('Eve', 'B', 88),
    ('Frank', 'A', 89),
    ('Grace', 'C', 82)
]

print("\n學生成績:")
for student in students:
    print(f"  {student[0]}: 等級 {student[1]}, 分數 {student[2]}")

# 按等級分組
sorted_students = sorted(students, key=lambda x: x[1])
print("\n按等級分組:")
for grade, grade_students in groupby(sorted_students, key=lambda x: x[1]):
    student_list = list(grade_students)
    avg_score = sum(s[2] for s in student_list) / len(student_list)
    print(f"等級 {grade} ({len(student_list)} 人，平均分: {avg_score:.1f}):")
    for student in student_list:
        print(f"  {student[0]}: {student[2]} 分")

# 案例3: 購物記錄分析
purchases = [
    ('2023-10-01', '電子產品', '筆記本電腦', 25000),
    ('2023-10-01', '書籍', 'Python 教程', 500),
    ('2023-10-02', '電子產品', '滑鼠', 800),
    ('2023-10-02', '書籍', '資料結構', 450),
    ('2023-10-02', '電子產品', '鍵盤', 1200),
    ('2023-10-03', '書籍', '演算法導論', 800),
    ('2023-10-03', '電子產品', '螢幕', 5000)
]

print("\n購物記錄:")
for purchase in purchases:
    print(f"  {purchase[0]}: {purchase[2]} ({purchase[1]}) - ${purchase[3]}")

# 按日期分組
sorted_by_date = sorted(purchases, key=lambda x: x[0])
print("\n按日期分組:")
for date, date_purchases in groupby(sorted_by_date, key=lambda x: x[0]):
    purchase_list = list(date_purchases)
    total_amount = sum(p[3] for p in purchase_list)
    print(f"{date} ({len(purchase_list)} 筆交易，總額: ${total_amount:,}):")
    for purchase in purchase_list:
        print(f"  {purchase[2]} ({purchase[1]}) - ${purchase[3]}")

# 按類別分組
sorted_by_category = sorted(purchases, key=lambda x: x[1])
print("\n按類別分組:")
for category, category_purchases in groupby(sorted_by_category, key=lambda x: x[1]):
    purchase_list = list(category_purchases)
    total_amount = sum(p[3] for p in purchase_list)
    avg_price = total_amount / len(purchase_list)
    print(f"{category} ({len(purchase_list)} 件，總額: ${total_amount:,}, 平均價格: ${avg_price:.0f}):")
    for purchase in purchase_list:
        print(f"  {purchase[2]} - ${purchase[3]}")

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. groupby(iterable, key) 依賴於連續的相同元素
2. 必須先排序: sorted(iterable, key=key_func)
3. 分組鍵: key 函數決定分組依據
4. 迭代器特性: group 只能消費一次
5. 適用場景: 日誌分析、數據分類、統計分組
6. 效能: O(n) 時間，但需要 O(n log n) 排序
7. 替代方案: 如需要複雜分組，可考慮其他數據結構
"""

from itertools import groupby
from operator import itemgetter

rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},
    {'date': '07/02/2012', 'x': 3},
]

# 沒排序：07/02 會被分成兩段（因為 groupby 只看「連續」）
for k, g in groupby(rows, key=itemgetter('date')):
    list(g)

# 排序後：同 date 才會連在一起，分組才正確
rows.sort(key=itemgetter('date'))
for k, g in groupby(rows, key=itemgetter('date')):
    list(g)
