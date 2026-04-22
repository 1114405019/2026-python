# R11. 命名切片 slice（1.11）
"""
命名切片 slice：使用 slice() 物件為序列切片操作提供可讀的名稱。

這讓程式碼更易讀，特別是在處理複雜的切片邏輯時。
"""

# 基礎用法
print("=== 基礎用法 ===")

# 原始列表
data = list(range(1, 21))  # [1, 2, 3, ..., 20]
print(f"原始數據: {data}")

# 傳統切片
first_five = data[0:5]
last_five = data[-5:]
middle = data[5:15]
print(f"前5個: {first_five}")
print(f"後5個: {last_five}")
print(f"中間10個: {middle}")

# 使用命名切片
FIRST_FIVE = slice(0, 5)
LAST_FIVE = slice(-5, None)
MIDDLE = slice(5, 15)

print(f"使用命名切片 - 前5個: {data[FIRST_FIVE]}")
print(f"使用命名切片 - 後5個: {data[LAST_FIVE]}")
print(f"使用命名切片 - 中間10個: {data[MIDDLE]}")

# 進階應用
print("\n=== 進階應用 ===")

# 處理二維列表（矩陣）
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# 定義行列切片
ROW_SLICE = slice(0, 2)  # 前兩行
COL_SLICE = slice(1, 4)  # 第2-4列

selected_rows = matrix[ROW_SLICE]
print(f"選擇的行: {selected_rows}")

# 對每行應用列切片
selected_cols = [row[COL_SLICE] for row in matrix]
print(f"選擇的列: {selected_cols}")

# 處理字串
text = "Hello, World! This is a test string."
WORD_SLICE = slice(7, 12)  # 提取 "World"
print(f"提取單詞: '{text[WORD_SLICE]}'")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 解析 CSV 數據
csv_line = "John,Doe,30,Engineer,50000"
NAME_FIRST = slice(0, 1)
NAME_LAST = slice(1, 2)
AGE = slice(2, 3)
JOB = slice(3, 4)
SALARY = slice(4, 5)

fields = csv_line.split(',')
print(f"姓名: {fields[NAME_FIRST][0]} {fields[NAME_LAST][0]}")
print(f"年齡: {fields[AGE][0]}")
print(f"職業: {fields[JOB][0]}")
print(f"薪資: {fields[SALARY][0]}")

# 案例2: 處理日誌檔案
log_line = "2023-10-01 10:30:45 INFO User login successful"
TIMESTAMP = slice(0, 19)
LEVEL = slice(20, 24)
MESSAGE = slice(25, None)

print(f"時間戳: {log_line[TIMESTAMP]}")
print(f"日誌等級: {log_line[LEVEL]}")
print(f"訊息: {log_line[MESSAGE]}")

# 案例3: 圖像處理（模擬像素陣列）
image = [
    [255, 0, 0, 255, 0],
    [0, 255, 0, 0, 255],
    [0, 0, 255, 255, 0],
    [255, 255, 0, 0, 0],
    [0, 255, 255, 255, 255]
]

# 提取子區域
REGION = slice(1, 4), slice(1, 4)  # 3x3 區域
sub_region = [row[REGION[1]] for row in image[REGION[0]]]
print(f"子區域: {sub_region}")

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. slice(start, stop, step) 創建切片物件
2. 可以將切片物件儲存為變數，提供語意化的名稱
3. 適用於任何支援切片的序列（list, str, tuple 等）
4. 支援多維切片（例如用於二維列表）
5. 提高程式碼可讀性和維護性
6. 切片物件是不可變的，可以安全地重用
"""

record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
