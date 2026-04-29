import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    idx = 0
    T_str = input_data[idx]
    idx += 1
    T = int(T_str)
    MOD = 1000000007

    for t in range(1, T + 1):
        N = int(input_data[idx]); M = int(input_data[idx+1]); idx += 2
        grid = []
        for _ in range(N):
            grid.append([int(x) for x in input_data[idx:idx+M]])
            idx += M
        
        dp = {0: 1}
        for i in range(N):
            for j in range(M):
                new_dp = {}
                for mask, count in dp.items():
                    up = (mask >> j) & 1
                    left = (mask >> (j + 1)) & 1
                    
                    if grid[i][j] == 0:
                        if not up and not left:
                            new_dp[mask] = (new_dp.get(mask, 0) + count) % MOD
                    else:
                        # Plug DP transitions
                        if up and left:
                            m = mask ^ (1 << j) ^ (1 << (j + 1))
                            new_dp[m] = (new_dp.get(m, 0) + count) % MOD
                        elif up or left:
                            new_dp[mask] = (new_dp.get(mask, 0) + count) % MOD
                            m = mask ^ (1 << j) ^ (1 << (j + 1))
                            new_dp[m] = (new_dp.get(m, 0) + count) % MOD
                        else:
                            m = mask ^ (1 << j) ^ (1 << (j + 1))
                            new_dp[m] = (new_dp.get(m, 0) + count) % MOD
                dp = new_dp
            
            # Row shift
            new_dp = {}
            for mask, count in dp.items():
                if not (mask & (1 << M)):
                    new_dp[mask << 1] = count
            dp = new_dp
            
        print(f"Case {t}: {dp.get(0, 0)}")

if __name__ == "__main__":
    solve()
