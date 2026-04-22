# R13. 字典列表排序 itemgetter（1.13）
"""
字典列表排序 itemgetter：使用 operator.itemgetter 作為排序鍵，對字典列表進行排序。

這提供了比 lambda 函數更高效和清晰的方式來指定排序依據。
"""

from operator import itemgetter

# 基礎用法
print("=== 基礎用法 ===")

# 字典列表
people = [
    {'name': 'Alice', 'age': 25, 'score': 85},
    {'name': 'Bob', 'age': 30, 'score': 92},
    {'name': 'Charlie', 'age': 22, 'score': 78},
    {'name': 'David', 'age': 28, 'score': 88}
]

print("原始數據:")
for person in people:
    print(person)

# 按年齡排序
sorted_by_age = sorted(people, key=itemgetter('age'))
print("\n按年齡排序:")
for person in sorted_by_age:
    print(person)

# 按分數降序排序
sorted_by_score_desc = sorted(people, key=itemgetter('score'), reverse=True)
print("\n按分數降序排序:")
for person in sorted_by_score_desc:
    print(person)

# 進階應用
print("\n=== 進階應用 ===")

# 多重排序條件
# 先按分數降序，再按年齡升序
sorted_multi = sorted(people, key=itemgetter('score', 'age'), reverse=True)
print("多重排序（分數降序，年齡升序）:")
for person in sorted_multi:
    print(person)

# 與 lambda 比較
sorted_lambda = sorted(people, key=lambda x: (x['score'], x['age']), reverse=True)
print("\n使用 lambda 的等效排序:")
for person in sorted_lambda:
    print(person)

# 處理元組列表
coordinates = [(3, 1), (1, 4), (2, 2), (1, 3)]
sorted_coords = sorted(coordinates, key=itemgetter(0, 1))
print(f"\n座標排序: {sorted_coords}")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 學生成績排序
students = [
    {'name': '小明', 'chinese': 85, 'math': 92, 'english': 78},
    {'name': '小華', 'chinese': 90, 'math': 85, 'english': 88},
    {'name': '小美', 'chinese': 88, 'math': 95, 'english': 92}
]

# 按總分排序
sorted_by_total = sorted(students, key=lambda x: x['chinese'] + x['math'] + x['english'], reverse=True)
print("按總分排序:")
for student in sorted_by_total:
    print(f"{student['name']}: 總分 {student['chinese'] + student['math'] + student['english']}")

# 案例2: 商品銷售排序
products = [
    {'name': '筆記本電腦', 'price': 25000, 'sales': 150},
    {'name': '手機', 'price': 15000, 'sales': 300},
    {'name': '平板電腦', 'price': 12000, 'sales': 200}
]

# 按銷售額排序（價格 × 銷售量）
sorted_by_revenue = sorted(products, key=lambda x: x['price'] * x['sales'], reverse=True)
print("\n按銷售額排序:")
for product in sorted_by_revenue:
    revenue = product['price'] * product['sales']
    print(f"{product['name']}: 銷售額 {revenue}")

# 案例3: 檔案資訊排序
import os
files = [
    {'name': 'document.txt', 'size': 1024, 'modified': '2023-10-01'},
    {'name': 'image.jpg', 'size': 2048, 'modified': '2023-09-15'},
    {'name': 'spreadsheet.xlsx', 'size': 512, 'modified': '2023-10-05'}
]

# 按檔案大小排序
sorted_by_size = sorted(files, key=itemgetter('size'), reverse=True)
print("\n按檔案大小排序:")
for file in sorted_by_size:
    print(f"{file['name']}: {file['size']} bytes")

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. itemgetter(key) 創建一個函數，用於從序列或映射中提取指定鍵的值
2. 可以接受多個鍵：itemgetter('key1', 'key2') 返回元組
3. 比 lambda 函數更高效，因為它在 C 層級實現
4. 適用於任何支援索引或鍵訪問的物件
5. 對於字典列表排序，提供清晰的排序依據
6. 可以與 sorted()、min()、max() 等函數配合使用
"""

from operator import itemgetter

rows = [{'fname': 'Brian', 'uid': 1003}, {'fname': 'John', 'uid': 1001}]
sorted(rows, key=itemgetter('fname'))
sorted(rows, key=itemgetter('uid'))
sorted(rows, key=itemgetter('uid', 'fname'))
