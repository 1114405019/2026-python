import unittest
from task1_sequence_clean import clean_sequence

class TestTask1(unittest.TestCase):
    def test_normal_case(self):
        # 輸入範例
        input_data = "5 3 5 2 9 2 8 3 1"
        # 呼叫你的功能函式
        dedupe, asc, desc, evens = clean_sequence(input_data)
        
        # 檢查結果是否跟預期一樣
        self.assertEqual(dedupe, [5, 3, 2, 9, 8, 1])
        self.assertEqual(asc, [1, 2, 2, 3, 3, 5, 5, 8, 9])
        self.assertEqual(evens, [2, 2, 8])

if __name__ == '__main__':
    unittest.main()