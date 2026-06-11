def count_carries(a: int, b: int) -> int:
    if a < 0 or b < 0:
        raise ValueError("operands must be non-negative")
    carries = 0
    carry = 0
    while a > 0 or b > 0:
        digit_sum = (a % 10) + (b % 10) + carry
        carry = digit_sum // 10
        if carry:
            carries += 1
        a //= 10
        b //= 10
    return carries
