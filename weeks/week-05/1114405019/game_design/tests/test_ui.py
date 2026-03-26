import unittest
from unittest.mock import Mock, patch
import pygame
from game.models import Card, Hand
from bigtwo.ui.app import BigTwoApp


class TestUIApp(unittest.TestCase):
    """測試 UI 應用"""

    @patch('pygame.display.set_mode')
    @patch('pygame.init')
    @patch('pygame.display.set_caption')
    @patch('pygame.time.Clock')
    @patch('pygame.font.SysFont')
    def test_app_init(self, mock_font, mock_clock, mock_set_caption, mock_init, mock_set_mode):
        """測試應用初始化"""
        mock_screen = Mock()
        mock_set_mode.return_value = mock_screen

        app = BigTwoApp()

        mock_init.assert_called_once()
        mock_set_mode.assert_called_once_with((1200, 800))
        mock_set_caption.assert_called_once_with("Big Two Card Game")
        self.assertIsNotNone(app.game)
        self.assertIsNotNone(app.renderer)
        self.assertIsNotNone(app.input_handler)

    @patch('pygame.display.set_mode')
    @patch('pygame.init')
    @patch('pygame.display.set_caption')
    @patch('pygame.time.Clock')
    @patch('pygame.font.SysFont')
    def test_game_init(self, mock_font, mock_clock, mock_set_caption, mock_init, mock_set_mode):
        """測試遊戲初始化"""
        mock_screen = Mock()
        mock_set_mode.return_value = mock_screen

        app = BigTwoApp()
        app.setup()

        # 檢查遊戲是否正確初始化
        self.assertEqual(len(app.game.players), 4)
        self.assertIsNotNone(app.game.get_current_player())


if __name__ == '__main__':
    unittest.main()