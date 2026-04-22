import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from main import BigTwoGame
from models import Card


class TestBigTwoGame(unittest.TestCase):
    def test_club_three_holder_is_starting_player(self):
        game = BigTwoGame(["Alice", "Bob", "Carol", "Dave"], seed=42)
        game.start_game()

        holders = [player.has_club_three() for player in game.players]
        self.assertEqual(sum(holders), 1)
        self.assertTrue(holders[game.turn_manager.get_current_player_index()])

    def test_start_game_deals_all_cards(self):
        game = BigTwoGame(["Alice", "Bob", "Carol", "Dave"], seed=42)
        game.start_game()

        total_cards = sum(len(player.hand) for player in game.players)
        self.assertEqual(total_cards, 52)
        self.assertTrue(all(len(player.hand) == 13 for player in game.players))

    def test_process_play_removes_cards_and_checks_winner(self):
        game = BigTwoGame(["Alice", "Bob", "Carol", "Dave"], seed=42)
        game.start_game()

        current_index = game.turn_manager.get_current_player_index()
        player = game.players[current_index]
        initial_hand_size = len(player.hand)
        card = player.hand[0]

        success = game.process_play([card])
        self.assertTrue(success)
        self.assertEqual(len(player.hand), initial_hand_size - 1)

        self.assertFalse(game.game_over)


if __name__ == "__main__":
    unittest.main()
