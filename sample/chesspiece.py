# Base class for all other chess pieces
from abc import ABCMeta, abstractmethod

import sample.chessboard
import sample.constants

class ChessPiece():
    metaclass = ABCMeta

    def __init__(self, board, color, row, col, name):
        if type(board) != sample.chessboard.ChessBoard:
            raise TypeError("Must input valid chessboard.")

        if (color.lower() != sample.constants.WHITE) and (color.lower() != sample.constants.BLACK):
            raise ValueError("Color must be black or white.")

        self.name = name
        self.board = board
        self.color = color.lower()
        self.taken = False
        self.set_position(row, col)

    def get_name(self):
        return self.name

    def set_position(self, row, col):
        if row >= 8 or row < 0 or col >= 8 or col < 0:
            raise ValueError('Index out of bounds')
        self.row = row
        self.col = col

    def get_position(self):
        return self.row, self.col

    def got_taken(self):
        self.taken = True

    def is_taken(self):
        return self.taken

    def is_white(self):
        return self.color == 'white'

    def is_black(self):
        return not self.is_white()

    def set_board(self, board):
        self.board = board

    def get_board(self):
        return self.board

    def change_board(self, to_row, to_col):
        self.board.set_square(to_row, to_col, sample.constants.BLANK)
        self.set_position(to_row, to_col)
        self.board.set_square(self.row, self.col, self)

    # Input: a new position for the piece to move to (row, col)
    # 
    # This method will update the board and change the piece's position
    # upon a valid move
    # 
    # Returns: 
    #       False for all improper input (invalid move)
    #       True for a valid move
    @abstractmethod
    def move(self, to_row, to_col):
        pass


