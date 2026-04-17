# R12. Counter 統計 + most_common（1.12）
"""
Counter 統計 + most_common：使用 collections.Counter 進行元素計數，並獲取最常見的元素。

這是處理頻率統計的強大工具，特別適用於數據分析和文字處理。
"""

from collections import Counter

# 基礎用法
print("=== 基礎用法 ===")

# 統計列表中元素的出現次數
items = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counter = Counter(items)
print(f"原始數據: {items}")
print(f"計數結果: {counter}")

# 獲取最常見的元素
most_common = counter.most_common(2)
print(f"最常見的2個元素: {most_common}")

# 單個元素的計數
print(f"apple 出現次數: {counter['apple']}")
print(f"orange 出現次數: {counter['orange']}")  # 不存在的鍵返回 0

# 進階應用
print("\n=== 進階應用 ===")

# 統計字串中字符的頻率
text = "hello world, this is a test message"
char_counter = Counter(text)
print(f"字符頻率: {char_counter}")

# 統計單詞頻率（忽略大小寫和標點）
import re
words = re.findall(r'\b\w+\b', text.lower())
word_counter = Counter(words)
print(f"單詞頻率: {word_counter}")

# Counter 的數學運算
counter1 = Counter(['a', 'b', 'a', 'c'])
counter2 = Counter(['a', 'b', 'b', 'd'])
print(f"Counter1: {counter1}")
print(f"Counter2: {counter2}")
print(f"相加: {counter1 + counter2}")
print(f"相減: {counter1 - counter2}")
print(f"交集: {counter1 & counter2}")
print(f"聯集: {counter1 | counter2}")

# 實際案例
print("\n=== 實際案例 ===")

# 案例1: 分析投票結果
votes = ['候選人A', '候選人B', '候選人A', '候選人C', '候選人A', '候選人B']
vote_counter = Counter(votes)
print(f"投票統計: {vote_counter}")
print(f"得票最多的候選人: {vote_counter.most_common(1)[0]}")

# 案例2: 分析網站訪問日誌
access_logs = [
    '/home', '/about', '/home', '/contact', '/home',
    '/about', '/services', '/home', '/contact'
]
page_counter = Counter(access_logs)
print(f"頁面訪問統計: {page_counter}")
print(f"最受歡迎的頁面: {page_counter.most_common(3)}")

# 案例3: 分析購物車商品
shopping_cart = [
    '蘋果', '香蕉', '蘋果', '橘子', '香蕉', '蘋果', '葡萄'
]
product_counter = Counter(shopping_cart)
print(f"商品統計: {product_counter}")
print(f"購買最多的商品: {product_counter.most_common(1)[0]}")

# 語法重點總結
print("\n=== 語法重點總結 ===")
"""
1. Counter(iterable) 創建計數器物件
2. most_common(n) 返回最常見的 n 個元素及其計數
3. 支援數學運算：+（合併）、-（差集）、&（交集）、|（聯集）
4. 訪問不存在的鍵返回 0（不像普通字典會拋出 KeyError）
5. 可以轉換為普通字典：dict(counter)
6. 適用於任何可雜湊的元素
7. 時間複雜度：計數 O(n)，most_common O(m log m) 其中 m 是唯一元素數
"""

from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look']
word_counts = Counter(words)
word_counts.most_common(3)

word_counts.update(['eyes', 'eyes'])
