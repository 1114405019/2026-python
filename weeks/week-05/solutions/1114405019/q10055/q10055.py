import sys

# Since N and Q are up to 200,000, we use a Fenwick Tree (Binary Indexed Tree)
# for fast point updates and range sums.

class FenwickTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)
    
    def update(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)
            
    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    q = int(input_data[1])
    
    # 0 for increasing, 1 for decreasing.
    # Initially all are 0.
    funcs = [0] * (n + 1)
    bit = FenwickTree(n)
    
    idx = 2
    results = []
    for _ in range(q):
        type = int(input_data[idx])
        if type == 1:
            i = int(input_data[idx + 1])
            # Toggle: if 0 -> 1, delta = 1. If 1 -> 0, delta = -1.
            if funcs[i] == 0:
                bit.update(i, 1)
                funcs[i] = 1
            else:
                bit.update(i, -1)
                funcs[i] = 0
            idx += 2
        else:
            l = int(input_data[idx + 1])
            r = int(input_data[idx + 2])
            # The result depends on the parity of the number of decreasing functions
            total_dec = bit.query(r) - bit.query(l - 1)
            results.append(str(total_dec % 2))
            idx += 3
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
