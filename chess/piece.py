from dataclasses import dataclass, field, replace, make_dataclass
from typing import Set, Type

from chess.color import Color
from chess.line import Line
from chess.offset import DIAGONAL, Offset
from chess.piece_meta import PieceMeta
from chess.position import Position
from chess.ray import Ray


@dataclass(frozen=True)
class Piece:
    position: Position
    color: Color
    meta: PieceMeta = PieceMeta
    has_moved: bool = False

    def get_move_lines(self) -> Set[Line]:
        return self.adjust_lines_to_position(self.meta.move_lines)

    def get_capture_lines(self) -> Set[Line]:
        return self.adjust_lines_to_position(self.meta.capture_lines)

    def get_en_passant_lines(self) -> Set[Line]:
        return self.adjust_lines_to_position(self.meta.en_passant_lines)

    def get_castle_lines(self) -> Set[Line]:
        return self.adjust_lines_to_position(self.meta.castle_lines)

    def adjust_lines_to_position(self, lines: Set[Line]) -> Set[Line]:
        return {line.offset(dx=self.position.file, dy=self.position.rank) for line in lines}

    def move(self, position: Position) -> 'Piece':
        return replace(self, position=position, has_moved=True)

    def promote(self, promotion: Type['Piece']) -> 'Piece':
        return replace(self, meta=promotion.meta)


