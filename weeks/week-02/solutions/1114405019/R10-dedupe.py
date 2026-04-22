"""去重且保序

1. 以 set 檢查出現過的項目
2. yield 逐一產生未重複項目
3. key 參數可依自訂條件去重
"""

# 依序遍歷項目，第一次出現時產生並記錄到 seen
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

# 支援 key 參數，依自訂條件進行去重比較
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
