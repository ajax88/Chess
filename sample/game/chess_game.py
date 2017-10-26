from sample.game.abstract_game import Game
from sample.board.chess_board import ChessBoard


class ChessGame(Game):
    def __init__(self):
        self.board = ChessBoard()


    def start(self):
        pass

    def print_board(self):
        print(self.board)
