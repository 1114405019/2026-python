import unittest
from game.models import Card, Hand
from game.ai import AIStrategy
from game.classifier import CardType


class TestAIScore(unittest.TestCase):
    """測試 AI 評分功能"""

    def test_score_single(self):
        """測試單張評分"""
        hand = Hand([Card(14, 3), Card(13, 2), Card(12, 1), Card(11, 0), Card(10, 3),
                     Card(9, 2), Card(8, 1), Card(7, 0), Card(6, 3), Card(5, 2),
                     Card(4, 1), Card(3, 0)])  # 12張牌，出1張剩11張
        play = [Card(14, 3)]  # ♠A
        score = AIStrategy.score_play(play, hand)
        # 牌型: SINGLE(1) * 100 = 100
        # 數字: 14 * 10 = 140
        # 黑桃: 1 * 5 = 5
        # 剩餘: 11張, +0
        expected = 100 + 140 + 5  # 245
        self.assertEqual(score, expected)

    def test_score_pair_higher(self):
        """測試對子比單張分數高"""
        hand = Hand([Card(14, 0), Card(14, 1), Card(13, 2)])  # A對子 + K
        single_play = [Card(13, 2)]  # 單K
        pair_play = [Card(14, 0), Card(14, 1)]  # 對A

        single_score = AIStrategy.score_play(single_play, hand)
        pair_score = AIStrategy.score_play(pair_play, hand)

        self.assertGreater(pair_score, single_score)

    def test_score_triple_higher(self):
        """測試三條比對子分數高"""
        hand = Hand([Card(14, 0), Card(14, 1), Card(14, 2), Card(13, 3)])  # 三A + ♠K
        pair_play = [Card(14, 0), Card(14, 1)]  # 對A
        triple_play = [Card(14, 0), Card(14, 1), Card(14, 2)]  # 三A

        pair_score = AIStrategy.score_play(pair_play, hand)
        triple_score = AIStrategy.score_play(triple_play, hand)

        self.assertGreater(triple_score, pair_score)

    def test_score_near_empty(self):
        """測試剩1張時的高分數"""
        hand = Hand([Card(14, 3), Card(13, 2)])  # ♠A, ♥K
        play = [Card(14, 3)]  # 出♠A，剩1張
        score = AIStrategy.score_play(play, hand)
        # 應該包含 EMPTY_HAND_BONUS
        self.assertGreater(score, AIStrategy.EMPTY_HAND_BONUS)

    def test_score_low_cards(self):
        """測試剩2-3張時的加分"""
        hand = Hand([Card(14, 3), Card(13, 2), Card(12, 1)])  # 三張牌
        play = [Card(14, 3)]  # 出♠A，剩2張
        score = AIStrategy.score_play(play, hand)
        # 應該包含 NEAR_EMPTY_BONUS
        self.assertGreater(score, AIStrategy.NEAR_EMPTY_BONUS)

    def test_score_spade_bonus(self):
        """測試黑桃加分"""
        hand = Hand([Card(14, 3), Card(14, 0)])  # ♠A, ♣A
        spade_play = [Card(14, 3)]  # ♠A
        club_play = [Card(14, 0)]  # ♣A

        spade_score = AIStrategy.score_play(spade_play, hand)
        club_score = AIStrategy.score_play(club_play, hand)

        # 黑桃應該多5分
        self.assertEqual(spade_score, club_score + AIStrategy.SPADE_BONUS)


class TestAISelect(unittest.TestCase):
    """測試 AI 選擇功能"""

    def test_select_best(self):
        """測試選擇最佳出牌"""
        hand = Hand([Card(14, 0), Card(14, 1), Card(13, 2)])  # A對子 + K
        valid_plays = [
            [Card(13, 2)],  # 單K
            [Card(14, 0), Card(14, 1)]  # 對A
        ]

        best_play = AIStrategy.select_best(valid_plays, hand)
        # 應該選擇對A（分數更高）
        self.assertEqual(len(best_play), 2)
        self.assertTrue(all(card.rank == 14 for card in best_play))

    def test_select_first_turn(self):
        """測試第一回合只能選3♣"""
        hand = Hand([Card(3, 0), Card(4, 1)])  # 有3♣
        valid_plays = [
            [Card(3, 0)],  # 3♣
            [Card(4, 1)]   # 4♦
        ]

        best_play = AIStrategy.select_best(valid_plays, hand, is_first=True)
        # 第一回合應該選擇3♣
        self.assertEqual(len(best_play), 1)
        self.assertEqual(best_play[0].rank, 3)
        self.assertEqual(best_play[0].suit, 0)

    def test_select_empty(self):
        """測試無合法出牌時返回None"""
        hand = Hand([Card(3, 0)])
        valid_plays = []

        best_play = AIStrategy.select_best(valid_plays, hand)
        self.assertIsNone(best_play)


if __name__ == '__main__':
    unittest.main()