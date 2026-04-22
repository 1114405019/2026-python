# UVA 10035: Primary Arithmetic
# 計算兩個數字相加時產生的進位次數

import sys

def carry_operations(a, b):
    carry = 0
    count = 0
    while a > 0 or b > 0:
        digit_a = a % 10
        digit_b = b % 10
        if digit_a + digit_b + carry >= 10:
            count += 1
            carry = 1
        else:
            carry = 0
        a //= 10
        b //= 10
    return count

def main():
    for line in sys.stdin:
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break
        carries = carry_operations(a, b)
        if carries == 0:
            print("No carry operation.")
        elif carries == 1:
            print("1 carry operation.")
        else:
            print(f"{carries} carry operations.")

if __name__ == "__main__":
    main()</content>
<parameter name="filePath">c:\Users\yiteng\Downloads\0318\2026-python\weeks\week-04\solutions\solution_10035.py