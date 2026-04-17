# R06. defaultdict：自動處理缺失鍵的字典
# ============================================================================
# defaultdict 是 collections 模組中的強化版字典
# 當訪問不存在的鍵時，自動創建預設值，避免 KeyError
# 特別適用於計數、群組、累積等場景
# 比傳統的 dict + setdefault 更簡潔高效
# ============================================================================

from collections import defaultdict

## 1. 基礎 defaultdict 用法
# --------------------------------------------------------------------------
# defaultdict 接受一個工廠函數，當鍵不存在時自動呼叫

# 使用 list 作為預設值
print("=== 使用 list 作為預設值 ===")
d_list = defaultdict(list)
d_list['fruits'].append('apple')
d_list['fruits'].append('banana')
d_list['vegetables'].append('carrot')

print(f"水果：{d_list['fruits']}")
print(f"蔬菜：{d_list['vegetables']}")
print(f"不存在的鍵：{d_list['meat']}")  # 自動創建空列表

# 使用 set 作為預設值
print("\n=== 使用 set 作為預設值 ===")
d_set = defaultdict(set)
d_set['python'].add('Guido')
d_set['python'].add('Raymond')
d_set['java'].add('James')

print(f"Python 貢獻者：{d_set['python']}")
print(f"Java 貢獻者：{d_set['java']}")

## 2. 常見應用：文字計數
# --------------------------------------------------------------------------
# defaultdict(int) 用於計數是最常見的應用

print("\n=== 文字計數應用 ===")
text = "the quick brown fox jumps over the lazy dog"
word_count = defaultdict(int)

for word in text.split():
    word_count[word] += 1

print("單詞出現次數：")
for word, count in sorted(word_count.items()):
    print(f"  {word}: {count}")

# 比較：傳統方式需要檢查鍵是否存在
traditional_count = {}
for word in text.split():
    if word not in traditional_count:
        traditional_count[word] = 0
    traditional_count[word] += 1

print(f"\ndefaultdict 結果：{dict(word_count)}")
print(f"傳統方式結果：{traditional_count}")
print(f"結果是否相同：{word_count == traditional_count}")

## 3. 進階應用：群組與分類
# --------------------------------------------------------------------------
# 使用不同的預設值類型進行群組

print("\n=== 群組應用 ===")
# 按長度群組單詞
words_by_length = defaultdict(list)
for word in text.split():
    words_by_length[len(word)].append(word)

print("按單詞長度群組：")
for length, words in sorted(words_by_length.items()):
    print(f"  長度 {length}: {words}")

# 按首字母群組
words_by_initial = defaultdict(list)
for word in text.split():
    words_by_initial[word[0]].append(word)

print("\n按首字母群組：")
for initial, words in sorted(words_by_initial.items()):
    print(f"  {initial}: {words}")

## 4. 自訂預設值工廠函數
# --------------------------------------------------------------------------
# 可以傳入自訂函數作為預設值工廠

print("\n=== 自訂預設值工廠 ===")
def default_value():
    """自訂預設值函數"""
    return "預設值"

d_custom = defaultdict(default_value)
d_custom['existing'] = "實際值"
print(f"現有鍵：{d_custom['existing']}")
print(f"自動創建鍵：{d_custom['new_key']}")

# 使用 lambda 表達式
d_lambda = defaultdict(lambda: [0, 0, 0])  # 預設三元素列表
d_lambda['rgb']['red'] = 255  # 這會失敗，因為預設是列表不是字典
# 正確方式：
d_lambda = defaultdict(lambda: {'r': 0, 'g': 0, 'b': 0})
d_lambda['color1']['r'] = 255
d_lambda['color1']['g'] = 128
print(f"顏色字典：{dict(d_lambda)}")

## 5. 與傳統 dict.setdefaul() 的比較
# --------------------------------------------------------------------------
# defaultdict 通常比 setdefault 更簡潔

print("\n=== 與 setdefault 比較 ===")

# 使用 setdefault
d_traditional = {}
for word in text.split():
    d_traditional.setdefault(word, 0)
    d_traditional[word] += 1

# 使用 defaultdict
d_default = defaultdict(int)
for word in text.split():
    d_default[word] += 1

print(f"setdefault 結果：{d_traditional}")
print(f"defaultdict 結果：{dict(d_default)}")
print(f"結果相同：{d_traditional == d_default}")

## 6. 實際應用：多層巢狀結構
# --------------------------------------------------------------------------
# defaultdict 可以巢狀使用

print("\n=== 多層巢狀結構 ===")
# 創建巢狀字典結構
def nested_dict():
    return defaultdict(nested_dict)

# 或者使用 partial
from functools import partial
nested_defaultdict = partial(defaultdict, nested_dict)

# 學生成績系統
grades = nested_dict()
grades['Alice']['math'] = 95
grades['Alice']['english'] = 88
grades['Bob']['math'] = 87
grades['Bob']['science'] = 92

print("學生成績：")
for student, subjects in grades.items():
    print(f"  {student}: {dict(subjects)}")

# 訪問不存在的巢狀鍵
print(f"不存在的科目：{grades['Charlie']['history']}")  # 自動創建

## 7. 效能考量
# --------------------------------------------------------------------------
# defaultdict 在大量操作中通常更高效

import time

words = text.split() * 1000  # 重複文字以增加測試規模

# defaultdict 方式
start = time.time()
count_dd = defaultdict(int)
for word in words:
    count_dd[word] += 1
dd_time = time.time() - start

# 傳統方式
start = time.time()
count_trad = {}
for word in words:
    count_trad[word] = count_trad.get(word, 0) + 1
trad_time = time.time() - start

print(".4f")
print(".4f")
print(".2f")

## 8. 注意事項與陷阱
# --------------------------------------------------------------------------
# defaultdict 的自動創建可能導致意外行為

print("\n=== 注意事項 ===")
d = defaultdict(int)

# 訪問不存在的鍵會自動創建
print(f"訪問 'new_key' 前：{'new_key' in d}")  # False
value = d['new_key']  # 自動創建並設為 0
print(f"訪問 'new_key' 後：{'new_key' in d}, 值：{d['new_key']}")  # True, 0

# 檢查鍵是否存在時要小心
if 'another_key' in d:  # 這不會創建鍵
    print("鍵存在")
else:
    print("鍵不存在，但訪問會創建")

# 強制轉換為普通字典
regular_dict = dict(d)
print(f"轉換為普通字典：{regular_dict}")

# ============================================================================
# 語法重點總結：
# 1. defaultdict(factory) 自動處理缺失鍵
# 2. 常見工廠：list, set, int, float 等
# 3. 適用於計數、群組、巢狀結構
# 4. 比 setdefault 更簡潔高效
# 5. 注意自動創建鍵的副作用
# ============================================================================
