from dataclasses import dataclass, field, replace, make_dataclass
from typing import Set, Type

from chess.color import Color
from chess.line import Line
from chess.piece_type import PieceType
from chess.position import Position


@dataclass(frozen=True)
class Piece:
    position: Position
    color: Color
    type: PieceType = PieceType
    has_moved: bool = False

    def move(self, position: Position) -> 'Piece':
        return replace(self, position=position, has_moved=True)

    def promote(self, promotion: Type['Piece']) -> 'Piece':
        return replace(self, type=promotion.type)

    def is_ally(self, piece: 'Piece') -> bool:
        return self.color == piece.color

    def is_enemy(self, piece: 'Piece') -> bool:
        return self.color != piece.color

    def get_move_lines(self) -> Set[Line]:
        return self.adjust_lines_to_position(self.type.move_lines)

    def get_capture_lines(self) -> Set[Line]:
        return self.adjust_lines_to_position(self.type.capture_lines)

    def get_en_passant_lines(self) -> Set[Line]:
        return self.adjust_lines_to_position(self.type.en_passant_lines)

    def get_castle_lines(self) -> Set[Line]:
        return self.adjust_lines_to_position(self.type.castle_lines)

    def adjust_lines_to_position(self, lines: Set[Line]) -> Set[Line]:
        return {line.offset(dx=self.position.file, dy=self.position.rank) for line in lines}

