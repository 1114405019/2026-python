# 測試題目 118: UVA 118 - 機器人移動
# 測試機器人移動邏輯，包括轉向、前進、邊界和 scent。

import unittest
from question_118 import simulate_robot

class TestQuestion118(unittest.TestCase):
    
    def test_basic_movement(self):
        """測試基本移動"""
        scents = set()
        x, y, d, lost = simulate_robot(1, 1, 'N', 'F', 5, 5, scents)
        self.assertEqual((x, y, d, lost), (1, 2, 'N', False))
    
    def test_turning(self):
        """測試轉向"""
        scents = set()
        x, y, d, lost = simulate_robot(1, 1, 'N', 'L', 5, 5, scents)
        self.assertEqual((x, y, d, lost), (1, 1, 'W', False))
        x, y, d, lost = simulate_robot(1, 1, 'N', 'R', 5, 5, scents)
        self.assertEqual((x, y, d, lost), (1, 1, 'E', False))
    
    def test_lost(self):
        """測試掉落"""
        scents = set()
        x, y, d, lost = simulate_robot(0, 0, 'S', 'F', 5, 5, scents)
        self.assertEqual((x, y, d, lost), (0, 0, 'S', True))
        self.assertIn((0, 0), scents)
    
    def test_scent_prevents_lost(self):
        """測試 scent 防止掉落"""
        scents = {(0, 0)}
        x, y, d, lost = simulate_robot(0, 0, 'S', 'F', 5, 5, scents)
        self.assertEqual((x, y, d, lost), (0, 0, 'S', False))  # 忽略指令
    
    def test_multiple_commands(self):
        """測試多個指令"""
        scents = set()
        x, y, d, lost = simulate_robot(1, 1, 'N', 'FRFL', 5, 5, scents)
        # F: (1,2,N), R: (1,2,E), F: (2,2,E), L: (2,2,N)
        self.assertEqual((x, y, d, lost), (2, 2, 'N', False))

if __name__ == '__main__':
    unittest.main()