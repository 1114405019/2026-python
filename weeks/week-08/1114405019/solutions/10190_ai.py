import sys


def main():
    """讀取每一組測試資料，根據除法規則輸出結果。"""
    lines = [line.strip() for line in sys.stdin if line.strip() != ""]
    if not lines:
        return

    outputs = []
    for line in lines:
        parts = line.split()
        if len(parts) != 2:
            continue

        m, n = map(int, parts)
        # 如果除數小於 2，或 m 無法被 n 整除，立即輸出 Boring!
        if n < 2 or m % n != 0:
            outputs.append('Boring!')
            continue

        sequence = [str(m)]
        # 不斷整除 n，直到餘數不為 0
        while m % n == 0:
            m //= n
            sequence.append(str(m))

        outputs.append(' '.join(sequence))

    sys.stdout.write('\n'.join(outputs))


if __name__ == '__main__':
    main()
