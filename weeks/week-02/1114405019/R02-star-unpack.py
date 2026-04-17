# R02. 星號解包：處理不定長度序列
# ============================================================================
# 星號解包（Star Unpacking）是 Python 解包語法的高階應用
# 使用 * 可以將序列中剩餘的元素收集成一個列表
# 適用於處理長度不確定的序列，是函數式程式設計的重要工具
# ============================================================================

## 1. 星號解包基礎概念
# --------------------------------------------------------------------------
# * 用於解包時會收集剩餘的所有元素，形成一個新的列表
# * 可以出現在解包賦值的任何位置，但只能使用一次

# 範例：丟棄首尾，取中間值計算平均
def drop_first_last(grades):
    """
    計算成績平均值，排除最高分和最低分
    參數：grades - 成績列表
    返回：平均分數
    """
    first, *middle, last = grades
    if not middle:
        return 0.0
    return sum(middle) / len(middle)

grades = [85, 90, 78, 92, 88]
print(f"成績平均（排除極值）：{drop_first_last(grades)}")

## 2. 收集剩餘元素應用
# --------------------------------------------------------------------------
# 常見於處理包含可變數量資料的記錄

# 範例：解析聯絡人資訊
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(f"聯絡人：{name}")
print(f"郵箱：{email}")
print(f"電話號碼：{phone_numbers}")

# 範例：分割檔案路徑
path = '/usr/local/bin/python'
*dirs, filename = path.split('/')
print(f"目錄路徑：{dirs}")
print(f"檔案名稱：{filename}")

## 3. 星號在不同位置的用法
# --------------------------------------------------------------------------
# * 可以出現在賦值的開始、中間或結尾

# 範例：收集尾部元素
scores = [10, 8, 7, 1, 9, 5, 10, 3]
*trailing, current = scores
print(f"歷史分數：{trailing}")
print(f"當前分數：{current}")

# 範例：分割列表為頭、中、尾
items = [1, 2, 3, 4, 5, 6, 7]
head, *middle, tail = items
print(f"頭部：{head}, 中間：{middle}, 尾部：{tail}")

## 4. 進階應用：命令列參數處理
# --------------------------------------------------------------------------
# 在腳本中處理命令列參數時特別有用

# 模擬命令列參數（實際使用時用 sys.argv）
import sys
# 假設命令行為：python script.py arg1 arg2 arg3
mock_argv = ['script.py', 'input.txt', '--verbose', '--output=result.txt']
script_name, *args = mock_argv
print(f"腳本名稱：{script_name}")
print(f"參數列表：{args}")

# 解析簡單的命令列選項
def parse_simple_args(args):
    """簡單的參數解析器"""
    flags = []
    values = []
    for arg in args:
        if arg.startswith('--'):
            flags.append(arg[2:])
        else:
            values.append(arg)
    return flags, values

flags, values = parse_simple_args(args)
print(f"標誌：{flags}")
print(f"值：{values}")

## 5. 星號解包在函數參數中的應用
# --------------------------------------------------------------------------
# 雖然本節重點是賦值解包，但星號也可用於函數呼叫

# 範例：展開列表作為函數參數
def calculate_total(*numbers):
    """計算多個數字的總和"""
    return sum(numbers)

numbers_list = [1, 2, 3, 4, 5]
total = calculate_total(*numbers_list)  # 展開列表
print(f"數字總和：{total}")

# 範例：合併列表
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [*list1, *list2]  # 在列表字面量中使用 *
print(f"合併列表：{combined}")

## 6. 注意事項與最佳實踐
# --------------------------------------------------------------------------
# 1. * 只能在賦值中使用一次
# 2. 收集的元素總是列表類型
# 3. 如果沒有剩餘元素，* 會收集空列表
# 4. 在函數定義中使用 *args 收集參數

# 範例：處理空剩餘元素
single_item = [42]
first, *rest = single_item
print(f"第一個：{first}, 剩餘：{rest}")  # rest 為 []

# ============================================================================
# 語法重點總結：
# 1. * 用於收集序列中剩餘的元素
# 2. 適用於元組、列表、其他可迭代物件
# 3. 在函數呼叫中 * 用於展開序列
# 4. 常用於處理可變長度資料結構
# ============================================================================
