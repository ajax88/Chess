import sample.helpers.constants
from sample.chesspiece.abstract_chess_piece import ChessPiece


class Rook(ChessPiece):
    def __init__(self, board, color, row, col):
        super().__init__(board, color, row, col, sample.helpers.constants.ROOK)

    def move(self, to_row, to_col):
        if self.can_move(to_row, to_col):
            self.change_board(to_row, to_col)
            return True
        return False

    def can_move(self, to_row, to_col):
        if (to_col == self.col and not to_row == self.row) or (to_row == self.row and not to_col == self.col):
            if not self.board.is_blocked(self.row, self.col, to_row, to_col):
                return True
        return False
