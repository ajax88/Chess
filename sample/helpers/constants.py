BLANK = None
BLANK_CHAR = ' '
PAWN = 'p'
BISHOP = 'b'
QUEEN = 'q'
KING = 'k'
KNIGHT = 'n'
ROOK = 'r'
WHITE = 'white'
BLACK = 'black'
INVALID_PAWN_MOVE = "Invalid pawn move."
MOVE_OUT_OF_BOUNDS = "Move position is out of bounds."
INVALID_INPUT_COLOR = "Color must be either black or white"
PIECE_CHARS = ['n', 'b', 'r', 'k', 'q', 'p']
BOARD_CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
BOARD_NUMS = [i for i in range(1, 9)]


def get_other_color(color):
    if str(color).__eq__(WHITE):
        return BLACK
    elif str(color).__eq__(BLACK):
        return WHITE
    else:
        raise ValueError(INVALID_INPUT_COLOR)
