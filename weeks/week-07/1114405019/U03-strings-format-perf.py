# U03. 字串格式化效能與陷阱（2.14–2.20）
# join vs + / format_map 缺失鍵 / bytes 索引差異

# Remember（記憶）
# - 字串串接用 join() 而非 + 以避免 O(n²) 效能問題
# - format_map() 配合 __missing__ 可處理缺失鍵
# - bytes 索引回傳整數，而非字元

import timeit

# ── join 效能優於 + （2.14）──────────────────────────
parts = [f"item{i}" for i in range(1000)]


def bad_concat():
    s = ""
    for p in parts:
        s += p  # 每次建立新字串，O(n²)
    return s


def good_join():
    return "".join(parts)  # 一次分配，O(n)


t1 = timeit.timeit(bad_concat, number=500)
t2 = timeit.timeit(good_join, number=500)
print(f"+串接: {t1:.3f}s  join: {t2:.3f}s")

# ── format_map 處理缺失鍵（2.15）─────────────────────
class SafeSub(dict):
    def __missing__(self, key: str) -> str:
        return "{" + key + "}"  # 缺失時保留佔位符


name = "Guido"
s = "{name} has {n} messages."
result = s.format_map(SafeSub(vars()))
print(f"安全格式化: {result}")  # 預期輸出: Guido has {n} messages.

# ── bytes 索引回傳整數（2.20）────────────────────────
a = "Hello"
b = b"Hello"
print(f"字串索引: {repr(a[0])}")  # 'H'（字元）
print(f"bytes 索引: {b[0]}")  # 72（整數 = ord('H')）

# bytes 不能直接 format，需先格式化再 encode
formatted = "{:10s} {:5d}".format("ACME", 100)
encoded = formatted.encode("ascii")
print(f"格式化後 encode: {encoded}")  # 預期輸出: b'ACME            100'
