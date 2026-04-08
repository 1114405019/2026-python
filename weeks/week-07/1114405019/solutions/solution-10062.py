import sys

def build_fenwick(n):
    bit = [0] * (n + 1)
    for i in range(1, n + 1):
        j = i
        while j <= n:
            bit[j] += 1
            j += j & -j
    return bit


def fenwick_find(bit, k):
    idx = 0
    step = 1 << (len(bit).bit_length() - 1)
    while step:
        nxt = idx + step
        if nxt < len(bit) and bit[nxt] < k:
            k -= bit[nxt]
            idx = nxt
        step >>= 1
    return idx + 1


def fenwick_add(bit, idx, val):
    while idx < len(bit):
        bit[idx] += val
        idx += idx & -idx


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    counts = [0] * (n + 1)
    for i in range(2, n + 1):
        try:
            counts[i] = int(next(it))
        except StopIteration:
            counts[i] = 0

    bit = build_fenwick(n)
    result = [0] * (n + 1)
    for i in range(n, 1, -1):
        pos = fenwick_find(bit, counts[i] + 1)
        result[i] = pos
        fenwick_add(bit, pos, -1)

    result[1] = fenwick_find(bit, 1)
    out = "\n".join(str(result[i]) for i in range(1, n + 1))
    sys.stdout.write(out)


if __name__ == "__main__":
    main()
