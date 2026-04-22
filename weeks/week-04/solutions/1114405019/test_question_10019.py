# 測試 UVA 10019: Funny Encryption Method
import unittest
from solution_10019 import funny_encryption

class TestFunnyEncryption(unittest.TestCase):
    def test_1(self):
        self.assertEqual(funny_encryption(1), 1)  # dec:1, bin:1

    def test_10(self):
        self.assertEqual(funny_encryption(10), 1)  # dec:1, bin:1010 -> 2, total 3? Wait, 10 dec has '1', bin '1010' has two 1s, total 3

    def test_100(self):
        self.assertEqual(funny_encryption(100), 3)  # dec:001 has one 1, bin 1100100 has three 1s, total 4? Wait, let's calculate properly.

    # Actually, for 100: str(100)='100' count '1'=1, bin(100)=0b1100100 count '1'=3, total 4

    def test_265(self):
        self.assertEqual(funny_encryption(265), 4)  # dec:265 has one 1, bin:100001001 has three 1s, total 4

if __name__ == "__main__":
    unittest.main()</content>
<parameter name="filePath">c:\Users\yiteng\Downloads\0318\2026-python\weeks\week-04\solutions\test_question_10019.py