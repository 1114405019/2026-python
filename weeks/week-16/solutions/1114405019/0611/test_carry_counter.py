"""進位計數 — 測試骨架

題目：count_carries(a, b) 回傳直式計算 a + b 時發生進位的次數。
      若 a 或 b 為負數，應 raise ValueError("operands must be non-negative")。

待辦：
  1. 自己打提示詞跟 AI 拆 test case，補齊至少 3 個
     - 至少 1 個 edge case（提示一個方向：進位會不會連鎖？）
     - 至少 1 個例外案例
  2. 跑 `python -m unittest` 確認全紅
  3. commit: "test: add failing tests for carry counter"
  4. 寫 carry_counter.py，全綠後 commit: "feat: implement carry counter"
  5. 寫 AI_LOG.md（提示詞逐字記錄）
"""

import unittest

from carry_counter import count_carries


class TestCountCarries(unittest.TestCase):
    def test_no_carry(self):
        # 123 + 456 = 579，每位相加都不進位
        self.assertEqual(count_carries(123, 456), 0)

    def test_all_carries(self):
        # 555 + 555：個位 10 進位、十位 11 進位、百位 11 進位 → 3
        self.assertEqual(count_carries(555, 555), 3)

    def test_single_carry(self):
        # 123 + 594：個位 3+4=7 不進；十位 2+9=11 進位；百位 1+5+1=7 不進 → 1
        self.assertEqual(count_carries(123, 594), 1)

    def test_chain_carry(self):
        # 999 + 1：個位 9+1=10 進位 → 十位 9+0+1=10 進位 → 百位 9+0+1=10 進位 → 3
        self.assertEqual(count_carries(999, 1), 3)

    def test_edge_zero(self):
        # 0 + 0 = 0，無進位
        self.assertEqual(count_carries(0, 0), 0)

    def test_edge_one_zero(self):
        # 任一為 0，不應有進位（除非另一個本身就需要進位，這裡用簡單值）
        self.assertEqual(count_carries(0, 999), 0)

    def test_invalid_negative_a(self):
        with self.assertRaises(ValueError) as ctx:
            count_carries(-1, 5)
        self.assertEqual(str(ctx.exception), "operands must be non-negative")

    def test_invalid_negative_b(self):
        with self.assertRaises(ValueError) as ctx:
            count_carries(5, -1)
        self.assertEqual(str(ctx.exception), "operands must be non-negative")

    def test_invalid_both_negative(self):
        with self.assertRaises(ValueError) as ctx:
            count_carries(-3, -7)
        self.assertEqual(str(ctx.exception), "operands must be non-negative")


if __name__ == "__main__":
    unittest.main()
