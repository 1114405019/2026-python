# 題目 272: UVA 272 - TeX 引號替換
# 將輸入中的雙引號替換為 TeX 風格的引號：第一個 " 為 ``，第二個為 ''，交替進行。

import sys

def process_line(line, is_left_quote):
    """
    處理單行文字，將雙引號替換為 TeX 引號。
    
    參數:
    line (str): 輸入行
    is_left_quote (bool): 是否為左引號的旗標
    
    返回:
    tuple: (處理後的行, 更新後的旗標)
    """
    result = []
    for char in line:
        if char == '"':
            if is_left_quote:
                result.append('``')
            else:
                result.append("''")
            is_left_quote = not is_left_quote
        else:
            result.append(char)
    return ''.join(result), is_left_quote

def main():
    """
    主函數，讀取所有輸入行，處理並輸出。
    """
    is_left_quote = True  # 開始時為左引號
    for line in sys.stdin:
        processed_line, is_left_quote = process_line(line, is_left_quote)
        print(processed_line, end='')  # 保留原始換行

if __name__ == "__main__":
    main()