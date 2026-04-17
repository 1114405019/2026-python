# U02. 星號解包為何能處理「不定長」且結果固定是 list（1.2）
"""
星號解包為何能處理「不定長」且結果固定是 list

星號解包運算符 * 能夠吸收序列中剩餘的所有元素到一個列表中，
無論剩餘元素數量多少，這使得它非常適合處理不定長度的序列。
"""

# 基礎用法
print("=== 基礎用法 ===")

# 基本星號解包
numbers = [1, 2, 3, 4, 5]

# 吸收剩餘元素到列表
first, *rest = numbers
print(f"first: {first}, rest: {rest} (類型: {type(rest)})")

*head, last = numbers
print(f"head: {head}, last: {last} (類型: {type(head)})")

first, *middle, last = numbers
print(f"first: {first}, middle: {middle}, last: {last}")

# 邊界情況
only_one = [42]
a, *b = only_one
print(f"單元素: a={a}, b={b}")

empty_rest = [1, 2]
x, *y = empty_rest
print(f"無剩餘: x={x}, y={y}")

# 進階應用
print("\n=== 進階應用 ===")

# 多重星號（Python 3.5+）
# 注意：只能有一個星號
# first, *middle, *rest = [1, 2, 3, 4]  # 錯誤：多個星號

# 在函數調用中使用星號解包
def calculate_sum(a, b, c, d=0):
    return a + b + c + d

values = [1, 2, 3, 4]
result = calculate_sum(*values)  # 解包為位置參數
print(f"函數調用解包: calculate_sum(*{values}) = {result}")

# 在列表/集合推導式中
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [x for row in matrix for x in row]
print(f"展平矩陣: {flattened}")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 解析命令行參數
command_args = ["program.py", "input.txt", "--verbose", "--output=result.txt"]

program, *options = command_args
print(f"程式: {program}")
print(f"選項: {options}")

# 分離檔案參數和旗標
files = []
flags = []
for arg in options:
    if arg.startswith('--'):
        flags.append(arg)
    else:
        files.append(arg)

print(f"檔案參數: {files}")
print(f"旗標: {flags}")

# 案例2: 處理巢狀列表
nested_data = [
    ["Alice", "Bob", "Charlie"],
    ["David"],
    ["Eve", "Frank", "Grace", "Henry"]
]

print("\n處理群組數據:")
for group in nested_data:
    leader, *members = group
    print(f"組長: {leader}, 成員: {members}")

# 案例3: 日誌記錄解析
log_entries = [
    "INFO 2023-10-01 10:00:00 User login",
    "ERROR 2023-10-01 10:05:00 Database connection failed",
    "WARNING 2023-10-01 10:10:00 Low disk space",
    "INFO 2023-10-01 10:15:00 Data backup completed successfully with 1024 files"
]

print("\n解析日誌:")
for entry in log_entries:
    parts = entry.split()
    level, date, time, *message_parts = parts
    message = ' '.join(message_parts)
    print(f"[{level}] {date} {time}: {message}")

# 案例4: 檔案路徑處理
file_paths = [
    "/home/user/document.txt",
    "/usr/local/bin/python",
    "/tmp/cache/temp.dat"
]

print("\n檔案路徑分析:")
for path in file_paths:
    *dirs, filename = path.split('/')
    print(f"路徑: {path}")
    print(f"  目錄: {'/'.join(dirs) if dirs else '根目錄'}")
    print(f"  檔案: {filename}")

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. 星號解包: *var = iterable 將剩餘元素收集到列表 var 中
2. 結果總是列表: 即使沒有元素也是空列表 []
3. 只能一個星號: 在單一解包語句中只能使用一個 *
4. 位置靈活: 可在任何位置使用 *var
5. 函數調用: func(*args) 解包為位置參數
6. 適用場景: 不定長度數據、參數解包、數據分割
7. 效能: 直接操作，不創建不必要的臨時物件
"""

record = ('Dave', 'dave@example.com')
name, email, *phones = record
# phones == []  仍是 list
