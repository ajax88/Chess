import sample.helpers.constants
from sample.chessboard.abstract_chess_piece import ChessPiece


class Pawn(ChessPiece):
    def __init__(self, board, color, row, col):
        super().__init__(board, color, row, col, sample.helpers.constants.PAWN)
        self.going_up = True if (self.is_white() and not self.board.is_flipped()) or \
            (self.is_black() and self.board.is_flipped()) else False

    def move(self, to_row, to_col):
        if self.can_move(to_row, to_col):
            if self.move_will_cause_check():
                raise ValueError(sample.helpers.constants.MOVE_KING_IN_CHECK)
            self.change_board(to_row, to_col)
            return True
        return False

    def can_move(self, to_row, to_col):
        # diagonal moves
        if to_col != self.col:
            if abs(to_col-self.col) != 1:
                return False
            else:
                if (to_row - self.row) == (-1 if self.going_up else 1):
                    to_square = self.board.get_square(to_row, to_col)
                    if to_square is None or to_square.is_white() == self.is_white():
                        return False
                    else:
                        return True
                else:
                    return False
        # two spaces forward
        elif (to_row - self.row) == 2 * (-1 if self.going_up else 1):
            if self.board.is_blocked(self.row, self.col, to_row, to_col) or self.has_moved:
                return False
            else:
                if self.board.get_square(to_row, to_col) is not None:
                    return False
                return True

        # once space forward
        elif (to_row - self.row) == (-1 if self.going_up else 1):
            if self.board.is_blocked(self.row, self.col, to_row, to_col):
                return False
            else:
                if self.board.get_square(to_row, to_col) is not None:
                    return False
                return True
        else:
            return False
#TODO: Add in enpassant logic
