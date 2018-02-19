import sample.helpers.constants
from sample.chessboard.abstract_chess_piece import ChessPiece


class Queen(ChessPiece):
    def __init__(self, board, color, row, col):
        super().__init__(board, color, row, col, sample.helpers.constants.QUEEN)

    def can_move(self, to_row, to_col):
        if abs(to_row - self.row) == abs(to_col - self.col) or \
                (to_col == self.col and not to_row == self.row) or (to_row == self.row and not to_col == self.col):
            if not self.board.is_blocked(self.row, self.col, to_row, to_col):
                return True
        return False
