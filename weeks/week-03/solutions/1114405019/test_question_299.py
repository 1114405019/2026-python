# 測試題目 299: UVA 299 - 火車車廂排序
# 測試逆序對計算。

import unittest
from question_299 import count_inversions

class TestQuestion299(unittest.TestCase):
    
    def test_no_inversions(self):
        """測試無逆序"""
        self.assertEqual(count_inversions([1, 2, 3]), 0)
    
    def test_single_inversion(self):
        """測試單個逆序"""
        self.assertEqual(count_inversions([1, 3, 2]), 1)
    
    def test_multiple_inversions(self):
        """測試多個逆序"""
        self.assertEqual(count_inversions([3, 1, 2]), 2)
        self.assertEqual(count_inversions([5, 4, 3, 2, 1]), 10)
    
    def test_already_sorted(self):
        """測試已排序"""
        self.assertEqual(count_inversions([1, 2, 3, 4, 5]), 0)

if __name__ == '__main__':
    unittest.main()