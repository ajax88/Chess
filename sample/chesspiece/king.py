import sample.helpers.constants
from sample.chesspiece.abstract_chess_piece import ChessPiece


class King(ChessPiece):
    def __init__(self, board, color, row, col):
        super().__init__(board, color, row, col, sample.helpers.constants.KING)

    def move(self, to_row, to_col):
        if self.can_move(to_row, to_col):
            self.change_board(to_row, to_col)
            return True
        return False

    def can_move(self, to_row, to_col):
        if abs(to_col - self.col) == 1 or abs(to_row - self.row) == 1:
            curr_spot = self.board.get_square(to_row, to_col)
            return True if curr_spot is None or self.is_white() != curr_spot.is_white() else False

