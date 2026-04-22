import unittest
import sys
from io import StringIO

class TestUVA10071(unittest.TestCase):
    """UVA 10071 - Back to High School Physics 的單元測試"""

    def test_sample_input_1(self):
        """測試範例輸入 0 0"""
        v, t = 0, 0
        expected = 0
        result = 2 * v * t
        self.assertEqual(result, expected)

    def test_sample_input_2(self):
        """測試範例輸入 5 12"""
        v, t = 5, 12
        expected = 120  # 假設公式是 2*v*t
        result = 2 * v * t
        self.assertEqual(result, expected)

    def test_negative_v(self):
        """測試負速度"""
        v, t = -5, 10
        expected = -100
        result = 2 * v * t
        self.assertEqual(result, expected)

    def test_zero_t(self):
        """測試時間為 0"""
        v, t = 10, 0
        expected = 0
        result = 2 * v * t
        self.assertEqual(result, expected)

    def test_positive_values(self):
        """測試正值"""
        v, t = 3, 4
        expected = 24
        result = 2 * v * t
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()