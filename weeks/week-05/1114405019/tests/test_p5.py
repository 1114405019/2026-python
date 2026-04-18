import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from manager import TurnManager
from models import Card
from rules import RuleEngine


class TestTurnManager(unittest.TestCase):
    def setUp(self) -> None:
        self.players = ["A", "B", "C", "D"]
        self.manager = TurnManager(self.players, RuleEngine())

    def test_pass_three_players_gives_free_play_to_last_winner(self):
        # Player A plays first and becomes last_player.
        self.manager.record_play(0, [Card(3, 0)])
        self.manager.current_player_index = 1

        self.manager.pass_turn()
        self.assertEqual(self.manager.current_player_index, 2)
        self.assertIsNotNone(self.manager.last_play)

        self.manager.pass_turn()
        self.assertEqual(self.manager.current_player_index, 3)
        self.assertIsNotNone(self.manager.last_play)

        self.manager.pass_turn()
        self.assertEqual(self.manager.current_player_index, 0)
        self.assertIsNone(self.manager.last_play)
        self.assertEqual(self.manager.pass_count, 0)
        self.assertFalse(any(self.manager.passed))
        self.assertTrue(self.manager.can_free_play())

    def test_next_turn_skips_passed_players(self):
        self.manager.passed = [False, True, False, True]
        self.manager.current_player_index = 0
        self.manager.next_turn()
        self.assertEqual(self.manager.current_player_index, 2)

    def test_reset_round_preserves_last_player(self):
        self.manager.record_play(2, [Card(4, 0)])
        self.manager.pass_count = 3
        self.manager.reset_round()
        self.assertEqual(self.manager.current_player_index, 2)
        self.assertIsNone(self.manager.last_play)
        self.assertEqual(self.manager.pass_count, 0)


if __name__ == "__main__":
    unittest.main()
