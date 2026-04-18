import sys

import pygame

from robot_core import RobotManager


MAP_WIDTH = 5
MAP_HEIGHT = 5
CELL_SIZE = 80
MARGIN = 20
HUD_HEIGHT = 140
WINDOW_WIDTH = (MAP_WIDTH + 1) * CELL_SIZE + MARGIN * 2
WINDOW_HEIGHT = (MAP_HEIGHT + 1) * CELL_SIZE + MARGIN * 2 + HUD_HEIGHT
BACKGROUND_COLOR = (30, 30, 30)
GRID_COLOR = (80, 80, 80)
LINE_COLOR = (120, 120, 120)
ROBOT_COLOR = (240, 220, 70)
SCENT_COLOR = (220, 80, 80)
TEXT_COLOR = (240, 240, 240)

DIRECTION_ARROWS = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0),
}


def world_to_screen(x: int, y: int) -> tuple[int, int]:
    """Convert UVA world coordinates to pygame screen coordinates."""
    screen_x = MARGIN + x * CELL_SIZE
    screen_y = MARGIN + (MAP_HEIGHT - y) * CELL_SIZE
    return screen_x, screen_y


def draw_grid(surface: pygame.Surface) -> None:
    for row in range(MAP_HEIGHT + 2):
        start_pos = (MARGIN, MARGIN + row * CELL_SIZE)
        end_pos = (MARGIN + (MAP_WIDTH + 1) * CELL_SIZE, MARGIN + row * CELL_SIZE)
        pygame.draw.line(surface, LINE_COLOR, start_pos, end_pos, 1)

    for col in range(MAP_WIDTH + 2):
        start_pos = (MARGIN + col * CELL_SIZE, MARGIN)
        end_pos = (MARGIN + col * CELL_SIZE, MARGIN + (MAP_HEIGHT + 1) * CELL_SIZE)
        pygame.draw.line(surface, LINE_COLOR, start_pos, end_pos, 1)


def draw_scent(surface: pygame.Surface, scent: set[tuple[int, int, str]]) -> None:
    for x, y, _dir in scent:
        screen_x, screen_y = world_to_screen(x, y)
        center = (screen_x + CELL_SIZE // 2, screen_y + CELL_SIZE // 2)
        radius = CELL_SIZE // 6
        pygame.draw.circle(surface, SCENT_COLOR, center, radius)
        pygame.draw.line(
            surface,
            BACKGROUND_COLOR,
            (center[0] - radius, center[1] - radius),
            (center[0] + radius, center[1] + radius),
            2,
        )
        pygame.draw.line(
            surface,
            BACKGROUND_COLOR,
            (center[0] + radius, center[1] - radius),
            (center[0] - radius, center[1] + radius),
            2,
        )


def draw_robot(surface: pygame.Surface, manager: RobotManager) -> None:
    screen_x, screen_y = world_to_screen(manager.x, manager.y)
    center_x = screen_x + CELL_SIZE // 2
    center_y = screen_y + CELL_SIZE // 2
    direction = manager.dir
    dx, dy = DIRECTION_ARROWS[direction]
    length = CELL_SIZE * 0.35

    points = [
        (center_x + dx * length, center_y + dy * length),
        (center_x - dy * length * 0.5, center_y + dx * length * 0.5),
        (center_x + dy * length * 0.5, center_y - dx * length * 0.5),
    ]

    pygame.draw.polygon(surface, ROBOT_COLOR, points)
    pygame.draw.circle(surface, (50, 50, 50), (center_x, center_y), 10)


def draw_hud(surface: pygame.Surface, manager: RobotManager, font: pygame.font.Font | None) -> None:
    if font is None:
        return  # Skip HUD rendering if font is not available

    hud_x = MARGIN
    hud_y = MARGIN + (MAP_HEIGHT + 1) * CELL_SIZE + 10
    status_text = f"Position: ({manager.x}, {manager.y})  Dir: {manager.dir}  LOST: {manager.lost}"
    scent_text = f"Scent count: {len(manager.scent)}"
    help_text = "Controls: L/R/F - move | N - new robot | C - clear scent | ESC - exit"

    status_surface = font.render(status_text, True, TEXT_COLOR)
    scent_surface = font.render(scent_text, True, TEXT_COLOR)
    help_surface = font.render(help_text, True, TEXT_COLOR)
    info_surface = font.render("Origin: UVA (0,0) bottom-left", True, TEXT_COLOR)

    surface.blit(status_surface, (hud_x, hud_y))
    surface.blit(scent_surface, (hud_x, hud_y + 30))
    surface.blit(help_surface, (hud_x, hud_y + 60))
    surface.blit(info_surface, (hud_x, hud_y + 90))


def main() -> None:
    try:
        pygame.init()
    except Exception as e:
        print(f"pygame.init() failed: {e}. Initializing modules manually.")
        pygame.display.init()
        pygame.event.init()
        try:
            pygame.font.init()
        except Exception as font_e:
            print(f"pygame.font.init() failed: {font_e}. Font rendering may not work.")

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Robot Lost Simulator")
    try:
        font = pygame.font.Font(None, 24)
    except Exception as e:
        print(f"Failed to create font: {e}. Using fallback.")
        font = None  # Fallback if font creation fails

    clock = pygame.time.Clock()

    manager = RobotManager(width=MAP_WIDTH, height=MAP_HEIGHT, x=0, y=0, dir="N")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_l:
                    manager.execute_command("L")
                elif event.key == pygame.K_r:
                    manager.execute_command("R")
                elif event.key == pygame.K_f:
                    manager.execute_command("F")
                elif event.key == pygame.K_n:
                    manager = RobotManager(
                        width=MAP_WIDTH,
                        height=MAP_HEIGHT,
                        x=0,
                        y=0,
                        dir="N",
                        scent=manager.scent,
                    )
                elif event.key == pygame.K_c:
                    manager.scent.clear()

        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(
            screen,
            GRID_COLOR,
            (MARGIN, MARGIN, (MAP_WIDTH + 1) * CELL_SIZE, (MAP_HEIGHT + 1) * CELL_SIZE),
        )
        draw_grid(screen)
        draw_scent(screen, manager.scent)
        draw_robot(screen, manager)
        if font:
            draw_hud(screen, manager, font)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
