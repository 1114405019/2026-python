# R08. 字典的極值查找：min/max 與 key 參數
# ============================================================================
# 在字典上使用 min/max 函數查找極值
# 使用 key 參數指定比較基準，可以按值或鍵進行比較
# zip() 可以將鍵值對轉換為可比較的元組
# 適用於查找最便宜/最貴項目、按條件排序等
# ============================================================================

## 1. 基礎字典極值查找
# --------------------------------------------------------------------------
# 使用 min/max 在字典上查找極值

prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75, 'GOOG': 205.45}

print(f"股票價格：{prices}")

# 查找最便宜的股票（按值比較）
min_price = min(prices.values())
print(f"最低價格：{min_price}")

# 查找最貴的股票（按值比較）
max_price = max(prices.values())
print(f"最高價格：{max_price}")

# 查找按字母順序的第一支股票（按鍵比較）
first_stock = min(prices.keys())
print(f"字母順序第一支：{first_stock}")

## 2. 使用 key 參數的自訂比較
# --------------------------------------------------------------------------
# key 參數指定比較的基準函數

# 按價格找最便宜的股票（返回鍵）
cheapest_stock = min(prices, key=lambda k: prices[k])
print(f"最便宜的股票：{cheapest_stock}（價格：{prices[cheapest_stock]}）")

# 按價格找最貴的股票
most_expensive = max(prices, key=lambda k: prices[k])
print(f"最貴的股票：{most_expensive}（價格：{prices[most_expensive]}）")

# 按股票代碼長度排序
shortest_code = min(prices, key=lambda k: len(k))
print(f"代碼最短的股票：{shortest_code}")

## 3. 使用 zip 的極值查找
# --------------------------------------------------------------------------
# zip(values, keys) 創建 (值, 鍵) 元組進行比較

# 查找最便宜的股票及其價格
min_by_zip = min(zip(prices.values(), prices.keys()))
print(f"zip 方式的最低價：價格={min_by_zip[0]}, 股票={min_by_zip[1]}")

# 查找最貴的股票及其價格
max_by_zip = max(zip(prices.values(), prices.keys()))
print(f"zip 方式的最高價：價格={max_by_zip[0]}, 股票={max_by_zip[1]}")

# 排序所有股票（按價格）
sorted_by_zip = sorted(zip(prices.values(), prices.keys()))
print("按價格排序的股票：")
for price, stock in sorted_by_zip:
    print(f"  {stock}: ${price}")

## 4. 進階應用：複雜條件的極值查找
# --------------------------------------------------------------------------
# 使用更複雜的 key 函數

portfolio = [
    {'name': 'ACME', 'shares': 100, 'price': 45.23},
    {'name': 'AAPL', 'shares': 50, 'price': 612.78},
    {'name': 'FB', 'shares': 200, 'price': 10.75},
    {'name': 'GOOG', 'shares': 75, 'price': 205.45}
]

print(f"\n投資組合：{portfolio}")

# 按總價值找最大投資
highest_value = max(portfolio, key=lambda s: s['shares'] * s['price'])
print(f"總價值最大的投資：{highest_value['name']}（價值：${highest_value['shares'] * highest_value['price']:.2f}）")

# 按每股價格找最便宜
cheapest_per_share = min(portfolio, key=lambda s: s['price'])
print(f"每股最便宜：{cheapest_per_share['name']}（每股：${cheapest_per_share['price']}）")

# 按投資份額排序
sorted_by_value = sorted(portfolio, key=lambda s: s['shares'] * s['price'], reverse=True)
print("按總價值排序：")
for stock in sorted_by_value:
    value = stock['shares'] * stock['price']
    print(f"  {stock['name']}: ${value:.2f}")

## 5. 多重條件的極值查找
# --------------------------------------------------------------------------
# 使用元組作為 key 進行多重條件排序

employees = [
    {'name': 'Alice', 'age': 30, 'salary': 75000},
    {'name': 'Bob', 'age': 25, 'salary': 80000},
    {'name': 'Charlie', 'age': 35, 'salary': 75000},
    {'name': 'David', 'age': 28, 'salary': 70000}
]

print(f"\n員工資料：{employees}")

# 按薪資降序，年齡升序排序（薪資相同時年輕的優先）
sorted_employees = sorted(employees, key=lambda e: (-e['salary'], e['age']))
print("按薪資降序，年齡升序排序：")
for emp in sorted_employees:
    print(f"  {emp['name']}: 年齡{emp['age']}, 薪資${emp['salary']}")

# 查找最佳候選人（薪資最高，年齡最小）
best_candidate = min(employees, key=lambda e: (-e['salary'], e['age']))
print(f"最佳候選人：{best_candidate['name']}（薪資${best_candidate['salary']}, 年齡{best_candidate['age']}）")

## 6. 實際應用：資料分析場景
# --------------------------------------------------------------------------
# 在資料分析中的實際應用

sales_data = {
    'Q1': {'revenue': 100000, 'profit': 15000},
    'Q2': {'revenue': 120000, 'profit': 18000},
    'Q3': {'revenue': 95000, 'profit': 12000},
    'Q4': {'revenue': 135000, 'profit': 22000}
}

print(f"\n季度銷售資料：{sales_data}")

# 查找利潤最高的季度
best_quarter = max(sales_data, key=lambda q: sales_data[q]['profit'])
print(f"利潤最高的季度：{best_quarter}（利潤：${sales_data[best_quarter]['profit']}）")

# 查找收入最低的季度
worst_revenue = min(sales_data, key=lambda q: sales_data[q]['revenue'])
print(f"收入最低的季度：{worst_revenue}（收入：${sales_data[worst_revenue]['revenue']}）")

# 按利潤率排序季度
sorted_by_margin = sorted(sales_data.items(),
                         key=lambda x: x[1]['profit'] / x[1]['revenue'],
                         reverse=True)
print("按利潤率排序的季度：")
for quarter, data in sorted_by_margin:
    margin = data['profit'] / data['revenue']
    print(f"  {quarter}: 利潤率 {margin:.1%}")

## 7. 效能考量與最佳實踐
# --------------------------------------------------------------------------
# zip 方式 vs key 參數方式的比較

import time

# 大型字典測試
large_dict = {f'key{i}': i * 1.1 for i in range(10000)}

# 使用 key 參數
start = time.time()
for _ in range(100):
    result1 = min(large_dict, key=lambda k: large_dict[k])
key_time = time.time() - start

# 使用 zip 方式
start = time.time()
for _ in range(100):
    result2 = min(zip(large_dict.values(), large_dict.keys()))
zip_time = time.time() - start

print(".4f")
print(".4f")
print(".2f")

# 驗證結果一致
assert result1 == result2[1], "結果不一致！"

## 8. 常見陷阱與注意事項
# --------------------------------------------------------------------------
# 使用 min/max 時的注意事項

print("\n=== 注意事項 ===")

# 空字典會引發錯誤
try:
    min({}, key=lambda k: k)
except ValueError as e:
    print(f"空字典錯誤：{e}")

# key 函數必須為所有元素返回可比較的值
mixed_dict = {'a': 1, 'b': 'hello', 'c': [1, 2]}
try:
    max(mixed_dict, key=lambda k: mixed_dict[k])
except TypeError as e:
    print(f"類型錯誤：{e}")

# 正確處理混合類型
mixed_dict_safe = {'a': 1, 'b': 2, 'c': 3}  # 全部轉為數字
safe_max = max(mixed_dict_safe, key=lambda k: mixed_dict_safe[k])
print(f"安全比較結果：{safe_max}")

# ============================================================================
# 語法重點總結：
# 1. min/max(dict, key=func) 按自訂基準比較
# 2. zip(values, keys) 創建 (值, 鍵) 元組
# 3. key=lambda k: dict[k] 按值比較
# 4. 多重條件用元組：(-salary, age)
# 5. 適用於查找極值、排序等場景
# ============================================================================
