# 題目 490: UVA 490 - 文字旋轉 90 度 (簡化版本)
# 簡單旋轉邏輯。

def rotate(lines):
    if not lines:
        return []
    max_len = max(len(l) for l in lines)
    padded = [l.ljust(max_len) for l in lines]
    return [''.join(padded[r][c] for r in range(len(padded)-1, -1, -1)).rstrip() for c in range(max_len)]

# 範例
if __name__ == "__main__":
    sample = ["AB", "CD"]
    print(rotate(sample))  # ['DC', 'BA']