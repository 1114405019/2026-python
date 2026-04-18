import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from models import Card, Deck


class TestCardAndDeck(unittest.TestCase):
    def test_card_power_order_two_vs_ace(self):
        two = Card(rank=15, suit=0)
        ace = Card(rank=14, suit=0)
        self.assertTrue(two > ace)
        self.assertGreater(two.power, ace.power)

    def test_card_power_order_spade_three_vs_club_three(self):
        spade_three = Card(rank=3, suit=3)
        club_three = Card(rank=3, suit=0)
        self.assertTrue(spade_three > club_three)
        self.assertGreater(spade_three.power, club_three.power)

    def test_card_equality_and_hash(self):
        card1 = Card(rank=14, suit=3)
        card2 = Card(rank=14, suit=3)
        self.assertEqual(card1, card2)
        self.assertEqual(hash(card1), hash(card2))

    def test_deck_shuffle_changes_order(self):
        deck = Deck()
        original = deck.cards.copy()
        deck.shuffle(seed=42)
        self.assertNotEqual(deck.cards, original)
        self.assertCountEqual(deck.cards, original)

    def test_deck_deal_four_players(self):
        deck = Deck()
        hands = deck.deal(num_players=4)
        self.assertEqual(len(hands), 4)
        self.assertEqual(len(hands[0]), 13)
        self.assertEqual(len(hands[1]), 13)
        self.assertEqual(len(hands[2]), 13)
        self.assertEqual(len(hands[3]), 13)
        all_cards = [card for hand in hands for card in hand]
        self.assertCountEqual(all_cards, deck.cards)

    def test_deck_deal_invalid_player_count(self):
        deck = Deck()
        with self.assertRaises(ValueError):
            deck.deal(0)


if __name__ == "__main__":
    unittest.main()
