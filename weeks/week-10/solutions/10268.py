import sys

def solve():
    # Precompute dp table
    # dp[k][t] = max floors with k eggs and t trials
    dp = [[0] * 64 for _ in range(101)]
    for j in range(1, 64):
        for i in range(1, 101):
            dp[i][j] = dp[i - 1][j - 1] + 1 + dp[i][j - 1]
    
    input_data = sys.stdin.read().split()
    if not input_data: return
    it = iter(input_data)
    
    while True:
        try:
            k = int(next(it))
            n = int(next(it))
        except StopIteration:
            break
        
        if k == 0: break
        
        ans = -1
        lookup_k = min(k, 100)
        for j in range(1, 64):
            if dp[lookup_k][j] >= n:
                ans = j
                break
        
        if ans == -1:
            print("More than 63 trials needed.")
        else:
            print(ans)

if __name__ == "__main__":
    solve()
