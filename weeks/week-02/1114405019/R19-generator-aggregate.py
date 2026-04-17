# R19. 轉換+聚合：生成器表達式（1.19）
"""
轉換+聚合：生成器表達式（1.19）

使用生成器表達式進行數據轉換和聚合操作，結合內建函數如 sum()、max()、min() 等。

生成器表達式提供了記憶體高效的數據處理方式。
"""

# 基礎用法
print("=== 基礎用法 ===")

# 原始數據
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"原始數據: {numbers}")

# 基本聚合
total = sum(numbers)
maximum = max(numbers)
minimum = min(numbers)
count = len(numbers)
average = total / count

print(f"總和: {total}")
print(f"最大值: {maximum}")
print(f"最小值: {minimum}")
print(f"數量: {count}")
print(f"平均值: {average}")

# 使用生成器表達式進行轉換+聚合
squares_sum = sum(x**2 for x in numbers)
even_sum = sum(x for x in numbers if x % 2 == 0)
positive_count = sum(1 for x in numbers if x > 0)

print(f"平方和: {squares_sum}")
print(f"偶數和: {even_sum}")
print(f"正數個數: {positive_count}")

# 進階應用
print("\n=== 進階應用 ===")

# 處理複雜數據結構
data = [
    {'name': 'Alice', 'scores': [85, 92, 78]},
    {'name': 'Bob', 'scores': [88, 95, 82]},
    {'name': 'Charlie', 'scores': [90, 87, 93]}
]

# 計算每個人的平均分
averages = [sum(person['scores']) / len(person['scores']) for person in data]
print(f"個人平均分: {averages}")

# 使用生成器計算全班平均分
class_average = sum(
    sum(person['scores']) / len(person['scores'])
    for person in data
) / len(data)
print(f"全班平均分: {class_average:.2f}")

# 計算最高分和最低分
all_scores = (score for person in data for score in person['scores'])
highest_score = max(all_scores)
lowest_score = min(score for person in data for score in person['scores'])

print(f"最高分: {highest_score}")
print(f"最低分: {lowest_score}")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 銷售數據分析
sales = [
    {'product': 'A', 'quarterly_sales': [100, 120, 95, 110]},
    {'product': 'B', 'quarterly_sales': [80, 90, 85, 95]},
    {'product': 'C', 'quarterly_sales': [150, 160, 140, 170]}
]

print("產品銷售分析:")
for product in sales:
    quarterly = product['quarterly_sales']
    total_sales = sum(quarterly)
    avg_quarterly = total_sales / len(quarterly)
    max_quarter = max(quarterly)
    min_quarter = min(quarterly)

    print(f"{product['product']}:")
    print(f"  總銷售: {total_sales}")
    print(f"  季度平均: {avg_quarterly:.1f}")
    print(f"  最高季度: {max_quarter}")
    print(f"  最低季度: {min_quarter}")

# 全年總銷售
total_yearly_sales = sum(
    sum(product['quarterly_sales']) for product in sales
)
print(f"\n全年總銷售: {total_yearly_sales}")

# 案例2: 文字統計
text = """
Python is a high-level programming language known for its simplicity and readability.
It supports multiple programming paradigms and has a large standard library.
Python is widely used in web development, data science, and automation.
"""

# 統計單詞數量和平均長度
import re
words = re.findall(r'\b\w+\b', text.lower())

word_count = sum(1 for _ in words)
unique_words = len(set(words))
avg_word_length = sum(len(word) for word in words) / word_count

print("
文字統計:")
print(f"總單詞數: {word_count}")
print(f"唯一單詞數: {unique_words}")
print(f"平均單詞長度: {avg_word_length:.2f}")

# 統計句子數量
sentences = re.split(r'[.!?]+', text.strip())
sentence_count = sum(1 for s in sentences if s.strip())
print(f"句子數量: {sentence_count}")

# 案例3: 檔案大小統計
import os

# 模擬檔案資訊
files = [
    {'name': 'document.txt', 'size': 1024},
    {'name': 'image.jpg', 'size': 2048000},
    {'name': 'script.py', 'size': 512},
    {'name': 'data.csv', 'size': 1048576},
    {'name': 'archive.zip', 'size': 5242880}
]

# 統計檔案大小
total_size = sum(file['size'] for file in files)
avg_size = total_size / len(files)
max_size_file = max(files, key=lambda f: f['size'])
min_size_file = min(files, key=lambda f: f['size'])

print("
檔案統計:")
print(f"總大小: {total_size:,} bytes")
print(f"平均大小: {avg_size:,.0f} bytes")
print(f"最大檔案: {max_size_file['name']} ({max_size_file['size']:,} bytes)")
print(f"最小檔案: {min_size_file['name']} ({min_size_file['size']:,} bytes)")

# 按檔案類型統計
extensions = {}
for file in files:
    ext = os.path.splitext(file['name'])[1]
    if ext not in extensions:
        extensions[ext] = []
    extensions[ext].append(file['size'])

print("\n按類型統計:")
for ext, sizes in extensions.items():
    count = len(sizes)
    total = sum(sizes)
    avg = total / count
    print(f"{ext or '無擴展名'}: {count} 個檔案, 總大小 {total:,} bytes, 平均 {avg:,.0f} bytes")

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. 生成器表達式: (expr for item in iterable if condition) - 記憶體高效
2. 與聚合函數結合: sum(), max(), min(), len() 等
3. 巢狀生成器: 處理複雜數據結構
4. 條件過濾: 在生成器中包含 if 條件
5. 鏈式操作: 多個生成器表達式組合
6. 適用場景: 大數據處理、統計計算、數據轉換
7. 效能優勢: 避免創建中間列表，節省記憶體
"""

nums = [1, 2, 3]
sum(x * x for x in nums)

s = ('ACME', 50, 123.45)
','.join(str(x) for x in s)

portfolio = [{'name': 'AOL', 'shares': 20}, {'name': 'YHOO', 'shares': 75}]
min(s['shares'] for s in portfolio)
min(portfolio, key=lambda s: s['shares'])
