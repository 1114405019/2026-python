# 題目 118: UVA 118 - 機器人移動 (簡化版本)
# 簡化模擬機器人移動，專注於基本邏輯。

directions = ['N', 'E', 'S', 'W']
left = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
right = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

def simulate(x, y, d, ins, mx, my, scents):
    lost = False
    for c in ins:
        if c == 'L': d = left[d]
        elif c == 'R': d = right[d]
        elif c == 'F':
            nx, ny = x + move[d][0], y + move[d][1]
            if nx < 0 or nx > mx or ny < 0 or ny > my:
                if (x, y) not in scents:
                    scents.add((x, y))
                    lost = True
                    break
            else:
                x, y = nx, ny
    return x, y, d, lost

# 範例使用
if __name__ == "__main__":
    # 簡單測試
    scents = set()
    print(simulate(1, 1, 'N', 'F', 5, 5, scents))  # 前進到 (1,2,N)
    print(simulate(1, 1, 'N', 'FF', 5, 5, scents))  # 掉落