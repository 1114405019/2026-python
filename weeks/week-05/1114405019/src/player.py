from __future__ import annotations

from typing import List

try:
    from .models import Card
except ImportError:
    from models import Card


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand: List[Card] = []

    def add_cards(self, cards: List[Card]) -> None:
        self.hand.extend(cards)

    def sort_hand(self) -> None:
        self.hand.sort()

    def play_cards(self, cards: List[Card]) -> List[Card]:
        missing = [card for card in cards if card not in self.hand]
        if missing:
            raise ValueError(f"Cannot play cards not in hand: {missing}")

        played: List[Card] = []
        for card in cards:
            self.hand.remove(card)
            played.append(card)
        return played

    def has_club_three(self) -> bool:
        return any(card.rank == 3 and card.suit == 0 for card in self.hand)
