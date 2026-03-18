def clean_sequence(input_str):
    # 將字串轉換為整數列表
    nums = list(map(int, input_str.split()))
    
    # 1. 去重（保留第一次出現順序）
    # 使用 dict.fromkeys 是 Python 中最簡單保留順序的去重方式
    dedupe = list(dict.fromkeys(nums))
    
    # 2. 由小到大排序
    asc = sorted(nums)
    
    # 3. 由大到小排序
    desc = sorted(nums, reverse=True)
    
    # 4. 偶數序列（維持原始順序）
    evens = [x for x in nums if x % 2 == 0]
    
    return dedupe, asc, desc, evens

if __name__ == "__main__":
    # 讓你可以手動測試
    try:
        user_input = input().strip()
        if user_input:
            d, a, ds, e = clean_sequence(user_input)
            print(f"dedupe: {' '.join(map(str, d))}")
            print(f"asc: {' '.join(map(str, a))}")
            print(f"desc: {' '.join(map(str, ds))}")
            print(f"evens: {' '.join(map(str, e))}")
    except EOFError:
        pass