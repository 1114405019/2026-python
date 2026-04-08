import sys
from collections import Counter


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    arr = [int(x) for x in data[1:1 + n]]
    sum3 = Counter()
    sum2 = Counter()

    for a in arr:
        for b in arr:
            for c in arr:
                sum3[a + b + c] += 1

    for d in arr:
        for e in arr:
            sum2[d + e] += 1

    total = 0
    for f in arr:
        for s2, count2 in sum2.items():
            total += count2 * sum3[f - s2]

    sys.stdout.write(str(total))


if __name__ == "__main__":
    main()
