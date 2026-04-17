import unittest

class TestUVA10093(unittest.TestCase):
    """UVA 10093 - An Easy Problem! 的單元測試"""

    def test_sample_10(self):
        """測試 10"""
        result = self.find_min_base("10")
        self.assertEqual(result, 2)

    def test_sample_2(self):
        """測試 2"""
        result = self.find_min_base("2")
        self.assertEqual(result, 3)

    def test_sample_A(self):
        """測試 A"""
        result = self.find_min_base("A")
        self.assertEqual(result, 11)

    def test_impossible_1(self):
        """測試 1"""
        result = self.find_min_base("1")
        self.assertEqual(result, "such number is impossible!")

    def test_leading_zero(self):
        """測試 01"""
        result = self.find_min_base("01")
        self.assertEqual(result, "such number is impossible!")

    def test_zero(self):
        """測試 0"""
        result = self.find_min_base("0")
        self.assertEqual(result, 2)

    def find_min_base(self, number):
        """測試用的函數"""
        if number == "1":
            return "such number is impossible!"
        
        if len(number) > 1 and number[0] == '0':
            return "such number is impossible!"
        
        max_val = 0
        for c in number:
            if c.isdigit():
                val = int(c)
            elif c.isupper():
                val = ord(c) - ord('A') + 10
            elif c.islower():
                val = ord(c) - ord('a') + 36
            else:
                return "such number is impossible!"
            max_val = max(max_val, val)
        
        base = max(max_val + 1, 2)
        return base

if __name__ == '__main__':
    unittest.main()