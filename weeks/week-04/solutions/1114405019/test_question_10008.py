# 測試 UVA 10008: What's Cryptanalysis?
import unittest
from solution_10008 import cryptanalysis

class TestCryptanalysis(unittest.TestCase):
    def test_sample1(self):
        lines = ["This is a test.", "Count me 1 2 3 4 5."]
        expected = ["T 6", "S 5", "E 4", "I 3", "A 2", "C 2", "M 2", "N 2", "O 2", "U 2", "H 1", "R 1"]
        self.assertEqual(cryptanalysis(lines), expected)

    def test_no_letters(self):
        lines = ["123 !@#"]
        self.assertEqual(cryptanalysis(lines), [])

    def test_single_letter(self):
        lines = ["A"]
        self.assertEqual(cryptanalysis(lines), ["A 1"])

    def test_mixed_case(self):
        lines = ["Aa Bb"]
        self.assertEqual(cryptanalysis(lines), ["A 2", "B 2"])

if __name__ == "__main__":
    unittest.main()</content>
<parameter name="filePath">c:\Users\yiteng\Downloads\0318\2026-python\weeks\week-04\solutions\test_question_10008.py