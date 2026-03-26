"""
Phase 1: 資料模型

實作 Card、Deck、Hand、Player 類別，構成遊戲的基礎資料結構。
"""

from typing import List, Optional, Tuple
from enum import IntEnum
from random import shuffle as random_shuffle


class CardType(IntEnum):
    """牌型列舉（Phase 2 使用）"""
    INVALID = 0
    SINGLE = 1
    PAIR = 2
    TRIPLE = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8


class Card:
    """
    撲克牌類別
    
    屬性：
        rank (int): 牌的數字，3-15（3=3, 14=A, 15=2）
        suit (int): 牌的花色，0-3（0=♣, 1=♦, 2=♥, 3=♠）
    """
    
    # 花色對應符號
    SUITS = {
        0: "♣",
        1: "♦",
        2: "♥",
        3: "♠"
    }
    
    # rank 對應名字
    RANKS = {
        3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
        10: "T", 11: "J", 12: "Q", 13: "K", 14: "A", 15: "2"
    }
    
    # rank 大小順序（用於比較）
    # 數字順序：2 > A > K > Q > J > T > 9 > 8 > 7 > 6 > 5 > 4 > 3
    RANK_ORDER = {
        15: 14,  # 2 最大
        14: 13,  # A
        13: 12,  # K
        12: 11,  # Q
        11: 10,  # J
        10: 9,   # T
        9: 8,
        8: 7,
        7: 6,
        6: 5,
        5: 4,
        4: 3,
        3: 2     # 3 最小
    }
    
    # 花色大小順序（用於比較）
    # ♠ > ♥ > ♦ > ♣ => 3 > 2 > 1 > 0
    SUIT_ORDER = {
        3: 4,  # ♠ 最大
        2: 3,  # ♥
        1: 2,  # ♦
        0: 1   # ♣ 最小
    }
    
    def __init__(self, rank: int, suit: int) -> None:
        """
        初始化牌
        
        Args:
            rank: 牌的數字（3-15）
            suit: 牌的花色（0-3）
        """
        self.rank = rank
        self.suit = suit
    
    def __repr__(self) -> str:
        """
        回傳牌的字串表示，格式為 "♠A"
        """
        return f"{self.SUITS[self.suit]}{self.RANKS[self.rank]}"
    
    def __eq__(self, other: "Card") -> bool:
        """
        比較兩張牌是否相等
        
        Args:
            other: 另一張牌
            
        Returns:
            若 rank 與 suit 都相同則回傳 True
        """
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit
    
    def __hash__(self) -> int:
        """
        回傳牌的雜湊值，用於集合與字典
        """
        return hash((self.rank, self.suit))
    
    def __lt__(self, other: "Card") -> bool:
        """
        比較兩張牌的大小（<）
        
        先比 rank，再比 suit：
        - rank 大的牌較大
        - rank 相同則 suit 大的牌較大
        
        Args:
            other: 另一張牌
            
        Returns:
            若 self < other 則回傳 True
        """
        if not isinstance(other, Card):
            return NotImplemented
        
        # 比較 rank（使用大小順序）
        if self.RANK_ORDER[self.rank] != self.RANK_ORDER[other.rank]:
            return self.RANK_ORDER[self.rank] < self.RANK_ORDER[other.rank]
        
        # rank 相同時比 suit
        return self.SUIT_ORDER[self.suit] < self.SUIT_ORDER[other.suit]
    
    def __le__(self, other: "Card") -> bool:
        """小於等於"""
        return self == other or self < other
    
    def __gt__(self, other: "Card") -> bool:
        """大於"""
        return not self <= other
    
    def __ge__(self, other: "Card") -> bool:
        """大於等於"""
        return not self < other
    
    def to_sort_key(self) -> Tuple[int, int]:
        """
        回傳排序鍵，用於 sorted() 函數
        
        Returns:
            (rank, suit) 元組
        """
        return (self.rank, self.suit)


class Deck:
    """
    牌堆類別
    
    屬性：
        cards (List[Card]): 所有牌
    """
    
    def __init__(self) -> None:
        """初始化牌堆，建立 52 張牌"""
        self.cards: List[Card] = []
        self._create_cards()
    
    def _create_cards(self) -> None:
        """
        建立 52 張牌（4 花色 × 13 數字）
        
        按照順序建立：從 ♣3 到 ♠A 等
        """
        # rank 從 3 到 15 (15=2)
        for rank in range(3, 16):
            # suit 從 0 到 3 (0=♣, 1=♦, 2=♥, 3=♠)
            for suit in range(4):
                self.cards.append(Card(rank, suit))
    
    def __len__(self) -> int:
        """回傳剩餘牌數"""
        return len(self.cards)
    
    def shuffle(self) -> None:
        """洗牌，打亂牌堆的順序"""
        random_shuffle(self.cards)
    
    def deal(self, n: int) -> List[Card]:
        """
        發 n 張牌
        
        Args:
            n: 要發的牌數
            
        Returns:
            發出的牌列表（最多 52 張，即使 n > 52）
        """
        # 發的牌數不超過堆中剩餘牌數
        num_to_deal = min(n, len(self.cards))
        dealt_cards = self.cards[:num_to_deal]
        self.cards = self.cards[num_to_deal:]
        return dealt_cards


class Hand(list):
    """
    手牌類別，繼承自 list
    
    代表玩家持有的所有牌，支援排序、搜尋等操作。
    """
    
    def __init__(self, cards: Optional[List[Card]] = None) -> None:
        """
        初始化手牌
        
        Args:
            cards: 初始牌列表，若為 None 則為空
        """
        super().__init__()
        if cards:
            self.extend(cards)
    
    def sort_desc(self) -> None:
        """
        按 rank 倒序排序，同 rank 時按 suit 正序
        
        數字順序：2 > A > K > Q > J > T > 9 > 8 > 7 > 6 > 5 > 4 > 3
        花色順序：♠ > ♥ > ♦ > ♣
        
        更新：使用 Card 的比較運算符，倒序排列
        """
        # 正序排列後，反轉得到倒序效果
        self.sort(reverse=True)
    
    def find_3_clubs(self) -> Optional[Card]:
        """
        找 3♣（3 of clubs）
        
        Returns:
            若找到 3♣ 則回傳 Card 物件，否則回傳 None
        """
        for card in self:
            if card.rank == 3 and card.suit == 0:  # 3♣
                return card
        return None
    
    def remove(self, cards: List[Card]) -> None:
        """
        移除指定的牌
        
        Args:
            cards: 要移除的牌列表
        """
        for card in cards:
            if card in self:
                super().remove(card)


class Player:
    """
    玩家類別
    
    屬性：
        name (str): 玩家名稱
        is_ai (bool): 是否為 AI 玩家
        hand (Hand): 手牌
        score (int): 分數
    """
    
    def __init__(self, name: str, is_ai: bool = False) -> None:
        """
        初始化玩家
        
        Args:
            name: 玩家名稱
            is_ai: 是否為 AI 玩家，預設為 False（人類玩家）
        """
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0
    
    def take_cards(self, cards: List[Card]) -> None:
        """
        接收牌（加入到手牌中）
        
        Args:
            cards: 要接收的牌列表
        """
        self.hand.extend(cards)
    
    def play_cards(self, cards: List[Card]) -> List[Card]:
        """
        出牌（從手牌中移除並回傳）
        
        Args:
            cards: 要出的牌列表
            
        Returns:
            出的牌列表
        """
        self.hand.remove(cards)
        return cards
    
    def __repr__(self) -> str:
        """回傳玩家的字串表示"""
        player_type = "AI" if self.is_ai else "Human"
        return f"Player({self.name}, {player_type}, score={self.score})"
