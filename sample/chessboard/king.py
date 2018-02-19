import sample.helpers.constants
from sample.chessboard.abstract_chess_piece import ChessPiece


class King(ChessPiece):
    def __init__(self, board, color, row, col):
        super().__init__(board, color, row, col, sample.helpers.constants.KING)

    def can_move(self, to_row, to_col):
        if abs(to_col - self.col) == 2 and to_row == self.row: # castle on either side
            if self.has_moved:
                return False
            if self.board.is_blocked(self.row, self.col, to_row, to_col): # TODO: Check if rook is blocked... prevents fringe case where an enemy piece is in the way of the check
                return False
            ## TODO: get rook, check if it's blocked. See if king would be in check with both moves that it would make
            ## TODO: if valid, switch em up

        if abs(to_col - self.col) == 1 or abs(to_row - self.row) == 1:
            curr_spot = self.board.get_square(to_row, to_col)
            return True if curr_spot is None or self.is_white() != curr_spot.is_white() else False
