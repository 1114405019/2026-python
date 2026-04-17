# R15. 分組 groupby（1.15）
"""
分組 groupby：使用 itertools.groupby 對已排序的序列進行分組操作。

groupby 要求輸入序列必須先按分組鍵排序，然後將連續的相同元素分組。
"""

from itertools import groupby
from operator import itemgetter

# 基礎用法
print("=== 基礎用法 ===")

# 必須先排序才能正確分組
data = [('A', 1), ('B', 2), ('A', 3), ('B', 4), ('A', 5)]
sorted_data = sorted(data, key=itemgetter(0))  # 按第一個元素排序
print(f"原始數據: {data}")
print(f"排序後: {sorted_data}")

# 使用 groupby 分組
grouped = groupby(sorted_data, key=itemgetter(0))
print("\n分組結果:")
for key, group in grouped:
    print(f"{key}: {list(group)}")

# 進階應用
print("\n=== 進階應用 ===")

# 分組統計
people = [
    ('Alice', 'Engineering'),
    ('Bob', 'Sales'),
    ('Charlie', 'Engineering'),
    ('David', 'Sales'),
    ('Eve', 'Marketing'),
    ('Frank', 'Engineering')
]

# 按部門分組並統計人數
sorted_people = sorted(people, key=itemgetter(1))
grouped_dept = groupby(sorted_people, key=itemgetter(1))

print("部門分組統計:")
for dept, members in grouped_dept:
    member_list = list(members)
    print(f"{dept}: {len(member_list)} 人 - {member_list}")

# 自訂分組鍵函數
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorted_nums = sorted(numbers, key=lambda x: x % 3)  # 按除以3的餘數分組

grouped_nums = groupby(sorted_nums, key=lambda x: x % 3)
print("\n按餘數分組:")
for remainder, nums in grouped_nums:
    print(f"餘數 {remainder}: {list(nums)}")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 日誌分析
logs = [
    ('2023-10-01', 'INFO', 'User login'),
    ('2023-10-01', 'ERROR', 'Database connection failed'),
    ('2023-10-01', 'INFO', 'Data processed'),
    ('2023-10-02', 'WARNING', 'Low disk space'),
    ('2023-10-02', 'INFO', 'Backup completed'),
    ('2023-10-03', 'ERROR', 'Network timeout')
]

# 按日期分組日誌
sorted_logs = sorted(logs, key=itemgetter(0))
grouped_logs = groupby(sorted_logs, key=itemgetter(0))

print("按日期分組的日誌:")
for date, day_logs in grouped_logs:
    print(f"\n{date}:")
    for log in day_logs:
        print(f"  {log[1]}: {log[2]}")

# 案例2: 學生成績分級
students = [
    ('小明', 85, 'A'),
    ('小華', 92, 'A'),
    ('小美', 78, 'B'),
    ('小李', 88, 'A'),
    ('小王', 65, 'C'),
    ('小張', 72, 'B')
]

# 按等級分組
sorted_students = sorted(students, key=itemgetter(2))
grouped_grades = groupby(sorted_students, key=itemgetter(2))

print("\n按等級分組的學生:")
for grade, grade_students in grouped_grades:
    student_names = [s[0] for s in grade_students]
    avg_score = sum(s[1] for s in grade_students) / len(student_names)
    print(f"等級 {grade}: {student_names} (平均分: {avg_score:.1f})")

# 案例3: 購物清單分類
shopping_items = [
    ('蘋果', '水果'),
    ('牛奶', '乳製品'),
    ('麵包', '烘焙品'),
    ('香蕉', '水果'),
    ('起司', '乳製品'),
    ('餅乾', '烘焙品'),
    ('橘子', '水果')
]

# 按類別分組
sorted_items = sorted(shopping_items, key=itemgetter(1))
grouped_items = groupby(sorted_items, key=itemgetter(1))

print("\n購物清單分類:")
for category, items in grouped_items:
    item_names = [item[0] for item in items]
    print(f"{category}: {item_names}")

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. groupby(iterable, key=None) 對已排序的序列進行分組
2. 輸入序列必須先按分組鍵排序，否則分組結果不正確
3. 返回迭代器，每次產生 (key, group) 對，其中 group 是迭代器
4. group 只能被消費一次，之後會耗盡
5. key 函數用於確定分組依據，預設為 identity 函數
6. 適用於任何可排序的序列
7. 時間複雜度 O(n)，但需要先排序 O(n log n)
"""

from itertools import groupby
from operator import itemgetter

rows = [{'date': '07/01/2012', 'address': '...'}, {'date': '07/02/2012', 'address': '...'}]
rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key=itemgetter('date')):
    for i in items:
        pass
