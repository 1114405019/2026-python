"""
UVA 10242 - Fourth Point!!
Technical Adjutant Analysis:
- System Framework: Euclidean Geometry - Parallelogram Vector Addition.
- Algorithm: Finding the vertex opposite to the shared point using vector relations.
- Complexity:
    - Time: O(1) per case.
    - Space: O(1).
"""

import sys

def solve():
    # Process each line representing one parallelogram definition
    for line in sys.stdin:
        coords = list(map(float, line.split()))
        if not coords:
            continue

        # Parse 4 pairs of coordinates (8 values)
        # Note: Two pairs are identical, representing the shared vertex B
        p = [(coords[i], coords[i+1]) for i in range(0, 8, 2)]

        # Identification Logic:
        # A, B, C are vertices. B is the common point.
        # Parallelogram Fourth Point D satisfies: D - A = C - B => D = A + C - B
        if p[0] == p[2]:
            a, b, c = p[1], p[0], p[3]
        elif p[0] == p[3]:
            a, b, c = p[1], p[0], p[2]
        elif p[1] == p[2]:
            a, b, c = p[0], p[1], p[3]
        else: # p[1] == p[3]
            a, b, c = p[0], p[1], p[2]

        # Implementation of Vector Addition D = A + C - B
        res_x = a[0] + c[0] - b[0]
        res_y = a[1] + c[1] - b[1]

        # Output with strictly 3 decimal places
        print(f"{res_x:.3f} {res_y:.3f}")

if __name__ == "__main__":
    solve()
