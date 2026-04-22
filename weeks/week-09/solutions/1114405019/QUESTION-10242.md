# Technical Analysis: QUESTION-10242 (Fourth Point!!)

## Technical Logic
- **System Framework**: Euclidean Geometric Vector Solver.
- **Architectural Analysis**: 
  The task is to determine the fourth vertex of a parallelogram given three vertices where one is common to two sides. By utilizing the vector property $\vec{D} = \vec{A} + \vec{C} - \vec{B}$ (where $B$ is the vertex shared by sides $BA$ and $BC$), the system computes coordinates in a 2D Cartesian plane.
- **Complexity Profile**:
  - **Time Complexity**: $O(1)$ per test case.
  - **Space Complexity**: $O(1)$.
- **Mathematical Selection**: Vector addition and subtraction.

## Solution Code
```python
import sys

def solve():
    for line in sys.stdin:
        coords = list(map(float, line.split()))
        if not coords:
            continue
        
        p = [(coords[i], coords[i+1]) for i in range(0, 8, 2)]
        
        if p[0] == p[2]:
            a, b, c = p[1], p[0], p[3]
        elif p[0] == p[3]:
            a, b, c = p[1], p[0], p[2]
        elif p[1] == p[2]:
            a, b, c = p[0], p[1], p[3]
        else:
            a, b, c = p[0], p[1], p[2]
            
        res_x = a[0] + c[0] - b[0]
        res_y = a[1] + c[1] - b[1]
        
        print(f"{res_x:.3f} {res_y:.3f}")

if __name__ == "__main__":
    solve()
```

## Test Cases
**Sample Input**
```text
0.000 0.000 0.000 1.000 0.000 1.000 1.000 1.000
1.000 0.000 3.500 3.500 3.500 3.500 0.000 1.000
```

**Expected Output**
```text
1.000 0.000
-2.500 -2.500
```
