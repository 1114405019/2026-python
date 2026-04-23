# A Mid-summer Night's Dream - Hand-typed version
import sys

def main():
    # Read everything and split by whitespace
    data = sys.stdin.read().split()
    if not data:
        return
        
    idx = 0
    while idx < len(data):
        try:
            n = int(data[idx])
            idx += 1
            
            x = []
            for _ in range(n):
                x.append(int(data[idx]))
                idx += 1
                
            x.sort()
            
            # Median logic
            if n % 2 == 1:
                # Odd number of items
                m1 = x[n // 2]
                ans1 = m1
                ans2 = 0
                for val in x:
                    if val == m1:
                        ans2 += 1
                ans3 = 1
            else:
                # Even number of items
                m1 = x[n // 2 - 1]
                m2 = x[n // 2]
                ans1 = m1
                ans2 = 0
                for val in x:
                    if val >= m1 and val <= m2:
                        ans2 += 1
                ans3 = m2 - m1 + 1
                
            print(f"{ans1} {ans2} {ans3}")
            
        except:
            break

if __name__ == "__main__":
    main()
