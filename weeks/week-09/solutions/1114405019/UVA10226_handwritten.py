import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    try:
        num_cases = int(input_data[0])
    except (ValueError, IndexError):
        return

    idx = 2
    first = True
    for _ in range(num_cases):
        if not first:
            print()
        first = False

        counts = {}
        total = 0
        while idx < len(input_data) and input_data[idx].strip():
            species = input_data[idx].strip()
            counts[species] = counts.get(species, 0) + 1
            total += 1
            idx += 1

        for species in sorted(counts.keys()):
            percentage = (counts[species] / total) * 100
            print(f"{species} {percentage:.4f}")
        idx += 1

if __name__ == "__main__":
    solve()
