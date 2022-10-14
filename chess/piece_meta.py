
from typing import Set

from chess.path import Path


class PieceMeta:
    name: str
    letter: str
    value: int
    symbol: str
    html_decimal: str
    html_hex: str

    def get_move_paths(self) -> Set[Path]:
        return set()

    def get_capture_paths(self) -> Set[Path]:
        return set()

    def get_en_passant_paths(self) -> Set[Path]:
        return set()

    def get_castle_paths(self) -> Set[Path]:
        return set()












