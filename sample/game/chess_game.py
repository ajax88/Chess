from sample.game.abstract_game import Game
from sample.board.chess_board import ChessBoard
from sample.player.chess_player import ChessPlayer
from sample.helpers import constants

import os


class ChessGame(Game):
    def __init__(self, flip_board):
        self.board = ChessBoard(flip_board)
        self.player1 = ChessPlayer(constants.BLANK_CHAR, self.board, None)
        self.player2 = ChessPlayer(constants.BLANK_CHAR, self.board, None)

    def start(self):
        self.init_players()
        self.play_game()

    def print_board(self):
        print(self.board)

    def change_current_player (self) :
        if self.current_player == self.player1 :
            self.current_player = self.player2
        else :
            self.current_player = self.player1


    def init_players(self):
        p1_name = input("Enter player 1 name : ")
        p2_name = input("Enter player 2 name : ")
        self.player1.set_name(p1_name)
        self.player2.set_name(p2_name)
        while True:
            try:
                p1_color = input(p1_name + ", do you want black or white? ")
                self.player1.set_color(p1_color)
                break
            except ValueError:
                print("Color must be either black or white.")

        self.player2.set_color(constants.get_other_color(self.player1.get_color()))
        if (self.player1.color == "white") : 
            self.current_player = self.player1
        else:
            self.current_player = self.player2

    def get_player_1(self):
        return self.player1

    def get_player_2(self):
        return self.player2

#   TODO// handle switched board
    def parse_move(self, move):
        move = move.lower()

        if len(move) == 2:
            return 'p', self.current_player.get_color(), constants.BOARD_CHARS.index(move[0]), \
                   constants.BOARD_NUMS_REVERSE.index(move[1])
        elif len(move) == 3:
            return move[0], self.current_player.get_color(), constants.BOARD_CHARS.index(move[1]), \
                   constants.BOARD_NUMS_REVERSE.index(move[2])
        elif len(move) == 4:
            pass # specific pawn move
        elif len(move) == 6:
            pass #specific move:
        else:
            raise ValueError("Invalid move input.")

    def convert_to_row_col(self, letter_number):
        letter = letter_number[0]
        number = letter_number[1]
        return constants.BOARD_CHARS.index(letter), constants.BOARD_NUMS.index(number)

    def play_game(self):
        game_over = False
        while(not game_over):
            os.system('clear')
            print(self.board)
            print(self.current_player.get_name() + ", it's your turn. ")

            moveSuccess = False
            move_string = input("Move: ")
            while(not moveSuccess):
                if (move_string == "quit") :
                    game_over = True
                    break
                (pieceType, color, row, col) = self.parse_move(move_string);
                moveSuccess = self.board.makeMove(pieceType, color, row, col)
                if not moveSuccess:
                    move_string = input("Invalid move. Please enter a new, valid move: ")
                    continue
                else:
                    break

            self.change_current_player()
            input("PAUSED for debugging. Press any key to continue.")






