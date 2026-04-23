import sys

def main():
    # A bit more manual parsing
    data = sys.stdin.read().split()
    if not data:
        return
        
    n = int(data[0])
    q = int(data[1])
    
    # functions[i] = 0 if increasing, 1 if decreasing
    functions = [0] * (n + 1)
    
    ptr = 2
    for _ in range(q):
        cmd = int(data[ptr])
        ptr += 1
        if cmd == 1:
            idx = int(data[ptr])
            ptr += 1
            # Flip monotonicity
            if functions[idx] == 0:
                functions[idx] = 1
            else:
                functions[idx] = 0
        else:
            left = int(data[ptr])
            right = int(data[ptr+1])
            ptr += 2
            
            # Use simple loop for range composition
            # (Incr composition is XOR sum of states)
            total_xor = 0
            for i in range(left, right + 1):
                total_xor ^= functions[i]
            print(total_xor)

if __name__ == "__main__":
    main()
