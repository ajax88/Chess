from context import sample
from sample.chessboard import ChessBoard
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





if __name__ == '__main__':
	unittest.main()


