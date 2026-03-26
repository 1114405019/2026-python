from typing import List, Optional
from game.models import Card, Deck, Player
from game.classifier import HandClassifier
from game.finder import HandFinder
from game.ai import AIStrategy


class BigTwoGame:
    """Big Two 遊戲控制器"""

    def __init__(self):
        self.players: List[Player] = []
        self.deck = Deck()
        self.current_player_index = 0
        self.last_play: Optional[List[Card]] = None
        self.pass_count = 0
        self.round_number = 1
        self.winner: Optional[Player] = None

        # 依賴的組件
        self.classifier = HandClassifier()
        self.finder = HandFinder()
        self.ai_strategy = AIStrategy()

    def setup(self) -> None:
        """初始化遊戲"""
        # 建立4位玩家：1人3AI
        self.players = [
            Player("Human", is_ai=False),
            Player("AI-1", is_ai=True),
            Player("AI-2", is_ai=True),
            Player("AI-3", is_ai=True)
        ]

        # 洗牌
        self.deck.shuffle()

        # 發牌：每人13張
        for _ in range(13):
            for player in self.players:
                cards = self.deck.deal(1)
                if cards:
                    player.take_cards(cards)

        # 找到持有3♣的玩家作為先手
        for i, player in enumerate(self.players):
            if any(card.rank == 3 and card.suit == 0 for card in player.hand):
                self.current_player_index = i
                break

        # 初始化遊戲狀態
        self.last_play = None
        self.pass_count = 0
        self.round_number = 1
        self.winner = None

    def play(self, cards: List[Card]) -> bool:
        """玩家出牌"""
        current_player = self.get_current_player()

        # 檢查是否為有效的出牌
        if not self._is_valid_play(cards, current_player):
            return False

        # 從手牌中移除這些牌
        current_player.play_cards(cards)

        # 設定最後出牌
        self.last_play = cards

        # 重置過牌計數
        self.pass_count = 0

        # 檢查勝利
        self.check_winner()

        # 輪到下一位玩家
        self.next_turn()

        return True

    def _is_valid_play(self, cards: List[Card], player: Player) -> bool:
        """檢查出牌是否有效"""
        # 第一回合必須出3♣
        if self.last_play is None:
            return (len(cards) == 1 and
                    cards[0].rank == 3 and
                    cards[0].suit == 0 and
                    cards[0] in player.hand)

        # 檢查牌型是否有效
        card_type, _, _ = self.classifier.classify(cards)
        if card_type == CardType.INVALID:
            return False

        # 檢查是否能壓過上一手牌
        if not self.classifier.can_play(cards, self.last_play):
            return False

        # 檢查玩家是否有這些牌
        for card in cards:
            if card not in player.hand:
                return False

        return True

    def pass_turn(self) -> None:
        """過牌"""
        self.pass_count += 1

        # 檢查是否需要重置回合
        self.check_round_reset()

        # 輪到下一位玩家
        self.next_turn()

    def next_turn(self) -> None:
        """輪到下一位玩家"""
        self.current_player_index = (self.current_player_index + 1) % 4

    def check_round_reset(self) -> None:
        """檢查是否需要重置回合"""
        if self.pass_count >= 3:
            self.last_play = None
            self.pass_count = 0
            self.round_number += 1

    def check_winner(self) -> Optional[Player]:
        """檢查是否有玩家獲勝"""
        for player in self.players:
            if len(player.hand) == 0:
                self.winner = player
                return player
        return None

    def is_game_over(self) -> bool:
        """檢查遊戲是否結束"""
        if self.winner is not None:
            return True
        # 自動檢查勝利條件
        return self.check_winner() is not None

    def get_current_player(self) -> Player:
        """取得當前玩家"""
        return self.players[self.current_player_index]

    def ai_turn(self) -> bool:
        """AI自動回合"""
        current_player = self.get_current_player()

        # 取得所有有效的出牌
        valid_plays = self.finder.get_all_valid_plays(current_player.hand, self.last_play)

        if not valid_plays:
            # 無牌可出，過牌
            self.pass_turn()
            return False

        # AI選擇最佳出牌
        best_play = self.ai_strategy.select_best(valid_plays, current_player.hand)

        # 出牌
        return self.play(best_play)