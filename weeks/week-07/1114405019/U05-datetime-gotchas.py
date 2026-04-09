# U05. 日期時間的陷阱（3.12–3.15）
# timedelta 不支援月份 / strptime 效能問題

# Remember（記憶）
# - timedelta 不支援月份，需手動處理月份加減
# - strptime 效能差，手動解析更快但需小心格式驗證
# - 月份加減時注意日期 clamp 到目標月最後一天

import timeit
import calendar
from datetime import datetime, timedelta

# ── timedelta 不支援月份（3.12）──────────────────────
dt = datetime(2012, 9, 23)
try:
    dt + timedelta(months=1)  # 會報錯
except TypeError as e:
    print(f"錯誤: {e}")

# 正確做法：用 calendar 取得目標月份天數，並將日期 clamp 到該月最後一天
def add_one_month(dt: datetime) -> datetime:
    # 計算目標的年與月
    year = dt.year
    month = dt.month + 1
    if month == 13:
        year += 1
        month = 1

    # 取得目標月份的天數，並把日期限制在該月最後一天
    _, days_in_target_month = calendar.monthrange(year, month)
    day = min(dt.day, days_in_target_month)

    return dt.replace(year=year, month=month, day=day)


result1 = add_one_month(datetime(2012, 1, 31))
print(f"加一月 (1/31): {result1}")  # 預期輸出: 2012-02-29
result2 = add_one_month(datetime(2012, 9, 23))
print(f"加一月 (9/23): {result2}")  # 預期輸出: 2012-10-23

# ── strptime 效能問題（3.15）─────────────────────────
dates = [f"2012-{m:02d}-{d:02d}" for m in range(1, 13) for d in range(1, 29)]


def use_strptime(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d")


def use_manual(s: str) -> datetime:
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


assert use_strptime("2012-09-20") == use_manual("2012-09-20")

t1 = timeit.timeit(lambda: [use_strptime(d) for d in dates], number=100)
t2 = timeit.timeit(lambda: [use_manual(d) for d in dates], number=100)
print(f"strptime: {t1:.3f}s  手動解析: {t2:.3f}s（快 {t1 / t2:.1f} 倍）")
