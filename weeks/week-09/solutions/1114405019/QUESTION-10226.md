# Technical Analysis: QUESTION-10226 (Hardwood Species)

## Technical Logic
- **System Framework**: Frequency distribution analysis of categorical data for environmental monitoring.
- **Architectural Analysis**: 
  The system processes a continuous stream of species data, requiring efficient accumulation and lexicographical reporting. A hash-based mapping strategy is deployed to ensure constant-time updates, followed by a sorted traversal for the final report generation.
- **Algorithm Complexity**:
  - **Time Complexity**: $O(N \log M)$, where $N$ is the total number of tree entries and $M$ is the number of unique species. The bottleneck is the sorting of $M$ species.
  - **Space Complexity**: $O(M)$ to maintain the frequency map of unique species.
- **Data Structures**: `dict` (Hash Map) for frequency counts; `list` for sorted output buffering.

## Solution Code
```python
import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    try:
        t = int(input_data[0])
    except:
        return
        
    idx = 2
    first = True
    
    for _ in range(t):
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
```

## Test Cases
**Sample Input**
```text
1

Red Alder
Ash
Aspen
Ash
Cherries
Maple
```

**Expected Output**
```text
Ash 33.3333
Aspen 16.6667
Cherries 16.6667
Maple 16.6667
Red Alder 16.6667
```
