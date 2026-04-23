import sys

# Read everything
input_data = sys.stdin.read().split()
if len(input_data) > 0:
    t_str = input_data[0]
    t = int(t_str)
    
    pos = 1
    for i in range(t):
        r = int(input_data[pos])
        pos = pos + 1
        
        houses = []
        for j in range(r):
            houses.append(int(input_data[pos]))
            pos = pos + 1
            
        # Basic sorting
        houses.sort()
        
        # Finding the middle house
        mid = r // 2
        vito_house = houses[mid]
        
        # Calculate total distance
        ans = 0
        for h in houses:
            d = h - vito_house
            if d < 0:
                d = -d
            ans = ans + d
            
        print(ans)
