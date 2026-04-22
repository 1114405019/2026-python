# 測試 UVA 10035: Primary Arithmetic
import unittest
from solution_10035 import carry_operations

class TestPrimaryArithmetic(unittest.TestCase):
    def test_no_carry(self):
        self.assertEqual(carry_operations(123, 456), 0)

    def test_one_carry(self):
        self.assertEqual(carry_operations(555, 555), 3)  # 5+5+1=11, carry 1 each time

    def test_multiple_carries(self):
        self.assertEqual(carry_operations(999, 1), 3)

    def test_zero(self):
        self.assertEqual(carry_operations(0, 0), 0)

if __name__ == "__main__":
    unittest.main()</content>
<parameter name="filePath">c:\Users\yiteng\Downloads\0318\2026-python\weeks\week-04\solutions\test_question_10035.py