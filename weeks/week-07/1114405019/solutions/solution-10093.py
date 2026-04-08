import sys


def count_bits(x):
    return bin(x).count("1")


def is_valid_row(mask):
    return (mask & (mask << 1)) == 0 and (mask & (mask << 2)) == 0


def main():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    first = data[0].strip().split()
    if len(first) < 2:
        return
    n = int(first[0])
    m = int(first[1])
    grid = [line.strip() for line in data[1:1 + n]]

    row_masks = []
    for row in grid:
        mask = 0
        for j, ch in enumerate(row):
            if ch == "P":
                mask |= 1 << j
        row_masks.append(mask)

    all_valid = [mask for mask in range(1 << m) if is_valid_row(mask)]
    dp = {(0, 0): 0}

    for r in range(n):
        available = [mask for mask in all_valid if (mask & row_masks[r]) == mask]
        new_dp = {}
        for (prev, prev2), value in dp.items():
            for cur in available:
                if (cur & prev) != 0 or (cur & prev2) != 0:
                    continue
                key = (cur, prev)
                new_dp[key] = max(new_dp.get(key, -1), value + count_bits(cur))
        dp = new_dp

    answer = max(dp.values()) if dp else 0
    sys.stdout.write(str(answer))


if __name__ == "__main__":
    main()
