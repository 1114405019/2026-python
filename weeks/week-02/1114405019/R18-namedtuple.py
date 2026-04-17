# R18. namedtuple（1.18）
"""
namedtuple：使用 collections.namedtuple 創建輕量級的不可變物件，類似於簡單的類別。

namedtuple 提供了元組的效率和類別的可讀性，是介於元組和類別之間的理想選擇。
"""

from collections import namedtuple

# 基礎用法
print("=== 基礎用法 ===")

# 定義 namedtuple
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age email')

# 創建實例
p1 = Point(10, 20)
p2 = Point(x=5, y=15)
print(f"點 p1: {p1}")
print(f"點 p2: {p2}")

person1 = Person('Alice', 25, 'alice@example.com')
person2 = Person(name='Bob', age=30, email='bob@example.com')
print(f"人 person1: {person1}")
print(f"人 person2: {person2}")

# 訪問屬性
print(f"p1.x: {p1.x}, p1.y: {p1.y}")
print(f"person1.name: {person1.name}, person1.age: {person1.age}")

# 索引訪問（仍然是元組）
print(f"p1[0]: {p1[0]}, p1[1]: {p1[1]}")

# 進階應用
print("\n=== 進階應用 ===")

# 帶有預設值的 namedtuple
Employee = namedtuple('Employee', 'name department salary', defaults=['Engineering', 50000])
emp1 = Employee('Alice')
emp2 = Employee('Bob', 'Sales')
emp3 = Employee('Charlie', 'Engineering', 60000)
print(f"員工 emp1: {emp1}")
print(f"員工 emp2: {emp2}")
print(f"員工 emp3: {emp3}")

# 轉換為字典
point_dict = p1._asdict()
print(f"點轉字典: {point_dict}")

# 替換值（創建新實例）
p3 = p1._replace(x=100)
print(f"替換後的點: {p3}")
print(f"原始點不變: {p1}")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 座標系統
Coordinate = namedtuple('Coordinate', 'latitude longitude altitude', defaults=[0.0])

locations = [
    Coordinate(40.7128, -74.0060, 10),  # 紐約
    Coordinate(34.0522, -118.2437),     # 洛杉磯
    Coordinate(51.5074, -0.1278, 35)    # 倫敦
]

print("地理座標:")
for loc in locations:
    print(f"緯度: {loc.latitude:.4f}, 經度: {loc.longitude:.4f}, 海拔: {loc.altitude}m")

# 案例2: 股票數據
Stock = namedtuple('Stock', 'symbol price change volume')

portfolio = [
    Stock('AAPL', 150.25, 2.5, 1000000),
    Stock('GOOGL', 2800.50, -15.2, 500000),
    Stock('MSFT', 305.75, 5.8, 800000)
]

print("\n股票投資組合:")
total_value = 0
for stock in portfolio:
    value = stock.price * stock.volume
    total_value += value
    print(f"{stock.symbol}: ${stock.price} ({stock.change:+.1f}), 成交量: {stock.volume:,}, 價值: ${value:,.0f}")

print(f"總價值: ${total_value:,.0f}")

# 案例3: HTTP 響應
HTTPResponse = namedtuple('HTTPResponse', 'status_code headers body')

responses = [
    HTTPResponse(200, {'Content-Type': 'application/json'}, '{"message": "success"}'),
    HTTPResponse(404, {'Content-Type': 'text/html'}, '<h1>Not Found</h1>'),
    HTTPResponse(500, {'Content-Type': 'text/plain'}, 'Internal Server Error')
]

print("\nHTTP 響應:")
for resp in responses:
    print(f"狀態碼: {resp.status_code}")
    print(f"內容類型: {resp.headers.get('Content-Type', 'unknown')}")
    print(f"響應體: {resp.body[:50]}...")
    print()

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. namedtuple(typename, field_names) 創建具名元組類別
2. field_names 可以是字串（空格分隔）或序列
3. 支援預設值：defaults 參數
4. 屬性訪問：obj.field_name
5. 索引訪問：obj[index]（向後相容）
6. _asdict() 轉換為字典
7. _replace(**kwargs) 創建新實例（不可變性）
8. 記憶體效率高於普通類別
9. 適用於簡單數據結構，如座標、記錄等
"""

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
sub.addr

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)
s = s._replace(shares=75)
