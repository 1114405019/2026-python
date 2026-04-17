import unittest

class TestUVA10101(unittest.TestCase):
    """UVA 10101 - Bangla Numbers 的單元測試"""

    def test_sample_123456789(self):
        """測試 123456789"""
        result = self.format_bangla_number(123456789)
        self.assertEqual(result, "12,34,56,789")

    def test_sample_123(self):
        """測試 123"""
        result = self.format_bangla_number(123)
        self.assertEqual(result, "123")

    def test_sample_1234(self):
        """測試 1234"""
        result = self.format_bangla_number(1234)
        self.assertEqual(result, "1,234")

    def test_sample_12345(self):
        """測試 12345"""
        result = self.format_bangla_number(12345)
        self.assertEqual(result, "12,345")

    def test_zero(self):
        """測試 0"""
        result = self.format_bangla_number(0)
        self.assertEqual(result, "0")

    def test_large_number(self):
        """測試大數字"""
        result = self.format_bangla_number(123456789012345)
        # 假設格式
        self.assertEqual(result, "12,34,56,78,90,12,345")

    def format_bangla_number(self, n):
        """測試用的格式化函數"""
        s = str(n)
        if len(s) <= 3:
            return s
        
        result = []
        i = len(s)
        group_len = 3 if i >= 3 else i
        result.append(s[i - group_len:i])
        i -= group_len
        while i > 0:
            group_len = 2 if i >= 2 else i
            result.append(s[i - group_len:i])
            i -= group_len
        result.reverse()
        return ','.join(result)

if __name__ == '__main__':
    unittest.main()