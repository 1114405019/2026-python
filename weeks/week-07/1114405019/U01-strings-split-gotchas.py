# U01. 字串分割與匹配的陷阱（2.1–2.11）
# 捕獲分組保留分隔符 / startswith 必須傳 tuple / strip 只處理頭尾

# Remember（記憶）
# - 捕獲分組會保留分隔符在結果中
# - startswith/endswith 只接受 str 或 tuple，不接受 list
# - strip() 只移除頭尾空白，中間空白需用 regex 或 replace

import re

# ── 捕獲分組保留分隔符（2.1）─────────────────────────
line = "asdf fjdk; afed, fjek,asdf, foo"
fields = re.split(r"(;|,|\s)\s*", line)
values = fields[::2]  # 偶數索引 = 實際值
delimiters = fields[1::2] + [""]
rebuilt = "".join(v + d for v, d in zip(values, delimiters))
print(f"重建字串: {rebuilt}")  # 預期輸出: asdf fjdk;afed,fjek,asdf,foo

# ── startswith 必須傳 tuple（2.2）────────────────────
url = "http://www.python.org"
choices = ["http:", "ftp:"]
try:
    url.startswith(choices)  # 會報錯
except TypeError as e:
    print(f"錯誤: startswith 不接受 list: {e}")

print(f"url 以 tuple 開頭檢查: {url.startswith(tuple(choices))}")  # True

# ── strip 只處理頭尾，不處理中間（2.11）──────────────
s = "  hello     world  "
print(f"strip() 結果: {repr(s.strip())}")  # 'hello     world'（中間空白保留）
print(f"replace() 過頭: {repr(s.replace(' ', ''))}")  # 'helloworld'（詞間空白也消）
cleaned = re.sub(r'\s+', ' ', s.strip())
print(f"正確清理: {repr(cleaned)}")  # 'hello world'

# 生成器逐行清理（高效，不預載入記憶體）
lines = ["  apple  \n", "  banana  \n"]
for line in (l.strip() for l in lines):
    print(f"清理後: {repr(line)}")  # 預期輸出: 'apple', 'banana'
