from __future__ import annotations

import pygame
import sys
from typing import List, Optional, Tuple

try:
    from .main import BigTwoGame
    from .models import Card
    from .rules import RuleEngine
    from .evaluator import PatternEvaluator
except ImportError:
    from main import BigTwoGame
    from models import Card
    from rules import RuleEngine
    from evaluator import PatternEvaluator


# 商業級遊戲常數
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
CARD_WIDTH = 60
CARD_HEIGHT = 90
CARD_SPACING = 20

# 字型偏好設定 (解決中文顯示問題)
FONT_PREFERENCE = ['microsoftjhenghei', 'simhei', 'arialunicode', 'arial', 'sans-serif']

# 玩家位置 (中心點)
PLAYER_POSITIONS = {
    0: (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 120),  # 南 - Human
    1: (120, SCREEN_HEIGHT // 2),                  # 西 - V1 立希
    2: (SCREEN_WIDTH // 2, 120),                   # 北 - V2 爽世
    3: (SCREEN_WIDTH - 120, SCREEN_HEIGHT // 2),   # 東 - V3 愛音
}

# 桌面中央位置
TABLE_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# 顏色定義
TABLE_GREEN = (34, 139, 34)    # 深綠色
TABLE_BROWN = (139, 69, 19)    # 咖啡色
CARD_WHITE = (255, 255, 255)
CARD_SELECTED = (255, 255, 200)
BUTTON_NORMAL = (70, 130, 180)
BUTTON_HOVER = (100, 149, 237)
BUTTON_PASS = (220, 20, 60)
BUTTON_PASS_HOVER = (255, 69, 0)


def draw_gradient_background(surface: pygame.Surface) -> None:
    """繪製漸層背景 (深綠到咖啡色)"""
    for y in range(SCREEN_HEIGHT):
        # 從上到下漸層: 深綠 -> 咖啡色
        ratio = y / SCREEN_HEIGHT
        r = int(TABLE_GREEN[0] * (1 - ratio) + TABLE_BROWN[0] * ratio)
        g = int(TABLE_GREEN[1] * (1 - ratio) + TABLE_BROWN[1] * ratio)
        b = int(TABLE_GREEN[2] * (1 - ratio) + TABLE_BROWN[2] * ratio)
        pygame.draw.line(surface, (r, g, b), (0, y), (SCREEN_WIDTH, y))


def draw_card(surface: pygame.Surface, card: Card, pos: Tuple[int, int], selected: bool = False) -> pygame.Rect:
    """繪製高品質撲克牌 (Standard Poker Style)"""
    x, y = pos
    rect = pygame.Rect(x - CARD_WIDTH//2, y - CARD_HEIGHT//2, CARD_WIDTH, CARD_HEIGHT)

    # 卡牌陰影 (更精細)
    shadow_offset = 4
    shadow_rect = rect.move(shadow_offset, shadow_offset)
    pygame.draw.rect(surface, (50, 50, 50, 120), shadow_rect, border_radius=10)

    # 卡牌背景
    base_color = CARD_SELECTED if selected else CARD_WHITE
    pygame.draw.rect(surface, base_color, rect, border_radius=10)

    # 精細邊框
    border_color = (0, 0, 0) if not selected else (255, 215, 0)
    pygame.draw.rect(surface, border_color, rect, 3, border_radius=10)

    # 內部精細線條
    inner_rect = rect.inflate(-6, -6)
    pygame.draw.rect(surface, (200, 200, 200), inner_rect, 1, border_radius=6)

    # 選中光暈
    if selected:
        glow_color = (255, 255, 0, 80)
        glow_surface = pygame.Surface((rect.width + 20, rect.height + 20), pygame.SRCALPHA)
        pygame.draw.rect(glow_surface, glow_color, glow_surface.get_rect(), border_radius=12)
        surface.blit(glow_surface, (rect.x - 10, rect.y - 10))

    # 繪製花色符號 (正確的撲克牌形狀)
    suit_color = (255, 0, 0) if card.suit_str() in ['♥', '♦'] else (0, 0, 0)
    symbol_size = 20

    # 符號位置 (左上角)
    symbol_x = x - CARD_WIDTH//2 + 8
    symbol_y = y - CARD_HEIGHT//2 + 8

    draw_suit_symbol(surface, card.suit_str(), (symbol_x, symbol_y), symbol_size, suit_color)

    # 繪製數字 (右下角)
    rank_font = pygame.font.Font(None, 18)
    rank_text = rank_font.render(card.rank_str(), True, suit_color)
    rank_rect = rank_text.get_rect()
    rank_rect.bottomright = (x + CARD_WIDTH//2 - 6, y + CARD_HEIGHT//2 - 6)
    surface.blit(rank_text, rank_rect)

    return rect


def draw_suit_symbol(surface: pygame.Surface, suit: str, pos: Tuple[int, int], size: int, color: Tuple[int, int, int]) -> None:
    """Draw clear suit symbols using standard geometric shapes"""
    x, y = pos
    center_x, center_y = x + size // 2, y + size // 2

    if suit == '♠':  # Spade - Black
        # Upper triangle
        pygame.draw.polygon(surface, (0, 0, 0), [
            (center_x, y),
            (x + size//4, center_y - size//4),
            (x + 3*size//4, center_y - size//4)
        ])
        # Lower triangle (inverted)
        pygame.draw.polygon(surface, (0, 0, 0), [
            (center_x, y + size),
            (x + size//4, center_y + size//4),
            (x + 3*size//4, center_y + size//4)
        ])
        # Stem
        pygame.draw.rect(surface, (0, 0, 0), (center_x - 1, center_y, 2, size//2))

    elif suit == '♥':  # Heart - Red
        # Left half-circle
        pygame.draw.circle(surface, (255, 0, 0), (center_x - size//4, center_y - size//4), size//4)
        # Right half-circle
        pygame.draw.circle(surface, (255, 0, 0), (center_x + size//4, center_y - size//4), size//4)
        # Bottom triangle
        pygame.draw.polygon(surface, (255, 0, 0), [
            (center_x, center_y - size//4),
            (x, center_y + size//4),
            (x + size, center_y + size//4)
        ])

    elif suit == '♦':  # Diamond - Red
        # Simple diamond shape
        pygame.draw.polygon(surface, (255, 0, 0), [
            (center_x, y),
            (x + size, center_y),
            (center_x, y + size),
            (x, center_y)
        ])

    elif suit == '♣':  # Club - Black
        # Three circles
        circle_radius = size // 6
        pygame.draw.circle(surface, (0, 0, 0), (center_x - size//4, center_y - size//4), circle_radius)
        pygame.draw.circle(surface, (0, 0, 0), (center_x + size//4, center_y - size//4), circle_radius)
        pygame.draw.circle(surface, (0, 0, 0), (center_x, center_y + size//4), circle_radius)
        # Stem
        pygame.draw.rect(surface, (0, 0, 0), (center_x - 1, center_y, 2, size//2))


class GameGUI:
    def __init__(self, player_names: List[str], seed: Optional[int] = None) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Big Two - Professional Edition")
        self.clock = pygame.time.Clock()

        # Initialize fonts
        self.font = pygame.font.Font(None, 24)
        self.large_font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 18)

        # 載入頭像
        self.avatars = self.load_avatars()

        # Standard player names
        player_names = ["Player 1 (You)", "Player 2", "Player 3", "Player 4"]
        self.game = BigTwoGame(player_names, seed=seed)
        self.game.start_game()

        self.selected_indices: List[int] = []
        self.warning: Optional[str] = None
        self.current_pattern: Optional[str] = None
        self.ai_animation: Optional[dict] = None  # AI 出牌動畫狀態

        # 按鈕
        self.play_button_rect = pygame.Rect(SCREEN_WIDTH - 200, SCREEN_HEIGHT - 120, 160, 50)
        self.pass_button_rect = pygame.Rect(SCREEN_WIDTH - 200, SCREEN_HEIGHT - 60, 160, 50)

        # 玩家頭像框 (圓形)
        self.avatar_radius = 40

    def load_font(self, font_preferences: List[str], size: int) -> pygame.font.Font:
        """載入字型，依偏好順序嘗試"""
        for font_name in font_preferences:
            try:
                return pygame.font.SysFont(font_name, size)
            except:
                continue
        # 如果都失敗，使用預設字型
        return pygame.font.Font(None, size)

    def load_avatars(self) -> dict[int, Optional[pygame.Surface]]:
        """載入玩家頭像"""
        avatars = {}
        avatar_files = {
            1: "taki.png",   # V1 立希
            2: "soyo.png",   # V2 爽世
            3: "anon.png"    # V3 愛音
        }

        for player_index, filename in avatar_files.items():
            try:
                # 嘗試從 assets 資料夾載入
                image = pygame.image.load(f"assets/{filename}")
                # 縮放到適當大小
                image = pygame.transform.scale(image, (self.avatar_radius * 2, self.avatar_radius * 2))
                avatars[player_index] = image
            except:
                avatars[player_index] = None  # 沒有圖片時為 None

        return avatars

    def run(self) -> None:
        while True:
            self.handle_events()
            self.update_ai_turns()
            self.update_animations()
            self.render()
            pygame.display.flip()
            self.clock.tick(60)  # 提高到 60 FPS 以獲得更流暢的動畫

    def handle_events(self) -> None:
        mouse_pos = pygame.mouse.get_pos()
        self.play_button_hovered = self.play_button_rect.collidepoint(mouse_pos)
        self.pass_button_hovered = self.pass_button_rect.collidepoint(mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.handle_click(event.pos)
                self.handle_click(event.pos)

    def handle_click(self, pos: Tuple[int, int]) -> None:
        if self.is_human_turn() and not self.ai_animation:
            # 檢查是否點擊了手牌
            hand_rects = self.get_human_hand_rects()
            for index, rect in enumerate(hand_rects):
                if rect.collidepoint(pos):
                    if index in self.selected_indices:
                        self.selected_indices.remove(index)
                    else:
                        self.selected_indices.append(index)
                    self.update_selected_pattern()
                    return

            # 檢查按鈕
            if self.play_button_rect.collidepoint(pos):
                self.try_play()
                return
            if self.pass_button_rect.collidepoint(pos):
                self.do_pass()
                return

    def update_selected_pattern(self) -> None:
        """更新選中牌的牌型顯示"""
        if not self.selected_indices:
            self.current_pattern = None
            return

        hand = self.game.players[0].hand
        selected_cards = [hand[i] for i in self.selected_indices if i < len(hand)]
        if not selected_cards:
            self.current_pattern = None
            return

        result = PatternEvaluator.classify(selected_cards)
        if result:
            pattern_names = {
                1: "單張",
                2: "對子",
                3: "順子",
                4: "葫蘆",
                5: "四條",
                6: "同花順"
            }
            self.current_pattern = pattern_names.get(result.pattern_type, "無效牌型")
        else:
            self.current_pattern = "無效牌型"

    def is_human_turn(self) -> bool:
        return self.game.turn_manager.get_current_player_index() == 0 and not self.game.game_over

    def get_human_hand_rects(self) -> List[pygame.Rect]:
        """獲取人類玩家手牌的碰撞箱"""
        hand = self.game.players[0].hand
        rects: List[pygame.Rect] = []
        center_x, center_y = PLAYER_POSITIONS[0]

        # 計算起始位置以居中顯示
        total_width = len(hand) * (CARD_WIDTH + CARD_SPACING) - CARD_SPACING
        start_x = center_x - total_width // 2

        for i, _ in enumerate(hand):
            x = start_x + i * (CARD_WIDTH + CARD_SPACING) + CARD_WIDTH // 2
            y = center_y
            if i in self.selected_indices:
                y -= 15  # 選中時上移
            rects.append(pygame.Rect(x - CARD_WIDTH//2, y - CARD_HEIGHT//2, CARD_WIDTH, CARD_HEIGHT))
        return rects

    def try_play(self) -> None:
        if not self.is_human_turn() or self.ai_animation:
            return

        hand = self.game.players[0].hand
        selected_cards = [hand[i] for i in self.selected_indices if i < len(hand)]
        if not selected_cards:
            self.warning = "請選擇要出的牌。"
            return

        last_play = self.game.turn_manager.last_play
        can_play = self.game.rule_engine.can_beat(last_play, selected_cards, is_first_turn=(last_play is None and self.game.turn_manager.pass_count == 0))
        if not can_play:
            self.warning = "無效出牌，請選擇其他牌或 PASS。"
            return

        if self.game.process_play(selected_cards):
            self.selected_indices = []
            self.warning = None
            self.current_pattern = None
        else:
            self.warning = "出牌失敗。"

    def do_pass(self) -> None:
        if not self.is_human_turn() or self.ai_animation:
            return
        self.game.process_play([])
        self.selected_indices = []
        self.warning = None
        self.current_pattern = None

    def update_ai_turns(self) -> None:
        if not self.game.game_over and not self.is_human_turn() and not self.ai_animation:
            current_index = self.game.turn_manager.get_current_player_index()
            hand = self.game.players[current_index].hand
            last_play = self.game.turn_manager.last_play
            played = False
            selected_card = None

            # 找出最小的合法牌
            for card in sorted(hand, key=lambda c: c.power):
                if self.game.rule_engine.can_beat(last_play, [card], is_first_turn=(last_play is None and self.game.turn_manager.pass_count == 0)):
                    selected_card = card
                    played = True
                    break

            if played and selected_card:
                # 啟動出牌動畫
                start_pos = PLAYER_POSITIONS[current_index]
                self.ai_animation = {
                    'card': selected_card,
                    'start_pos': start_pos,
                    'end_pos': TABLE_CENTER,
                    'progress': 0.0,
                    'duration': 30,  # 0.5 秒動畫 (60 FPS)
                    'will_play': True
                }
            else:
                # 啟動 PASS 動畫
                start_pos = PLAYER_POSITIONS[current_index]
                self.ai_animation = {
                    'card': None,
                    'start_pos': start_pos,
                    'end_pos': TABLE_CENTER,
                    'progress': 0.0,
                    'duration': 30,
                    'will_play': False
                }

    def update_animations(self) -> None:
        """更新動畫狀態"""
        if self.ai_animation:
            self.ai_animation['progress'] += 1.0 / self.ai_animation['duration']
            if self.ai_animation['progress'] >= 1.0:
                # 動畫完成，執行實際出牌
                if self.ai_animation['will_play'] and self.ai_animation['card']:
                    self.game.process_play([self.ai_animation['card']])
                else:
                    self.game.process_play([])
                self.ai_animation = None

    def render(self) -> None:
        # 繪製漸層背景
        draw_gradient_background(self.screen)

        # 渲染各個元件
        self.render_players()
        self.render_table()
        self.render_animations()
        self.render_ui()

    def render_players(self) -> None:
        """渲染所有玩家"""
        for i, player in enumerate(self.game.players):
            pos = PLAYER_POSITIONS[i]
            self.render_player_avatar(i, pos)
            self.render_player_hand(i, pos)

    def render_player_avatar(self, player_index: int, pos: Tuple[int, int]) -> None:
        """渲染玩家頭像和資訊"""
        x, y = pos

        # 渲染頭像
        if player_index in self.avatars and self.avatars[player_index]:
            # 有頭像圖片
            avatar_rect = self.avatars[player_index].get_rect(center=pos)
            self.screen.blit(self.avatars[player_index], avatar_rect)
            # 圓形邊框
            pygame.draw.circle(self.screen, (255, 255, 255), pos, self.avatar_radius, 3)
        else:
            # 沒有圖片時畫漸層圓形
            self.draw_gradient_circle(pos, self.avatar_radius)
            pygame.draw.circle(self.screen, (255, 255, 255), pos, self.avatar_radius, 3)

            # 在圓形中寫名字縮寫
            name = self.game.players[player_index].name
            if player_index == 0:
                initial = "H"
            else:
                # 提取中文名字的第一個字
                initial = name.split()[1][0] if len(name.split()) > 1 else name[0]

            initial_font = pygame.font.Font(None, 32)
            initial_text = initial_font.render(initial, True, (255, 255, 255))
            initial_rect = initial_text.get_rect(center=pos)
            self.screen.blit(initial_text, initial_rect)

        # 玩家名稱
        name = self.game.players[player_index].name
        name_text = self.font.render(name, True, (255, 255, 255))
        name_rect = name_text.get_rect(center=(x, y + self.avatar_radius + 20))
        self.screen.blit(name_text, name_rect)

        # 剩餘牌數
        cards_left = len(self.game.players[player_index].hand)
        cards_text = self.small_font.render(f"{cards_left} cards", True, (255, 255, 255))
        cards_rect = cards_text.get_rect(center=(x, y + self.avatar_radius + 40))
        self.screen.blit(cards_text, cards_rect)

        # 當前玩家指示器
        if self.game.turn_manager.get_current_player_index() == player_index and not self.game.game_over:
            indicator_color = (255, 255, 0) if player_index == 0 else (255, 100, 100)
            pygame.draw.circle(self.screen, indicator_color, (x, y - self.avatar_radius - 10), 8)

    def draw_gradient_circle(self, center: Tuple[int, int], radius: int) -> None:
        """繪製漸層圓形"""
        x, y = center
        for r in range(radius, 0, -1):
            # 從中心到邊緣的漸層
            ratio = r / radius
            color = (
                int(100 + 100 * ratio),  # 紅色漸層
                int(150 + 50 * ratio),   # 綠色漸層
                int(200 + 55 * ratio)    # 藍色漸層
            )
            pygame.draw.circle(self.screen, color, (x, y), r)

    def render_player_hand(self, player_index: int, pos: Tuple[int, int]) -> None:
        """渲染玩家手牌"""
        if player_index == 0:  # Human player - 顯示實際牌
            hand = self.game.players[0].hand
            rects = self.get_human_hand_rects()
            for i, (card, rect) in enumerate(zip(hand, rects)):
                selected = i in self.selected_indices
                draw_card(self.screen, card, (rect.centerx, rect.centery), selected)
        else:  # AI players - 只顯示牌背
            hand_size = len(self.game.players[player_index].hand)
            if hand_size > 0:
                x, y = pos
                # 根據位置調整手牌顯示方向
                if player_index == 1:  # 西
                    for i in range(min(hand_size, 5)):  # 最多顯示5張
                        card_x = x - 80 - i * 15
                        card_y = y - 20 + i * 5
                        self.draw_card_back((card_x, card_y))
                elif player_index == 2:  # 北
                    for i in range(min(hand_size, 7)):  # 最多顯示7張
                        card_x = x - 60 + i * 15
                        card_y = y - 80 - i * 3
                        self.draw_card_back((card_x, card_y))
                elif player_index == 3:  # 東
                    for i in range(min(hand_size, 5)):  # 最多顯示5張
                        card_x = x + 80 + i * 15
                        card_y = y - 20 + i * 5
                        self.draw_card_back((card_x, card_y))

    def draw_card_back(self, pos: Tuple[int, int]) -> None:
        """繪製牌背"""
        x, y = pos
        rect = pygame.Rect(x - CARD_WIDTH//2, y - CARD_HEIGHT//2, CARD_WIDTH, CARD_HEIGHT)

        # 牌背圖案 (藍色漸層)
        pygame.draw.rect(self.screen, (70, 130, 180), rect, border_radius=6)
        pygame.draw.rect(self.screen, (30, 60, 120), rect, 2, border_radius=6)

        # 簡單花紋
        pattern_color = (100, 160, 200)
        pygame.draw.circle(self.screen, pattern_color, (x, y), 8)
        pygame.draw.circle(self.screen, pattern_color, (x-12, y-12), 4)
        pygame.draw.circle(self.screen, pattern_color, (x+12, y+12), 4)

    def render_table(self) -> None:
        """渲染桌面中央區域 (高質感牌池)"""
        # Card Pool Area - with rounded corners and shadow
        pool_rect = pygame.Rect(350, 280, 580, 240)

        # 陰影
        shadow_rect = pool_rect.move(6, 6)
        pygame.draw.rect(self.screen, (0, 0, 0, 100), shadow_rect, border_radius=25)

        # 主體 - 深咖啡色漸層
        pygame.draw.rect(self.screen, (101, 67, 33), pool_rect, border_radius=20)
        # 內部亮邊
        inner_rect = pool_rect.inflate(-8, -8)
        pygame.draw.rect(self.screen, (139, 101, 67), inner_rect, border_radius=15)

        # 金色邊框
        pygame.draw.rect(self.screen, (218, 165, 32), pool_rect, 4, border_radius=20)

        # 標題
        title_text = self.large_font.render("Card Pool", True, (255, 215, 0))
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 300))
        self.screen.blit(title_text, title_rect)

        # Display last play
        last_play = self.game.turn_manager.last_play
        last_player = self.game.turn_manager.last_player_index

        if last_play and last_player is not None:
            player_name = self.game.players[last_player].name
            last_play_title = self.font.render(f"Last Play by: {player_name}", True, (255, 255, 255))
            title_rect = last_play_title.get_rect(center=(SCREEN_WIDTH // 2, 340))
            self.screen.blit(last_play_title, title_rect)

            # Display cards played - centered
            total_width = len(last_play) * (CARD_WIDTH + 10) - 10
            start_x = SCREEN_WIDTH // 2 - total_width // 2

            for i, card in enumerate(last_play):
                card_x = start_x + i * (CARD_WIDTH + 10) + CARD_WIDTH // 2
                card_y = 400
                draw_card(self.screen, card, (card_x, card_y), False)
        else:
            waiting_text = self.font.render("Waiting for player to play...", True, (200, 200, 200))
            waiting_rect = waiting_text.get_rect(center=(SCREEN_WIDTH // 2, 400))
            self.screen.blit(waiting_text, waiting_rect)

    def render_animations(self) -> None:
        """渲染動畫效果"""
        if self.ai_animation:
            progress = self.ai_animation['progress']
            start_pos = self.ai_animation['start_pos']
            end_pos = self.ai_animation['end_pos']

            # 計算當前位置 (簡單線性插值)
            current_x = start_pos[0] + (end_pos[0] - start_pos[0]) * progress
            current_y = start_pos[1] + (end_pos[1] - start_pos[1]) * progress

            if self.ai_animation['card']:
                # 繪製移動中的牌
                draw_card(self.screen, self.ai_animation['card'], (int(current_x), int(current_y)), False)
            else:
                # PASS 動畫 - 顯示 "PASS" 文字
                pass_text = self.large_font.render("PASS", True, (255, 0, 0))
                pass_rect = pass_text.get_rect(center=(int(current_x), int(current_y)))
                self.screen.blit(pass_text, pass_rect)

    def render_ui(self) -> None:
        """渲染使用者介面"""
        # 當前狀態
        current_index = self.game.turn_manager.get_current_player_index()
        if not self.game.game_over:
            status_text = f"輪到: {self.game.players[current_index].name}"
            status_color = (255, 255, 255) if current_index == 0 else (255, 200, 200)
        else:
            status_text = f"遊戲結束! {self.game.winner.name} 獲勝!"
            status_color = (255, 255, 0)

        status_label = self.large_font.render(status_text, True, status_color)
        self.screen.blit(status_label, (20, 20))

        # 選中牌型顯示
        if self.current_pattern:
            pattern_text = f"選中牌型: {self.current_pattern}"
            pattern_label = self.font.render(pattern_text, True, (255, 255, 0))
            self.screen.blit(pattern_label, (20, 60))

        # 警告訊息
        if self.warning:
            warning_label = self.font.render(self.warning, True, (255, 100, 100))
            self.screen.blit(warning_label, (20, 100))

        # 按鈕 (只在人類回合顯示)
        if self.is_human_turn() and not self.ai_animation:
            self.render_buttons()

    def render_buttons(self) -> None:
        """渲染 3D 風格按鈕"""
        self.render_3d_button(self.play_button_rect, "PLAY",
                             getattr(self, 'play_button_hovered', False))
        self.render_3d_button(self.pass_button_rect, "PASS",
                             getattr(self, 'pass_button_hovered', False), is_pass=True)

    def render_3d_button(self, rect: pygame.Rect, text: str, hovered: bool, is_pass: bool = False) -> None:
        """渲染 3D 風格按鈕"""
        # 按鈕顏色
        if is_pass:
            base_color = BUTTON_PASS_HOVER if hovered else BUTTON_PASS
        else:
            base_color = BUTTON_HOVER if hovered else BUTTON_NORMAL

        # 3D 效果 - 主體
        pygame.draw.rect(self.screen, base_color, rect, border_radius=15)

        # 高光 (上邊和左邊)
        highlight_color = (
            min(base_color[0] + 40, 255),
            min(base_color[1] + 40, 255),
            min(base_color[2] + 40, 255)
        )
        # 上邊高光
        top_highlight = pygame.Rect(rect.x + 3, rect.y + 3, rect.width - 6, 6)
        pygame.draw.rect(self.screen, highlight_color, top_highlight, border_radius=12)
        # 左邊高光
        left_highlight = pygame.Rect(rect.x + 3, rect.y + 3, 6, rect.height - 6)
        pygame.draw.rect(self.screen, highlight_color, left_highlight, border_radius=12)

        # 陰影 (下邊和右邊)
        shadow_color = (
            max(base_color[0] - 40, 0),
            max(base_color[1] - 40, 0),
            max(base_color[2] - 40, 0)
        )
        # 下邊陰影
        bottom_shadow = pygame.Rect(rect.x + 3, rect.y + rect.height - 9, rect.width - 6, 6)
        pygame.draw.rect(self.screen, shadow_color, bottom_shadow, border_radius=12)
        # 右邊陰影
        right_shadow = pygame.Rect(rect.x + rect.width - 9, rect.y + 3, 6, rect.height - 6)
        pygame.draw.rect(self.screen, shadow_color, right_shadow, border_radius=12)

        # 外框
        pygame.draw.rect(self.screen, (0, 0, 0), rect, 2, border_radius=15)

        # 文字
        button_text = self.large_font.render(text, True, (255, 255, 255))
        text_rect = button_text.get_rect(center=rect.center)
        self.screen.blit(button_text, text_rect)


if __name__ == "__main__":
    gui = GameGUI(["Human", "V1 立希 (Taki)", "V2 爽世 (Soyo)", "V3 愛音 (Anon)"], seed=42)
    gui.run()
