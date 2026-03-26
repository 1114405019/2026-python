"""
Big Two Game Input Handler

負責處理用戶輸入事件
"""

import pygame
from typing import List, Tuple
from bigtwo.game.game import BigTwoGame


class InputHandler:
    """輸入處理器"""

    def __init__(self, renderer):
        self.renderer = renderer
        self.selected_indices: List[int] = []

    def handle_event(self, event: pygame.event.Event, game: BigTwoGame) -> bool:
        """處理單個事件"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.handle_click(event.pos, game)
        elif event.type == pygame.KEYDOWN:
            return self.handle_key(event.key, game)
        return True

    def handle_click(self, pos: Tuple[int, int], game: BigTwoGame) -> bool:
        """處理滑鼠點擊"""
        x, y = pos

        # 檢查按鈕點擊
        buttons = self.get_buttons(game)
        for button_text, rect in buttons:
            if self.is_point_in_rect(pos, rect):
                return self.handle_button_click(button_text, game)

        # 檢查手牌點擊（只對人類玩家）
        current_player = game.get_current_player()
        if not current_player.is_ai:
            if self.handle_hand_click(pos, current_player.hand, game):
                return True

        return True

    def handle_key(self, key: int, game: BigTwoGame) -> bool:
        """處理鍵盤輸入"""
        if key == pygame.K_RETURN:  # Enter
            return self.try_play(game)
        elif key == pygame.K_p:  # P
            game.pass_turn()
            return True
        elif key == pygame.K_r:  # R - 重新開始
            game.setup()
            self.selected_indices = []
            return True
        elif key == pygame.K_ESCAPE:  # ESC
            return False
        return True

    def handle_button_click(self, button_text: str, game: BigTwoGame) -> bool:
        """處理按鈕點擊"""
        if button_text == "Play":
            return self.try_play(game)
        elif button_text == "Pass":
            game.pass_turn()
            return True
        elif button_text == "New Game":
            game.setup()
            self.selected_indices = []
            return True
        return True

    def handle_hand_click(self, pos: Tuple[int, int], hand: List, game: BigTwoGame) -> bool:
        """處理手牌點擊"""
        # 計算點擊的卡牌索引
        hand_x, hand_y = self.get_hand_position(game)
        scale = 1.2  # 當前玩家手牌放大比例
        spacing = int(self.renderer.CARD_SPACING * scale)

        for i, card in enumerate(hand):
            card_x = hand_x + i * spacing
            card_width = int(self.renderer.CARD_WIDTH * scale)
            card_height = int(self.renderer.CARD_HEIGHT * scale)

            if (card_x <= pos[0] <= card_x + card_width and
                hand_y <= pos[1] <= hand_y + card_height):
                # 切換選中狀態
                if i in self.selected_indices:
                    self.selected_indices.remove(i)
                else:
                    self.selected_indices.append(i)
                return True
        return False

    def try_play(self, game: BigTwoGame) -> bool:
        """嘗試出牌"""
        if not self.selected_indices:
            return True  # 沒有選牌，不做任何事

        current_player = game.get_current_player()
        selected_cards = [current_player.hand[i] for i in sorted(self.selected_indices)]

        # 嘗試出牌
        if game.play(selected_cards):
            # 出牌成功，清空選中
            self.selected_indices = []
            return True
        else:
            # 出牌失敗，保持選中狀態
            return True

    def get_buttons(self, game: BigTwoGame) -> List[Tuple[str, Tuple[int, int, int, int]]]:
        """取得按鈕列表"""
        screen_width, screen_height = self.renderer.screen.get_size()
        button_width, button_height = 100, 40
        button_y = screen_height - 60

        buttons = []

        # Play 按鈕
        play_x = screen_width // 2 - button_width - 10
        buttons.append(("Play", (play_x, button_y, button_width, button_height)))

        # Pass 按鈕
        pass_x = screen_width // 2 + 10
        buttons.append(("Pass", (pass_x, button_y, button_width, button_height)))

        # New Game 按鈕（遊戲結束時顯示）
        if game.is_game_over():
            new_game_x = screen_width - button_width - 20
            buttons.append(("New Game", (new_game_x, button_y, button_width, button_height)))

        return buttons

    def get_hand_position(self, game: BigTwoGame) -> Tuple[int, int]:
        """取得當前玩家手牌位置"""
        screen_width, screen_height = self.renderer.screen.get_size()
        hand_y = screen_height - 200  # 距離底部200像素
        hand_x = screen_width // 2 - (len(game.get_current_player().hand) * int(self.renderer.CARD_SPACING * 1.2)) // 2
        return hand_x, hand_y

    def is_point_in_rect(self, point: Tuple[int, int], rect: Tuple[int, int, int, int]) -> bool:
        """檢查點是否在矩形內"""
        px, py = point
        rx, ry, rw, rh = rect
        return rx <= px <= rx + rw and ry <= py <= ry + rh

    def clear_selection(self) -> None:
        """清空選中"""
        self.selected_indices = []