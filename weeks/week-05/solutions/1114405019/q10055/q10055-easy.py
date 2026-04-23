import sys

# Easy version using a simple loop for each query
# Note: This might be slow for large N and Q
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    q = int(input_data[1])
    
    # 0 = increasing, 1 = decreasing
    funcs = [0] * (n + 1)
    
    idx = 2
    for _ in range(q):
        query_type = int(input_data[idx])
        if query_type == 1:
            i = int(input_data[idx + 1])
            if funcs[i] == 0:
                funcs[i] = 1
            else:
                funcs[i] = 0
            idx += 2
        else:
            l = int(input_data[idx + 1])
            r = int(input_data[idx + 2])
            
            # Count decreasing functions in range [L, R] using a loop
            decreasing_count = 0
            for k in range(l, r + 1):
                if funcs[k] == 1:
                    decreasing_count += 1
            
            # If the number of decreasing functions is odd, the whole thing is decreasing
            if decreasing_count % 2 == 1:
                print(1)
            else:
                print(0)
            idx += 3

if __name__ == "__main__":
    solve()
