"""defaultdict / setdefault

1. 使用 defaultdict 自動建立預設容器
2. list/set 為多值字典常見類型
3. setdefault 也可達到類似效果
"""

from collections import defaultdict

# 使用 defaultdict(list) 讓不存在的鍵自動建立空列表
d = defaultdict(list)
d['a'].append(1); d['a'].append(2)

# 改用 defaultdict(set) 讓相同值只出現一次
d = defaultdict(set)
d['a'].add(1); d['a'].add(2)

# 若不想引入 defaultdict，也可以用 dict.setdefault 建立預設值
d = {}
d.setdefault('a', []).append(1)
