import math
import sys


def main():
    data = sys.stdin.read().split()
    if not data:
        return

    outputs = []
    pair_index = 1
    for i in range(0, len(data), 2):
        if i + 1 >= len(data):
            break

        a_bin, b_bin = data[i], data[i + 1]
        a = int(a_bin, 2)
        b = int(b_bin, 2)
        gcd_value = math.gcd(a, b)
        outputs.append(f'Pair #{pair_index}: {gcd_value:b}')
        pair_index += 1

    sys.stdout.write('\n'.join(outputs))


if __name__ == '__main__':
    main()
