from sample.chesspiece import ChessPiece
import sample.constants

class Bishop(ChessPiece):
    def __init__(self, board, color, row, col):
        super().__init__(board, color, row, col, sample.constants.BISHOP)

    def move(self, to_row, to_col):
        pass