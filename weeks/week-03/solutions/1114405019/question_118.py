# 題目 118: UVA 118 - 機器人移動
# 模擬機器人在矩形網格中的移動，處理指令並考慮邊界和 scent 標記。

import sys

# 方向定義：N, E, S, W
directions = ['N', 'E', 'S', 'W']

# 左轉和右轉的變化
left_turn = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
right_turn = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}

# 前進的變化
move_delta = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

def is_out_of_bounds(x, y, max_x, max_y):
    """檢查位置是否超出邊界"""
    return x < 0 or x > max_x or y < 0 or y > max_y

def simulate_robot(initial_x, initial_y, initial_dir, instructions, max_x, max_y, scents):
    """
    模擬單個機器人的移動。
    
    參數:
    initial_x, initial_y (int): 初始位置
    initial_dir (str): 初始方向
    instructions (str): 指令字串
    max_x, max_y (int): 網格大小
    scents (set): 已有的 scent 位置
    
    返回:
    tuple: (最終x, 最終y, 最終方向, 是否掉落)
    """
    x, y, dir = initial_x, initial_y, initial_dir
    lost = False
    
    for cmd in instructions:
        if cmd == 'L':
            dir = left_turn[dir]
        elif cmd == 'R':
            dir = right_turn[dir]
        elif cmd == 'F':
            dx, dy = move_delta[dir]
            new_x, new_y = x + dx, y + dy
            if is_out_of_bounds(new_x, new_y, max_x, max_y):
                if (x, y) not in scents:
                    scents.add((x, y))
                    lost = True
                    break  # 掉落，停止
                # 如果有 scent，忽略指令
            else:
                x, y = new_x, new_y
    
    return x, y, dir, lost

def main():
    """
    主函數，讀取輸入並處理每個機器人。
    """
    lines = sys.stdin.readlines()
    if not lines:
        return
    
    # 第一行：max_x max_y
    max_x, max_y = map(int, lines[0].split())
    scents = set()
    
    i = 1
    while i < len(lines):
        # 機器人初始位置
        parts = lines[i].strip().split()
        x, y = int(parts[0]), int(parts[1])
        dir = parts[2]
        i += 1
        
        # 指令
        instructions = lines[i].strip()
        i += 1
        
        # 模擬
        final_x, final_y, final_dir, lost = simulate_robot(x, y, dir, instructions, max_x, max_y, scents)
        
        # 輸出
        print(f"{final_x} {final_y} {final_dir}", end="")
        if lost:
            print(" LOST")
        else:
            print()

if __name__ == "__main__":
    main()