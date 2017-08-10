from board import Board
from termcolor import colored


class ChessBoard(Board):
	def __init__(self):
		super().__init__(8, 8)
		for i in range(self.row):
			for j in range(self.col):
				if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
					self.board[i][j] = colored(' ', 'grey')
				else:
					self.board[i][j] = colored(' ', 'grey', 'on_white')



	def __str__(self):
		my_str = ''
		counter = 8
		for row in self.board:
			my_str += ' '
			for _ in range(self.row):
				my_str += ' -'
			my_str += '\n'
			my_str += str(counter)
			my_str += '|'
			for c in row:
				my_str += c
				my_str += '|'
			my_str += '\n'
			counter -= 1
		my_str += ' '
		for _ in range(self.row):
			my_str += ' -'

		my_str += '\n  a b c d e f g h'
		return my_str


