# U01. 解包失敗的原因：變數數量 ≠ 元素數量（1.1）
"""
解包失敗的原因：變數數量 ≠ 元素數量

當進行序列解包時，如果變數數量與序列元素數量不匹配，會引發 ValueError。

理解這個錯誤的原因有助於正確使用解包語法。
"""

# 基礎用法
print("=== 基礎用法 ===")

# 正確的解包
a, b, c = [1, 2, 3]
print(f"正確解包: a={a}, b={b}, c={c}")

# 解包失敗：變數太多
try:
    x, y = [1, 2, 3]  # 2個變數 vs 3個元素
except ValueError as e:
    print(f"解包失敗（變數太少）: {e}")

# 解包失敗：變數太少
try:
    p, q, r, s = [1, 2, 3]  # 4個變數 vs 3個元素
except ValueError as e:
    print(f"解包失敗（變數太多）: {e}")

# 進階應用
print("\n=== 進階應用 ===")

# 使用 * 運算符處理不定長度
# 星號解包：吸收多餘元素
first, *rest = [1, 2, 3, 4, 5]
print(f"星號解包: first={first}, rest={rest}")

*head, last = [1, 2, 3, 4, 5]
print(f"星號解包: head={head}, last={last}")

first, *middle, last = [1, 2, 3, 4, 5]
print(f"星號解包: first={first}, middle={middle}, last={last}")

# 忽略不需要的元素
_, important, _ = [1, 42, 3]  # 使用 _ 忽略不需要的值
print(f"忽略元素: important={important}")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 解析座標
coordinates = [(10, 20), (30, 40), (50, 60)]

print("解析座標:")
for coord in coordinates:
    x, y = coord  # 正確：2個變數 vs 2個元素
    print(f"點: ({x}, {y})")

# 錯誤示例：嘗試解包為3個值
try:
    for coord in coordinates:
        x, y, z = coord  # 錯誤：3個變數 vs 2個元素
except ValueError as e:
    print(f"座標解包錯誤: {e}")

# 正確做法：使用星號處理可能的多餘維度
coords_with_optional_z = [(10, 20), (30, 40, 5), (50, 60)]
print("\n處理不定長度座標:")
for coord in coords_with_optional_z:
    x, y, *z = coord
    z_value = z[0] if z else 0
    print(f"點: ({x}, {y}, {z_value})")

# 案例2: 檔案路徑解析
paths = [
    "/home/user/file.txt",
    "/home/user/documents/report.pdf",
    "/home/user/pictures/vacation/photo.jpg"
]

print("\n解析檔案路徑:")
for path in paths:
    parts = path.split('/')
    *dirs, filename = parts
    print(f"路徑: {path}")
    print(f"  目錄: {'/'.join(dirs)}")
    print(f"  檔案: {filename}")

# 案例3: CSV 數據解析
csv_lines = [
    "Alice,25,Engineer",
    "Bob,30,Designer,New York",  # 多了一個欄位
    "Charlie,28,Manager"
]

print("\n解析 CSV 數據:")
for line in csv_lines:
    fields = line.split(',')
    name, age, job, *extra = fields  # 使用 *extra 處理多餘欄位
    print(f"姓名: {name}, 年齡: {age}, 職位: {job}")
    if extra:
        print(f"  額外資訊: {extra}")

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. 解包語法: a, b, c = iterable 要求變數數量 == 元素數量
2. ValueError: 當變數數量 != 元素數量時拋出
3. 星號解包: first, *rest = iterable 吸收多餘元素到列表
4. 忽略變數: 使用 _ 忽略不需要的值
5. 適用場景: 解析固定格式數據、處理不定長度序列
6. 錯誤預防: 使用 try-except 或星號解包處理不確定長度
7. 效能: 解包是淺複製，對於大型物件更高效
"""

p = (4, 5)
# x, y, z = p  # ValueError：元素只有 2 個但變數要 3 個
