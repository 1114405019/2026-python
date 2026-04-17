"""字典集合運算

1. 使用 keys/items 集合取得交集與差集
2. set operations 檢查字典鍵/項目關係
3. 用集合運算篩選字典鍵
"""

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

# keys() 與 items() 可以直接進行集合運算
a.keys() & b.keys()
a.keys() - b.keys()
a.items() & b.items()

# 利用集合差集建立新字典，排除不需要的鍵
c = {k: a[k] for k in a.keys() - {'z', 'w'}}
