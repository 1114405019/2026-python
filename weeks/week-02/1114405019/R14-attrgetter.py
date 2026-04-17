"""attrgetter

1. 依物件屬性排序
2. attrgetter 比 lambda 更簡潔
3. 適用於自定義類別列表排序
"""

from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id

# 建立 User 物件列表
users = [User(23), User(3), User(99)]

# 依 user_id 屬性排序物件列表
sorted(users, key=attrgetter('user_id'))
