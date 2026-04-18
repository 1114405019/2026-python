from __future__ import annotations

from typing import List, Optional

try:
    from .evaluator import PatternEvaluator
    from .models import Card
    from .rules import RuleEngine
except ImportError:
    from evaluator import PatternEvaluator
    from models import Card
    from rules import RuleEngine


class TurnManager:
    def __init__(self, players: List[str], rule_engine: RuleEngine) -> None:
        if not players:
            raise ValueError("players list must not be empty")

        self.players = players
        self.rule_engine = rule_engine
        self.current_player_index = 0
        self.last_play: Optional[List[Card]] = None
        self.last_player_index: Optional[int] = None
        self.pass_count = 0
        self.passed = [False] * len(players)
        self.round_number = 1
        self.turn_history: List[tuple[int, Optional[List[Card]]]] = []

    def get_current_player_index(self) -> int:
        return self.current_player_index

    def get_current_player(self) -> str:
        return self.players[self.current_player_index]

    def record_play(self, player_index: int, cards: List[Card]) -> None:
        self.last_play = list(cards)
        self.last_player_index = player_index
        self.pass_count = 0
        self.turn_history.append((player_index, list(cards)))

    def pass_turn(self) -> None:
        self.passed[self.current_player_index] = True
        self.turn_history.append((self.current_player_index, None))
        self.pass_count += 1

        if self.is_new_round():
            self.reset_round()
        else:
            self.next_turn()

    def next_turn(self) -> None:
        num_players = len(self.players)
        for _ in range(num_players):
            self.current_player_index = (self.current_player_index + 1) % num_players
            if not self.passed[self.current_player_index]:
                return

        if self.is_new_round():
            self.reset_round()

    def is_new_round(self) -> bool:
        return self.last_play is not None and self.pass_count >= len(self.players) - 1

    def reset_round(self) -> None:
        self.passed = [False] * len(self.players)
        self.pass_count = 0
        self.last_play = None
        self.round_number += 1
        if self.last_player_index is not None:
            self.current_player_index = self.last_player_index

    def submit_play(self, player_index: int, cards: List[Card]) -> bool:
        if player_index != self.current_player_index:
            return False

        if not PatternEvaluator.is_valid_pattern(cards):
            return False

        if self.last_play is not None and not self.rule_engine.can_beat(self.last_play, cards):
            return False

        self.record_play(player_index, cards)
        self.next_turn()
        return True

    def can_free_play(self) -> bool:
        return self.last_play is None and self.pass_count == 0
