# 測試 UVA 948: Fibonaccimal Base
import unittest
from solution_948 import fibonaccimal_base

class TestFibonaccimalBase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(fibonaccimal_base(0), "0")

    def test_one(self):
        self.assertEqual(fibonaccimal_base(1), "1")

    def test_two(self):
        self.assertEqual(fibonaccimal_base(2), "10")

    def test_three(self):
        self.assertEqual(fibonaccimal_base(3), "100")

    def test_four(self):
        self.assertEqual(fibonaccimal_base(4), "101")

    def test_five(self):
        self.assertEqual(fibonaccimal_base(5), "1000")

    def test_six(self):
        self.assertEqual(fibonaccimal_base(6), "1001")

    def test_seven(self):
        self.assertEqual(fibonaccimal_base(7), "1010")

    def test_eight(self):
        self.assertEqual(fibonaccimal_base(8), "10000")

    def test_large(self):
        self.assertEqual(fibonaccimal_base(13), "100000")

if __name__ == "__main__":
    unittest.main()</content>
<parameter name="filePath">c:\Users\yiteng\Downloads\0318\2026-python\weeks\week-04\solutions\test_question_948.py