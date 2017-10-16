from sample.chesspiece import ChessPiece
import sample.constants

class Knight(ChessPiece):
    def __init__(self, board, color, row, col):
        super().__init__(board, color, row, col, sample.constants.KNIGHT)

    def move(self, to_row, to_col):
        pass