import sample.helpers.constants
from sample.chesspiece.abstractchesspiece import ChessPiece


class Queen(ChessPiece):
    def __init__(self, board, color, row, col):
        super().__init__(board, color, row, col, sample.helpers.constants.QUEEN)

    def move(self, to_row, to_col):
        pass