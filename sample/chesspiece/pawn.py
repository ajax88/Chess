import sample.helpers.constants
from sample.chesspiece.abstract_chess_piece import ChessPiece


class Pawn(ChessPiece):
    def __init__(self, board, color, row, col):
        super().__init__(board, color, row, col, sample.helpers.constants.PAWN)
        self.going_up = True if (self.is_white() and not self.board.is_flipped()) or \
            (self.is_black() and self.board.is_flipped()) else False

    def move(self, to_row, to_col): 
        print("attempting to move a pawn from (" + str(self.row) + "," + str(self.col) + ") to (" + str(to_row) + "," + str(to_col) + ").")

        # diagonal moves
        if to_col != self.col:
            if abs(to_col-self.col) != 1:
                return False
            else:
                if (to_row - self.row) == (-1 if self.going_up else 1):
                    to_square = self.board.get_square(to_row, to_col)
                    if to_square is None:
                        return False
                    else:
                        if to_square.is_white() == self.is_white():
                            return False
                        else:
                            self.change_board(to_row, to_col)
                            return True
                else:
                    return False
        # two spaces forward
        elif (to_row - self.row) == 2 * (-1 if self.going_up else 1):
            if self.board.is_blocked(self.row, self.col, to_row, to_col) or self.has_moved:
                return False
            else:
                poss_piece = self.board.get_square(to_row, to_col)
                if poss_piece is not None:
                    return False
                self.change_board(to_row, to_col)
                return True

        # once space forward
        elif (to_row - self.row) == (-1 if self.going_up else 1):
            if self.board.is_blocked(self.row, self.col, to_row, to_col):
                return False
            else:
                poss_piece = self.board.get_square(to_row, to_col)
                if poss_piece is not None:
                    return False
                self.change_board(to_row, to_col)
                return True

#TODO: Add in enpassant logic
        else:
            return False

