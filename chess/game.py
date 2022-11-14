import datetime

from dataclasses import dataclass

from chess.board import Board
from chess.metadata import PlayerName, Date, Site, Result


class Game:
    def __init__(self, board: Board, rules: Rules):
        self.board = board
        self.rules = rules


@dataclass(frozen=True)
class GameMetadata:
    """Metadata about a game, based off of the PGN standard"""

    event: str
    site: Site
    date: Date
    round: int
    white: PlayerName
    black: PlayerName
    result: Result

    white_elo: int
    black_elo: int
    time_control: str
    termination: str
    white_clock: datetime.time
    black_clock: datetime.time
    white_time: datetime.time
    black_time: datetime.time
    white_inc: datetime.time
    black_inc: datetime.time
    white_rating_diff: int
    black_rating_diff: int
    eco: str
    opening: str
    variation: str
    sub_variation: str
    moves: int
    ply_count: int
    fen: str




