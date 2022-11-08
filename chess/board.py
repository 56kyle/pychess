from dataclasses import replace
from typing import Set, Dict, Type

from chess.bishop import Bishop
from chess.castle_right import CastleRight
from chess.color import Color
from chess.king import KingType
from chess.knight import Knight
from chess.line import Line
from chess.offset import Offset
from chess.pawn import PawnType

from chess.piece import Piece
from chess.position import Position
from chess.queen import Queen
from chess.rook import Rook
from chess.size import Size


class Board:
    size: Size = Size(width=8, height=8)
    color_promotion_positions: Dict[Color, Set[Position]] = {
        Color.WHITE: {Position(file=file, rank=8) for file in range(1, 9)},
        Color.BLACK: {Position(file=file, rank=1) for file in range(1, 9)},
    }
    allowed_promotions: Set[Type[Piece]] = {
        Knight,
        Bishop,
        Rook,
        Queen,
    }

    def __init__(self,
                 pieces: Set[Piece],
                 castling_rights: Set[CastleRight],
                 en_passant_target_position: Position = None,
                 half_move_draw_clock: int = 0,
                 full_move_number: int = 0):
        self.pieces: Set[Piece] = pieces
        self.castling_rights: Set[CastleRight] = castling_rights
        self.en_passant_target_position: Position = en_passant_target_position
        self.half_move_draw_clock: int = half_move_draw_clock
        self.full_move_number: int = full_move_number

    def move(self, piece: Piece, destination: Position):
        self._validate_destination_is_empty(destination=destination)
        self._validate_in_bounds(position=destination)

        self.pieces.remove(piece)
        self.pieces.add(piece.move(destination))

    def _validate_destination_is_empty(self, destination: Position):
        if self.get_piece(destination) is not None:
            raise ValueError(f'Piece already at {destination}')

    def _validate_in_bounds(self, position: Position):
        if position not in self.size:
            raise ValueError(f'Position {position} is out of bounds')

    def promote(self, piece: Piece, promotion: Type[Piece]):
        self._validate_is_allowed_promotion(promotion=promotion)
        self.pieces.remove(piece)
        self.pieces.add(piece.promote(promotion=promotion))

    def _validate_is_allowed_promotion(self, promotion: Type[Piece]):
        if promotion not in self.allowed_promotions:
            raise ValueError(f'Invalid promotion: {promotion}')

    def get_colored_pieces(self, color: Color) -> Set[Piece]:
        return {piece for piece in self.pieces if piece.color == color}

    def get_piece(self, position: Position) -> Piece | None:
        for piece in self.pieces:
            if piece.position == position:
                return piece
        return None

    def is_promotion_position(self, color: Color, position: Position) -> bool:
        return position in self.color_promotion_positions[color]

    def is_check_present(self, color: Color = None) -> bool:
        for piece in self.pieces:
            targets = self.get_piece_targets(piece=piece)
            if any(targeted_piece.type == KingType for targeted_piece in targets):
                if color is None or piece.color == color:
                    return True
        return False

    """
    def is_checkmate_present(self, color: Color) -> bool:
        if not self.is_check_present(color=color):
            return False
        for piece in self.get_colored_pieces(color=color):
            if self.get_piece_moves

        return True
    """

    def get_first_encountered_piece_in_line(self, line: Line) -> Piece | None:
        closest_piece: Piece | None = None
        closest_distance: float | None = None
        for piece in self.pieces:
            if piece.position in line and piece.position != line.p1:
                distance = piece.position.distance_to(line.p1)
                if closest_distance is None or distance < closest_distance:
                    closest_piece = piece
                    closest_distance = distance
        return closest_piece

    def get_piece_movements(self, piece: Piece) -> Set[Position]:
        movements = set()
        move_lines: Set[Line] = piece.get_move_lines()
        castle_lines: Set[Line] = piece.get_castle_lines()
        for line in move_lines | castle_lines:
            dx = line.p2.file - line.p1.file
            dy = line.p2.rank - line.p1.rank
            current_position: Position = line.p2
            while current_position in self.size and current_position in line:
                if self.get_piece(current_position) is not None:
                    break
                movements.add(current_position)
                current_position = current_position.offset(dx=dx, dy=dy)
        return movements

    def get_piece_targets(self, piece: Piece) -> Set[Piece]:
        capture_targets: Set[Piece] = self.get_piece_capture_targets(piece=piece)
        en_passant_targets: Set[Piece] = self.get_piece_en_passant_targets(piece=piece)
        return capture_targets | en_passant_targets

    def get_piece_capture_targets(self, piece: Piece) -> Set[Piece]:
        targets = set()
        for line in piece.get_capture_lines():
            encountered_piece: Piece | None = self.get_first_encountered_piece_in_line(line)
            if encountered_piece is not None and piece.is_enemy(piece=encountered_piece):
                targets.add(encountered_piece)
        return targets

    def get_piece_en_passant_targets(self, piece: Piece) -> Set[Piece]:
        targets = set()
        if self.en_passant_target_position is not None:
            for line in piece.get_en_passant_lines():
                if self.en_passant_target_position in line:
                    encountered_piece: Piece | None = self.get_piece(
                            replace(self.en_passant_target_position, rank=piece.position.rank)
                        )
                    if encountered_piece is not None and piece.is_enemy(piece=encountered_piece):
                        targets.add(encountered_piece)
        return targets

