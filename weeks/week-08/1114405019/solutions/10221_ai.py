import math
import sys


def main():
    lines = [line.strip() for line in sys.stdin if line.strip() != ""]
    if not lines:
        return

    outputs = []
    for line in lines:
        parts = line.split()
        if len(parts) != 3:
            continue

        s = int(parts[0])
        a = float(parts[1])
        unit = parts[2].lower()

        if unit == 'min':
            a /= 60.0

        # 取最小夾角，當角度超過 180 度時使用 360-a
        if a > 180.0:
            a = 360.0 - a

        r = 6440.0 + s
        theta = math.radians(a)
        arc_length = r * theta
        chord_length = 2.0 * r * math.sin(theta / 2.0)
        outputs.append(f'{arc_length:.6f} {chord_length:.6f}')

    sys.stdout.write('\n'.join(outputs))


if __name__ == '__main__':
    main()
