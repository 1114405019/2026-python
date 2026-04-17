"""itemgetter

1. 從字典列表中依欄位排序
2. single key 與 multiple key 排序用法
3. itemgetter 比 lambda 更簡潔
"""

from operator import itemgetter

rows = [{'fname': 'Brian', 'uid': 1003}, {'fname': 'John', 'uid': 1001}]

# 按 fname 欄位排序
sorted(rows, key=itemgetter('fname'))

# 按 uid 欄位排序
sorted(rows, key=itemgetter('uid'))

# 依 uid 再依 fname 進行複合排序
sorted(rows, key=itemgetter('uid', 'fname'))
