"""
Phase 2: 牌型分類測試

測試 HandClassifier 類別的分類、比較、合法性檢查功能
"""

import unittest
import sys
from pathlib import Path

# 加入父目錄到 sys.path，以便導入 game 模組
sys.path.insert(0, str(Path(__file__).parent.parent))

from game.models import Card
from game.classifier import CardType, HandClassifier


class TestCardType(unittest.TestCase):
    """測試 CardType 列舉"""
    
    def test_cardtype_values(self):
        """測試各牌型列舉值"""
        self.assertEqual(CardType.SINGLE, 1)
        self.assertEqual(CardType.PAIR, 2)
        self.assertEqual(CardType.TRIPLE, 3)
        self.assertEqual(CardType.STRAIGHT, 4)
        self.assertEqual(CardType.FLUSH, 5)
        self.assertEqual(CardType.FULL_HOUSE, 6)
        self.assertEqual(CardType.FOUR_OF_A_KIND, 7)
        self.assertEqual(CardType.STRAIGHT_FLUSH, 8)


class TestClassifySingle(unittest.TestCase):
    """測試單張分類"""
    
    def test_classify_single_ace(self):
        """測試單張 A"""
        cards = [Card(14, 3)]  # ♠A
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.SINGLE, 14, 3))
    
    def test_classify_single_two(self):
        """測試單張 2"""
        cards = [Card(15, 0)]  # 2♣
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.SINGLE, 15, 0))
    
    def test_classify_single_three(self):
        """測試單張 3"""
        cards = [Card(3, 0)]  # ♣3
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.SINGLE, 3, 0))


class TestClassifyPair(unittest.TestCase):
    """測試對子分類"""
    
    def test_classify_pair(self):
        """測試對子 A"""
        cards = [Card(14, 3), Card(14, 2)]  # ♠A, ♥A
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.PAIR, 14, 3))  # ♠A 花色較大
    
    def test_classify_pair_diff_rank(self):
        """測試不同 rank 的兩張牌"""
        cards = [Card(14, 3), Card(13, 3)]  # ♠A, ♠K
        result = HandClassifier.classify(cards)
        self.assertIsNone(result)
    
    def test_classify_pair_from_three(self):
        """測試從三張牌中取兩張（但分類時只看兩張）"""
        cards = [Card(14, 3), Card(14, 2), Card(14, 1)]  # 三張 A
        # 注意：這裡測試的是兩張牌的情況
        pair_cards = cards[:2]
        result = HandClassifier.classify(pair_cards)
        self.assertEqual(result, (CardType.PAIR, 14, 3))


class TestClassifyTriple(unittest.TestCase):
    """測試三條分類"""
    
    def test_classify_triple(self):
        """測試三條 A"""
        cards = [Card(14, 3), Card(14, 2), Card(14, 1)]  # ♠A, ♥A, ♦A
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.TRIPLE, 14, 3))
    
    def test_classify_triple_not_enough(self):
        """測試三張牌但無法形成三條"""
        cards = [Card(14, 3), Card(14, 2), Card(13, 1)]  # 兩張A和一張K
        result = HandClassifier.classify(cards)
        self.assertIsNone(result)


class TestClassifyFiveCards(unittest.TestCase):
    """測試五張牌型分類"""
    
    def test_classify_straight(self):
        """測試順子"""
        cards = [
            Card(3, 0), Card(4, 1), Card(5, 2),  # ♣3, ♦4, ♥5
            Card(6, 3), Card(7, 3)               # ♠6, ♠7
        ]
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.STRAIGHT, 7, 3))  # 最大牌 ♠7
    
    def test_classify_straight_ace_low(self):
        """測試 A-2-3-4-5 順子"""
        cards = [
            Card(14, 0), Card(15, 1), Card(3, 2),  # A♣, 2♦, 3♥
            Card(4, 3), Card(5, 3)                 # 4♠, 5♠
        ]
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.STRAIGHT, 5, 3))  # 最大牌 5♠
    
    def test_classify_flush(self):
        """測試同花"""
        cards = [
            Card(3, 0), Card(5, 0), Card(7, 0),  # ♣3, ♣5, ♣7
            Card(9, 0), Card(11, 0)              # ♣9, ♣J
        ]
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.FLUSH, 11, 0))  # 最大牌 ♣J
    
    def test_classify_full_house(self):
        """測試葫蘆"""
        cards = [
            Card(14, 3), Card(14, 2), Card(14, 1),  # 三張 A
            Card(4, 0), Card(4, 1)                  # 兩張 4
        ]
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.FULL_HOUSE, 14, 0))  # 用三條的 rank
    
    def test_classify_four_of_a_kind(self):
        """測試四條"""
        cards = [
            Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0),  # 四張 A
            Card(5, 1)                                           # 單張 ♦5
        ]
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.FOUR_OF_A_KIND, 14, 1))  # 四條 A，單張 ♦5
    
    def test_classify_straight_flush(self):
        """測試同花順"""
        cards = [
            Card(3, 0), Card(4, 0), Card(5, 0),  # ♣3, ♣4, ♣5
            Card(6, 0), Card(7, 0)               # ♣6, ♣7
        ]
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.STRAIGHT_FLUSH, 7, 0))  # 最大牌 ♣7


class TestCompare(unittest.TestCase):
    """測試牌型比較"""
    
    def test_compare_single_rank(self):
        """測試單張比較：A > K"""
        play1 = [Card(14, 3)]  # ♠A
        play2 = [Card(13, 3)]  # ♠K
        result = HandClassifier.compare(play1, play2)
        self.assertEqual(result, 1)
    
    def test_compare_single_suit(self):
        """測試單張比較：♠A > ♥A"""
        play1 = [Card(14, 3)]  # ♠A
        play2 = [Card(14, 2)]  # ♥A
        result = HandClassifier.compare(play1, play2)
        self.assertEqual(result, 1)
    
    def test_compare_pair_rank(self):
        """測試對子比較：對A > 對K"""
        play1 = [Card(14, 3), Card(14, 2)]  # 對A
        play2 = [Card(13, 3), Card(13, 2)]  # 對K
        result = HandClassifier.compare(play1, play2)
        self.assertEqual(result, 1)
    
    def test_compare_pair_suit(self):
        """測試對子比較：♠♥A > ♦♣A"""
        play1 = [Card(14, 3), Card(14, 2)]  # ♠♥A
        play2 = [Card(14, 1), Card(14, 0)]  # ♦♣A
        result = HandClassifier.compare(play1, play2)
        self.assertEqual(result, 1)
    
    def test_compare_different_type(self):
        """測試不同牌型比較：對子 > 單張"""
        play1 = [Card(14, 3), Card(14, 2)]  # 對A
        play2 = [Card(15, 3)]               # 單張2
        result = HandClassifier.compare(play1, play2)
        self.assertEqual(result, 1)
    
    def test_compare_flush_vs_straight(self):
        """測試同花 vs 順子：同花 > 順子"""
        flush = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]  # 同花
        straight = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]  # 順子
        result = HandClassifier.compare(flush, straight)
        self.assertEqual(result, 1)


class TestCanPlay(unittest.TestCase):
    """測試出牌合法性檢查"""
    
    def test_can_play_first_3clubs(self):
        """測試第一回合出 3♣"""
        cards = [Card(3, 0)]  # ♣3
        result = HandClassifier.can_play(None, cards)
        self.assertTrue(result)
    
    def test_can_play_first_not_3clubs(self):
        """測試第一回合不出 3♣"""
        cards = [Card(14, 3)]  # ♠A
        result = HandClassifier.can_play(None, cards)
        self.assertFalse(result)
    
    def test_can_play_same_type(self):
        """測試相同牌型：對6 > 對5"""
        last_play = [Card(5, 3), Card(5, 2)]  # 對5
        cards = [Card(6, 3), Card(6, 2)]     # 對6
        result = HandClassifier.can_play(last_play, cards)
        self.assertTrue(result)
    
    def test_can_play_diff_type(self):
        """測試不同牌型：對5 vs 單張6"""
        last_play = [Card(5, 3), Card(5, 2)]  # 對5
        cards = [Card(6, 3)]                  # 單張6
        result = HandClassifier.can_play(last_play, cards)
        self.assertFalse(result)
    
    def test_can_play_not_stronger(self):
        """測試不出更大的牌：對10 vs 對5"""
        last_play = [Card(5, 3), Card(5, 2)]  # 對5
        cards = [Card(10, 3), Card(10, 2)]    # 對10
        result = HandClassifier.can_play(last_play, cards)
        self.assertTrue(result)  # 對10 > 對5
    
    def test_can_play_weaker(self):
        """測試出更小的牌：對4 vs 對5"""
        last_play = [Card(5, 3), Card(5, 2)]  # 對5
        cards = [Card(4, 3), Card(4, 2)]      # 對4
        result = HandClassifier.can_play(last_play, cards)
        self.assertFalse(result)  # 對4 < 對5


class TestEdgeCases(unittest.TestCase):
    """測試邊界情況"""
    
    def test_empty_cards(self):
        """測試空牌列表"""
        result = HandClassifier.classify([])
        self.assertIsNone(result)
    
    def test_classify_invalid_combo(self):
        """測試無效的牌組合（6張牌）"""
        cards = [
            Card(14, 3), Card(13, 2), Card(12, 1),  # A, K, Q
            Card(11, 0), Card(10, 3), Card(9, 2)    # J, T, 9
        ]
        result = HandClassifier.classify(cards)
        self.assertIsNone(result)
    
    def test_cant_form_pair(self):
        """測試無法形成對子的兩張牌"""
        cards = [Card(14, 3), Card(13, 2)]  # ♠A, ♥K
        result = HandClassifier.classify(cards)
        self.assertIsNone(result)
    
    def test_five_cards_none(self):
        """測試無法形成任何五張牌型的組合"""
        cards = [
            Card(14, 3), Card(13, 2), Card(12, 1),  # A, K, Q
            Card(10, 0), Card(8, 3)                 # T, 8
        ]
        result = HandClassifier.classify(cards)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()