# 題目 10101

**題名**: UVA 10101

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a094)
- [Yui Huang 題解](https://yuihuang.com/zj-a094/)

## 題目敘述

這是一個很古老的遊戲：用**木棒**在桌上拼出一個**不成立的等式**，移動且只移動**一根木棒**使得等式成立。

現在輪到你了：從輸入讀入一個式子，如果移動一根木棒可以使等式成立，則輸出新的等式，否則輸出 `No`。

**說明與限制：**

1. 式子中只會出現**加號和減號**（包括負號），且有且僅有一個等號。不會出現括號、乘號或除號，也不會有 `++`、`--`、`+-` 或 `-+` 出現。
2. 式子中不會出現 **8 個或 8 個以上的連續數字**。
3. 你只能移動用來構成**數字的木棒**，不能移動構成運算符（`+`、`-`、`=`）的木棒，所以加號、減號、等號不會改變。移動前後，木棒構成的數字必須嚴格符合標準七段顯示器的 0~9。
4. 修改**前**的等式中的數不會以 `0` 開頭，但允許修改**後**的等式中的數以數字 `0` 開頭。

## 輸入說明

從輸入讀入一行字串，該字串包括一個以 **`#`** 字元結尾的式子（ASCII 碼 35）。

- 式子中沒有空格或其他分隔符
- 輸入資料嚴格符合邏輯
- 字串長度 ≤ 1000
- 注意：`#` 字元後面可能有一些與題目無關的字元

## 輸出說明

輸出僅一行：

- 若**有解**，輸出正確的等式，格式與輸入格式相同（以 `#` 結尾，中間不能有分隔符，也不要加入多餘字元）。
- 若**無解**，輸出 `No`（N 大寫，o 小寫）。

---

## 解題思路

本題可用七段顯示器的數字段碼建模。每個數字 0~9 對應一組段碼，移動一根木棒等效於將一個數字的某一段熄滅，並在另一個數字上點亮同一段。

對於輸入式子，先提取所有數字位置。枚舉從哪個數字取出一段和將該段放到哪個數字，嘗試更新兩個數字的段碼。如果更新後兩個數字依然對應 0~9，且變更後的整個等式成立，就輸出該結果；否則輸出 `No`。

## 解題代碼

```python
import sys

SEGMENTS = {
    0: 0x3F,
    1: 0x06,
    2: 0x5B,
    3: 0x4F,
    4: 0x66,
    5: 0x6D,
    6: 0x7D,
    7: 0x07,
    8: 0x7F,
    9: 0x6F,
}
SEG_TO_DIGIT = {v: k for k, v in SEGMENTS.items()}


def eval_expr(expr):
    total = 0
    num = 0
    sign = 1
    i = 0
    while i < len(expr):
        ch = expr[i]
        if ch == "+":
            total += sign * num
            num = 0
            sign = 1
            i += 1
        elif ch == "-":
            total += sign * num
            num = 0
            sign = -1
            i += 1
        else:
            start = i
            while i < len(expr) and expr[i].isdigit():
                i += 1
            num = int(expr[start:i])
    total += sign * num
    return total


def main():
    raw = sys.stdin.read()
    if not raw:
        return
    idx = raw.find("#")
    expr = raw[:idx] if idx != -1 else raw.strip()
    expr = expr.strip()
    if not expr:
        sys.stdout.write("No")
        return

    chars = list(expr)
    digit_positions = [i for i, ch in enumerate(chars) if ch.isdigit()]
    original_digits = [int(chars[i]) for i in digit_positions]

    for src_idx in range(len(digit_positions)):
        for tgt_idx in range(len(digit_positions)):
            if src_idx == tgt_idx:
                continue
            src_pos = digit_positions[src_idx]
            tgt_pos = digit_positions[tgt_idx]
            src_digit = original_digits[src_idx]
            tgt_digit = original_digits[tgt_idx]
            src_seg = SEGMENTS[src_digit]
            tgt_seg = SEGMENTS[tgt_digit]
            movable = src_seg & ~tgt_seg
            while movable:
                bit = movable & -movable
                movable -= bit
                new_src = src_seg & ~bit
                new_tgt = tgt_seg | bit
                if new_src not in SEG_TO_DIGIT or new_tgt not in SEG_TO_DIGIT:
                    continue
                new_expr = chars.copy()
                new_expr[src_pos] = str(SEG_TO_DIGIT[new_src])
                new_expr[tgt_pos] = str(SEG_TO_DIGIT[new_tgt])
                new_expr = "".join(new_expr)
                lhs, rhs = new_expr.split("=", 1)
                if eval_expr(lhs) == eval_expr(rhs):
                    sys.stdout.write(new_expr + "#")
                    return

    sys.stdout.write("No")


if __name__ == "__main__":
    main()
```

## 測試用例

```
輸入:
1+1=1#

輸出:
No
```
