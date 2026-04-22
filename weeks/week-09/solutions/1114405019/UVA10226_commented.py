"""
UVA 10226 - Hardwood Species
Technical Adjutant Analysis:
- System Framework: Categorical Frequency Distribution.
- Algorithm: Hash Map Frequency Accumulation.
- Complexity:
    - Time: O(N log M) where N is total tree count and M is unique species count (log M from sorting).
    - Space: O(M) for dictionary storage.
"""

import sys

def solve():
    # Read entire input and split into lines for processing
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    try:
        # First line denotes the number of test cases
        num_cases = int(input_data[0])
    except (ValueError, IndexError):
        return

    # Starting index after the first blank line following num_cases
    idx = 2
    first = True

    for _ in range(num_cases):
        # Blank line between case outputs
        if not first:
            print()
        first = False

        counts = {}
        total = 0

        # Process lines until an empty line or end of data
        while idx < len(input_data) and input_data[idx].strip():
            species = input_data[idx].strip()
            # O(1) average case lookup and update
            counts[species] = counts.get(species, 0) + 1
            total += 1
            idx += 1

        # O(M log M) sort where M is the number of unique species
        for species in sorted(counts.keys()):
            percentage = (counts[species] / total) * 100
            # Output format: Name Percentage (4 decimal places)
            print(f"{species} {percentage:.4f}")

        # Skip the blank line between cases in the input
        idx += 1

if __name__ == "__main__":
    solve()
