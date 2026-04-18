import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from models import Card
from rules import RuleEngine


class TestRuleEngine(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = RuleEngine()

    def test_spade_two_beats_club_two(self):
        last_play = [Card(15, 0)]
        current_play = [Card(15, 3)]
        self.assertTrue(self.engine.can_beat(last_play, current_play))

    def test_pair_three_cannot_beat_pair_four(self):
        last_play = [Card(4, 0), Card(4, 1)]
        current_play = [Card(3, 0), Card(3, 1)]
        self.assertFalse(self.engine.can_beat(last_play, current_play))

    def test_pair_four_beats_pair_three(self):
        last_play = [Card(3, 0), Card(3, 1)]
        current_play = [Card(4, 0), Card(4, 1)]
        self.assertTrue(self.engine.can_beat(last_play, current_play))

    def test_first_turn_requires_club_three(self):
        current_play = [Card(14, 3)]
        last_play = None
        self.assertFalse(self.engine.can_beat(last_play, current_play, is_first_turn=True))
        current_play = [Card(3, 0)]
        self.assertTrue(self.engine.can_beat(last_play, current_play, is_first_turn=True))

    def test_same_pair_different_suit(self):
        last_play = [Card(7, 0), Card(7, 1)]
        current_play = [Card(7, 2), Card(7, 3)]
        self.assertTrue(self.engine.can_beat(last_play, current_play))


if __name__ == "__main__":
    unittest.main()
