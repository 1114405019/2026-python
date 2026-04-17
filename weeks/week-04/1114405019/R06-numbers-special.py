# R06-numbers-special.py. Numbers Special (2.20)

x = float('inf')
y = 5
print(x > y) # True, infinity check

x = float('-inf')
y = -10
print(x < y) # True, negative infinity

x = float('nan')
print(x != x) # True, nan not equal to itself

x = 1.5
y = 2.0
print(x / y) # 0.75, float division

x = 7
y = 3
print(x / y) # 2.3333333333333335, float division
