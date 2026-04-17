# U08. 字典最值為何常用 zip(values, keys)（1.8）
"""
字典最值為何常用 zip(values, keys)

當需要在字典中找到最大/最小值時，使用 zip(values, keys) 可以同時獲取值和對應的鍵。
這種方法避免了重複遍歷，並且在值相等時保持穩定的鍵順序。
"""

# 基礎用法
print("=== 基礎用法 ===")

# 成績字典
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 88}

print(f"成績數據: {scores}")

# 找到最高分
max_score = max(scores.values())
print(f"最高分: {max_score}")

# 但我們需要知道是誰得了最高分
# 方法1: 使用 zip(values, keys)
max_with_key = max(zip(scores.values(), scores.keys()))
print(f"最高分及學生: 分數={max_with_key[0]}, 學生={max_with_key[1]}")

# 方法2: 使用 key 參數
max_student = max(scores, key=scores.get)
print(f"最高分學生: {max_student} (分數: {scores[max_student]})")

# zip 的優勢：同時獲取值和鍵
min_with_key = min(zip(scores.values(), scores.keys()))
print(f"最低分及學生: 分數={min_with_key[0]}, 學生={min_with_key[1]}")

# 進階應用
print("\n=== 進階應用 ===")

# 多重條件排序
students = [
    {'name': 'Alice', 'score': 85, 'age': 20},
    {'name': 'Bob', 'score': 92, 'age': 22},
    {'name': 'Charlie', 'score': 85, 'age': 19},  # 與 Alice 分數相同
    {'name': 'David', 'score': 88, 'age': 21}
]

# 按分數降序，然後按年齡升序
best_student = max(students, key=lambda s: (s['score'], -s['age']))
print(f"最佳學生 (考慮分數和年齡): {best_student}")

# 使用 zip 處理多個序列
names = ['Alice', 'Bob', 'Charlie', 'David']
scores_list = [85, 92, 78, 88]

# 找到最高分的學生
max_info = max(zip(scores_list, names))
print(f"最高分: {max_info[0]} 分，學生: {max_info[1]}")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 銷售數據分析
sales_data = {
    '筆記本電腦': 150000,
    '手機': 280000,
    '平板電腦': 95000,
    '螢幕': 120000,
    '鍵盤': 45000
}

print("銷售數據:")
for product, amount in sales_data.items():
    print(f"  {product}: ${amount:,}")

# 找到最暢銷的產品
best_seller = max(zip(sales_data.values(), sales_data.keys()))
print(f"\n最暢銷產品: {best_seller[1]} (銷售額: ${best_seller[0]:,})")

# 找到銷售最差的產品
worst_seller = min(zip(sales_data.values(), sales_data.keys()))
print(f"銷售最差產品: {worst_seller[1]} (銷售額: ${worst_seller[0]:,})")

# 計算銷售排名
ranked_products = sorted(zip(sales_data.values(), sales_data.keys()), reverse=True)
print("\n銷售排名:")
for i, (amount, product) in enumerate(ranked_products, 1):
    print(f"  {i}. {product}: ${amount:,}")

# 案例2: 員工績效評估
employees = {
    'Alice': {'score': 85, 'projects': 5, 'experience': 3},
    'Bob': {'score': 92, 'projects': 4, 'experience': 5},
    'Charlie': {'score': 78, 'projects': 6, 'experience': 2},
    'David': {'score': 88, 'projects': 5, 'experience': 4}
}

print("\n員工績效:")
for name, data in employees.items():
    print(f"  {name}: 分數={data['score']}, 專案={data['projects']}, 年資={data['experience']}")

# 綜合評分：分數權重 0.5，專案權重 0.3，年資權重 0.2
def performance_score(emp_data):
    return (emp_data['score'] * 0.5 +
            emp_data['projects'] * 10 * 0.3 +
            emp_data['experience'] * 2 * 0.2)

performance_scores = {name: performance_score(data) for name, data in employees.items()}
print(f"\n綜合績效分數: {performance_scores}")

# 找到最佳員工
best_employee = max(zip(performance_scores.values(), performance_scores.keys()))
print(f"最佳員工: {best_employee[1]} (綜合分數: {best_employee[0]:.1f})")

# 案例3: 系統監控數據
servers = {
    'web-01': {'cpu': 45.2, 'memory': 67.8, 'disk': 23.1},
    'web-02': {'cpu': 78.9, 'memory': 89.5, 'disk': 45.6},
    'db-01': {'cpu': 92.3, 'memory': 78.1, 'disk': 67.4},
    'cache-01': {'cpu': 34.7, 'memory': 56.2, 'disk': 12.8}
}

print("\n伺服器狀態:")
for server, metrics in servers.items():
    print(f"  {server}: CPU={metrics['cpu']}%, 記憶體={metrics['memory']}%, 磁碟={metrics['disk']}%")

# 找到 CPU 使用率最高的伺服器
highest_cpu = max(zip((m['cpu'] for m in servers.values()), servers.keys()))
print(f"\nCPU 使用率最高: {highest_cpu[1]} ({highest_cpu[0]}%)")

# 找到記憶體使用率最低的伺服器
lowest_memory = min(zip((m['memory'] for m in servers.values()), servers.keys()))
print(f"記憶體使用率最低: {lowest_memory[1]} ({lowest_memory[0]}%)")

# 計算綜合負載（CPU + 記憶體 + 磁碟）
server_loads = {}
for server, metrics in servers.items():
    load = metrics['cpu'] + metrics['memory'] + metrics['disk']
    server_loads[server] = load

highest_load = max(zip(server_loads.values(), server_loads.keys()))
print(f"綜合負載最高: {highest_load[1]} (負載: {highest_load[0]:.1f})")

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. zip(values, keys) 將值和鍵配對，用於同時獲取兩者
2. max(zip(values, keys)) 返回 (最大值, 對應鍵)
3. min(zip(values, keys)) 返回 (最小值, 對應鍵)
4. 穩定性: 值相等時，保持原始鍵的順序
5. 適用場景: 字典最值查找、多條件排序
6. 替代方案: max(dict, key=dict.get) 只返回鍵
7. 效能: 單次遍歷，避免重複查找
"""

prices = {'A': 2.0, 'B': 1.0}

min(prices)            # 回傳 key 的最小值（字母序）
min(prices.values())   # 回傳最小 value，但你不知道是哪個 key

min(zip(prices.values(), prices.keys()))
# 回傳 (最小value, 對應key)，一次拿到兩者
