# UVA 10038 手打練習 - Jolly Jumpers
# 筆記：檢查每對相鄰數字差的絕對值，是不是 1 到 n-1 且每個只出現一次
# 用 set 記錄看過的差

import sys

for line in sys.stdin:
    nums = list(map(int, line.split()))
    n = nums[0]  # 第一個是 n
    seq = nums[1:]  # 後面是序列
    seen = set()  # 記錄差值
    jolly = True
    for i in range(1, n):
        d = abs(seq[i] - seq[i-1])  # 相鄰差絕對值
        if d < 1 or d >= n or d in seen:  # 不符合條件
            jolly = False
            break
        seen.add(d)  # 加進 set
    # 輸出
    print("Jolly" if jolly else "Not jolly")</content>
<parameter name="filePath">c:\Users\yiteng\Downloads\0318\2026-python\weeks\week-04\solutions\hand10038.py