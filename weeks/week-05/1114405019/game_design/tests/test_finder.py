import unittest
from game.models import Card, Hand
from game.finder import HandFinder
from game.classifier import HandClassifier, CardType


class TestFindSingles(unittest.TestCase):
    """測試單張搜尋"""

    def test_find_singles_normal(self):
        """測試正常手牌的單張搜尋"""
        hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2)])
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 3)
        # 檢查每組都是單張
        for single in singles:
            self.assertEqual(len(single), 1)

    def test_find_singles_empty(self):
        """測試空手牌"""
        hand = Hand([])
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 0)


class TestFindPairs(unittest.TestCase):
    """測試對子搜尋"""

    def test_find_pairs_normal(self):
        """測試正常對子搜尋"""
        hand = Hand([Card(3, 0), Card(3, 1), Card(4, 2), Card(4, 3), Card(5, 0)])
        pairs = HandFinder.find_pairs(hand)
        # 應該有 2 個對子（3有1種組合，4有1種組合，5沒有）
        self.assertEqual(len(pairs), 2)  # C(2,2)=1 for 3, C(2,2)=1 for 4

    def test_find_pairs_four_cards(self):
        """測試4張相同rank的牌"""
        hand = Hand([Card(3, 0), Card(3, 1), Card(3, 2), Card(3, 3)])
        pairs = HandFinder.find_pairs(hand)
        # C(4,2) = 6
        self.assertEqual(len(pairs), 6)

    def test_find_pairs_no_pairs(self):
        """測試沒有對子的手牌"""
        hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 0)


class TestFindTriples(unittest.TestCase):
    """測試三條搜尋"""

    def test_find_triples_normal(self):
        """測試正常三條搜尋"""
        hand = Hand([Card(3, 0), Card(3, 1), Card(3, 2), Card(4, 0), Card(4, 1)])
        triples = HandFinder.find_triples(hand)
        # 只有3有三條
        self.assertEqual(len(triples), 1)
        self.assertEqual(len(triples[0]), 3)
        self.assertTrue(all(card.rank == 3 for card in triples[0]))

    def test_find_triples_four_cards(self):
        """測試4張相同rank的牌"""
        hand = Hand([Card(3, 0), Card(3, 1), Card(3, 2), Card(3, 3)])
        triples = HandFinder.find_triples(hand)
        # C(4,3) = 4
        self.assertEqual(len(triples), 4)

    def test_find_triples_no_triples(self):
        """測試沒有三條的手牌"""
        hand = Hand([Card(3, 0), Card(3, 1), Card(4, 2), Card(5, 0)])
        triples = HandFinder.find_triples(hand)
        self.assertEqual(len(triples), 0)


class TestFindFives(unittest.TestCase):
    """測試五張牌型搜尋"""

    def test_find_straight(self):
        """測試順子搜尋"""
        hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0), Card(8, 1)])
        fives = HandFinder.find_fives(hand)
        # 應該至少有一個順子
        self.assertTrue(len(fives) > 0)
        # 檢查是否有順子
        has_straight = any(HandClassifier.classify(cards)[0] == CardType.STRAIGHT for cards in fives)
        self.assertTrue(has_straight)

    def test_find_flush(self):
        """測試同花搜尋"""
        hand = Hand([Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0), Card(14, 1)])
        fives = HandFinder.find_fives(hand)
        # 應該至少有一個同花
        self.assertTrue(len(fives) > 0)
        has_flush = any(HandClassifier.classify(cards)[0] == CardType.FLUSH for cards in fives)
        self.assertTrue(has_flush)

    def test_find_full_house(self):
        """測試葫蘆搜尋"""
        hand = Hand([Card(14, 0), Card(14, 1), Card(14, 2), Card(3, 0), Card(3, 1), Card(13, 2)])
        fives = HandFinder.find_fives(hand)
        # 應該至少有一個葫蘆
        self.assertTrue(len(fives) > 0)
        has_full_house = any(HandClassifier.classify(cards)[0] == CardType.FULL_HOUSE for cards in fives)
        self.assertTrue(has_full_house)

    def test_find_four_of_a_kind(self):
        """測試四條搜尋"""
        hand = Hand([Card(14, 0), Card(14, 1), Card(14, 2), Card(14, 3), Card(3, 0)])
        fives = HandFinder.find_fives(hand)
        # 應該至少有一個四條
        self.assertTrue(len(fives) > 0)
        has_four = any(HandClassifier.classify(cards)[0] == CardType.FOUR_OF_A_KIND for cards in fives)
        self.assertTrue(has_four)

    def test_find_straight_flush(self):
        """測試同花順搜尋"""
        hand = Hand([Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0), Card(14, 1)])
        fives = HandFinder.find_fives(hand)
        # 應該至少有一個同花順
        self.assertTrue(len(fives) > 0)
        has_straight_flush = any(HandClassifier.classify(cards)[0] == CardType.STRAIGHT_FLUSH for cards in fives)
        self.assertTrue(has_straight_flush)


class TestValidPlays(unittest.TestCase):
    """測試合法出牌搜尋"""

    def test_valid_plays_first_turn(self):
        """測試第一回合只能出3♣"""
        hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2)])  # 有3♣
        valid_plays = HandFinder.get_all_valid_plays(hand, None)
        self.assertEqual(len(valid_plays), 1)
        self.assertEqual(len(valid_plays[0]), 1)
        self.assertEqual(valid_plays[0][0].rank, 3)
        self.assertEqual(valid_plays[0][0].suit, 0)

    def test_valid_plays_first_turn_no_three_clubs(self):
        """測試第一回合沒有3♣"""
        hand = Hand([Card(3, 1), Card(4, 1), Card(5, 2)])  # 沒有3♣
        valid_plays = HandFinder.get_all_valid_plays(hand, None)
        self.assertEqual(len(valid_plays), 0)

    def test_valid_plays_after_single(self):
        """測試上家出單張後的合法出牌"""
        hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)])
        last_play = [Card(4, 0)]  # 上家出單4
        valid_plays = HandFinder.get_all_valid_plays(hand, last_play)

        # 應該包含比上家大的單張
        single_plays = [play for play in valid_plays if len(play) == 1]
        self.assertTrue(len(single_plays) > 0)
        # 檢查所有單張都比上家牌大
        for play in single_plays:
            self.assertTrue(HandClassifier.compare(play, last_play) == 1)

    def test_valid_plays_after_pair(self):
        """測試上家出對子後的合法出牌"""
        hand = Hand([Card(5, 0), Card(5, 1), Card(6, 0), Card(6, 1), Card(7, 2)])
        last_play = [Card(5, 2), Card(5, 3)]  # 上家出對5
        valid_plays = HandFinder.get_all_valid_plays(hand, last_play)

        # 應該只包含對子和更大的牌型
        pair_plays = [play for play in valid_plays if len(play) == 2]
        self.assertTrue(len(pair_plays) > 0)
        # 檢查對子都比對5大
        for play in pair_plays:
            self.assertTrue(HandClassifier.compare(play, last_play))

    def test_no_valid_plays(self):
        """測試沒有合法出牌的情況"""
        hand = Hand([Card(3, 0), Card(4, 1)])  # 只有小牌
        last_play = [Card(14, 0)]  # 上家出A
        valid_plays = HandFinder.get_all_valid_plays(hand, last_play)
        self.assertEqual(len(valid_plays), 0)


if __name__ == '__main__':
    unittest.main()