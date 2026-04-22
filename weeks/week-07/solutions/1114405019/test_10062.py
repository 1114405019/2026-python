import unittest
from collections import Counter
import sys
from io import StringIO

class TestUVA10062(unittest.TestCase):
    """UVA 10062 - Tell me the frequencies! 的單元測試"""

    def test_basic_frequency_count(self):
        """測試基本字元頻率計算"""
        # 測試輸入：AAABBC
        # 預期輸出：
        # 67 1  (C)
        # 66 2  (B)
        # 65 3  (A)
        input_text = "AAABBC"
        expected = ["67 1", "66 2", "65 3"]

        result = self._process_line(input_text)
        self.assertEqual(result, expected)

    def test_numbers_frequency(self):
        """測試數字字元頻率"""
        # 測試輸入：122333
        # 預期輸出：
        # 49 1  (1)
        # 50 2  (2)
        # 51 3  (3)
        input_text = "122333"
        expected = ["49 1", "50 2", "51 3"]

        result = self._process_line(input_text)
        self.assertEqual(result, expected)

    def test_mixed_characters(self):
        """測試混合字元"""
        input_text = "aBc!@#"
        # 計算頻率並排序
        expected = self._calculate_expected(input_text)
        result = self._process_line(input_text)
        self.assertEqual(result, expected)

    def test_empty_line(self):
        """測試空行"""
        input_text = ""
        expected = []
        result = self._process_line(input_text)
        self.assertEqual(result, expected)

    def test_single_character(self):
        """測試單一字元"""
        input_text = "A"
        expected = ["65 1"]
        result = self._process_line(input_text)
        self.assertEqual(result, expected)

    def test_same_frequency_different_ascii(self):
        """測試相同頻率不同 ASCII 值"""
        input_text = "BA"
        # B=66, A=65，頻率都是1，應按 ASCII 降序：66 1, 65 1
        expected = ["66 1", "65 1"]
        result = self._process_line(input_text)
        self.assertEqual(result, expected)

    def _process_line(self, line):
        """處理單行輸入，返回結果列表"""
        if not line:
            return []

        # 計算頻率
        freq = Counter(line)

        # 按頻率升序，相同頻率按 ASCII 降序排序
        sorted_chars = sorted(freq.items(), key=lambda x: (x[1], -ord(x[0])))

        # 格式化輸出
        result = []
        for char, count in sorted_chars:
            ascii_val = ord(char)
            result.append(f"{ascii_val} {count}")

        return result

    def _calculate_expected(self, line):
        """計算預期輸出（用於測試）"""
        if not line:
            return []

        freq = Counter(line)
        sorted_chars = sorted(freq.items(), key=lambda x: (x[1], -ord(x[0])))
        return [f"{ord(char)} {count}" for char, count in sorted_chars]

if __name__ == '__main__':
    unittest.main()