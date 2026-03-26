"""
Big Two Game Application

主應用程式，整合遊戲邏輯和UI
"""

import pygame
from typing import Optional
from bigtwo.game.game import BigTwoGame
from bigtwo.ui.render import Renderer
from bigtwo.ui.input import InputHandler


class BigTwoApp:
    """Big Two 遊戲應用"""

    # 視窗設定
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800
    FPS = 60

    # 玩家位置（四人座位）
    PLAYER_POSITIONS = {
        0: (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150),  # 底部（人類玩家）
        1: (SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2),   # 右
        2: (SCREEN_WIDTH // 2, 50),                    # 頂部
        3: (100, SCREEN_HEIGHT // 2)                   # 左
    }

    # 中央出牌區
    CENTER_PLAY_AREA = (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50)

    def __init__(self, screen_width: int = SCREEN_WIDTH, screen_height: int = SCREEN_HEIGHT):
        """初始化應用"""
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Big Two Card Game")

        self.clock = pygame.time.Clock()
        self.running = False

        # 遊戲組件
        self.game = BigTwoGame()
        self.renderer = Renderer(self.screen)
        self.input_handler = InputHandler(self.renderer)

        # AI 回合計時器
        self.ai_timer = 0
        self.ai_delay = 1000  # AI 出牌延遲 1 秒

    def setup(self) -> None:
        """設定遊戲"""
        self.game.setup()
        self.input_handler.clear_selection()

    def render(self) -> None:
        """渲染遊戲畫面"""
        self.renderer.clear_screen()

        # 繪製玩家
        for i, player in enumerate(self.game.players):
            pos = self.PLAYER_POSITIONS[i]
            is_current = (i == self.game.current_player_index)
            selected = self.input_handler.selected_indices if (i == 0 and not player.is_ai) else []

            # 玩家資訊
            self.renderer.draw_player(player, pos[0] - 50, pos[1] - 20, is_current)

            # 手牌
            if i == 0:  # 底部玩家（人類）
                hand_x = pos[0] - (len(player.hand) * int(self.renderer.CARD_SPACING * 1.2)) // 2
                hand_y = pos[1] + 20
                self.renderer.draw_hand(player.hand, hand_x, hand_y, selected, is_current=True)
            else:  # 其他玩家
                hand_x = pos[0] - (len(player.hand) * int(self.renderer.CARD_SPACING * 0.8)) // 2
                hand_y = pos[1] + 20
                self.renderer.draw_hand(player.hand, hand_x, hand_y, [], is_current=False)

        # 繪製中央出牌區
        if self.game.last_play:
            last_player_index = (self.game.current_player_index - 1) % 4
            last_player_name = self.game.players[last_player_index].name
            self.renderer.draw_last_play(self.game.last_play, last_player_name,
                                       self.CENTER_PLAY_AREA[0], self.CENTER_PLAY_AREA[1])
        else:
            self.renderer.draw_last_play(None, "", self.CENTER_PLAY_AREA[0], self.CENTER_PLAY_AREA[1])

        # 繪製按鈕
        mouse_pos = pygame.mouse.get_pos()
        buttons = self.input_handler.get_buttons(self.game)
        self.renderer.draw_buttons(buttons, mouse_pos)

        # 繪製遊戲狀態訊息
        self.draw_game_status()

        pygame.display.flip()

    def draw_game_status(self) -> None:
        """繪製遊戲狀態訊息"""
        screen_width, screen_height = self.screen.get_size()

        # 回合資訊
        round_text = f"Round: {self.game.round_number}"
        self.renderer.draw_message(round_text, 10, 10)

        # 過牌計數
        pass_text = f"Pass count: {self.game.pass_count}"
        self.renderer.draw_message(pass_text, 10, 30)

        # 遊戲結束訊息
        if self.game.is_game_over() and self.game.winner:
            winner_text = f"Game Over! Winner: {self.game.winner.name}"
            self.renderer.draw_message(winner_text, screen_width // 2 - 100, screen_height // 2,
                                    'player' if not self.game.winner.is_ai else 'ai')

        # 當前玩家提示
        current_player = self.game.get_current_player()
        if not current_player.is_ai:
            prompt_text = "Select cards and click Play, or press P to Pass"
            self.renderer.draw_message(prompt_text, screen_width // 2 - 150, screen_height - 100)
        else:
            prompt_text = f"Waiting for {current_player.name} to play..."
            self.renderer.draw_message(prompt_text, screen_width // 2 - 100, screen_height - 100, 'ai')

    def update(self) -> None:
        """更新遊戲邏輯"""
        if self.game.is_game_over():
            return

        current_player = self.game.get_current_player()

        # AI 回合邏輯
        if current_player.is_ai:
            self.ai_timer += self.clock.get_time()
            if self.ai_timer >= self.ai_delay:
                print(f"DEBUG: {current_player.name} 開始思考出牌...")
                try:
                    self.game.ai_turn()
                    print(f"DEBUG: {current_player.name} 出牌結束，換下一位。")
                except Exception as e:
                    print(f"ERROR: AI 出牌出事了！錯誤訊息: {e}")
                    # 如果 AI 壞了，強制跳過它的回合，免得卡死遊戲
                    self.game.pass_turn() 
                
                self.ai_timer = 0

    def handle_events(self) -> bool:
        """處理事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):
                if not self.input_handler.handle_event(event, self.game):
                    return False
        return True

    def run(self) -> None:
        """主遊戲迴圈"""
        self.running = True
        self.setup()

        while self.running:
            if not self.handle_events():
                self.running = False
                break

            self.update()
            self.render()
            self.clock.tick(self.FPS)

        self.cleanup()

    def cleanup(self) -> None:
        """清理資源"""
        pygame.quit()