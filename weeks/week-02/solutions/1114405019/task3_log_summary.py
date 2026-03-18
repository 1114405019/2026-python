from collections import Counter

def summarize_logs(logs):
    if not logs:
        return [], None, 0
    
    # 1. 統計每位使用者的事件數
    users = [log[0] for log in logs]
    user_counts = Counter(users)
    
    # 排序規則：次數降序 (-x[1])，使用者名稱升序 (x[0])
    sorted_users = sorted(user_counts.items(), key=lambda x: (-x[1], x[0]))
    
    # 2. 統計全域最常見的 action
    actions = [log[1] for log in logs]
    action_counts = Counter(actions)
    
    # 取得最常見的一個 (most_common 回傳的是 list of tuples)
    top_action, top_count = action_counts.most_common(1)[0]
    
    return sorted_users, top_action, top_count

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().splitlines()
    if input_data:
        m = int(input_data[0])
        logs = [tuple(line.split()) for line in input_data[1:m+1]]
        
        user_res, act_name, act_count = summarize_logs(logs)
        
        for name, count in user_res:
            print(f"{name} {count}")
        if act_name:
            print(f"top_action: {act_name} {act_count}")