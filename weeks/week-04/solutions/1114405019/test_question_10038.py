# 測試 UVA 10038: Jolly Jumpers
import unittest
from solution_10038 import is_jolly_jumper

class TestJollyJumpers(unittest.TestCase):
    def test_jolly(self):
        self.assertTrue(is_jolly_jumper([1, 4, 2, 3]))

    def test_not_jolly(self):
        self.assertFalse(is_jolly_jumper([1, 4, 2, -1, 6]))

    def test_single(self):
        self.assertTrue(is_jolly_jumper([5]))

    def test_two_jolly(self):
        self.assertTrue(is_jolly_jumper([1, 2]))

    def test_two_not(self):
        self.assertFalse(is_jolly_jumper([1, 1]))

if __name__ == "__main__":
    unittest.main()</content>
<parameter name="filePath">c:\Users\yiteng\Downloads\0318\2026-python\weeks\week-04\solutions\test_question_10038.py