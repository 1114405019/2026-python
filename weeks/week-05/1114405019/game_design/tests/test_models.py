"""
Phase 1: 資料模型測試

測試 Card、Deck、Hand、Player 四個基礎類別
"""

import unittest
import sys
from pathlib import Path

# 加入父目錄到 sys.path，以便導入 game 模組
sys.path.insert(0, str(Path(__file__).parent.parent))

from game.models import Card, Deck, Hand, Player


class TestCard(unittest.TestCase):
    """測試 Card 類別"""
    
    def test_card_creation(self):
        """測試卡牌建立"""
        card = Card(rank=14, suit=3)
        self.assertEqual(card.rank, 14)
        self.assertEqual(card.suit, 3)
    
    def test_card_repr_ace_spade(self):
        """測試卡牌表示：♠A"""
        card = Card(14, 3)  # A of Spade
        self.assertEqual(repr(card), "♠A")
    
    def test_card_repr_three_club(self):
        """測試卡牌表示：♣3"""
        card = Card(3, 0)  # 3 of Club
        self.assertEqual(repr(card), "♣3")
    
    def test_card_repr_two_diamond(self):
        """測試卡牌表示：♦2"""
        card = Card(15, 1)  # 2 of Diamond
        self.assertEqual(repr(card), "♦2")
    
    def test_card_compare_suit_spade_vs_heart(self):
        """測試花色比較：♠ > ♥"""
        spade_a = Card(14, 3)
        heart_a = Card(14, 2)
        self.assertGreater(spade_a, heart_a)
    
    def test_card_compare_suit_heart_vs_diamond(self):
        """測試花色比較：♥ > ♦"""
        heart_a = Card(14, 2)
        diamond_a = Card(14, 1)
        self.assertGreater(heart_a, diamond_a)
    
    def test_card_compare_suit_diamond_vs_club(self):
        """測試花色比較：♦ > ♣"""
        diamond_a = Card(14, 1)
        club_a = Card(14, 0)
        self.assertGreater(diamond_a, club_a)
    
    def test_card_compare_rank_two_vs_ace(self):
        """測試數字比較：2 > A"""
        two = Card(15, 0)  # 2 of Club
        ace = Card(14, 3)  # A of Spade
        self.assertGreater(two, ace)
    
    def test_card_compare_rank_ace_vs_king(self):
        """測試數字比較：A > K"""
        ace = Card(14, 0)  # A of Club
        king = Card(13, 3)  # K of Spade
        self.assertGreater(ace, king)
    
    def test_card_compare_equal(self):
        """測試相等比較"""
        card1 = Card(14, 3)
        card2 = Card(14, 3)
        self.assertEqual(card1, card2)
        self.assertFalse(card1 < card2)
        self.assertFalse(card1 > card2)
    
    def test_card_to_sort_key(self):
        """測試排序鍵"""
        card = Card(14, 3)
        self.assertEqual(card.to_sort_key(), (14, 3))
    
    def test_card_hash(self):
        """測試雜湊值"""
        card1 = Card(14, 3)
        card2 = Card(14, 3)
        card3 = Card(13, 3)
        self.assertEqual(hash(card1), hash(card2))
        self.assertNotEqual(hash(card1), hash(card3))
    
    def test_card_in_set(self):
        """測試卡牌在集合中的行為"""
        card1 = Card(14, 3)
        card2 = Card(14, 3)
        card3 = Card(13, 3)
        card_set = {card1, card3}
        self.assertIn(card2, card_set)


class TestDeck(unittest.TestCase):
    """測試 Deck 類別"""
    
    def test_deck_has_52_cards(self):
        """測試牌堆有 52 張牌"""
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
    
    def test_deck_all_unique(self):
        """測試所有牌都是唯一的"""
        deck = Deck()
        self.assertEqual(len(set(deck.cards)), 52)
    
    def test_deck_all_ranks(self):
        """測試有所有 13 個數字"""
        deck = Deck()
        ranks = set(card.rank for card in deck.cards)
        expected_ranks = set(range(3, 16))  # 3-15
        self.assertEqual(ranks, expected_ranks)
    
    def test_deck_all_suits(self):
        """測試有所有 4 個花色"""
        deck = Deck()
        suits = set(card.suit for card in deck.cards)
        expected_suits = {0, 1, 2, 3}
        self.assertEqual(suits, expected_suits)
    
    def test_deck_shuffle(self):
        """測試洗牌（牌序改變）"""
        deck1 = Deck()
        original_cards = deck1.cards.copy()
        
        # 洗牌後應該和原來不同
        # 注意：理論上有極小概率洗牌後順序和原來一樣
        # 但 52 張牌的情況下這個概率非常小
        deck1.shuffle()
        
        # 至少有大部分牌的位置改變了
        different_count = sum(1 for a, b in zip(original_cards, deck1.cards) if a != b)
        self.assertGreater(different_count, 40)  # 至少 40 張牌位置改變
    
    def test_deal_5_cards(self):
        """測試發 5 張牌"""
        deck = Deck()
        dealt = deck.deal(5)
        self.assertEqual(len(dealt), 5)
        self.assertEqual(len(deck.cards), 47)
    
    def test_deal_multiple_times(self):
        """測試多次發牌"""
        deck = Deck()
        dealt1 = deck.deal(5)
        dealt2 = deck.deal(3)
        self.assertEqual(len(dealt1), 5)
        self.assertEqual(len(dealt2), 3)
        self.assertEqual(len(deck.cards), 44)
    
    def test_deal_exceed(self):
        """測試發超過牌堆的牌數"""
        deck = Deck()
        dealt = deck.deal(60)
        self.assertEqual(len(dealt), 52)
        self.assertEqual(len(deck.cards), 0)
    
    def test_deal_empty_deck(self):
        """測試從空牌堆發牌"""
        deck = Deck()
        deck.deal(52)
        dealt = deck.deal(5)
        self.assertEqual(len(dealt), 0)


class TestHand(unittest.TestCase):
    """測試 Hand 類別"""
    
    def test_hand_creation_empty(self):
        """測試建立空手牌"""
        hand = Hand()
        self.assertEqual(len(hand), 0)
    
    def test_hand_creation_with_cards(self):
        """測試用卡牌初始化手牌"""
        cards = [Card(14, 3), Card(13, 3), Card(3, 0)]
        hand = Hand(cards)
        self.assertEqual(len(hand), 3)
    
    def test_hand_sort_desc(self):
        """測試排序（倒序）"""
        # 建立未排序的手牌
        cards = [Card(3, 0), Card(14, 3), Card(3, 3), Card(13, 2)]
        hand = Hand(cards)
        
        # 排序
        hand.sort_desc()
        
        # 驗證順序：♠A > ♥K > ♠3 > ♣3
        self.assertEqual(repr(hand[0]), "♠A")
        self.assertEqual(repr(hand[1]), "♥K")
        self.assertEqual(repr(hand[2]), "♠3")
        self.assertEqual(repr(hand[3]), "♣3")
    
    def test_hand_find_3_clubs(self):
        """測試找 3♣"""
        cards = [Card(14, 3), Card(3, 0), Card(13, 3)]
        hand = Hand(cards)
        three_clubs = hand.find_3_clubs()
        self.assertIsNotNone(three_clubs)
        self.assertEqual(three_clubs.rank, 3)
        self.assertEqual(three_clubs.suit, 0)
    
    def test_hand_find_3_clubs_not_found(self):
        """測試找不到 3♣"""
        cards = [Card(14, 3), Card(3, 1), Card(13, 3)]  # 3♦ instead
        hand = Hand(cards)
        three_clubs = hand.find_3_clubs()
        self.assertIsNone(three_clubs)
    
    def test_hand_remove(self):
        """測試移除牌"""
        cards = [Card(14, 3), Card(13, 2), Card(3, 0)]
        hand = Hand(cards)
        
        to_remove = [Card(14, 3), Card(3, 0)]
        hand.remove(to_remove)
        
        self.assertEqual(len(hand), 1)
        self.assertEqual(hand[0].rank, 13)
    
    def test_hand_remove_not_found(self):
        """測試移除不存在的牌"""
        cards = [Card(14, 3), Card(13, 2)]
        hand = Hand(cards)
        
        to_remove = [Card(3, 0)]  # 不存在
        hand.remove(to_remove)
        
        # 手牌數量不變
        self.assertEqual(len(hand), 2)
    
    def test_hand_remove_partial(self):
        """測試部分移除"""
        cards = [Card(14, 3), Card(13, 2), Card(3, 0)]
        hand = Hand(cards)
        
        to_remove = [Card(14, 3), Card(5, 0)]  # 5♣ 不存在
        hand.remove(to_remove)
        
        # 只移除存在的牌
        self.assertEqual(len(hand), 2)
        self.assertNotIn(Card(14, 3), hand)
    
    def test_hand_iteration(self):
        """測試遍歷手牌"""
        cards = [Card(14, 3), Card(13, 2)]
        hand = Hand(cards)
        
        collected = [card for card in hand]
        self.assertEqual(len(collected), 2)


class TestPlayer(unittest.TestCase):
    """測試 Player 類別"""
    
    def test_player_human_creation(self):
        """測試建立人類玩家"""
        player = Player("Alice", is_ai=False)
        self.assertEqual(player.name, "Alice")
        self.assertFalse(player.is_ai)
        self.assertEqual(len(player.hand), 0)
        self.assertEqual(player.score, 0)
    
    def test_player_ai_creation(self):
        """測試建立 AI 玩家"""
        player = Player("AI_1", is_ai=True)
        self.assertEqual(player.name, "AI_1")
        self.assertTrue(player.is_ai)
        self.assertEqual(len(player.hand), 0)
    
    def test_player_take_cards(self):
        """測試拿牌"""
        player = Player("Alice")
        cards = [Card(14, 3), Card(13, 2), Card(3, 0)]
        
        player.take_cards(cards)
        
        self.assertEqual(len(player.hand), 3)
    
    def test_player_take_multiple_times(self):
        """測試多次拿牌"""
        player = Player("Alice")
        cards1 = [Card(14, 3), Card(13, 2)]
        cards2 = [Card(3, 0)]
        
        player.take_cards(cards1)
        player.take_cards(cards2)
        
        self.assertEqual(len(player.hand), 3)
    
    def test_player_play_cards(self):
        """測試出牌"""
        player = Player("Alice")
        cards = [Card(14, 3), Card(13, 2), Card(3, 0)]
        player.take_cards(cards)
        
        to_play = [Card(14, 3), Card(3, 0)]
        played = player.play_cards(to_play)
        
        self.assertEqual(len(played), 2)
        self.assertEqual(len(player.hand), 1)
        self.assertIn(Card(13, 2), player.hand)
    
    def test_player_play_cards_return_value(self):
        """測試出牌的回傳值"""
        player = Player("Alice")
        cards = [Card(14, 3), Card(13, 2)]
        player.take_cards(cards)
        
        to_play = [Card(14, 3)]
        returned = player.play_cards(to_play)
        
        self.assertEqual(len(returned), 1)
        self.assertEqual(returned[0].rank, 14)
        self.assertEqual(returned[0].suit, 3)


class TestIntegration(unittest.TestCase):
    """整合測試：多個類別的協作"""
    
    def test_game_setup_basic(self):
        """測試基本遊戲設置"""
        # 建立牌堆和玩家
        deck = Deck()
        player1 = Player("Player 1", is_ai=False)
        player2 = Player("Player 2", is_ai=True)
        
        # 發牌
        deck.shuffle()
        cards1 = deck.deal(13)
        cards2 = deck.deal(13)
        
        player1.take_cards(cards1)
        player2.take_cards(cards2)
        
        # 驗證
        self.assertEqual(len(player1.hand), 13)
        self.assertEqual(len(player2.hand), 13)
        self.assertEqual(len(deck.cards), 26)
    
    def test_find_3_clubs_in_hand(self):
        """測試在牌堆中找 3♣"""
        deck = Deck()
        all_cards = deck.cards
        
        # 找 3♣
        three_clubs = None
        for card in all_cards:
            if card.rank == 3 and card.suit == 0:
                three_clubs = card
                break
        
        self.assertIsNotNone(three_clubs)
        
        # 發牌給玩家，檢查是否有 3♣
        deck.shuffle()
        cards = deck.deal(13)
        hand = Hand(cards)
        
        found = hand.find_3_clubs()
        
        # 注意：不一定找得到，因為 52 張牌中 3♣ 只有 1 張
        # 但如果在發的 13 張牌中，應該能找到
        if Card(3, 0) in hand:
            self.assertIsNotNone(found)


if __name__ == '__main__':
    unittest.main()
