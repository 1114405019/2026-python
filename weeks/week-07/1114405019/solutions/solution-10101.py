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

    equal_pos = expr.find("=")
    if equal_pos == -1:
        sys.stdout.write("No")
        return

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
