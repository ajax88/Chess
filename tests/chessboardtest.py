from context import sample
from sample.chessboard import ChessBoard
from sample.rook import Rook
from sample.bishop import Bishop
import unittest

class TestChessBoardMethods(unittest.TestCase):
    def test_initialization(self):
        print("Testing initialization of chessboard.")

        board = ChessBoard()
        print(board)

        print("Success.")

    def test_improper_input(self):
        print("Testing proper bad input handling.")

        board = ChessBoard()

        print("Success.")

    def test_flipped(self):
        print("Testing flipped board functionality.")

        board =ChessBoard(flipboard=True)
        print(board)
        print("Success.")

    def test_move(self):
        print("Testing move function with pawn.")

        board = ChessBoard()
        p1 = board.get_white_pieces()[0]
        p1_row, p1_col = p1.get_position()

        print(str(p1_row) + " " + str(p1_col))
        print(p1.get_name())

        with (self.assertRaises(ValueError)):
            p1.move(p1_row -1 , p1_col + 1)

        print(board)

    def test_is_blocked(self):
        print ("Testing is blocked function.")

        board = ChessBoard()
        rook = Rook(board, "white", 5, 2)
        board.set_square(5, 2, rook)

        # Test horiz. non-blocked
        # Rook 5,2 --> 5,6
        self.assertEqual(board.is_blocked(5, 2, 5, 6), False)
        # Rook 5,2 --> 5,0
        self.assertEqual(board.is_blocked(5, 2, 5, 0), False)

        #Test vert. non blocked
        print(board)
        self.assertEqual(board.is_blocked(5, 2, 2, 2), False)
        rook.set_position(2, 3)
        board.set_square(2, 3, rook)
        self.assertEqual(board.is_blocked(2, 3, 5, 3), False)

        #Test diagonal directions non blocked
        bishop = Bishop(board, "white", 4, 4)
        board.set_square(4, 4, bishop)
        self.assertEqual(board.is_blocked(4, 4, 2, 2), False)
        self.assertEqual(board.is_blocked(4, 4, 2, 6), False)
        self.assertEqual(board.is_blocked(4, 4, 5, 3), False)
        self.assertEqual(board.is_blocked(4, 4, 5, 5), False)

        #Test above with blocked

        #Test error cases:
        # No piece exists at start position
        with (self.assertRaises(ValueError)):
            board.is_blocked(3, 3, 4, 4)
        # Non straight path given
        with (self.assertRaises(ValueError)):
            board.is_blocked(3, 1, 4, 4)

        print("Success")





if __name__ == '__main__':
    unittest.main()


