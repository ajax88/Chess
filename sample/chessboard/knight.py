import sample.helpers.constants
from sample.chessboard.abstract_chess_piece import ChessPiece


class Knight(ChessPiece):
    def __init__(self, board, color, row, col):
        super().__init__(board, color, row, col, sample.helpers.constants.KNIGHT)

    def can_move(self, to_row, to_col):
        if (abs(to_row - self.row) == 1 and abs(to_col - self.col) == 2) or \
                (abs(to_col - self.col) == 1 and abs(to_row - self.row) == 2):
            poss_piece = self.board.get_square(to_row, to_col)
            if poss_piece is None or poss_piece.is_white() != self.is_white():
                return True
        return False
