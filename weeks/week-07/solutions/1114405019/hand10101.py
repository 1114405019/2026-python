#!/usr/bin/env python3

import sys

for line in sys.stdin:
    n = int(line.strip())
    s = str(n)
    if len(s) <= 3:
        print(s)
        continue
    result = []
    i = len(s)
    gl = 3 if i >= 3 else i
    result.append(s[i - gl:i])
    i -= gl
    while i > 0:
        gl = 2 if i >= 2 else i
        result.append(s[i - gl:i])
        i -= gl
    result.reverse()
    print(','.join(result))