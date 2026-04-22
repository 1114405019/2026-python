"""星號解包

1. 可處理不定長序列
2. '*' 保留中間或尾部多餘元素
3. 適用於 tuple/list 和可迭代物件
"""

# 將第一筆與最後一筆固定取出，中間其餘元素打包成 list
def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)

# 解包 tuple 時，前兩個欄位固定，剩餘電話號碼放入 list
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

# 星號解包也可以放在左側前面，保留剩餘元素
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
