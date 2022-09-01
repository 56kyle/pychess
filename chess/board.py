
from typing import List, Set

import numpy as np

from chess.color import Color
from chess.move import Move
from chess.path import Path, AllowedPathTypes, INFINITE_STEPS
from chess.square import Square
from chess.unit import (
    Unit,
    BlackKing,
    BlackQueen,
    BlackRook,
    BlackBishop,
    BlackKnight,
    BlackPawn,
    WhiteKing,
    WhiteQueen,
    WhiteRook,
    WhiteBishop,
    WhiteKnight,
    WhitePawn,
)

standard_black_pieces = [
    BlackRook, BlackKnight, BlackBishop, BlackQueen, BlackKing, BlackBishop, BlackKnight, BlackRook,
    BlackPawn, BlackPawn, BlackPawn, BlackPawn, BlackPawn, BlackPawn, BlackPawn, BlackPawn,

]

standard_white_pieces = [
    WhitePawn, WhitePawn, WhitePawn, WhitePawn, WhitePawn, WhitePawn, WhitePawn, WhitePawn,
    WhiteRook, WhiteKnight, WhiteBishop, WhiteQueen, WhiteKing, WhiteBishop, WhiteKnight, WhiteRook,
]

standard_pieces = [*standard_black_pieces, *standard_white_pieces]


standard_board_array = np.array(
    [[BlackRook, BlackKnight, BlackBishop, BlackQueen, BlackKing, BlackBishop, BlackKnight, BlackRook],
     [BlackPawn, BlackPawn, BlackPawn, BlackPawn, BlackPawn, BlackPawn, BlackPawn, BlackPawn],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None],
     [WhitePawn, WhitePawn, WhitePawn, WhitePawn, WhitePawn, WhitePawn, WhitePawn, WhitePawn],
     [WhiteRook, WhiteKnight, WhiteBishop, WhiteQueen, WhiteKing, WhiteBishop, WhiteKnight, WhiteRook]]
)

class ChessBoard:
    def __init__(self, array: np.ndarray = standard_board_array, *args, **kwargs):
        self._array: np.ndarray = array

    def __eq__(self, other):
        if isinstance(other, ChessBoard):
            return np.array_equal(self._array, other._array)
        elif isinstance(other, np.ndarray):
            return np.array_equal(self._array, other)
        else:
            return False

    def get(self, square: Square) -> Unit | None:
        return self._array[square.row][square.column]

    def set(self, square: Square, unit: Unit | None):
        self._array[square.row][square.column] = unit

    def get_height(self) -> int:
        return self._array.shape[0]

    def get_width(self) -> int:
        return self._array.shape[1]

    def get_max_y_index(self) -> int:
        return self.get_height() - 1

    def get_max_x_index(self) -> int:
        return self.get_width() - 1

    def get_units(self) -> List[Unit]:
        units = []
        for square in self._array.flatten():
            if square is not None:
                units.append(square)
        return units

    def get_absolute_max_path_steps(self) -> int:
        return max(self.get_height(), self.get_width())

    def is_valid_square(self, square: Square) -> bool:
        return 0 <= square.row < self.get_height() and 0 <= square.column < self.get_width()

    def get_path_squares(self, square: Square, path: Path) -> Set[Square]:
        unit: Unit | None = self.get(square=square)
        if unit is None:
            return set()
        if path.max_steps == INFINITE_STEPS:
            raise ValueError("Path with infinite steps is not supported")

        ends: Set[Square] = set()
        for steps in range(1, path.max_steps + 1):
            end_square: Square = square.offset(path.offset * steps)
            ends.add(end_square)
        return ends

    def get_valid_paths(self, square: Square) -> Set[Path]:
        unit: Unit | None = self.get(square=square)
        if unit is None:
            return set()

        paths: Set[Path] = set()
        for path in unit.paths:
            board_fitted_path: Path = self._fit_path_max_steps_to_board(square=square, path=path)
            blocked_path_fitted_path: Path = self._fit_path_max_steps_to_blocked_path(
                square=square,
                path=board_fitted_path
            )
            if blocked_path_fitted_path.max_steps > 0:
                paths.add(blocked_path_fitted_path)
        return paths

    def _fit_path_max_steps_to_board(self, square: Square, path: Path):
        board_limited_max_steps: int = 0
        for _ in range(self.get_absolute_max_path_steps()):
            square: Square = square.offset(path.offset)
            if not self.is_valid_square(square=square):
                break
            board_limited_max_steps += 1
        return path.with_limited_max_steps(max_steps=board_limited_max_steps)

    def _fit_path_max_steps_to_blocked_path(self, square: Square, path: Path):
        max_steps: int = 0
        unit: Unit | None = self.get(square=square)
        if unit is None:
            return path.with_limited_max_steps(max_steps=max_steps)
        for steps in range(1, self.get_absolute_max_path_steps() + 1):
            end_square: Square = square.offset(path.offset * steps)
            if not self.is_valid_square(square=end_square):
                break
            end_square_unit: Unit | None = self.get(square=end_square)
            if end_square_unit is not None:
                if (path.allowed_path_types != AllowedPathTypes.MOVE_ONLY) and (end_square_unit.color != unit.color):
                    max_steps += 1
                break
            max_steps += 1
        return path.with_limited_max_steps(max_steps=max_steps)
