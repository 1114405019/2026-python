import sys


def parse_input():
    """從標準輸入讀取所有資料，並回傳分行後的清單。"""
    data = sys.stdin.read().splitlines()
    # 去除輸入中可能的空白行，避免影響解析
    return [line.strip() for line in data if line.strip() != ""]


def build_minefield(rows, n, m):
    """依照地雷配置，計算每個空白格周圍 8 個方向的地雷數量。"""
    # 8 個方向：上下左右與四個斜角
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    result = []
    for i in range(n):
        row_result = []
        for j in range(m):
            if rows[i][j] == '*':
                # 地雷格子直接保留
                row_result.append('*')
                continue

            count = 0
            for di, dj in directions:
                ni, nj = i + di, j + dj
                # 邊界檢查：只有在合法座標內才讀取地雷資訊
                if 0 <= ni < n and 0 <= nj < m and rows[ni][nj] == '*':
                    count += 1
            row_result.append(str(count))
        result.append(''.join(row_result))
    return result


def main():
    lines = parse_input()
    if not lines:
        return

    outputs = []
    field_index = 1
    idx = 0

    while idx < len(lines):
        parts = lines[idx].split()
        idx += 1
        if len(parts) != 2:
            # 如果讀到非預期格式行，直接忽略
            continue

        n, m = map(int, parts)
        if n == 0 and m == 0:
            break

        # 讀取 n 行地雷地圖，並保留原始順序
        rows = lines[idx: idx + n]
        idx += n

        field_output = [f"Field #{field_index}:"]
        field_output.extend(build_minefield(rows, n, m))
        outputs.append('\n'.join(field_output))
        field_index += 1

    # 行與行之間以空行分隔，最後不多印空行
    sys.stdout.write('\n\n'.join(outputs))


if __name__ == '__main__':
    main()
