from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum
from typing import List, Optional, Tuple

try:
    from .models import Card
except ImportError:
    from models import Card


class PatternType(IntEnum):
    SINGLE = 1
    PAIR = 2
    STRAIGHT = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    STRAIGHT_FLUSH = 6


@dataclass(frozen=True)
class PatternResult:
    pattern_type: PatternType
    primary_rank: int
    strength: int
    cards: Tuple[Card, ...]

    def signature(self) -> Tuple[int, int]:
        return (self.pattern_type, self.strength)


class PatternEvaluator:
    @staticmethod
    def classify(cards: List[Card]) -> Optional[PatternResult]:
        if not cards:
            return None

        cards = list(cards)
        if len(cards) == 1:
            card = cards[0]
            return PatternResult(PatternType.SINGLE, card.rank, card.power, (card,))

        if len(cards) == 2 and PatternEvaluator.is_pair(cards):
            strength = max(card.power for card in cards)
            return PatternResult(PatternType.PAIR, cards[0].rank, strength, tuple(cards))

        if len(cards) == 5:
            if PatternEvaluator.is_straight_flush(cards):
                strength = PatternEvaluator._straight_strength(cards)
                return PatternResult(PatternType.STRAIGHT_FLUSH, strength, strength, tuple(cards))
            if PatternEvaluator.is_four_of_a_kind(cards):
                quad_rank, _ = PatternEvaluator._find_n_of_a_kind(cards, 4)
                strength = PatternEvaluator._highest_power_of_rank(cards, quad_rank)
                return PatternResult(PatternType.FOUR_OF_A_KIND, quad_rank, strength, tuple(cards))
            if PatternEvaluator.is_full_house(cards):
                triple_rank, _ = PatternEvaluator._find_n_of_a_kind(cards, 3)
                strength = PatternEvaluator._highest_power_of_rank(cards, triple_rank)
                return PatternResult(PatternType.FULL_HOUSE, triple_rank, strength, tuple(cards))
            if PatternEvaluator.is_straight(cards):
                strength = PatternEvaluator._straight_strength(cards)
                return PatternResult(PatternType.STRAIGHT, strength, strength, tuple(cards))

        return None

    @staticmethod
    def is_valid_pattern(cards: List[Card]) -> bool:
        return PatternEvaluator.classify(cards) is not None

    @staticmethod
    def is_pair(cards: List[Card]) -> bool:
        return len(cards) == 2 and cards[0].rank == cards[1].rank

    @staticmethod
    def is_straight(cards: List[Card]) -> bool:
        if len(cards) != 5:
            return False

        ranks = sorted({card.rank for card in cards})
        if len(ranks) != 5:
            return False

        # Special case A-2-3-4-5
        if ranks == [3, 4, 5, 14, 15]:
            return True

        if 15 in ranks:
            return False

        return ranks == list(range(ranks[0], ranks[0] + 5))

    @staticmethod
    def is_full_house(cards: List[Card]) -> bool:
        if len(cards) != 5:
            return False

        counts = PatternEvaluator._rank_counts(cards)
        return sorted(counts.values()) == [2, 3]

    @staticmethod
    def is_four_of_a_kind(cards: List[Card]) -> bool:
        if len(cards) != 5:
            return False

        counts = PatternEvaluator._rank_counts(cards)
        return 4 in counts.values()

    @staticmethod
    def is_flush(cards: List[Card]) -> bool:
        if len(cards) != 5:
            return False
        suits = {card.suit for card in cards}
        return len(suits) == 1

    @staticmethod
    def is_straight_flush(cards: List[Card]) -> bool:
        return PatternEvaluator.is_straight(cards) and PatternEvaluator.is_flush(cards)

    @staticmethod
    def get_pattern_signature(cards: List[Card]) -> Optional[Tuple[PatternType, int]]:
        result = PatternEvaluator.classify(cards)
        return result.signature() if result else None

    @staticmethod
    def _rank_counts(cards: List[Card]) -> dict[int, int]:
        counts: dict[int, int] = {}
        for card in cards:
            counts[card.rank] = counts.get(card.rank, 0) + 1
        return counts

    @staticmethod
    def _find_n_of_a_kind(cards: List[Card], n: int) -> Tuple[int, int]:
        counts = PatternEvaluator._rank_counts(cards)
        for rank, count in counts.items():
            if count == n:
                return rank, count
        return -1, 0

    @staticmethod
    def _highest_power_of_rank(cards: List[Card], rank: int) -> int:
        return max(card.power for card in cards if card.rank == rank)

    @staticmethod
    def _straight_strength(cards: List[Card]) -> int:
        ranks = sorted({card.rank for card in cards})
        if ranks == [3, 4, 5, 14, 15]:
            # treat A-2-3-4-5 as the lowest straight
            return min(card.power for card in cards)
        return max(card.power for card in cards)
