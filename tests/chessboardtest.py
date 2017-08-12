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



if __name__ == '__main__':
	unittest.main()


