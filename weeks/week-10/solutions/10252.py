import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    it = iter(input_data)
    
    try:
        t_str = next(it)
        t = int(t_str)
    except StopIteration: return

    for _ in range(t):
        n = int(next(it))
        x = []
        y = []
        for _ in range(n):
            x.append(int(next(it)))
            y.append(int(next(it)))
        
        x.sort()
        y.sort()
        
        mid_x1 = x[(n - 1) // 2]
        mid_x2 = x[n // 2]
        mid_y1 = y[(n - 1) // 2]
        mid_y2 = y[n // 2]
        
        sum_dist = 0
        for i in range(n):
            sum_dist += abs(x[i] - mid_x1) + abs(y[i] - mid_y1)
        
        count = (mid_x2 - mid_x1 + 1) * (mid_y2 - mid_y1 + 1)
        print(f"{sum_dist} {count}")

if __name__ == "__main__":
    solve()
