import sys

KEYBOARD = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"


def build_decode_map():
    """建立解碼對照表，將每個字元對應到鍵盤上左邊的按鍵。"""
    mapping = {}
    for i in range(1, len(KEYBOARD)):
        mapping[KEYBOARD[i]] = KEYBOARD[i - 1]
    # 支援小寫字母輸入，並保留原始大小寫形式
    for char in list(mapping.keys()):
        if char.isalpha():
            mapping[char.lower()] = mapping[char].lower()
    # 空白字元保留不變
    mapping[' '] = ' '
    return mapping


def main():
    decode_map = build_decode_map()
    data = sys.stdin.read()
    if data == '':
        return

    output_chars = []
    for ch in data:
        if ch == '\n':
            output_chars.append('\n')
            continue
        output_chars.append(decode_map.get(ch, ch))

    sys.stdout.write(''.join(output_chars))


if __name__ == '__main__':
    main()
