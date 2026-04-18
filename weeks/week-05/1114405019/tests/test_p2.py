import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from models import Card
from player import Player


class TestPlayer(unittest.TestCase):
    def test_add_cards_and_has_club_three(self):
        player = Player("Alice")
        cards = [Card(3, 0), Card(14, 3)]
        player.add_cards(cards)
        self.assertTrue(player.has_club_three())
        self.assertIn(Card(14, 3), player.hand)

    def test_sort_hand_orders_cards_by_power(self):
        player = Player("Bob")
        unsorted = [Card(15, 0), Card(3, 3), Card(14, 2), Card(3, 0)]
        player.add_cards(unsorted)

        player.sort_hand()

        expected = [Card(3, 0), Card(3, 3), Card(14, 2), Card(15, 0)]
        self.assertEqual(player.hand, expected)
        self.assertEqual(player.hand[0], Card(3, 0))
        self.assertEqual(player.hand[-1], Card(15, 0))

    def test_play_cards_removes_cards_from_hand(self):
        player = Player("Carol")
        hand = [Card(3, 0), Card(4, 0), Card(15, 3)]
        player.add_cards(hand)

        played = player.play_cards([Card(4, 0), Card(15, 3)])
        self.assertEqual(played, [Card(4, 0), Card(15, 3)])
        self.assertEqual(player.hand, [Card(3, 0)])

    def test_play_cards_missing_raises(self):
        player = Player("Dave")
        player.add_cards([Card(3, 0)])
        with self.assertRaises(ValueError):
            player.play_cards([Card(4, 0)])

    def test_sort_hand_club_three_first_spade_two_last(self):
        player = Player("Eve")
        player.add_cards([Card(14, 1), Card(15, 3), Card(3, 0), Card(4, 2)])
        player.sort_hand()

        self.assertEqual(player.hand[0], Card(3, 0))
        self.assertEqual(player.hand[-1], Card(15, 3))


if __name__ == "__main__":
    unittest.main()
