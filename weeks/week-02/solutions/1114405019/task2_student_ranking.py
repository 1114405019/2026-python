def rank_students(students, k):
    # 分數降序(-x[1]), 年齡升序(x[2]), 姓名升序(x[0])
    sorted_data = sorted(students, key=lambda x: (-x[1], x[2], x[0]))
    return sorted_data[:k]

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().split()
    if input_data:
        n, k = int(input_data[0]), int(input_data[1])
        students = []
        idx = 2
        for _ in range(n):
            name = input_data[idx]
            score = int(input_data[idx+1])
            age = int(input_data[idx+2])
            students.append((name, score, age))
            idx += 3
        
        for res in rank_students(students, k):
            print(f"{res[0]} {res[1]} {res[2]}")