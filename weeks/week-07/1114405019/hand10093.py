#!/usr/bin/env python3

import sys

for line in sys.stdin:
    num = line.strip()
    if num == "1" or (len(num) > 1 and num[0] == '0'):
        print("such number is impossible!")
        continue
    max_d = 0
    for c in num:
        if c.isdigit():
            v = int(c)
        elif c.isupper():
            v = ord(c) - ord('A') + 10
        elif c.islower():
            v = ord(c) - ord('a') + 36
        else:
            print("such number is impossible!")
            break
        max_d = max(max_d, v)
    else:
        print(max(max_d + 1, 2))