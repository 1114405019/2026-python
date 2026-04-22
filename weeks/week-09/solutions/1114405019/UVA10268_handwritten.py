import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    while idx < len(input_data):
        try:
            x = int(input_data[idx])
            idx += 1
            # Note: The problem doesn't explicitly give the number of coefficients.
            # We need to read until the end of the line. But sys.stdin.read().split()
            # loses line boundaries. We should read line by line.
            pass
        except:
            break

    # Re-implementing with line awareness
    sys.stdin.seek(0)
    lines = sys.stdin.read().splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        try:
            x = int(line)
            coeffs = list(map(int, lines[i+1].split()))
            i += 2
        except (ValueError, IndexError):
            break

        n = len(coeffs) - 1
        res = 0
        for j in range(n):
            res = res * x + coeffs[j] * (n - j)
        print(int(res))

if __name__ == "__main__":
    solve()
