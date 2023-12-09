import curses
from curses import window
from time import sleep

from pylife.grid import LifeGrid
from pylife.patterns import Pattern

__all__ = ["CursesView"]


class CursesView:
    def __init__(
        self,
        pattern: Pattern,
        gen: int = 10,
        frame_rate: int = 7,
        bbox: tuple[int, int, int, int] = (0, 0, 20, 20),
    ) -> None:
        self.pattern = pattern
        self.gen = gen
        self.frame_rate = frame_rate
        self.bbox = bbox

    def show(self) -> None:
        curses.wrapper(self._draw)

    def _draw(self, screen: window) -> None:
        current_grid = LifeGrid(self.pattern)
        curses.curs_set(0)
        screen.clear()

        try:
            screen.addstr(0, 0, current_grid.as_string(self.bbox))
        except curses.error as err:
            msg = (f"Error: terminal too small for pattern '{self.pattern.name}'",)
            raise ValueError(msg) from err

        for _ in range(self.gen):
            current_grid.evolve()
            screen.addstr(0, 0, current_grid.as_string(self.bbox))
            screen.refresh()
            sleep(1 / self.frame_rate)
