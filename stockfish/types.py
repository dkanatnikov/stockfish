from enum import Enum
from dataclasses import dataclass
import os


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


@dataclass
class BenchmarkParameters:
    ttSize: int = 16
    threads: int = 1
    limit: int = 13
    fenFile: str = "default"
    limitType: str = "depth"
    evalType: str = "mixed"

    def __post_init__(self):
        self.ttSize = self.ttSize if self.ttSize in range(1, 128001) else 16
        self.threads = self.threads if self.threads in range(1, 513) else 1
        self.limit = self.limit if self.limit in range(1, 10001) else 13
        self.fenFile = (
            self.fenFile
            if self.fenFile.endswith(".fen") and os.path.isfile(self.fenFile)
            else "default"
        )
        self.limitType = (
            self.limitType
            if self.limitType in ["depth", "perft", "nodes", "movetime"]
            else "depth"
        )
        self.evalType = (
            self.evalType
            if self.evalType in ["mixed", "classical", "NNUE"]
            else "mixed"
        )
