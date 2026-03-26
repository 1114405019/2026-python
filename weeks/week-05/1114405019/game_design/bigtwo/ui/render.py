"""
Big Two Game Renderer

負責遊戲畫面的渲染
"""

import pygame
from typing import List, Tuple, Optional
from bigtwo.game.models import Card, Hand, Player, CardType


class Renderer:
    """遊戲渲染器"""

    # 顏色定義
    COLORS = {
        'background': (45, 45, 45),
        'card_back': (74, 144, 217),
        'spade_club': (255, 255, 255),      # 黑桃、梅花：白色
        'heart_diamond': (231, 76, 60),     # 紅心、方塊：紅色
        'player': (46, 204, 113),           # 玩家：綠色
        'ai': (149, 165, 166),              # AI：灰色
        'selected': (241, 196, 15),         # 選中：黃色
        'button': (52, 152, 219),           # 按鈕：藍色
        'button_hover': (41, 128, 185),     # 按鈕懸停：深藍色
        'text': (255, 255, 255),            # 文字：白色
        'error': (231, 76, 60),             # 錯誤：紅色
    }

    # 卡牌尺寸
    CARD_WIDTH = 60
    CARD_HEIGHT = 90
    CARD_SPACING = 20

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.Font(None, 16)
        self.small_font = pygame.font.Font(None, 12)
        self.large_font = pygame.font.Font(None, 24)

    def draw_card(self, card: Card, x: int, y: int, selected: bool = False) -> None:
        """繪製單張牌"""
        # 卡牌背景
        color = self.COLORS['selected'] if selected else self.COLORS['card_back']
        pygame.draw.rect(self.screen, color, (x, y, self.CARD_WIDTH, self.CARD_HEIGHT), border_radius=5)

        # 邊框
        border_color = self.COLORS['selected'] if selected else (0, 0, 0)
        pygame.draw.rect(self.screen, border_color, (x, y, self.CARD_WIDTH, self.CARD_HEIGHT), 2, border_radius=5)

        # 花色和數字
        suit_color = self.COLORS['spade_club'] if card.suit in [0, 3] else self.COLORS['heart_diamond']
        text = card.RANKS[card.rank]

        # 左上角
        suit_text = pygame.font.Font(None, 14).render(card.SUITS[card.suit], True, suit_color)
        self.screen.blit(suit_text, (x + 5, y + 5))

        rank_text = pygame.font.Font(None, 16).render(text, True, suit_color)
        self.screen.blit(rank_text, (x + 5, y + 20))

        # 右下角（旋轉）
        suit_text_rotated = pygame.transform.rotate(suit_text, 180)
        self.screen.blit(suit_text_rotated, (x + self.CARD_WIDTH - 15, y + self.CARD_HEIGHT - 20))

        rank_text_rotated = pygame.transform.rotate(rank_text, 180)
        self.screen.blit(rank_text_rotated, (x + self.CARD_WIDTH - 15, y + self.CARD_HEIGHT - 35))

    def draw_hand(self, hand: Hand, x: int, y: int, selected_indices: List[int], is_current: bool = False) -> None:
        """繪製手牌"""
        scale = 1.2 if is_current else 0.8
        width = int(self.CARD_WIDTH * scale)
        height = int(self.CARD_HEIGHT * scale)
        spacing = int(self.CARD_SPACING * scale)

        for i, card in enumerate(hand):
            card_x = x + i * spacing
            selected = i in selected_indices
            self.draw_card_scaled(card, card_x, y, selected, scale)

    def draw_card_scaled(self, card: Card, x: int, y: int, selected: bool, scale: float) -> None:
        """繪製縮放的卡牌"""
        width = int(self.CARD_WIDTH * scale)
        height = int(self.CARD_HEIGHT * scale)

        # 卡牌背景
        color = self.COLORS['selected'] if selected else self.COLORS['card_back']
        pygame.draw.rect(self.screen, color, (x, y, width, height), border_radius=5)

        # 邊框
        border_color = self.COLORS['selected'] if selected else (0, 0, 0)
        pygame.draw.rect(self.screen, border_color, (x, y, width, height), 2, border_radius=5)

        if scale >= 1.0:
            # 花色和數字
            suit_color = self.COLORS['spade_club'] if card.suit in [0, 3] else self.COLORS['heart_diamond']
            text = card.RANKS[card.rank]

            font_size = int(14 * scale)
            suit_text = pygame.font.Font(None, font_size).render(card.SUITS[card.suit], True, suit_color)
            self.screen.blit(suit_text, (x + 5, y + 5))

            rank_font_size = int(16 * scale)
            rank_text = pygame.font.Font(None, rank_font_size).render(text, True, suit_color)
            self.screen.blit(rank_text, (x + 5, y + int(20 * scale)))

    def draw_player(self, player: Player, x: int, y: int, is_current: bool) -> None:
        """繪製玩家資訊"""
        color = self.COLORS['player'] if not player.is_ai else self.COLORS['ai']
        name = f"{player.name} ({len(player.hand)} cards)"

        if is_current:
            name = f"> {name} <"

        text = self.font.render(name, True, color)
        self.screen.blit(text, (x, y))

    def draw_last_play(self, cards: Optional[List[Card]], player_name: str, x: int, y: int) -> None:
        """繪製上家出牌"""
        if not cards:
            text = self.small_font.render("No cards played yet", True, self.COLORS['text'])
            self.screen.blit(text, (x, y))
            return

        # 顯示玩家名稱
        player_text = self.small_font.render(f"Last play by {player_name}:", True, self.COLORS['text'])
        self.screen.blit(player_text, (x, y))

        # 繪製卡牌
        card_y = y + 20
        for i, card in enumerate(cards):
            card_x = x + i * (self.CARD_WIDTH + 5)
            self.draw_card(card, card_x, card_y)

    def draw_buttons(self, buttons: List[Tuple[str, Tuple[int, int, int, int]]], mouse_pos: Tuple[int, int]) -> None:
        """繪製按鈕"""
        for text, rect in buttons:
            x, y, w, h = rect
            is_hover = rect[0] <= mouse_pos[0] <= rect[0] + rect[2] and rect[1] <= mouse_pos[1] <= rect[1] + rect[3]

            color = self.COLORS['button_hover'] if is_hover else self.COLORS['button']
            pygame.draw.rect(self.screen, color, rect, border_radius=5)

            # 按鈕文字
            text_surf = self.font.render(text, True, self.COLORS['text'])
            text_rect = text_surf.get_rect(center=(x + w//2, y + h//2))
            self.screen.blit(text_surf, text_rect)

    def draw_message(self, message: str, x: int, y: int, color_key: str = 'text') -> None:
        """繪製訊息"""
        color = self.COLORS.get(color_key, self.COLORS['text'])
        text = self.font.render(message, True, color)
        self.screen.blit(text, (x, y))

    def clear_screen(self) -> None:
        """清除畫面"""
        self.screen.fill(self.COLORS['background'])