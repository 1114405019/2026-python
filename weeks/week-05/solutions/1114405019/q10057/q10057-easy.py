import sys

# Simple version with minimal functions
input_data = sys.stdin.read().split()

pos = 0
while pos < len(input_data):
    # Read n
    n_str = input_data[pos]
    pos = pos + 1
    n = int(n_str)
    
    # Read n numbers
    numbers = []
    for i in range(n):
        numbers.append(int(input_data[pos]))
        pos = pos + 1
    
    # Sort
    numbers.sort()
    
    if n % 2 != 0:
        # Odd
        mid = n // 2
        a = numbers[mid]
        
        count = 0
        for x in numbers:
            if x == a:
                count = count + 1
        
        print(a, count, 1)
    else:
        # Even
        mid1 = n // 2 - 1
        mid2 = n // 2
        
        a = numbers[mid1]
        b = numbers[mid2]
        
        count = 0
        for x in numbers:
            if x >= a and x <= b:
                count = count + 1
        
        diff = b - a + 1
        print(a, count, diff)
