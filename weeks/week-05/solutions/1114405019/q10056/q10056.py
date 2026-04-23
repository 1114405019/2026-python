import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    s = int(input_data[idx])
    idx += 1
    
    for _ in range(s):
        n = int(input_data[idx])
        p = float(input_data[idx + 1])
        i = int(input_data[idx + 2])
        idx += 3
        
        if p == 0:
            print("0.0000")
            continue
            
        # Formula for geometric series: P = (p * (1-p)^(i-1)) / (1 - (1-p)^N)
        q = 1 - p
        ans = (p * (q ** (i - 1))) / (1 - (q ** n))
        print(f"{ans:.4f}")

if __name__ == "__main__":
    solve()
