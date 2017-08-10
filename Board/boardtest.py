from board import Board
from termcolor import colored


board = Board(5, 10)
print(board)


try:
	board.set_square(2, 2, 'cd')
	print(board.get_square(2, 2))
	print(board.get_square(5, 10))
except ValueError as err:
	print(err.args)


print(colored('  hi ', 'white', 'on_grey'))

