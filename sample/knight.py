from sample.chesspiece import ChessPiece

class Knight(ChessPiece):
	def __init__(self, board, color, row, col):
		super().__init__(board, color, row, col)
		self.name = 'n'

	def move(self, to_row, to_col):
		pass