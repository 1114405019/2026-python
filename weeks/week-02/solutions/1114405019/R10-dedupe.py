# R10. 去重且保序（1.10）
"""
去重且保序：使用 dict.fromkeys() 或 OrderedDict 來去除重複元素，同時保持原始順序。

這個技巧在處理列表或序列時非常有用，特別是在需要保留元素出現順序的情況下。
"""

# 基礎用法
print("=== 基礎用法 ===")

# 原始列表包含重複元素
items = [1, 3, 2, 1, 4, 2, 5]
print(f"原始列表: {items}")

# 使用 dict.fromkeys() 去重且保序
unique_items = list(dict.fromkeys(items))
print(f"去重後的列表: {unique_items}")

# 另一種方式：使用 set，但不保序
unique_set = list(set(items))
print(f"使用 set 去重（不保序）: {unique_set}")

# 進階應用
print("\n=== 進階應用 ===")

# 處理字串列表
words = ["apple", "banana", "apple", "cherry", "banana"]
unique_words = list(dict.fromkeys(words))
print(f"字串去重: {unique_words}")

# 處理包含 None 的列表
data = [None, 1, None, 2, 1, None]
unique_data = list(dict.fromkeys(data))
print(f"包含 None 的去重: {unique_data}")

# 自訂去重條件（例如忽略大小寫）
case_insensitive = ["Apple", "banana", "APPLE", "Cherry"]
unique_case = list({word.lower(): word for word in case_insensitive}.values())
print(f"忽略大小寫去重: {unique_case}")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 處理用戶輸入的標籤
user_tags = ["python", "web", "python", "data", "web", "ai"]
clean_tags = list(dict.fromkeys(user_tags))
print(f"用戶標籤去重: {clean_tags}")

# 案例2: 合併多個列表並去重
list1 = [1, 2, 3]
list2 = [2, 3, 4, 5]
list3 = [3, 4, 5, 6]
merged = list1 + list2 + list3
unique_merged = list(dict.fromkeys(merged))
print(f"合併列表去重: {unique_merged}")

# 案例3: 處理檔案路徑列表
import os
paths = ["/home/user/file1.txt", "/home/user/file2.txt", "/home/user/file1.txt", "/tmp/temp.txt"]
unique_paths = list(dict.fromkeys(paths))
print(f"檔案路徑去重: {unique_paths}")

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. dict.fromkeys(iterable) 創建字典，鍵來自 iterable，值預設為 None
2. 轉換回 list 保持插入順序（Python 3.7+ 字典有序）
3. 適用於任何可雜湊的元素（int, str, tuple 等）
4. 時間複雜度 O(n)，空間複雜度 O(n)
5. 相比 set()，dict.fromkeys() 更明確表達「去重且保序」的意圖
6. 如果需要自訂去重邏輯，可以使用 key 參數（需手動實現）
"""

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
