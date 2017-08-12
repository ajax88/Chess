from sample.board import Board
from sample.chesspiece import ChessPiece
from sample.pawn import Pawn
from sample.rook import Rook
from sample.knight import Knight
from sample.bishop import Bishop
from sample.queen import Queen
from sample.king import King

from termcolor import colored


class ChessBoard(Board):
	def __init__(self, flipboard=False):
		super().__init__(8, 8)
		self.flipboard = flipboard
		for i in range(8):
			# set up pawns
			colors = ['white', 'black']
			self.set_square(6, i, Pawn(self, colors[0 + self.flipboard], 6, i))
			self.set_square(1, i, Pawn(self, colors[1 - self.flipboard], 1, i))

			# set up rooks
			if i == 0 or i == 7:
				self.set_square(7, i, Rook(self, colors[0 + self.flipboard], 7, i))
				self.set_square(0, i, Rook(self, colors[1 - self.flipboard], 0, i))

			# set up knigts
			if i == 1 or i == 6:
				self.set_square(7, i, Knight(self, colors[0 + self.flipboard], 7, i))
				self.set_square(0, i, Knight(self, colors[1 - self.flipboard], 0, i))

			# set up bishops 
			if i == 2 or i == 5:
				self.set_square(7, i, Bishop(self, colors[0 + self.flipboard], 7, i))
				self.set_square(0, i, Bishop(self, colors[1 - self.flipboard], 0, i))

			# set up queen
			if i == 3:
				self.set_square(7, i, Queen(self, colors[0 + self.flipboard], 7, i))
				self.set_square(0, i, Queen(self, colors[1 - self.flipboard], 0, i))

			# set up king
			if i == 4:
				self.set_square(7, i, King(self, colors[0 + self.flipboard], 7, i))
				self.set_square(0, i, King(self, colors[1 - self.flipboard], 0, i))



	def __str__(self):
		my_str = ''

		for i in range(self.row):

			# dash border
			my_str += ' '
			for _ in range(self.row):
				my_str += ' -'

			# side numbers 
			my_str += '\n'
			my_str += str(self.flipboard * (i + 1) + (1-self.flipboard) *(8-i))

			my_str += '|'

			for j in range(self.col):
				piece = self.get_square(i,j)
				piece_color = 'grey'
				if piece == None:
					char_piece = ' '
				else:
					char_piece = piece.get_name()
					if piece.is_white():
						piece_color = 'red'


				if ((i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)) - self.flipboard:
					my_str += colored(char_piece, piece_color)
				else:
					my_str += colored(char_piece, piece_color, 'on_white')

				my_str += '|'

			my_str += '\n'
		# last dash border
		my_str += ' '
		for _ in range(self.row):
			my_str += ' -'
		if not self.flipboard:
			my_str += '\n  a b c d e f g h'
		else:
			my_str += '\n h f g e d c b a'
		return my_str



