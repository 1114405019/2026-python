# UVA 10038: Jolly Jumpers
# 檢查序列是否為 Jolly Jumper：相鄰差絕對值為 1 到 n-1 且唯一

import sys

def is_jolly_jumper(nums):
    n = len(nums)
    if n == 1:
        return True
    seen = set()
    for i in range(1, n):
        diff = abs(nums[i] - nums[i-1])
        if diff < 1 or diff >= n or diff in seen:
            return False
        seen.add(diff)
    return len(seen) == n - 1

def main():
    for line in sys.stdin:
        nums = list(map(int, line.split()))
        n = nums[0]
        sequence = nums[1:]
        if is_jolly_jumper(sequence):
            print("Jolly")
        else:
            print("Not jolly")

if __name__ == "__main__":
    main()</content>
<parameter name="filePath">c:\Users\yiteng\Downloads\0318\2026-python\weeks\week-04\solutions\solution_10038.py