# UVA 10008: What's Cryptanalysis?
# 統計輸入中字母的出現頻率，大小寫視為相同，按頻率降序輸出，相同頻率按字母升序

import sys
from collections import Counter

def cryptanalysis(lines):
    # 合併所有行，轉小寫，只保留字母
    text = ''.join(lines).lower()
    letters = [c for c in text if c.isalpha()]
    # 統計頻率
    freq = Counter(letters)
    # 排序：先頻率降序，再字母升序
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    # 輸出
    result = []
    for char, count in sorted_freq:
        result.append(f"{char.upper()} {count}")
    return result

def main():
    input = sys.stdin.read
    data = input().splitlines()
    n = int(data[0])
    lines = data[1:1+n]
    output = cryptanalysis(lines)
    for line in output:
        print(line)

if __name__ == "__main__":
    main()</content>
<parameter name="filePath">c:\Users\yiteng\Downloads\0318\2026-python\weeks\week-04\solutions\solution_10008.py