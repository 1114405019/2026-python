# R14. 物件排序 attrgetter（1.14）
"""
物件排序 attrgetter：使用 operator.attrgetter 作為排序鍵，對物件列表進行排序。

這提供了比 lambda 函數更高效和清晰的方式來指定物件屬性作為排序依據。
"""

from operator import attrgetter

# 定義一個簡單的類別
class Person:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, score={self.score})"

# 基礎用法
print("=== 基礎用法 ===")

# 創建物件列表
people = [
    Person('Alice', 25, 85),
    Person('Bob', 30, 92),
    Person('Charlie', 22, 78),
    Person('David', 28, 88)
]

print("原始數據:")
for person in people:
    print(person)

# 按年齡排序
sorted_by_age = sorted(people, key=attrgetter('age'))
print("\n按年齡排序:")
for person in sorted_by_age:
    print(person)

# 按分數降序排序
sorted_by_score_desc = sorted(people, key=attrgetter('score'), reverse=True)
print("\n按分數降序排序:")
for person in sorted_by_score_desc:
    print(person)

# 進階應用
print("\n=== 進階應用 ===")

# 多重排序條件
# 先按分數降序，再按年齡升序
sorted_multi = sorted(people, key=attrgetter('score', 'age'), reverse=True)
print("多重排序（分數降序，年齡升序）:")
for person in sorted_multi:
    print(person)

# 與 lambda 比較
sorted_lambda = sorted(people, key=lambda x: (x.score, x.age), reverse=True)
print("\n使用 lambda 的等效排序:")
for person in sorted_lambda:
    print(person)

# 處理巢狀屬性
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class Classroom:
    def __init__(self, students):
        self.students = students

    def get_top_student(self):
        return max(self.students, key=attrgetter('grade'))

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 員工薪資排序
class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def __repr__(self):
        return f"Employee({self.name}, {self.department}, ${self.salary})"

employees = [
    Employee('小明', '工程', 50000),
    Employee('小華', '銷售', 45000),
    Employee('小美', '工程', 55000),
    Employee('小李', '銷售', 40000)
]

# 按薪資排序
sorted_by_salary = sorted(employees, key=attrgetter('salary'), reverse=True)
print("按薪資排序:")
for emp in sorted_by_salary:
    print(emp)

# 按部門和薪資排序
sorted_by_dept_salary = sorted(employees, key=attrgetter('department', 'salary'))
print("\n按部門和薪資排序:")
for emp in sorted_by_dept_salary:
    print(emp)

# 案例2: 商品庫存排序
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Product({self.name}, ${self.price}, 庫存:{self.stock})"

products = [
    Product('筆記本', 25, 100),
    Product('鉛筆', 5, 200),
    Product('橡皮擦', 3, 150),
    Product('尺', 10, 50)
]

# 按庫存量排序（找出庫存不足的商品）
sorted_by_stock = sorted(products, key=attrgetter('stock'))
print("\n按庫存量排序:")
for product in sorted_by_stock:
    print(product)

# 案例3: 學生成績排序
students = [
    Student('小明', 85),
    Student('小華', 92),
    Student('小美', 78),
    Student('小李', 88)
]

# 按成績排序
sorted_by_grade = sorted(students, key=attrgetter('grade'), reverse=True)
print("\n按成績排序:")
for student in sorted_by_grade:
    print(f"{student.name}: {student.grade} 分")

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. attrgetter(attr) 創建一個函數，用於從物件中提取指定屬性的值
2. 可以接受多個屬性：attrgetter('attr1', 'attr2') 返回元組
3. 比 lambda 函數更高效，因為它在 C 層級實現
4. 適用於任何有指定屬性的物件
5. 對於物件列表排序，提供清晰的排序依據
6. 可以與 sorted()、min()、max() 等函數配合使用
7. 支援巢狀屬性訪問（如果物件有對應的屬性）
"""

from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id

users = [User(23), User(3), User(99)]
sorted(users, key=attrgetter('user_id'))
