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
