from dataclasses import replace, dataclass
from typing import Type, Iterable

from chess.bishop import Bishop
from chess.castle import Castle
from chess.castle_right import CastleRight
from chess.color import Color
from chess.king import KingType
from chess.knight import Knight
from chess.line import Line
from chess.move import Move

from chess.piece import Piece
from chess.position import Position
from chess.position_constants import *
from chess.queen import Queen
from chess.ray import Ray
from chess.rect import Rect
from chess.rook import Rook, RookType
from chess.segment import Segment


class Board:
    rect: Rect = Rect(p1=A1, p2=H8)
    color_promotion_positions: dict[Color, set[Position]] = {
        Color.WHITE: {Position(file=file, rank=8) for file in range(1, 9)},
        Color.BLACK: {Position(file=file, rank=1) for file in range(1, 9)},
    }
    allowed_promotions: set[Type[Piece]] = {
        Knight,
        Bishop,
        Rook,
        Queen,
    }

    def __init__(self,
                 pieces: set[Piece],
                 castling_rights: set[CastleRight] = None,
                 en_passant_target_position: Position = None,
                 half_move_draw_clock: int = 0,
                 full_move_number: int = 0):
        self.pieces: set[Piece] = pieces if pieces else set()
        self.castling_rights: set[CastleRight] = castling_rights if castling_rights else set()
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
        if position not in self.rect:
            raise ValueError(f'Position {position} is out of bounds')

    def promote(self, piece: Piece, promotion: Type[Piece]):
        self._validate_is_allowed_promotion(promotion=promotion)
        self.pieces.remove(piece)
        self.pieces.add(piece.promote(promotion=promotion))

    def _validate_is_allowed_promotion(self, promotion: Type[Piece]):
        if promotion not in self.allowed_promotions:
            raise ValueError(f'Invalid promotion: {promotion}')

    def get_colored_pieces(self, color: Color) -> set[Piece]:
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
            targets = self.get_piece_capture_targets(piece=piece)
            for targeted_piece in targets:
                if targeted_piece.color == color or color is None:
                    if targeted_piece.type == KingType:
                        return True
        return False

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

    def get_piece_moves(self, piece: Piece) -> set[Move]:
        movement_moves: set[Move] = self.get_piece_movement_moves(piece=piece)
        capture_moves: set[Move] = self.get_piece_capture_moves(piece=piece)
        en_passant_moves: set[Move] = self.get_piece_en_passant_moves(piece=piece)
        castle_moves: set[Move] = self.get_piece_castle_moves(piece=piece)
        return movement_moves | capture_moves | en_passant_moves | castle_moves

    def _get_ray_as_segment_in_board(self, ray: Ray) -> Segment:
        last_position: Position | None = None
        for position in ray.iter_positions():
            if position not in self.rect:
                return Segment(p1=ray.p1, p2=last_position)
            if last_position is None:
                raise ValueError('Ray must have at least one position in board')
            last_position: Position = position

    def _iter_line_positions(self, line: Line) -> Iterable[Position]:
        for position in line.iter_positions():
            if position not in self.rect:
                continue
            yield position

    def _get_line_positions(self, line: Line) -> set[Position]:
        return {position for position in line.iter_positions()}

    def get_piece_movement_moves(self, piece: Piece) -> set[Move]:
        movements = self.get_piece_movements(piece=piece)
        return {
            Move(piece=piece, origin=piece.position, destination=position, captures=set()) for position in movements
        }

    def get_piece_movements(self, piece: Piece) -> set[Position]:
        movements = set()

        for line in piece.get_move_lines():
            for position in self._iter_line_positions(line):
                if position == piece.position:
                    continue
                if self.get_piece(position) is not None:
                    break
                movements.add(position)
        return movements

    def get_piece_capture_moves(self, piece: Piece) -> set[Move]:
        targets = self.get_piece_capture_targets(piece=piece)
        return {
            Move(piece=piece, origin=piece.position, destination=target.position, captures={target}) for target in targets
        }

    def get_piece_capture_targets(self, piece: Piece) -> set[Piece]:
        targets = set()
        for line in piece.get_capture_lines():
            encountered_piece: Piece | None = self.get_first_encountered_piece_in_line(line)
            if encountered_piece is not None and piece.is_enemy(piece=encountered_piece):
                targets.add(encountered_piece)
        return targets

    def get_piece_en_passant_moves(self, piece: Piece) -> set[Move]:
        targets = self.get_piece_en_passant_targets(piece=piece)
        return {
            Move(piece=piece, origin=piece.position, destination=target.position, captures={target}) for target in targets
        }

    def get_piece_en_passant_targets(self, piece: Piece) -> set[Piece]:
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

    def get_piece_threat_map(self, piece: Piece) -> set[Position]:
        threat_map = set()
        for line in piece.get_capture_lines():
            for position in line.iter_positions():
                if position not in self.rect:
                    break
                threat_map.add(position)
                if self.get_piece(position) is not None:
                    break
        return threat_map

    def get_piece_castle_moves(self, piece: Piece) -> set[Move]:
        castle_moves: set[Move] = set()
        for castle_right in self.castling_rights:
            if piece.type != KingType:
                continue
            if piece.color != castle_right.color:
                continue
            if piece.position != castle_right.king_origin:
                continue

            rook_origin_contents: Piece | None = self.get_piece(castle_right.rook_origin)
            if rook_origin_contents is None:
                continue
            if rook_origin_contents.type != RookType:
                continue
            if rook_origin_contents.color != castle_right.color:
                continue
            if rook_origin_contents.has_moved:
                continue

            if not self.is_castle_path_clear(king=piece, castle_right=castle_right):
                continue

            castle_moves.add(
                Castle(
                    piece=piece,
                    origin=piece.position,
                    destination=castle_right.king_destination,
                    rook=rook_origin_contents,
                    rook_origin=castle_right.rook_origin,
                    rook_destination=castle_right.rook_destination
                )
            )
        return castle_moves

    def is_castle_path_clear(self, king: Piece, castle_right: CastleRight) -> bool:
        king_path: Segment = Segment(p1=castle_right.king_origin, p2=castle_right.king_destination)
        for enemy in {p for p in self.pieces if king.is_enemy(p)}:
            if self.get_piece_threat_map(enemy) & self._get_line_positions(king_path):
                return False
        return True

