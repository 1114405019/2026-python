# U02. 正則表達式進階技巧（2.4–2.6）
# 預編譯效能 / sub 回呼函數 / 大小寫一致替換

# Remember（記憶）
# - 預編譯 regex 可提升重複使用效能
# - sub() 可接受回呼函數進行複雜替換
# - 大小寫一致替換需檢查匹配字串的大小寫狀態

import re
import timeit
from calendar import month_abbr

# ── 預編譯效能（2.4）──────────────────────────────────
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")


def using_module():
    return re.findall(r"(\d+)/(\d+)/(\d+)", text)


def using_compiled():
    return datepat.findall(text)


t1 = timeit.timeit(using_module, number=50_000)
t2 = timeit.timeit(using_compiled, number=50_000)
print(f"直接呼叫: {t1:.3f}s  預編譯: {t2:.3f}s")

# ── sub 回呼函數（2.5）────────────────────────────────
def change_date(m: re.Match) -> str:
    mon_name = month_abbr[int(m.group(1))]
    return f"{m.group(2)} {mon_name} {m.group(3)}"


result = datepat.sub(change_date, text)
print(f"日期替換結果: {result}")  # 預期輸出: Today is 27 Nov 2012. PyCon starts 13 Mar 2013.

# ── 保持大小寫一致的替換（2.6）───────────────────────
def matchcase(word: str):
    def replace(m: re.Match) -> str:
        t = m.group()
        if t.isupper():
            return word.upper()
        elif t.islower():
            return word.lower()
        elif t[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


s = "UPPER PYTHON, lower python, Mixed Python"
result2 = re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE)
print(f"大小寫一致替換: {result2}")  # 預期輸出: UPPER SNAKE, lower snake, Mixed Snake
