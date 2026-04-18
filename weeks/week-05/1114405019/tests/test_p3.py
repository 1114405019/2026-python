import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from evaluator import PatternEvaluator, PatternType
from models import Card


class TestPatternEvaluator(unittest.TestCase):
    def test_straight_flush_club_3_to_7(self):
        cards = [Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)]
        result = PatternEvaluator.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result.pattern_type, PatternType.STRAIGHT_FLUSH)

    def test_pair_detection(self):
        cards = [Card(14, 0), Card(14, 3)]
        result = PatternEvaluator.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result.pattern_type, PatternType.PAIR)

    def test_full_house_detection(self):
        cards = [Card(14, 0), Card(14, 1), Card(14, 2), Card(15, 0), Card(15, 1)]
        result = PatternEvaluator.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result.pattern_type, PatternType.FULL_HOUSE)

    def test_four_of_a_kind_detection(self):
        cards = [Card(7, 0), Card(7, 1), Card(7, 2), Card(7, 3), Card(3, 0)]
        result = PatternEvaluator.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result.pattern_type, PatternType.FOUR_OF_A_KIND)

    def test_straight_detection(self):
        cards = [Card(10, 0), Card(11, 1), Card(12, 2), Card(13, 3), Card(14, 0)]
        result = PatternEvaluator.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result.pattern_type, PatternType.STRAIGHT)

    def test_straight_flush_signature(self):
        cards = [Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)]
        signature = PatternEvaluator.get_pattern_signature(cards)
        self.assertIsNotNone(signature)
        self.assertEqual(signature[0], PatternType.STRAIGHT_FLUSH)

    def test_invalid_non_pair(self):
        cards = [Card(3, 0), Card(4, 0)]
        self.assertIsNone(PatternEvaluator.classify(cards))


if __name__ == "__main__":
    unittest.main()
