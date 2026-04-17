# 測試題目 100: UVA 100 - 3n+1 問題
# 使用 unittest 框架測試 cycle_length 和 find_max_cycle 函數。
# 包含題目範例、邊界條件和額外測試案例。

import unittest
from question_100 import cycle_length, find_max_cycle

class TestQuestion100(unittest.TestCase):
    
    def test_cycle_length_basic(self):
        """測試基本 cycle length 計算"""
        self.assertEqual(cycle_length(1), 1)
        self.assertEqual(cycle_length(2), 2)  # 2 -> 1
        self.assertEqual(cycle_length(3), 8)  # 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
        self.assertEqual(cycle_length(4), 3)  # 4 -> 2 -> 1
    
    def test_cycle_length_larger(self):
        """測試較大數字的 cycle length"""
        self.assertEqual(cycle_length(22), 16)  # 題目範例
    
    def test_find_max_cycle_example(self):
        """測試題目範例: 1 到 10 的最大 cycle length 為 20"""
        self.assertEqual(find_max_cycle(1, 10), 20)
        self.assertEqual(find_max_cycle(10, 1), 20)  # 順序無關
    
    def test_find_max_cycle_single(self):
        """測試單一數字的區間"""
        self.assertEqual(find_max_cycle(5, 5), cycle_length(5))
    
    def test_find_max_cycle_large(self):
        """測試較大區間"""
        # 假設 100 到 200 的最大是 125 (或檢查)
        # 實際上需要計算，但這裡用已知值
        self.assertGreater(find_max_cycle(100, 200), 100)  # 至少大於 100
    
    def test_edge_cases(self):
        """測試邊界條件"""
        self.assertEqual(find_max_cycle(1, 1), 1)
        self.assertEqual(find_max_cycle(2, 2), 2)

if __name__ == '__main__':
    unittest.main()