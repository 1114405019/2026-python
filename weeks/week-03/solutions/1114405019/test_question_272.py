# 測試題目 272: UVA 272 - TeX 引號替換
# 測試引號替換邏輯。

import unittest
from question_272 import process_line

class TestQuestion272(unittest.TestCase):
    
    def test_single_quote(self):
        """測試單個引號"""
        result, flag = process_line('"test"', True)
        self.assertEqual(result, "``test''")
        self.assertTrue(flag)
    
    def test_multiple_quotes(self):
        """測試多個引號"""
        result, flag = process_line('"a" "b"', True)
        self.assertEqual(result, "``a'' ``b''")
        self.assertTrue(flag)
    
    def test_no_quotes(self):
        """測試無引號"""
        result, flag = process_line('hello world', True)
        self.assertEqual(result, 'hello world')
        self.assertTrue(flag)
    
    def test_mixed(self):
        """測試混合文字"""
        result, flag = process_line('He said "yes".', True)
        self.assertEqual(result, "He said ``yes''.")
        self.assertTrue(flag)

if __name__ == '__main__':
    unittest.main()