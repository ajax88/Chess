import sample.helpers.constants
from sample.chesspiece.abstract_chess_piece import ChessPiece


class Pawn(ChessPiece):
    def __init__(self, board, color, row, col):
        super().__init__(board, color, row, col, sample.helpers.constants.PAWN)
        self.going_up = True if (self.is_white() and not self.board.is_flipped()) or \
            (self.is_black() and self.board.is_flipped()) else False

    def move(self, to_row, to_col): 
        #maybe move to parse move?
        if to_row >= 8 or to_row < 0 or to_col >= 8 or to_col < 0:
            raise ValueError(sample.helpers.constants.MOVE_OUT_OF_BOUNDS)

        # diagonal moves
        if to_col != self.col:
            if abs(to_col-self.col) != 1:
                raise ValueError(sample.helpers.constants.INVALID_PAWN_MOVE)
            else:
                if (to_row - self.row) == -1 if self.going_up else 1:
                    to_square = self.board.get_square(to_row, to_col)
                    if to_square is None:
                        raise ValueError(sample.helpers.constants.INVALID_PAWN_MOVE)
                    else:
                        if to_square.is_white() == self.is_white():
                            raise ValueError(sample.helpers.constants.INVALID_PAWN_MOVE)
                        else:
                            self.change_board(to_row, to_col)
                else:
                    raise ValueError(sample.helpers.constants.INVALID_PAWN_MOVE)
        # two spaces forward
        elif (to_row - self.row) == 2 * (-1 if self.going_up else 1):
            if self.board.is_blocked(self.row, self.col, to_row, to_col) or self.has_moved():
                raise ValueError(sample.helpers.constants.INVALID_PAWN_MOVE)
            else:
                self.change_board(to_row, to_col)

        # once space forward
        elif (to_row - self.row) == -1 if self.going_up else 1:
            if self.board.is_blocked(self.row, self.col, to_row, to_col):
                raise ValueError(sample.helpers.constants.INVALID_PAWN_MOVE)
            else:
                self.change_board(to_row, to_col)

#TODO: Add in enpassant logic
        else:
            raise ValueError(sample.helpers.constants.INVALID_PAWN_MOVE)

