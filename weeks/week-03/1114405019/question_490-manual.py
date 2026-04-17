# 文字旋轉 90 度，簡化版
# 旋轉文字，記得順時針

def rotate(lines):
    # 旋轉文字
    # lines 是行列表
    # 返回旋轉後的行
    if not lines:
        return []
    max_len = max(len(l) for l in lines)
    padded = [l.ljust(max_len) for l in lines]
    return [''.join(padded[r][c] for r in range(len(padded)-1, -1, -1)).rstrip() for c in range(max_len)]

# 測試
if __name__ == "__main__":
    sample = ["AB", "CD"]
    print(rotate(sample))  # 應該 ['CA', 'DB']