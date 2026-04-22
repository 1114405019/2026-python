from __future__ import annotations

from dataclasses import dataclass, field
from typing import Set, Tuple

DIRECTIONS = ["N", "E", "S", "W"]
MOVES = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


@dataclass
class RobotManager:
    width: int
    height: int
    scent: Set[Tuple[int, int, str]] = field(default_factory=set)
    x: int = 0
    y: int = 0
    dir: str = "N"
    lost: bool = False

    def __post_init__(self) -> None:
        if self.dir not in DIRECTIONS:
            raise ValueError(f"Invalid direction: {self.dir}")
        if self.width < 0 or self.height < 0:
            raise ValueError("Width and height must be non-negative")

    def execute_command(self, cmd: str) -> None:
        if self.lost:
            return

        if cmd == "L":
            self._rotate(-1)
        elif cmd == "R":
            self._rotate(1)
        elif cmd == "F":
            self._move_forward()
        else:
            raise ValueError(f"Unsupported command: {cmd}")

    def _rotate(self, step: int) -> None:
        current_index = DIRECTIONS.index(self.dir)
        new_index = (current_index + step) % len(DIRECTIONS)
        self.dir = DIRECTIONS[new_index]

    def _move_forward(self) -> None:
        dx, dy = MOVES[self.dir]
        next_x = self.x + dx
        next_y = self.y + dy

        if not self._is_within_bounds(next_x, next_y):
            if (self.x, self.y, self.dir) in self.scent:
                return
            self.scent.add((self.x, self.y, self.dir))
            self.lost = True
            return

        self.x = next_x
        self.y = next_y

    def _is_within_bounds(self, x: int, y: int) -> bool:
        return 0 <= x <= self.width and 0 <= y <= self.height

    def current_state(self) -> Tuple[int, int, str, bool]:
        return self.x, self.y, self.dir, self.lost
