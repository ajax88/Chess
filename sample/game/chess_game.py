from sample.game.abstract_game import Game
from sample.board.chess_board import ChessBoard
from sample.player.chess_player import ChessPlayer
from sample.helpers import constants


class ChessGame(Game):
    def __init__(self, flip_board):
        self.board = ChessBoard(flip_board)
        self.player1 = ChessPlayer(constants.BLANK_CHAR, self.board, None)
        self.player2 = ChessPlayer(constants.BLANK_CHAR, self.board, None)

    def start(self):
        self.init_players()


    def print_board(self):
        print(self.board)

    def init_players(self):
        p1_name = input("Enter player 1 name")
        p2_name = input("Enter player 2 name")
        self.player1.set_name(p1_name)
        self.player2.set_name(p2_name)
        while True:
            try:
                p1_color = input("Enter player 1 color")
                self.player1.set_color(p1_color)
                break
            except ValueError:
                print("Color must be either black or white.")

        self.player2.set_color(constants.get_other_color(self.player1.get_color()))

    def get_player_1(self):
        return self.player1

    def get_player_2(self):
        return self.player2

    def parse_move(self, move, color):
        move = move.lower()
        piece_name = move[0]





