from __future__ import annotations

from typing import List, Optional

try:
    from .evaluator import PatternEvaluator, PatternType
    from .models import Card
except ImportError:
    from evaluator import PatternEvaluator, PatternType
    from models import Card


class RuleEngine:
    def can_beat(
        self,
        last_play: Optional[List[Card]],
        current_play: List[Card],
        is_first_turn: bool = False,
    ) -> bool:
        if not current_play:
            return False

        current_result = PatternEvaluator.classify(current_play)
        if current_result is None:
            return False

        if is_first_turn and not any(card.is_three_of_clubs() for card in current_play):
            return False

        if last_play is None:
            return True

        last_result = PatternEvaluator.classify(last_play)
        if last_result is None:
            return False

        if len(last_play) != len(current_play):
            return False

        if len(current_play) == 5:
            if current_result.pattern_type != last_result.pattern_type:
                return current_result.pattern_type > last_result.pattern_type
            return current_result.strength > last_result.strength

        if current_result.pattern_type != last_result.pattern_type:
            return False

        return current_result.strength > last_result.strength

    def compare_plays(self, play_a: List[Card], play_b: List[Card]) -> int:
        result_a = PatternEvaluator.classify(play_a)
        result_b = PatternEvaluator.classify(play_b)

        if result_a is None or result_b is None:
            raise ValueError("Cannot compare invalid plays")

        if len(play_a) != len(play_b):
            raise ValueError("Cannot compare plays of different lengths")

        if result_a.pattern_type != result_b.pattern_type:
            if len(play_a) == 5:
                return 1 if result_a.pattern_type > result_b.pattern_type else -1
            raise ValueError("Cannot compare different pattern types for non-5-card plays")

        if result_a.strength != result_b.strength:
            return 1 if result_a.strength > result_b.strength else -1

        return 0
