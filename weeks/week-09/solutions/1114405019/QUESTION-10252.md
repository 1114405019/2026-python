# Technical Analysis: QUESTION-10252 (Common Permutation)

## Technical Logic
- **System Framework**: Character Frequency Intersection and Lexicographical Alignment.
- **Architectural Analysis**: 
  The system computes the intersection of two multiset representations of characters. By representing each string as a frequency vector of size 26 (for 'a'-'z'), the common permutation is derived by taking the minimum frequency for each character across both vectors. The result is naturally sorted due to the sequential traversal of the frequency vectors.
- **Complexity Profile**:
  - **Time Complexity**: $O(N + M + \Sigma)$, where $N, M$ are the lengths of the two strings and $\Sigma = 26$ is the alphabet size.
  - **Space Complexity**: $O(\Sigma)$ to store the character counts.
- **Data Structures**: Two fixed-size integer arrays (frequency buckets).

## Solution Code
```python
import sys

def solve():
    lines = sys.stdin.read().splitlines()
    for i in range(0, len(lines), 2):
        if i + 1 >= len(lines):
            break
        s1 = lines[i]
        s2 = lines[i+1]
        
        count1 = [0] * 26
        count2 = [0] * 26
        
        for char in s1:
            if 'a' <= char <= 'z':
                count1[ord(char) - ord('a')] += 1
        for char in s2:
            if 'a' <= char <= 'z':
                count2[ord(char) - ord('a')] += 1
        
        res = []
        for j in range(26):
            common = min(count1[j], count2[j])
            res.append(chr(ord('a') + j) * common)
        
        print("".join(res))

if __name__ == "__main__":
    solve()
```

## Test Cases
**Sample Input**
```text
pretty
women
walking
down
```

**Expected Output**
```text
e
nw
```
