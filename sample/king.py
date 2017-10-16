from sample.chesspiece import ChessPiece
import sample.constants

class King(ChessPiece):
    def __init__(self, board, color, row, col):
        super().__init__(board, color, row, col, sample.constants.KING)
        self.has_moved = False

    def move(self, to_row, to_col):
        pass