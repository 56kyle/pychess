import datetime

from dataclasses import dataclass

from chess.board import Board
from chess.metadata import PlayerName, Date, Site, Result, TimeControl
from chess.rules import Rules


@dataclass(frozen=True)
class GameMetadata:
    """Metadata about a game, based off of the PGN standard"""

    event: str = ''
    site: Site = ''
    date: Date = Date.today()
    round: int = 0
    white: PlayerName = PlayerName()
    black: PlayerName = PlayerName()
    result: Result = Result()

    white_elo: int = 0
    black_elo: int = 0
    time_control: TimeControl = TimeControl()
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


class Game:
    def __init__(self, board: Board, rules: Rules, metadata: GameMetadata):
        self.board: Board = board
        self.rules: Rules = rules
        self.metadata: GameMetadata = GameMetadata()




