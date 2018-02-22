import os

from sample.chessboard.chess_board import ChessBoard
from sample.helpers import constants
from sample.player.chess_player import ChessPlayer


class ChessGame(object):
    def __init__(self, flip_board, debug):
        self.flip_board = flip_board
        self.debug = debug
        self.board = ChessBoard(self.flip_board, self.debug)
        self.player1 = ChessPlayer(constants.BLANK_CHAR, self.board, None)
        self.player2 = ChessPlayer(constants.BLANK_CHAR, self.board, None)
        self.current_player = self.player1
        self.board_chars = constants.BOARD_CHARS[:]
        self.board_nums = constants.BOARD_NUMS[:]
        if self.flip_board:
            self.board_chars.reverse()
        else:
            self.board_nums.reverse()

    def start(self, player1Name='', player2Name=''):
        if player1Name == '' and player2Name == '':
            self.init_players()
            self.play_game()
            return

        self.player1.set_name(player1Name)
        self.player2.set_name(player2Name)
        while True:
            try:
                p1_color = input(player1Name + ", do you want black or white? ")
                self.player1.set_color(p1_color)
                break
            except ValueError:
                print("Color must be either black or white.")

        self.player2.set_color(constants.get_other_color(self.player1.get_color()))
        if (self.player1.color == "white"):
            self.current_player = self.player1
        else:
            self.current_player = self.player2
        self.play_game()

    def print_board(self):
        print(self.board)

    def change_current_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
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
        if (self.player1.color == "white"):
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
            row, col = self.convert_to_row_col(move)
            return 'p', self.current_player.get_color(), row, col, move[0], move[1]
        elif len(move) == 3:
            if move == "O-O":
                pass # attempt castle
            row, col = self.convert_to_row_col(move[1:]) # todo parse to readable square and return
            return move[0], self.current_player.get_color(), row, col, move[1:][0], move[1:][1]
        elif len(move) == 4:
            pass  # specific pawn move
        elif len(move) == 5 and move == "O-O-O":
            pass # attempt qsc
        elif len(move) == 6:
            pass  # specific move:
        else:
            raise ValueError("Invalid move input.")

    def play_game(self):
        game_over = False
        while (not game_over):
            os.system('clear')
            is_white = self.current_player.get_color() == constants.WHITE
            print(self.board)
            print(self.current_player.get_name() + ", it's your turn. ")
            print("Your {} {} pieces are as follows:".format(
                    len(self.board.get_white_pieces()) if is_white else len(self.board.get_black_pieces()),
                    constants.WHITE if is_white else constants.BLACK))
            print(list(map(lambda piece: piece.get_name(), self.board.get_white_pieces())) if is_white
                  else list(map(lambda piece: piece.get_name(), self.board.get_black_pieces())))

            move_success = False
            move_string = input("Move: ")
            while not move_success:
                if move_string == "quit":
                    game_over = True
                    break
                try:
                    (pieceType, color, row, col, letter, num) = self.parse_move(move_string)
                    move_success = self.board.make_move(pieceType, color, row, col)
                    if not move_success:
                        move_string = input("Cannot move {} {} to {}{}. Enter valid move:".format(color,
                                                                  constants.PIECE_TO_NAME_MAP[pieceType], letter, num))
                        continue
                    else:
                        break
                except ValueError as e:
                    move_string = input(e)
                    continue

            self.change_current_player()
            if self.board.in_checkmate(self.current_player.color):
                game_over = True

        print("Game Over!!")


    def convert_to_row_col(self, letter_number):
            letter = letter_number[0]
            number = letter_number[1]
            return self.board_nums.index(int(number)), self.board_chars.index(letter)
