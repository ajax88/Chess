from sample.chesspiece import ChessPiece

class Pawn(ChessPiece):
	def __init__(self, board, color, row, col):
		super().__init__(board, color, row, col)
		self.name = 'p'
		self.has_moved = False

	def move(self, to_row, to_col):
		if to_row >= 8 or to_row < 0 or to_col >= 8 or to_col < 0:
			raise ValueError('Index out of bounds')
