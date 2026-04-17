# TeX 引號替換，簡化版
# 替換 " 成 `` 和 ''，記得交替

def process_text(text):
    # 處理文字，換引號
    # text 是字串
    # 返回換好的字串
    result = []
    left = True
    for char in text:
        if char == '"':
            result.append('``' if left else "''")
            left = not left
        else:
            result.append(char)
    return ''.join(result)

# 測試
if __name__ == "__main__":
    sample = '"Hello" "World"'
    print(process_text(sample))  # 應該 ``Hello'' ``World''