# Vito's Family - Hand-typed version
import sys

def main():
    lines = sys.stdin.readlines()
    if not lines:
        return
        
    line_idx = 0
    t = int(lines[line_idx].strip())
    line_idx += 1
    
    for _ in range(t):
        # The data might be spread across lines or on one line
        data = []
        while len(data) == 0:
            data = lines[line_idx].split()
            line_idx += 1
            
        r = int(data[0])
        s = []
        # Check if all relative addresses are on the same line
        if len(data) > 1:
            for i in range(1, len(data)):
                s.append(int(data[i]))
        
        # If not enough addresses on first line, read more lines
        while len(s) < r:
            more_data = lines[line_idx].split()
            for val in more_data:
                s.append(int(val))
            line_idx += 1
            
        # Sorting is the key to find the median
        s.sort()
        
        # Pick the median
        home = s[r // 2]
        
        # Calculate total distance
        distance = 0
        for addr in s:
            d = addr - home
            if d < 0:
                distance -= d
            else:
                distance += d
        
        print(distance)

if __name__ == '__main__':
    main()
