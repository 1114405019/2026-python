import sys

def solve():
    for line in sys.stdin:
        coords = list(map(float, line.split()))
        if not coords:
            continue

        p = [(coords[i], coords[i+1]) for i in range(0, 8, 2)]

        # Determine the unique points and the duplicated point (common vertex)
        if p[0] == p[2]:
            a, b, c = p[1], p[0], p[3]
        elif p[0] == p[3]:
            a, b, c = p[1], p[0], p[2]
        elif p[1] == p[2]:
            a, b, c = p[0], p[1], p[3]
        else: # p[1] == p[3]
            a, b, c = p[0], p[1], p[2]

        # Parallelogram Fourth Point: D = A + C - B
        res_x = a[0] + c[0] - b[0]
        res_y = a[1] + c[1] - b[1]

        print(f"{res_x:.3f} {res_y:.3f}")

if __name__ == "__main__":
    solve()
