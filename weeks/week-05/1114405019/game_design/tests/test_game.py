import unittest
from game.models import Card, Deck, Hand, Player
from game.game import BigTwoGame
from game.classifier import CardType


class TestBigTwoGame(unittest.TestCase):
    """測試 BigTwoGame 遊戲流程"""

    def setUp(self):
        """每個測試前的準備"""
        self.game = BigTwoGame()

    def test_game_has_4_players(self):
        """測試遊戲有4位玩家"""
        self.game.setup()
        self.assertEqual(len(self.game.players), 4)

    def test_each_player_13_cards(self):
        """測試每位玩家有13張牌"""
        self.game.setup()
        for player in self.game.players:
            self.assertEqual(len(player.hand), 13)

    def test_total_cards_distributed(self):
        """測試總共發放52張牌"""
        self.game.setup()
        total_cards = sum(len(player.hand) for player in self.game.players)
        self.assertEqual(total_cards, 52)

    def test_first_player_has_3_clubs(self):
        """測試先手玩家持有3♣"""
        self.game.setup()
        first_player = self.game.get_current_player()
        has_3_clubs = any(card.rank == 3 and card.suit == 0 for card in first_player.hand)
        self.assertTrue(has_3_clubs)

    def test_one_human_three_ai(self):
        """測試1人3AI設定"""
        self.game.setup()
        human_count = sum(1 for player in self.game.players if not player.is_ai)
        ai_count = sum(1 for player in self.game.players if player.is_ai)
        self.assertEqual(human_count, 1)
        self.assertEqual(ai_count, 3)

    def test_play_removes_cards(self):
        """測試出牌後手牌減少"""
        self.game.setup()
        player = self.game.get_current_player()
        initial_count = len(player.hand)

        # 出3♣
        three_clubs = next(card for card in player.hand if card.rank == 3 and card.suit == 0)
        result = self.game.play([three_clubs])

        self.assertTrue(result)
        self.assertEqual(len(player.hand), initial_count - 1)

    def test_play_sets_last_play(self):
        """測試出牌設定last_play"""
        self.game.setup()
        player = self.game.get_current_player()

        # 出3♣
        three_clubs = next(card for card in player.hand if card.rank == 3 and card.suit == 0)
        self.game.play([three_clubs])

        self.assertIsNotNone(self.game.last_play)
        self.assertEqual(len(self.game.last_play), 1)
        self.assertEqual(self.game.last_play[0], three_clubs)

    def test_invalid_play(self):
        """測試非法出牌"""
        self.game.setup()
        player = self.game.get_current_player()

        # 嘗試出不是3♣的牌
        other_card = next(card for card in player.hand if not (card.rank == 3 and card.suit == 0))
        result = self.game.play([other_card])

        self.assertFalse(result)

    def test_pass_increments(self):
        """測試過牌計數增加"""
        self.game.setup()
        initial_pass_count = self.game.pass_count

        self.game.pass_turn()
        self.assertEqual(self.game.pass_count, initial_pass_count + 1)

    def test_three_passes_resets(self):
        """測試3人過牌後重置"""
        self.game.setup()
        # 模擬3人過牌
        for _ in range(3):
            self.game.pass_turn()

        self.assertEqual(self.game.pass_count, 0)
        self.assertIsNone(self.game.last_play)

    def test_turn_rotates(self):
        """測試回合輪轉"""
        self.game.setup()
        first_player = self.game.get_current_player()

        self.game.next_turn()
        second_player = self.game.get_current_player()

        self.assertNotEqual(first_player, second_player)

    def test_winner_when_empty(self):
        """測試玩家出完牌時設定勝利者"""
        self.game.setup()
        player = self.game.get_current_player()

        # 清空玩家的手牌
        player.hand = Hand([])

        winner = self.game.check_winner()
        self.assertEqual(winner, player)

    def test_game_over(self):
        """測試遊戲結束判定"""
        self.game.setup()
        player = self.game.get_current_player()
        player.hand = Hand([])  # 清空手牌

        self.assertTrue(self.game.is_game_over())

    def test_not_over(self):
        """測試遊戲未結束"""
        self.game.setup()
        self.assertFalse(self.game.is_game_over())

    def test_ai_turn_plays(self):
        """測試AI回合出牌"""
        self.game.setup()
        # 確保AI玩家持有3♣並成為先手
        ai_player = next(player for player in self.game.players if player.is_ai)
        three_clubs = Card(3, 0)

        # 找到持有3♣的玩家
        current_first_player = self.game.get_current_player()
        if three_clubs not in current_first_player.hand:
            # 如果當前先手沒有3♣，找到有3♣的玩家
            for player in self.game.players:
                if three_clubs in player.hand:
                    current_first_player = player
                    break

        # 如果持有3♣的玩家不是AI，將3♣轉移給AI玩家
        if current_first_player != ai_player:
            current_first_player.hand.remove([three_clubs])
            ai_player.take_cards([three_clubs])

        # 設定AI玩家為先手
        self.game.current_player_index = self.game.players.index(ai_player)

        initial_hand_count = len(ai_player.hand)
        result = self.game.ai_turn()

        # AI應該出牌成功
        self.assertTrue(result)
        self.assertEqual(len(ai_player.hand), initial_hand_count - 1)

    def test_ai_pass(self):
        """測試AI無牌可出時過牌"""
        self.game.setup()
        ai_player = next(player for player in self.game.players if player.is_ai)
        self.game.current_player_index = self.game.players.index(ai_player)

        # 設定一個很強的last_play，讓AI無法出牌
        self.game.last_play = [Card(14, 3), Card(14, 2)]  # 雙A

        # 給AI玩家弱牌
        ai_player.hand = Hand([Card(2, 0), Card(3, 1), Card(4, 2)])  # 弱牌

        initial_pass_count = self.game.pass_count
        result = self.game.ai_turn()

        # AI應該過牌
        self.assertFalse(result)
        self.assertEqual(self.game.pass_count, initial_pass_count + 1)

    def test_same_player_plays_twice(self):
        """測試3人過牌後同一玩家可出任意牌"""
        self.game.setup()
        first_player = self.game.get_current_player()

        # 先出3♣
        three_clubs = next(card for card in first_player.hand if card.rank == 3 and card.suit == 0)
        self.game.play([three_clubs])

        # 模擬其他3人過牌
        for _ in range(3):
            self.game.pass_turn()

        # 現在應該輪到第一個玩家，且last_play應該為None
        current = self.game.get_current_player()
        self.assertEqual(current, first_player)
        self.assertIsNone(self.game.last_play)


if __name__ == '__main__':
    unittest.main()