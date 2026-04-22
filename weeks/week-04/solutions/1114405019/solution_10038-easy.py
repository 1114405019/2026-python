# UVA 10038: Jolly Jumpers - 簡易版
# 檢查相鄰差絕對值 1 到 n-1 且不重複

import sys

for line in sys.stdin:
    nums = list(map(int, line.split()))
    n = nums[0]
    seq = nums[1:]
    seen = set()
    jolly = True
    for i in range(1, n):
        d = abs(seq[i] - seq[i-1])
        if d < 1 or d >= n or d in seen:
            jolly = False
            break
        seen.add(d)
    print("Jolly" if jolly else "Not jolly")</content>
<parameter name="filePath">c:\Users\yiteng\Downloads\0318\2026-python\weeks\week-04\solutions\solution_10038-easy.py