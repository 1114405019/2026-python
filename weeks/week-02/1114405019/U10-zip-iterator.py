# U10. zip 為何只能用一次（1.8）
"""
zip 為何只能用一次

zip() 返回的是一個迭代器（iterator），而不是列表。
迭代器是一次性的消耗品，使用一次後就會耗盡，這是為了節省記憶體。
"""

# 基礎用法
print("=== 基礎用法 ===")

# 創建 zip 物件
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

zipped = zip(names, ages)
print(f"zip 物件: {zipped}")
print(f"zip 類型: {type(zipped)}")

# 第一次使用
print("第一次遍歷:")
for name, age in zipped:
    print(f"{name}: {age}")

# 第二次使用 - 空的！
print("第二次遍歷:")
for name, age in zipped:
    print(f"{name}: {age}")  # 不會執行

print("zip 已耗盡")

# 正確做法：轉換為列表或重複創建
zipped_list = list(zip(names, ages))
print(f"\n轉換為列表: {zipped_list}")

# 或者重新創建 zip
zipped_again = zip(names, ages)
print("重新創建 zip:")
for name, age in zipped_again:
    print(f"{name}: {age}")

# 進階應用
print("\n=== 進階應用 ===")

# zip 的其他用途
# 1. 矩陣轉置
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = list(zip(*matrix))
print(f"原始矩陣: {matrix}")
print(f"轉置後: {transposed}")

# 2. 創建字典
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Taipei']
person_dict = dict(zip(keys, values))
print(f"創建字典: {person_dict}")

# 3. 並行迭代多個序列
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [10, 20, 30]

print("並行迭代:")
for item1, item2, item3 in zip(list1, list2, list3):
    print(f"{item1}, {item2}, {item3}")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 學生成績配對
students = ['Alice', 'Bob', 'Charlie', 'David']
math_scores = [85, 92, 78, 88]
english_scores = [90, 85, 92, 87]

print("學生成績:")
student_grades = list(zip(students, math_scores, english_scores))
for student, math, english in student_grades:
    avg = (math + english) / 2
    print(f"{student}: 數學 {math}, 英文 {english}, 平均 {avg:.1f}")

# 案例2: 產品庫存管理
products = ['筆記本', '手機', '平板']
prices = [25000, 15000, 12000]
stocks = [50, 30, 20]

print("\n產品庫存:")
inventory = list(zip(products, prices, stocks))
for product, price, stock in inventory:
    value = price * stock
    print(f"{product}: 單價 ${price:,}, 庫存 {stock}, 總值 ${value:,}")

# 案例3: 數據處理管道
def process_data(headers, *data_rows):
    """處理 CSV 類數據"""
    print(f"表頭: {headers}")

    # 使用 zip 將每行數據與表頭配對
    for i, row in enumerate(data_rows, 1):
        record = dict(zip(headers, row))
        print(f"記錄 {i}: {record}")

# 模擬 CSV 數據
headers = ['姓名', '年齡', '城市']
row1 = ['Alice', 25, 'Taipei']
row2 = ['Bob', 30, 'Kaohsiung']
row3 = ['Charlie', 28, 'Taichung']

process_data(headers, row1, row2, row3)

# 案例4: 比較兩個序列的差異
def find_differences(seq1, seq2):
    """找出兩個序列的差異"""
    differences = []
    for i, (a, b) in enumerate(zip(seq1, seq2)):
        if a != b:
            differences.append((i, a, b))
    return differences

list_a = [1, 2, 3, 4, 5]
list_b = [1, 2, 99, 4, 6]

diffs = find_differences(list_a, list_b)
print(f"\n序列差異: {diffs}")

# zip 與 itertools.zip_longest 的比較
from itertools import zip_longest

short_list = [1, 2, 3]
long_list = [10, 20, 30, 40, 50]

print(f"\nzip (短的決定長度): {list(zip(short_list, long_list))}")
print(f"zip_longest (填補 None): {list(zip_longest(short_list, long_list, fillvalue=None))}")

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. zip(*iterables) 返回迭代器，不是列表
2. 一次性消耗: 使用一次後迭代器耗盡
3. 記憶體高效: 不需要儲存所有配對結果
4. 長度由最短序列決定: zip(a, b) 長度為 min(len(a), len(b))
5. 常見用法: 轉置矩陣、創建字典、並行迭代
6. 轉換為列表: list(zip(...)) 保存結果以重複使用
7. itertools.zip_longest: 處理不同長度的序列
"""

prices = {'A': 2.0, 'B': 1.0}
z = zip(prices.values(), prices.keys())

min(z)  # OK（消耗掉迭代器）
# max(z)  # 會失敗：因為 z 已經被消耗完
