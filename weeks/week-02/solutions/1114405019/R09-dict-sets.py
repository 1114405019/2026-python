# R09. 字典的集合運算：鍵值比較與交集
# ============================================================================
# 字典的 keys() 和 items() 返回 dict_keys 物件，支援集合運算
# 可以輕鬆找出兩個字典的共同鍵、不同鍵、相同鍵值對等
# 適用於資料比較、合併、過濾等場景
# ============================================================================

## 1. 基礎字典集合運算
# --------------------------------------------------------------------------
# dict.keys() 和 dict.items() 支援集合運算

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

print(f"字典 a：{a}")
print(f"字典 b：{b}")

# 共同鍵（交集）
common_keys = a.keys() & b.keys()
print(f"共同鍵：{common_keys}")

# a 中有但 b 中沒有的鍵（差集）
unique_to_a = a.keys() - b.keys()
print(f"a 獨有的鍵：{unique_to_a}")

# b 中有但 a 中沒有的鍵
unique_to_b = b.keys() - a.keys()
print(f"b 獨有的鍵：{unique_to_b}")

# 聯集（所有鍵）
all_keys = a.keys() | b.keys()
print(f"所有鍵：{all_keys}")

## 2. 鍵值對的集合運算
# --------------------------------------------------------------------------
# items() 返回 (鍵, 值) 元組的集合

# 完全相同的鍵值對
common_items = a.items() & b.items()
print(f"相同的鍵值對：{common_items}")

# a 中有但 b 中不同的鍵值對
diff_items_a = a.items() - b.items()
print(f"a 中不同的鍵值對：{diff_items_a}")

# b 中有但 a 中不同的鍵值對
diff_items_b = b.items() - b.items()  # 這是空的，因為 b.items() 減去自己
print(f"b 中不同的鍵值對：{diff_items_b}")

## 3. 實際應用：字典過濾與合併
# --------------------------------------------------------------------------
# 使用集合運算進行字典操作

# 從字典中過濾特定鍵
c = {k: a[k] for k in a.keys() - {'z', 'w'}}
print(f"過濾後的字典 c：{c}")

# 合併字典，處理鍵衝突
def merge_dicts(d1, d2, conflict_resolver=None):
    """
    合併兩個字典
    conflict_resolver: 衝突解決函數，參數為 (key, val1, val2)
    """
    result = d1.copy()

    for key, val2 in d2.items():
        if key in result:
            if conflict_resolver:
                result[key] = conflict_resolver(key, result[key], val2)
            else:
                # 預設保留 d2 的值
                result[key] = val2
        else:
            result[key] = val2

    return result

# 測試合併
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 40}

merged = merge_dicts(dict1, dict2)
print(f"合併結果（保留後者）：{merged}")

# 自訂衝突解決器（相加）
merged_sum = merge_dicts(dict1, dict2, lambda k, v1, v2: v1 + v2)
print(f"合併結果（相加）：{merged_sum}")

## 4. 進階應用：資料比較與差異分析
# --------------------------------------------------------------------------
# 使用集合運算分析字典差異

def dict_diff(d1, d2):
    """
    比較兩個字典，返回差異報告
    """
    diff = {
        'added': d2.keys() - d1.keys(),      # 新增的鍵
        'removed': d1.keys() - d2.keys(),    # 刪除的鍵
        'changed': set(),                    # 值改變的鍵
        'unchanged': set()                   # 值相同的鍵
    }

    # 找出值改變的鍵
    for key in d1.keys() & d2.keys():
        if d1[key] != d2[key]:
            diff['changed'].add(key)
        else:
            diff['unchanged'].add(key)

    return diff

# 測試差異分析
old_config = {'host': 'localhost', 'port': 8080, 'debug': True, 'timeout': 30}
new_config = {'host': 'localhost', 'port': 9090, 'debug': False, 'ssl': True}

diff = dict_diff(old_config, new_config)
print(f"\n配置差異分析：")
print(f"  新增：{diff['added']}")
print(f"  刪除：{diff['removed']}")
print(f"  改變：{diff['changed']}")
print(f"  不變：{diff['unchanged']}")

## 5. 集合運算的效能特點
# --------------------------------------------------------------------------
# dict_keys 物件的集合運算是 O(min(len(d1), len(d2))) 時間複雜度

import time

# 創建大型字典
large_dict1 = {f'key{i}': i for i in range(10000)}
large_dict2 = {f'key{i}': i + 10000 for i in range(5000, 15000)}

# 測試集合運算效能
start = time.time()
common = large_dict1.keys() & large_dict2.keys()
intersection_time = time.time() - start

start = time.time()
diff = large_dict1.keys() - large_dict2.keys()
difference_time = time.time() - start

print(".4f")
print(".4f")

## 6. 實際應用：學生成績比較
# --------------------------------------------------------------------------
# 比較不同學期的學生成績

semester1 = {
    'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 88
}

semester2 = {
    'Alice': 90, 'Bob': 88, 'Eve': 95, 'Frank': 82
}

print(f"\n學期成績比較：")
print(f"學期 1：{semester1}")
print(f"學期 2：{semester2}")

# 找出持續參加的學生
continuing_students = semester1.keys() & semester2.keys()
print(f"持續參加的學生：{continuing_students}")

# 找出新加入的學生
new_students = semester2.keys() - semester1.keys()
print(f"新加入的學生：{new_students}")

# 找出退出的學生
left_students = semester1.keys() - semester2.keys()
print(f"退出的學生：{left_students}")

# 計算持續學生的成績變化
print("持續學生的成績變化：")
for student in continuing_students:
    change = semester2[student] - semester1[student]
    direction = "上升" if change > 0 else "下降" if change < 0 else "不變"
    print(f"  {student}: {semester1[student]} → {semester2[student]} ({direction} {abs(change)} 分)")

## 7. 注意事項與最佳實踐
# --------------------------------------------------------------------------
# 集合運算的注意事項

print("\n=== 注意事項 ===")

# keys() 返回 dict_keys 物件，不是集合
keys_obj = a.keys()
print(f"keys() 類型：{type(keys_obj)}")
print(f"是否支援交集：{hasattr(keys_obj, '__and__')}")

# 可以轉換為集合進行更多操作
keys_set = set(a.keys())
print(f"轉換為集合：{keys_set}")
print(f"集合支援更多操作：{hasattr(keys_set, 'issubset')}")

# items() 運算考慮鍵和值
items1 = {('x', 1), ('y', 2)}
items2 = {('x', 1), ('y', 3)}
intersection = items1 & items2
print(f"items 交集：{intersection}")

# 值不同時不匹配
d1 = {'a': 1, 'b': 2}
d2 = {'a': 1, 'b': 3}
same_items = d1.items() & d2.items()
print(f"相同 items：{same_items}")

# ============================================================================
# 語法重點總結：
# 1. keys() & keys() 求共同鍵
# 2. keys() - keys() 求差集鍵
# 3. items() & items() 求相同鍵值對
# 4. 適用於字典比較、合併、過濾
# 5. 時間複雜度為 O(min(len(d1), len(d2)))
# ============================================================================
