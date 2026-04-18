from __future__ import annotations

import functools
import random
from typing import List

SUIT_SYMBOLS = ["♣", "♦", "♥", "♠"]
RANK_SYMBOLS = {
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "J",
    12: "Q",
    13: "K",
    14: "A",
    15: "2",
}


@functools.total_ordering
class Card:
    """Big Two 卡片。

    rank: 3..15，其中 15 代表「2"。
    suit: 0..3，對應「♣, ♦, ♥, ♠」。
    """

    def __init__(self, rank: int, suit: int) -> None:
        if rank < 3 or rank > 15:
            raise ValueError("rank must be between 3 and 15")
        if suit < 0 or suit > 3:
            raise ValueError("suit must be between 0 and 3")

        self.rank = rank
        self.suit = suit
        self.power = self._compute_power()

    def _compute_power(self) -> int:
        # 以 Big Two 的順序計算唯一分數 0..51。
        # 3..A 對應 0..11，2 對應 12。
        rank_index = self.rank - 3 if self.rank != 15 else 12
        return rank_index * 4 + self.suit

    def __repr__(self) -> str:
        return f"{SUIT_SYMBOLS[self.suit]}{RANK_SYMBOLS[self.rank]}"

    def rank_str(self) -> str:
        return RANK_SYMBOLS[self.rank]

    def suit_str(self) -> str:
        return SUIT_SYMBOLS[self.suit]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other: Card) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self.power < other.power

    def __hash__(self) -> int:
        return hash((self.rank, self.suit))

    def to_sort_key(self) -> tuple[int, int]:
        return (self.rank, self.suit)

    def is_three_of_clubs(self) -> bool:
        return self.rank == 3 and self.suit == 0


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = self._create_standard_deck()

    def _create_standard_deck(self) -> List[Card]:
        return [Card(rank, suit) for rank in range(3, 16) for suit in range(4)]

    def shuffle(self, seed: int | None = None) -> None:
        if seed is not None:
            random.seed(seed)
        random.shuffle(self.cards)

    def deal(self, num_players: int) -> List[List[Card]]:
        if num_players < 1:
            raise ValueError("num_players must be at least 1")

        hands: List[List[Card]] = [[] for _ in range(num_players)]
        for index, card in enumerate(self.cards):
            hands[index % num_players].append(card)
        return hands

    def reset(self) -> None:
        self.cards = self._create_standard_deck()
