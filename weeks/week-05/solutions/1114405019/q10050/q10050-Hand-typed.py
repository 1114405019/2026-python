# Hartals - Hand-typed version
import sys

def main():
    # Read the number of test cases
    line = sys.stdin.readline()
    if not line:
        return
    t = int(line.strip())
    
    for _ in range(t):
        # Read N and P
        n = int(sys.stdin.readline().strip())
        p = int(sys.stdin.readline().strip())
        
        hartals = []
        for _ in range(p):
            hartals.append(int(sys.stdin.readline().strip()))
            
        lost = 0
        # Check every day from Sunday (1) to N
        for day in range(1, n + 1):
            # Friday is day 6, Saturday is day 7, 14, 21...
            if day % 7 == 6 or day % 7 == 0:
                continue
            
            # See if any party has a strike
            found = False
            for h in hartals:
                if day % h == 0:
                    found = True
                    break
            
            if found:
                lost += 1
                
        print(lost)

if __name__ == '__main__':
    main()
