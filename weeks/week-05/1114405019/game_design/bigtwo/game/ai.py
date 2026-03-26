from typing import List, Optional
from game.models import Card, Hand
from game.classifier import HandClassifier, CardType


class AIStrategy:
    """AI 策略類別，使用貪心演算法選擇最佳出牌"""

    # 牌型分數
    TYPE_SCORES = {
        CardType.SINGLE: 1,
        CardType.PAIR: 2,
        CardType.TRIPLE: 3,
        CardType.STRAIGHT: 4,
        CardType.FLUSH: 5,
        CardType.FULL_HOUSE: 6,
        CardType.FOUR_OF_A_KIND: 7,
        CardType.STRAIGHT_FLUSH: 8
    }

    # 加分常數
    EMPTY_HAND_BONUS = 10000
    NEAR_EMPTY_BONUS = 500
    SPADE_BONUS = 5

    @staticmethod
    def score_play(cards: List[Card], hand: Hand, is_first: bool = False) -> float:
        """評分出牌組合

        Args:
            cards: 要出的牌
            hand: 當前手牌
            is_first: 是否為第一回合

        Returns:
            評分分數
        """
        if not cards:
            return 0.0

        # 獲取牌型資訊
        classification = HandClassifier.classify(cards)
        if classification is None:
            return 0.0

        card_type, rank, suit = classification

        # 基礎評分：牌型分數 × 100 + 數字分數 × 10
        base_score = AIStrategy.TYPE_SCORES[card_type] * 100 + rank * 10

        # 剩餘牌數加分
        remaining_cards = len(hand) - len(cards)
        remaining_bonus = 0
        if remaining_cards == 1:
            remaining_bonus = AIStrategy.EMPTY_HAND_BONUS
        elif remaining_cards <= 3:
            remaining_bonus = AIStrategy.NEAR_EMPTY_BONUS

        # 黑桃加分
        spade_bonus = sum(AIStrategy.SPADE_BONUS for card in cards if card.suit == 3)

        return base_score + remaining_bonus + spade_bonus

    @staticmethod
    def select_best(valid_plays: List[List[Card]], hand: Hand, is_first: bool = False) -> Optional[List[Card]]:
        """選擇最佳出牌

        Args:
            valid_plays: 所有合法出牌
            hand: 當前手牌
            is_first: 是否為第一回合

        Returns:
            最佳出牌組合，若無則返回 None
        """
        if not valid_plays:
            return None

        # 第一回合：只能出3♣
        if is_first:
            three_clubs = [play for play in valid_plays if len(play) == 1 and play[0].rank == 3 and play[0].suit == 0]
            return three_clubs[0] if three_clubs else None

        # 其他回合：選擇分數最高的
        best_play = None
        best_score = -1

        for play in valid_plays:
            score = AIStrategy.score_play(play, hand, is_first)
            if score > best_score:
                best_score = score
                best_play = play

        return best_play