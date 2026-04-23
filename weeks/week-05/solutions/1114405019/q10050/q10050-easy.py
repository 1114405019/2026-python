import sys

# Simple version using a set or list to mark days
input_data = sys.stdin.read().split()
if input_data:
    t = int(input_data[0])
    idx = 1
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        p = int(input_data[idx])
        idx += 1
        
        # Mark all days from 1 to n
        days = [0] * (n + 1)
        
        for _ in range(p):
            h = int(input_data[idx])
            idx += 1
            # Mark every h-th day
            for strike_day in range(h, n + 1, h):
                days[strike_day] = 1
        
        count = 0
        for d in range(1, n + 1):
            # Check if it's a strike day and not a weekend
            # 6 is Friday, 7 is Saturday, 13 is Friday, 14 is Saturday...
            if days[d] == 1:
                if d % 7 != 6 and d % 7 != 0:
                    count = count + 1
        print(count)
