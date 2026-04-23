import sys

def solve():
    # Read all input at once for efficiency
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        r = int(input_data[idx])
        idx += 1
        # Extract relative locations and sort them to find the median
        s = sorted([int(input_data[idx + i]) for i in range(r)])
        idx += r
        
        # The optimal house location is the median
        median = s[r // 2]
        # Calculate sum of absolute differences
        total_dist = sum(abs(x - median) for x in s)
        print(total_dist)

if __name__ == "__main__":
    solve()
