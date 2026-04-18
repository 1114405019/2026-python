from __future__ import annotations

from typing import List, Optional

try:
    from .manager import TurnManager
    from .models import Card, Deck
    from .player import Player
    from .rules import RuleEngine
except ImportError:
    from manager import TurnManager
    from models import Card, Deck
    from player import Player
    from rules import RuleEngine


class BigTwoGame:
    def __init__(self, player_names: List[str], seed: Optional[int] = None) -> None:
        if len(player_names) != 4:
            raise ValueError("BigTwoGame requires exactly 4 players")

        self.deck = Deck()
        self.players = [Player(name) for name in player_names]
        self.rule_engine = RuleEngine()
        self.turn_manager = TurnManager([player.name for player in self.players], self.rule_engine)
        self.seed = seed
        self.winner: Optional[Player] = None
        self.game_over = False
        self.remaining_points: Optional[int] = None

    def setup_game(self) -> None:
        self.deck.reset()
        self.deck.shuffle(self.seed)
        hands = self.deck.deal(len(self.players))
        for player, cards in zip(self.players, hands):
            player.add_cards(cards)
            player.sort_hand()

    def find_club_three_player_index(self) -> int:
        for index, player in enumerate(self.players):
            if player.has_club_three():
                return index
        raise RuntimeError("No player has the 3 of clubs")

    def start_game(self) -> None:
        self.setup_game()
        club_three_index = self.find_club_three_player_index()
        self.turn_manager.current_player_index = club_three_index

    def process_play(self, cards: Optional[List[Card]]) -> bool:
        if self.game_over:
            return False

        if cards is None or len(cards) == 0:
            self.turn_manager.pass_turn()
            return True

        current_index = self.turn_manager.get_current_player_index()
        success = self.turn_manager.submit_play(current_index, cards)
        if success:
            self.players[current_index].play_cards(cards)
            winner = self.check_winner()
            if winner is not None:
                self.winner = winner
                self.game_over = True
            return True
        return False

    def check_winner(self) -> Optional[Player]:
        for player in self.players:
            if len(player.hand) == 0:
                self.remaining_points = sum(card.power for other in self.players if other is not player for card in other.hand)
                return player
        return None


if __name__ == "__main__":
    game = BigTwoGame(["Alice", "Bob", "Carol", "Dave"], seed=42)
    game.start_game()
    print(f"Starting player: {game.turn_manager.get_current_player()}")
    print("Player hands:")
    for player in game.players:
        print(player.name, player.hand)
