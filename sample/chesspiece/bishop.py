import sample.helpers.constants
from sample.chesspiece.abstract_chess_piece import ChessPiece


class Bishop(ChessPiece):
    def __init__(self, board, color, row, col):
        super().__init__(board, color, row, col, sample.helpers.constants.BISHOP)

    def move(self, to_row, to_col):
        if self.can_move(to_row, to_col):
            if self.move_will_cause_check():
                raise ValueError(sample.helpers.constants.MOVE_KING_IN_CHECK)
            self.change_board(to_row, to_col)
            return True
        return False

    def can_move(self, to_row, to_col):
        if abs(to_row - self.row) == abs(to_col - self.col):
            if not self.board.is_blocked(self.row, self.col, to_row, to_col):
                return True
        return False
