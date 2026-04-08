import sys


def find_group_size(start, day):
    offset = (start - 1) * start // 2
    target = day + offset
    lo = start
    hi = max(start, int((2 * target) ** 0.5) + 3)
    while lo < hi:
        mid = (lo + hi) // 2
        if mid * (mid + 1) // 2 >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo


def main():
    lines = sys.stdin.read().strip().split()
    if not lines:
        return
    out_lines = []
    for i in range(0, len(lines), 2):
        try:
            s = int(lines[i])
            d = int(lines[i + 1])
        except (IndexError, ValueError):
            break
        out_lines.append(str(find_group_size(s, d)))
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
