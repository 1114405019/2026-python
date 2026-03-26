from typing import List, Optional
from itertools import combinations
from .models import Hand, Card
from .classifier import HandClassifier, CardType


class HandFinder:
    """牌型搜尋器，用於從手牌中找到所有可能的出牌組合"""

    @staticmethod
    def find_singles(hand: Hand) -> List[List[Card]]:
        """找出所有單張牌組合

        Args:
            hand: 手牌

        Returns:
            所有單張牌的列表，每個元素是一個包含一張牌的列表
        """
        return [[card] for card in hand]

    @staticmethod
    def find_pairs(hand: Hand) -> List[List[Card]]:
        """找出所有對子組合

        Args:
            hand: 手牌

        Returns:
            所有對子的列表，每個元素是一個包含兩張相同rank牌的列表
        """
        pairs = []
        # 按rank分組
        rank_groups = {}
        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)

        # 對於每個有至少2張牌的rank，生成所有對子組合
        for rank, cards in rank_groups.items():
            if len(cards) >= 2:
                # 使用combinations生成所有2張的組合
                for pair in combinations(cards, 2):
                    pairs.append(list(pair))

        return pairs

    @staticmethod
    def find_triples(hand: Hand) -> List[List[Card]]:
        """找出所有三條組合

        Args:
            hand: 手牌

        Returns:
            所有三條的列表，每個元素是一個包含三張相同rank牌的列表
        """
        triples = []
        # 按rank分組
        rank_groups = {}
        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)

        # 對於每個有至少3張牌的rank，生成所有三條組合
        for rank, cards in rank_groups.items():
            if len(cards) >= 3:
                # 使用combinations生成所有3張的組合
                for triple in combinations(cards, 3):
                    triples.append(list(triple))

        return triples

    @staticmethod
    def find_fives(hand: Hand) -> List[List[Card]]:
        """找出所有五張牌型組合

        優先級順序（從高到低）：
        1. 同花順 (STRAIGHT_FLUSH)
        2. 四條 (FOUR_OF_A_KIND)
        3. 葫蘆 (FULL_HOUSE)
        4. 同花 (FLUSH)
        5. 順子 (STRAIGHT)

        Args:
            hand: 手牌

        Returns:
            所有五張牌型的列表
        """
        fives = []

        # 1. 找同花順
        straight_flushes = HandFinder._find_straight_flushes(hand)
        fives.extend(straight_flushes)

        # 2. 找四條
        four_of_a_kinds = HandFinder._find_four_of_a_kinds(hand)
        fives.extend(four_of_a_kinds)

        # 3. 找葫蘆
        full_houses = HandFinder._find_full_houses(hand)
        fives.extend(full_houses)

        # 4. 找同花
        flushes = HandFinder._find_flushes(hand)
        fives.extend(flushes)

        # 5. 找順子
        straights = HandFinder._find_straights(hand)
        fives.extend(straights)

        return fives

    @staticmethod
    def _find_straight_flushes(hand: Hand) -> List[List[Card]]:
        """找出所有同花順"""
        straight_flushes = []

        # 按花色分組
        suit_groups = {}
        for card in hand:
            if card.suit not in suit_groups:
                suit_groups[card.suit] = []
            suit_groups[card.suit].append(card)

        # 對於每個花色，找順子
        for suit, cards in suit_groups.items():
            if len(cards) >= 5:
                # 排序
                sorted_cards = sorted(cards, key=lambda c: c.rank)
                # 找順子
                straights = HandFinder._find_straights_in_sorted_cards(sorted_cards)
                straight_flushes.extend(straights)

        return straight_flushes

    @staticmethod
    def _find_four_of_a_kinds(hand: Hand) -> List[List[Card]]:
        """找出所有四條"""
        four_of_a_kinds = []

        # 按rank分組
        rank_groups = {}
        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)

        # 對於每個有4張牌的rank
        for rank, cards in rank_groups.items():
            if len(cards) == 4:
                # 需要再加一張其他牌
                other_cards = [c for c in hand if c.rank != rank]
                if other_cards:
                    # 任選一張其他牌
                    four_of_a_kinds.append(cards + [other_cards[0]])

        return four_of_a_kinds

    @staticmethod
    def _find_full_houses(hand: Hand) -> List[List[Card]]:
        """找出所有葫蘆"""
        full_houses = []

        # 按rank分組
        rank_groups = {}
        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)

        # 找三條和對子
        triples_ranks = [rank for rank, cards in rank_groups.items() if len(cards) >= 3]
        pairs_ranks = [rank for rank, cards in rank_groups.items() if len(cards) >= 2]

        for triple_rank in triples_ranks:
            for pair_rank in pairs_ranks:
                if triple_rank != pair_rank:
                    # 從三條中選3張，從對子中選2張
                    triple_cards = rank_groups[triple_rank][:3]
                    pair_cards = rank_groups[pair_rank][:2]
                    full_houses.append(triple_cards + pair_cards)

        return full_houses

    @staticmethod
    def _find_flushes(hand: Hand) -> List[List[Card]]:
        """找出所有同花"""
        flushes = []

        # 按花色分組
        suit_groups = {}
        for card in hand:
            if card.suit not in suit_groups:
                suit_groups[card.suit] = []
            suit_groups[card.suit].append(card)

        # 對於每個有5張或更多牌的花色
        for suit, cards in suit_groups.items():
            if len(cards) >= 5:
                # 選前5張（已排序）
                sorted_cards = sorted(cards, key=lambda c: (c.rank, c.suit), reverse=True)
                flushes.append(sorted_cards[:5])

        return flushes

    @staticmethod
    def _find_straights(hand: Hand) -> List[List[Card]]:
        """找出所有順子"""
        straights = []

        # 按rank排序
        sorted_cards = sorted(hand, key=lambda c: c.rank)

        # 找普通順子 (3-4-5-6-7 到 10-J-Q-K-A)
        for start_rank in range(3, 11):  # 3到10
            straight = HandFinder._find_straight_from_ranks(sorted_cards, start_rank)
            if straight:
                straights.append(straight)

        # 找A-2-3-4-5順子
        ace_low_straight = HandFinder._find_ace_low_straight(sorted_cards)
        if ace_low_straight:
            straights.append(ace_low_straight)

        return straights

    @staticmethod
    def _find_straight_from_ranks(sorted_cards: List[Card], start_rank: int) -> Optional[List[Card]]:
        """從指定rank開始找順子"""
        needed_ranks = [start_rank + i for i in range(5)]
        found_cards = []

        for rank in needed_ranks:
            rank_cards = [c for c in sorted_cards if c.rank == rank]
            if not rank_cards:
                return None
            # 選第一張（任意花色）
            found_cards.append(rank_cards[0])

        return found_cards

    @staticmethod
    def _find_ace_low_straight(sorted_cards: List[Card]) -> Optional[List[Card]]:
        """找A-2-3-4-5順子"""
        needed_ranks = [14, 3, 4, 5, 6]  # A=14, 2=3, 3=4, 4=5, 5=6
        found_cards = []

        for rank in needed_ranks:
            rank_cards = [c for c in sorted_cards if c.rank == rank]
            if not rank_cards:
                return None
            found_cards.append(rank_cards[0])

        return found_cards

    @staticmethod
    def _find_straights_in_sorted_cards(sorted_cards: List[Card]) -> List[List[Card]]:
        """在已排序的同花色牌中找順子"""
        straights = []

        # 普通順子
        for start_idx in range(len(sorted_cards) - 4):
            if (sorted_cards[start_idx + 4].rank - sorted_cards[start_idx].rank == 4 and
                all(sorted_cards[start_idx + i + 1].rank == sorted_cards[start_idx + i].rank + 1
                    for i in range(4))):
                straights.append(sorted_cards[start_idx:start_idx + 5])

        # A-2-3-4-5 同花順
        if (len(sorted_cards) >= 5 and
            sorted_cards[0].rank == 3 and  # 2
            sorted_cards[1].rank == 4 and  # 3
            sorted_cards[2].rank == 5 and  # 4
            sorted_cards[3].rank == 6 and  # 5
            sorted_cards[-1].rank == 14):  # A
            straights.append([sorted_cards[-1], sorted_cards[0], sorted_cards[1],
                            sorted_cards[2], sorted_cards[3]])

        return straights

    @staticmethod
    def get_all_valid_plays(hand: Hand, last_play: Optional[List[Card]]) -> List[List[Card]]:
        """根據上家的牌型，回傳所有合法出牌

        Args:
            hand: 手牌
            last_play: 上家的出牌，None表示第一回合

        Returns:
            所有合法出牌的列表
        """
        if last_play is None:
            # 第一回合：只能出3♣
            three_clubs = [card for card in hand if card.rank == 3 and card.suit == 0]
            return [[card] for card in three_clubs]

        # 判斷上家牌型
        last_card_type = HandClassifier.classify(last_play)[0]

        if last_card_type == CardType.SINGLE:
            # 上家單張：可以出單張、對子、三條、五張
            valid_plays = []
            valid_plays.extend(HandFinder.find_singles(hand))
            valid_plays.extend(HandFinder.find_pairs(hand))
            valid_plays.extend(HandFinder.find_triples(hand))
            valid_plays.extend(HandFinder.find_fives(hand))
            # 過濾出比上家大的牌
            valid_plays = [play for play in valid_plays if HandClassifier.compare(play, last_play) == 1]

        elif last_card_type == CardType.PAIR:
            # 上家對子：可以出對子、三條、五張
            valid_plays = []
            valid_plays.extend(HandFinder.find_pairs(hand))
            valid_plays.extend(HandFinder.find_triples(hand))
            valid_plays.extend(HandFinder.find_fives(hand))
            # 過濾出比上家大的牌
            valid_plays = [play for play in valid_plays if HandClassifier.compare(play, last_play) == 1]

        elif last_card_type == CardType.TRIPLE:
            # 上家三條：可以出三條、五張
            valid_plays = []
            valid_plays.extend(HandFinder.find_triples(hand))
            valid_plays.extend(HandFinder.find_fives(hand))
            # 過濾出比上家大的牌
            valid_plays = [play for play in valid_plays if HandClassifier.compare(play, last_play) == 1]

        else:
            # 上家五張牌：只能出五張牌且比上家大
            valid_plays = HandFinder.find_fives(hand)
            valid_plays = [play for play in valid_plays if HandClassifier.compare(play, last_play) == 1]

        return valid_plays