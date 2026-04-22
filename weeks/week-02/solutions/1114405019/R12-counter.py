"""Counter 統計

1. 以 Counter 計算序列中元素出現次數
2. most_common 取得最高頻率元素
3. update 可累加新的計數
"""

from collections import Counter

# Counter 會自動統計 list 中每個元素的出現次數
words = ['look', 'into', 'my', 'eyes', 'look']
word_counts = Counter(words)

# most_common 取得最常出現的前三個元素
word_counts.most_common(3)

# update 可用於後續新增元素的累計統計
word_counts.update(['eyes', 'eyes'])
