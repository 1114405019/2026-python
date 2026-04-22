"""
UVA 10252 - Common Permutation
Technical Adjutant Analysis:
- System Framework: Character Frequency Alignment.
- Algorithm: Counting intersections of lowercase character frequencies.
- Complexity:
    - Time: O(N + M + 26) where N, M are lengths of the input strings.
    - Space: O(26) for frequency arrays.
"""

import sys

def solve():
    # Read input lines into a list
    lines = sys.stdin.read().splitlines()
    # Process inputs in pairs (s1 and s2)
    for i in range(0, len(lines), 2):
        if i + 1 >= len(lines):
            break
        s1 = lines[i]
        s2 = lines[i+1]

        # Initialize frequency buckets for lowercase English alphabet
        count1 = [0] * 26
        count2 = [0] * 26

        # Populate frequency buckets for first string
        for char in s1:
            if 'a' <= char <= 'z':
                count1[ord(char) - ord('a')] += 1
        # Populate frequency buckets for second string
        for char in s2:
            if 'a' <= char <= 'z':
                count2[ord(char) - ord('a')] += 1

        # Determine the common characters in sorted order
        res = []
        for j in range(26):
            # Intersection is the minimum count for each character
            common = min(count1[j], count2[j])
            res.append(chr(ord('a') + j) * common)

        # Output the concatenated common characters
        print("".join(res))

if __name__ == "__main__":
    solve()
