import sys

"""
Problem 10055: Function Composition Monotonicity
Description: 
We have N functions, initially all increasing. 
Composition of two increasing functions is increasing.
Composition of an increasing and a decreasing function is decreasing.
Composition of two decreasing functions is increasing.
Basically, it's like multiplying signs where Increasing is +1 and Decreasing is -1.
Or more simply, XOR logic where Increasing is 0 and Decreasing is 1.

The query asks for the monotonicity of f_L(f_{L+1}(...(f_R(x))...)).
The result is Decreasing (1) if the number of decreasing functions in the range [L, R] is odd,
otherwise it's Increasing (0).
"""

class FenwickTree:
    def __init__(self, n):
        # Initialize the bit array with zeros
        self.tree = [0] * (n + 1)
    
    def update(self, i, delta):
        # Standard point update for Binary Indexed Tree
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)
            
    def query(self, i):
        # Standard prefix sum query for Binary Indexed Tree
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

def solve():
    # Read all tokens from input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # N: number of functions, Q: number of operations
    n = int(input_data[0])
    q = int(input_data[1])
    
    # Keep track of current state of each function: 0 (Increasing) or 1 (Decreasing)
    # Using 1-based indexing for convenience with Fenwick Tree
    current_states = [0] * (n + 1)
    bit = FenwickTree(n)
    
    idx = 2
    output = []
    
    for _ in range(q):
        query_type = int(input_data[idx])
        if query_type == 1:
            # Update function f_i
            i = int(input_data[idx + 1])
            if current_states[i] == 0:
                # Change from Increasing (0) to Decreasing (1)
                bit.update(i, 1)
                current_states[i] = 1
            else:
                # Change from Decreasing (1) to Increasing (0)
                bit.update(i, -1)
                current_states[i] = 0
            idx += 2
        else:
            # Query range [L, R]
            l = int(input_data[idx + 1])
            r = int(input_data[idx + 2])
            
            # Count how many functions are Decreasing in range [L, R]
            # count = prefix_sum(R) - prefix_sum(L-1)
            num_decreasing = bit.query(r) - bit.query(l - 1)
            
            # If the count is odd, the composition is Decreasing (1), else Increasing (0)
            if num_decreasing % 2 == 1:
                output.append("1")
            else:
                output.append("0")
            idx += 3
            
    # Print all results separated by newlines
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()
