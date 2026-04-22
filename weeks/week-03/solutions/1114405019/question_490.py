# 題目 490: UVA 490 - 文字旋轉 90 度
# 將輸入的文字矩陣順時針旋轉 90 度輸出。

import sys

def rotate_text(lines):
    """
    旋轉文字矩陣。
    
    參數:
    lines (list): 輸入行列表
    
    返回:
    list: 旋轉後的行列表
    """
    if not lines:
        return []
    
    # 找到最長行長度
    max_len = max(len(line.rstrip()) for line in lines)
    
    # 填充每行到 max_len
    padded_lines = [line.rstrip().ljust(max_len) for line in lines]
    
    # 旋轉：新矩陣的行數 = max_len, 列數 = len(lines)
    rotated = []
    for col in range(max_len):
        new_row = ''.join(padded_lines[row][col] for row in range(len(padded_lines) - 1, -1, -1))
        rotated.append(new_row.rstrip())  # 移除尾部空格
    
    return rotated

def main():
    """
    主函數，讀取輸入並輸出旋轉後的文字。
    """
    lines = [line.rstrip('\n') for line in sys.stdin.readlines()]
    rotated = rotate_text(lines)
    for row in rotated:
        print(row)

if __name__ == "__main__":
    main()