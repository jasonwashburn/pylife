"""Patterns for game of life."""
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Self

PATTERNS_FILE = Path(__file__).parent / "patterns.toml"


@dataclass
class Pattern:
    name: str
    alive_cells: set[tuple[int, int]]

    @classmethod
    def from_toml(cls, name: str, toml_data: dict[str, list[list[int]]]) -> Self:
        return cls(name, alive_cells={tuple(cell) for cell in toml_data["alive_cells"]})


def get_pattern(name: str, filename: Path = PATTERNS_FILE) -> Pattern:
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return Pattern.from_toml(name, toml_data=data[name])


def get_all_patterns(filename: Path = PATTERNS_FILE) -> list[Pattern]:
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return [Pattern.from_toml(name, toml_data) for name, toml_data in data.items()]
