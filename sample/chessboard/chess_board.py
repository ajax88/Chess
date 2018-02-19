from sample.chessboard.king import King
from sample.chessboard.knight import Knight
from sample.chessboard.pawn import Pawn
from sample.chessboard.queen import Queen
from termcolor import colored

import sample.chessboard.abstract_chess_piece
from sample.helpers import constants
from sample.board.board import Board
from sample.chessboard.bishop import Bishop
from sample.chessboard.rook import Rook


class ChessBoard(Board):
    def __init__(self, flip_board=False):
        super().__init__(8, 8)
        self.flip_board = flip_board
        colors = [sample.helpers.constants.WHITE, sample.helpers.constants.BLACK]
        self.white_pieces = []
        self.black_pieces = []
        for i in range(8):
            # set up pawns
            self.add_piece(Pawn(self, colors[0 + self.flip_board], 6, i))
            self.add_piece(Pawn(self, colors[1 - self.flip_board], 1, i))

            # set up rooks
            if i == 0 or i == 7:
                self.add_piece(Rook(self, colors[0 + self.flip_board], 7, i))
                self.add_piece(Rook(self, colors[1 - self.flip_board], 0, i))

            # set up knights
            if i == 1 or i == 6:
                self.add_piece(Knight(self, colors[0 + self.flip_board], 7, i))
                self.add_piece(Knight(self, colors[1 - self.flip_board], 0, i))

            # set up bishops 
            if i == 2 or i == 5:
                self.add_piece(Bishop(self, colors[0 + self.flip_board], 7, i))
                self.add_piece(Bishop(self, colors[1 - self.flip_board], 0, i))

            # set up queen
            if i == 3:
                self.add_piece(Queen(self, colors[0 + self.flip_board], 7, i + flip_board))
                self.add_piece(Queen(self, colors[1 - self.flip_board], 0, i + flip_board))

            # set up king
            if i == 4:
                self.add_piece(King(self, colors[0 + self.flip_board], 7, i - flip_board))
                self.add_piece(King(self, colors[1 - self.flip_board], 0, i - flip_board))

    def set_square(self, piece, row = None, col = None):
        if not isinstance(piece, sample.chessboard.abstract_chess_piece.ChessPiece):
            if piece is not None:
                raise ValueError("Chessboard squares must take a piece")

        if piece is not None:
            row, col = piece.get_position()
        super(ChessBoard, self).set_square(row, col, piece)

    def get_white_pieces(self):
        return self.white_pieces

    def get_black_pieces(self):
        return self.black_pieces

    def is_flipped(self):
        return self.flip_board

    def makeMove(self, pieceType, color, destinationRow, destinationCol):
        if color == constants.WHITE:
            pieces = self.white_pieces
        else:
            pieces = self.black_pieces

        for piece in pieces:
            if piece.get_name() == pieceType:
                # TODO Duplicate piece move to same place?
                success = piece.move(destinationRow, destinationCol)
                if success:
                    return True
        return False

    def __str__(self):
        my_str = ''

        for i in range(self.row):

            # dash border
            my_str += ' '
            for _ in range(self.row):
                my_str += ' -'

            # side numbers 
            my_str += '\n'
            my_str += str(self.flip_board * (i + 1) + (1 - self.flip_board) * (8 - i))

            my_str += '|'

            for j in range(self.col):
                piece = self.get_square(i, j)
                piece_color = 'grey'
                if piece is None:
                    char_piece = sample.helpers.constants.BLANK_CHAR
                else:
                    char_piece = piece.get_name()
                    if piece.is_white():
                        piece_color = 'red'

                if ((i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)) - self.flip_board:
                    my_str += colored(char_piece, piece_color)
                else:
                    my_str += colored(char_piece, piece_color, 'on_white')

                my_str += '|'

            my_str += '\n'
        # last dash border
        my_str += ' '
        for _ in range(self.row):
            my_str += ' -'
        if not self.flip_board:
            my_str += '\n  a b c d e f g h'
        else:
            my_str += '\n  h f g e d c b a'
        return my_str

    def is_blocked(self, start_row, start_col, end_row, end_col):
        # Ensure that boundary squares are unique
        if start_row == end_row and start_col == end_col:
            raise ValueError("is_blocked must take unique positions.")

        piece = self.get_square(start_row, start_col)
        if piece is None:
            raise ValueError("Starting position in is_blocked must have piece.")
        piece_is_white = piece.is_white()

        # Case 1: Diagonal move
        if abs(end_row - start_row) == abs(end_col - start_col):
            next_row = start_row
            next_col = start_col

            # Determine if column and row values should increase or decrease to get
            # diagonal direction
            r_dir = 1 if (start_row - end_row) > 0 else -1
            c_dir = 1 if (start_col - end_col) > 0 else -1

            next_row = next_row + -1 * r_dir
            next_col = next_col + -1 * c_dir

            while next_row != end_row and next_col != end_col:
                curr_spot = self.get_square(next_row, next_col)

                # If there is a piece sitting at the current spot, move is not possible
                if isinstance(curr_spot, sample.chessboard.abstract_chess_piece.ChessPiece):
                    return True
                next_row = next_row + -1 * r_dir
                next_col = next_col + -1 * c_dir

        # Case 2: Horizontal move
        elif start_row == end_row:
            c_dir = 1
            next_col = start_col
            if start_col - end_col > 0:
                c_dir = -1

            next_col += c_dir

            while next_col != end_col:
                curr_spot = self.get_square(start_row, next_col)
                if isinstance(curr_spot, sample.chessboard.abstract_chess_piece.ChessPiece):
                    return True
                next_col += c_dir


        # Case 3: Vertical move
        elif start_col == end_col:
            r_dir = 1
            next_row = start_row
            if start_row - end_row > 0:
                r_dir = -1

            next_row += r_dir

            while next_row != end_row:
                curr_spot = self.get_square(next_row, start_col)

                if isinstance(curr_spot, sample.chessboard.abstract_chess_piece.ChessPiece):
                    return True
                next_row += r_dir

        else:
            raise ValueError("is_blocked must take straight path.")


            # check the last square for a piece of the opposing color or None
        curr_spot = self.get_square(end_row, end_col)
        return False if curr_spot is None or curr_spot.is_white() != piece_is_white else True

    def get_pieces(self, name, color):
        to_return = []
        if color == constants.WHITE:
            for piece in self.white_pieces:
                if piece.get_name() == name:
                    to_return.append(piece)
        elif color == constants.BLACK:
            for piece in self.black_pieces:
                if piece.get_name() == name:
                    to_return.append(piece)
        return to_return

    def in_check(self, color):
        if color != constants.WHITE and color != constants.BLACK:
            raise ValueError(constants.INVALID_INPUT_COLOR)

        if color == constants.WHITE:
            white_king = self.get_pieces(constants.KING, constants.WHITE)[0]
            for piece in self.black_pieces:
                row, col = white_king.get_position()
                if piece.can_move(row, col):
                    return True

        if color == constants.BLACK:
            black_king = self.get_pieces(constants.KING, constants.BLACK)[0]
            for piece in self.white_pieces:
                row, col = black_king.get_position()
                if piece.can_move(row, col):
                    return True
        return False

    def add_piece(self, piece):
        self.set_square(piece)
        self.white_pieces.append(piece) if piece.color == constants.WHITE else self.black_pieces.append(piece)
