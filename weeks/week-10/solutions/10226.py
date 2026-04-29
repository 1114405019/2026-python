import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        bad = [[False] * (n + 1) for _ in range(n)]
        for i in range(n):
            while True:
                pos = int(input_data[idx])
                idx += 1
                if pos == 0: break
                bad[i][pos] = True
        
        p = [0] * n
        used = [False] * n
        last = [-1] * n
        first_perm = [True]

        def dfs(d):
            if d == n:
                res = []
                match_idx = 0
                if not first_perm[0]:
                    while match_idx < n and p[match_idx] == last[match_idx]:
                        match_idx += 1
                
                res.append(' ' * match_idx)
                for j in range(match_idx, n):
                    res.append(chr(p[j] + ord('A')))
                    last[j] = p[j]
                sys.stdout.write("".join(res) + "\n")
                first_perm[0] = False
                return

            for i in range(n):
                if not used[i] and not bad[i][d + 1]:
                    used[i] = True
                    p[d] = i
                    dfs(d + 1)
                    used[i] = False

        dfs(0)

if __name__ == "__main__":
    solve()
