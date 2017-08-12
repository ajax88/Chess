from sample.chesspiece import ChessPiece

class King(ChessPiece):
	def __init__(self, board, color, row, col):
		super().__init__(board, color, row, col)
		self.name = 'k'
		self.has_moved = False

	def move(self, to_row, to_col):
		pass