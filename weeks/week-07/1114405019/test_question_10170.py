import unittest

class TestUVA10170(unittest.TestCase):
    """UVA 10170 - The Hotel with Infinite Rooms 的單元測試"""

    def test_sample_1_1(self):
        """測試 S=1, D=1"""
        result = self.find_room(1, 1)
        self.assertEqual(result, 1)

    def test_sample_1_2(self):
        """測試 S=1, D=2"""
        result = self.find_room(1, 2)
        self.assertEqual(result, 2)

    def test_sample_1_3(self):
        """測試 S=1, D=3"""
        result = self.find_room(1, 3)
        self.assertEqual(result, 2)

    def test_sample_1_4(self):
        """測試 S=1, D=4"""
        result = self.find_room(1, 4)
        self.assertEqual(result, 3)

    def test_sample_1_10(self):
        """測試 S=1, D=10"""
        result = self.find_room(1, 10)
        self.assertEqual(result, 4)

    def test_s_2_d_1(self):
        """測試 S=2, D=1"""
        result = self.find_room(2, 1)
        self.assertEqual(result, 2)

    def find_room(self, S, D):
        """測試用的函數"""
        current_room = S
        guests_needed = D
        while guests_needed > current_room:
            guests_needed -= current_room
            current_room += 1
        return current_room

if __name__ == '__main__':
    unittest.main()