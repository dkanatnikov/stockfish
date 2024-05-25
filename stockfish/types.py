from enum import Enum


class Piece(Enum):
    WHITE_PAWN = "P"
    BLACK_PAWN = "p"
    WHITE_KNIGHT = "N"
    BLACK_KNIGHT = "n"
    WHITE_BISHOP = "B"
    BLACK_BISHOP = "b"
    WHITE_ROOK = "R"
    BLACK_ROOK = "r"
    WHITE_QUEEN = "Q"
    BLACK_QUEEN = "q"
    WHITE_KING = "K"
    BLACK_KING = "k"


class Capture(Enum):
    DIRECT_CAPTURE = "direct capture"
    EN_PASSANT = "en passant"
    NO_CAPTURE = "no capture"
