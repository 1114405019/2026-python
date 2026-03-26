"""
Phase 2: 牌型分類

實作 HandClassifier 類別，負責分類牌型、比較大小、檢查合法性。
"""

from typing import List, Optional, Tuple
from enum import IntEnum
from game.models import Card


class CardType(IntEnum):
    """牌型列舉"""
    SINGLE = 1        # 單張
    PAIR = 2          # 對子
    TRIPLE = 3       # 三條
    STRAIGHT = 4      # 順子
    FLUSH = 5         # 同花
    FULL_HOUSE = 6    # 葫蘆
    FOUR_OF_A_KIND = 7 # 四條
    STRAIGHT_FLUSH = 8 # 同花順


class HandClassifier:
    """
    牌型分類器
    
    負責分類牌型、比較大小、檢查出牌合法性。
    所有方法都是靜態方法。
    """
    
    @staticmethod
    def _is_straight(ranks: List[int]) -> bool:
        """
        檢查是否為順子
        
        Args:
            ranks: 牌的數字列表（已排序）
            
        Returns:
            是否為順子
        """
        if len(ranks) != 5:
            return False
        
        # 檢查一般順子（連續5張）
        for i in range(4):
            if ranks[i] + 1 != ranks[i + 1]:
                break
        else:
            return True
        
        # 檢查特殊順子：A-2-3-4-5
        # A=14, 2=15, 3=3, 4=4, 5=5
        # 排序後應為 [3,4,5,14,15]
        if ranks == [3, 4, 5, 14, 15]:
            return True
        
        return False
    
    @staticmethod
    def _is_flush(suits: List[int]) -> bool:
        """
        檢查是否為同花
        
        Args:
            suits: 牌的花色列表
            
        Returns:
            是否為同花
        """
        if len(suits) != 5:
            return False
        
        # 檢查所有花色是否相同
        return all(suit == suits[0] for suit in suits)
    
    @staticmethod
    def _count_ranks(cards: List[Card]) -> dict:
        """
        統計各 rank 的出現次數
        
        Args:
            cards: 卡牌列表
            
        Returns:
            rank -> count 的字典
        """
        rank_counts = {}
        for card in cards:
            rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1
        return rank_counts
    
    @staticmethod
    def _get_straight_max_rank(ranks: List[int]) -> int:
        """
        獲取順子的最大 rank
        
        Args:
            ranks: 已排序的 rank 列表
            
        Returns:
            順子的最大 rank
        """
        if len(ranks) != 5:
            return 0
        
        # 檢查是否為 A-2-3-4-5 順子
        if ranks == [3, 4, 5, 14, 15]:
            return 5  # A-2-3-4-5 中最大的是 5
        
        # 一般順子，返回最大的 rank
        return ranks[-1]
    
    @staticmethod
    def _find_max_card(cards: List[Card]) -> Card:
        """
        找出最大的一張牌
        
        Args:
            cards: 卡牌列表
            
        Returns:
            最大的牌
        """
        return max(cards)
    
    @staticmethod
    def classify(cards: List[Card]) -> Optional[Tuple[CardType, int, int]]:
        """
        分類牌型
        
        Args:
            cards: 要分類的牌列表
            
        Returns:
            (牌型, 數字, 花色) 或 None（無效牌型）
        """
        if not cards:
            return None
        
        n = len(cards)
        
        # 單張
        if n == 1:
            card = cards[0]
            return (CardType.SINGLE, card.rank, card.suit)
        
        # 對子
        elif n == 2:
            if cards[0].rank == cards[1].rank:
                # 取花色較大的牌作為代表
                max_card = max(cards)
                return (CardType.PAIR, max_card.rank, max_card.suit)
        
        # 三條
        elif n == 3:
            if (cards[0].rank == cards[1].rank == cards[2].rank):
                card = cards[0]
                return (CardType.TRIPLE, card.rank, card.suit)
        
        # 五張牌型
        elif n == 5:
            ranks = sorted([card.rank for card in cards])
            suits = [card.suit for card in cards]
            rank_counts = HandClassifier._count_ranks(cards)
            
            # 同花順：同花 + 順子
            if HandClassifier._is_flush(suits) and HandClassifier._is_straight(ranks):
                # 對於同花順，找順子中最大的牌
                max_rank_in_straight = HandClassifier._get_straight_max_rank(ranks)
                # 找該 rank 中花色最大的牌
                max_suit = max(card.suit for card in cards if card.rank == max_rank_in_straight)
                return (CardType.STRAIGHT_FLUSH, max_rank_in_straight, max_suit)
            
            # 四條：4張相同
            for rank, count in rank_counts.items():
                if count == 4:
                    # 找到四條的 rank
                    four_rank = rank
                    # 找到單張的牌
                    single_card = None
                    for card in cards:
                        if card.rank != four_rank:
                            single_card = card
                            break
                    return (CardType.FOUR_OF_A_KIND, four_rank, single_card.suit)
            
            # 葫蘆：3張相同 + 2張相同
            three_rank = None
            two_rank = None
            for rank, count in rank_counts.items():
                if count == 3:
                    three_rank = rank
                elif count == 2:
                    two_rank = rank
            
            if three_rank is not None and two_rank is not None:
                return (CardType.FULL_HOUSE, three_rank, 0)  # 花色不重要
            
            # 同花
            if HandClassifier._is_flush(suits):
                max_card = HandClassifier._find_max_card(cards)
                return (CardType.FLUSH, max_card.rank, max_card.suit)
            
            # 順子
            if HandClassifier._is_straight(ranks):
                # 對於順子，找順子中最大的牌
                max_rank_in_straight = HandClassifier._get_straight_max_rank(ranks)
                # 找該 rank 中花色最大的牌
                max_suit = max(card.suit for card in cards if card.rank == max_rank_in_straight)
                return (CardType.STRAIGHT, max_rank_in_straight, max_suit)
        
        # 無效牌型
        return None
    
    @staticmethod
    def compare(play1: List[Card], play2: List[Card]) -> int:
        """
        比較兩手牌的大小
        
        Args:
            play1: 第一手牌
            play2: 第二手牌
            
        Returns:
            1: play1 > play2
            -1: play1 < play2
            0: 平手
        """
        type1 = HandClassifier.classify(play1)
        type2 = HandClassifier.classify(play2)
        
        if type1 is None or type2 is None:
            return 0  # 無效牌型視為平手
        
        card_type1, rank1, suit1 = type1
        card_type2, rank2, suit2 = type2
        
        # 不同牌型：直接比較牌型等級
        if card_type1 != card_type2:
            return 1 if card_type1 > card_type2 else -1
        
        # 同牌型：比較數字
        if rank1 != rank2:
            return 1 if rank1 > rank2 else -1
        
        # 數字相同：比較花色
        return 1 if suit1 > suit2 else -1
    
    @staticmethod
    def can_play(last_play: Optional[List[Card]], cards: List[Card]) -> bool:
        """
        檢查是否可以出牌
        
        Args:
            last_play: 上家出的牌（None 表示第一回合）
            cards: 要出的牌
            
        Returns:
            是否可以出牌
        """
        # 第一回合：只能出 3♣
        if last_play is None:
            if len(cards) != 1:
                return False
            card = cards[0]
            return card.rank == 3 and card.suit == 0  # 3♣
        
        # 其他回合：檢查牌型和大小
        last_type = HandClassifier.classify(last_play)
        current_type = HandClassifier.classify(cards)
        
        if last_type is None or current_type is None:
            return False
        
        last_card_type, _, _ = last_type
        current_card_type, _, _ = current_type
        
        # 牌型必須相同
        if last_card_type != current_card_type:
            return False
        
        # 比較大小：必須比上家大
        return HandClassifier.compare(cards, last_play) == 1