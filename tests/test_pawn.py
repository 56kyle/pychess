from dataclasses import replace

import pytest

from chess.color import Color
from chess.line import Line
from chess.pawn import Pawn
from chess.position import Position
from chess.position_constants import A3, A2
from chess.segment import Segment


def test_filter_lines_to_color_with_white(dummy_a2_white_pawn):
    positive_line: Line = Segment(Position(0, 0), Position(0, 1))
    negative_line: Line = Segment(Position(0, 0), Position(0, -1))
    lines = {positive_line, negative_line}
    assert dummy_a2_white_pawn.type.filter_lines_to_color(color=Color.WHITE, lines=lines) == {positive_line}

def test_filter_lines_to_color_with_black(dummy_a6_black_pawn):
    positive_line: Line = Segment(Position(0, 0), Position(0, 1))
    negative_line: Line = Segment(Position(0, 0), Position(0, -1))
    lines = {positive_line, negative_line}
    assert dummy_a6_black_pawn.type.filter_lines_to_color(color=Color.BLACK, lines=lines) == {negative_line}

def test_get_move_lines_with_white_unmoved(dummy_a2_white_pawn):
    assert dummy_a2_white_pawn.type.get_move_lines(A2, Color.WHITE, False) == {Segment(Position(0, 0), Position(0, 1)), Segment(Position(0, 0), Position(0, 2))}

def test_get_move_lines_with_white_moved(dummy_a3_white_pawn):
    moved_pawn: Pawn = replace(dummy_a3_white_pawn, has_moved=True)
    assert moved_pawn.type.get_move_lines(A3, Color.WHITE, True) == {Segment(Position(0, 0), Position(0, 1))}


