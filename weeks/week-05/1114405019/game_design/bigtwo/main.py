#!/usr/bin/env python3
"""
Big Two Card Game - Main Entry Point

啟動遊戲應用程式
"""

from bigtwo.ui.app import BigTwoApp


def main():
    """主函數"""
    app = BigTwoApp()
    app.run()


if __name__ == "__main__":
    main()