from sample.chesspiece import ChessPiece

class Pawn(ChessPiece):
    def __init__(self, board, color, row, col):
        super().__init__(board, color, row, col)
        self.name = 'p'
        self.has_moved = False
        if (self.is_white() and not self.board.is_flipped()) or \
            (self.is_black() and self.board.is_flipped()):
            self.going_up = True
        else:
            self.going_up = False

    def move(self, to_row, to_col): 
        if to_row >= 8 or to_row < 0 or to_col >= 8 or to_col < 0:
            raise ValueError("Move position is out of bounds.")

        # diagonal moves
        if to_col != self.col:
            if abs(to_col-self.col) != 1:
                raise ValueError("Invalid pawn move.")
            else:
                if (to_row - self.row) == (1 - (self.going_up * 2)):
                    to_square = self.board.get_square(to_row, to_col)
                    if to_square is None:
                        raise ValueError("Invalid pawn move.")
                    else:
                        if to_square.is_white() == self.is_white():
                            raise ValueError("Invalid pawn move.")
                        else:
                            self.board.is_blocked(1,1,1,1)
                            return True
                else:
                    raise ValueError("Invalid pawn move.")


'''

        # two squares forward
        if to_col == self.col - 2 and not self.has_moved and 
            return True

        if to_col == self


        
        # Same position
        if to_row == self.row and to_col == self.col:
            return False

        if not self.diag_move(to_row, to_col) or 
                    not self.hor_move(to_row, to_col):
            return False

        if
        '''




