# 測試題目 490: UVA 490 - 文字旋轉 90 度
# 測試旋轉邏輯。

import unittest
from question_490 import rotate_text

class TestQuestion490(unittest.TestCase):
    
    def test_simple_rotate(self):
        """測試簡單旋轉"""
        lines = ["AB", "CD"]
        rotated = rotate_text(lines)
        self.assertEqual(rotated, ["CA", "DB"])
    
    def test_uneven_lines(self):
        """測試不等長行"""
        lines = ["A", "BC"]
        rotated = rotate_text(lines)
        self.assertEqual(rotated, ["BA", "C"])
    
    def test_single_line(self):
        """測試單行"""
        lines = ["HELLO"]
        rotated = rotate_text(lines)
        self.assertEqual(rotated, ["H", "E", "L", "L", "O"])
    
    def test_empty(self):
        """測試空輸入"""
        self.assertEqual(rotate_text([]), [])

if __name__ == '__main__':
    unittest.main()