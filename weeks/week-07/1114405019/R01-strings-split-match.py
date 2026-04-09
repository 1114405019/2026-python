# R01. 字串分割與匹配（2.1–2.3）
# re.split() 多分隔符 / startswith / endswith / fnmatch

# Remember（記憶）
# - re.split() 可處理多種分隔符，用 [] 或 | 組合
# - startswith/endswith 接受 tuple，不接受 list
# - fnmatch 支援 Shell 風格通配符，fnmatchcase 區分大小寫

import re
from fnmatch import fnmatch, fnmatchcase

# ── 2.1 多界定符分割 ──────────────────────────────────
line = "asdf fjdk; afed, fjek,asdf, foo"
result = re.split(r"[;,\s]\s*", line)
print(f"多分隔符分割結果: {result}")  # 預期輸出: ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 非捕獲分組：分組但不保留分隔符
result2 = re.split(r"(?:,|;|\s)\s*", line)
print(f"非捕獲分組分割: {result2}")  # 預期輸出: ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# ── 2.2 開頭/結尾匹配 ────────────────────────────────
filename = "spam.txt"
print(f"{filename} 結尾是 .txt: {filename.endswith('.txt')}")  # True
print(f"{filename} 開頭是 file:: {filename.startswith('file:')}")  # False

# 同時檢查多種後綴 → 傳入 tuple（不能傳 list）
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
suffixes = (".c", ".h")
filtered = [name for name in filenames if name.endswith(suffixes)]
print(f"過濾 .c 和 .h 檔案: {filtered}")  # 預期輸出: ['foo.c', 'spam.c', 'spam.h']

# 錯誤示範：startswith 不能傳 list
try:
    filename.startswith(["file:"])  # 會報錯
except TypeError as e:
    print(f"錯誤: startswith 不接受 list: {e}")

# ── 2.3 Shell 通配符匹配 ─────────────────────────────
print(f"fnmatch('foo.txt', '*.txt'): {fnmatch('foo.txt', '*.txt')}")  # True
print(f"fnmatch('Dat45.csv', 'Dat[0-9]*'): {fnmatch('Dat45.csv', 'Dat[0-9]*')}")  # True

# fnmatchcase 強制區分大小寫
print(f"fnmatchcase('foo.txt', '*.TXT'): {fnmatchcase('foo.txt', '*.TXT')}")  # False

addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]
st_addresses = [a for a in addresses if fnmatchcase(a, "* ST")]
print(f"匹配 * ST 的地址: {st_addresses}")  # 預期輸出: ['5412 N CLARK ST', '1060 W ADDISON ST']
