# 題目 272: UVA 272 - TeX 引號替換 (簡化版本)
# 簡單替換雙引號為 TeX 引號。

def process_text(text):
    """處理整個文字"""
    result = []
    left = True
    for char in text:
        if char == '"':
            result.append('``' if left else "''")
            left = not left
        else:
            result.append(char)
    return ''.join(result)

# 範例
if __name__ == "__main__":
    sample = '"Hello" "World"'
    print(process_text(sample))  # ``Hello'' ``World''