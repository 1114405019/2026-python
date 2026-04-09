# U04. 數字精度的陷阱與選擇（3.1–3.7）
# 銀行家捨入 / NaN 比較陷阱 / float vs Decimal 選擇

# Remember（記憶）
# - round() 使用銀行家捨入（五取偶），非傳統四捨五入
# - NaN 永遠不等於自己，用 math.isnan() 檢測
# - float 有精確度問題，金融計算用 Decimal

import math
import timeit
from decimal import Decimal, ROUND_HALF_UP

# ── 銀行家捨入（3.1）─────────────────────────────────
# Python round() 用「四捨六入五取偶」，不是日常四捨五入
print(f"round(0.5): {round(0.5)}")  # 0（不是 1！）
print(f"round(2.5): {round(2.5)}")  # 2（不是 3！）
print(f"round(3.5): {round(3.5)}")  # 4

# 若需傳統四捨五入，用 Decimal + ROUND_HALF_UP
def trad_round(x: float, n: int = 0) -> Decimal:
    d = Decimal(str(x))
    fmt = Decimal("1") if n == 0 else Decimal("0." + "0" * n)
    return d.quantize(fmt, rounding=ROUND_HALF_UP)


print(f"trad_round(0.5): {trad_round(0.5)}")  # 1
print(f"trad_round(2.5): {trad_round(2.5)}")  # 3

# ── NaN 無法用 == 比較（3.7）─────────────────────────
c = float("nan")
print(f"c == c: {c == c}")  # False（自己不等於自己！）
print(f"c == float('nan'): {c == float('nan')}")  # False
print(f"math.isnan(c): {math.isnan(c)}")  # True（唯一正確的檢測方式）

data = [1.0, float("nan"), 3.0, float("nan"), 5.0]
clean = [x for x in data if not math.isnan(x)]
print(f"清理 NaN: {clean}")  # [1.0, 3.0, 5.0]

# ── float vs Decimal 選擇（3.2）──────────────────────
# float：快但有誤差（科學/工程適用）
print(f"0.1 + 0.2: {0.1 + 0.2}")  # 0.30000000000000004
print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")  # False

# Decimal：精確但慢（金融/會計適用）
print(f"Decimal('0.1') + Decimal('0.2'): {Decimal('0.1') + Decimal('0.2')}")  # 0.3
print(f"Decimal 等式: {Decimal('0.1') + Decimal('0.2') == Decimal('0.3')}")  # True

t1 = timeit.timeit(lambda: 0.1 * 999, number=100_000)
t2 = timeit.timeit(lambda: Decimal("0.1") * 999, number=100_000)
print(f"float: {t1:.3f}s  Decimal: {t2:.3f}s（Decimal 約慢 {t2 / t1:.0f} 倍）")
