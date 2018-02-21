import unittest
from sample.chessboard.chess_board import ChessBoard
from sample.chessboard.pawn import Pawn
from sample.chessboard.bishop import Bishop
from sample.helpers import constants
from sample.game.chess_game import ChessGame


class TestChessBoardMethods(unittest.TestCase):
    def test_basic_opening(self):
        game = ChessGame(False, True)
        comp_board = ChessBoard()

        self.classic_opening(game, comp_board)
        self.assertEqual(game.board, comp_board)
        self.execute_expected_valid_move(game, "c3")
        self.assertNotEqual(game.board, comp_board)

    def test_move_into_check(self):
        game = ChessGame(False, True)
        comp_board = ChessBoard()

        self.classic_opening(game, comp_board)
        self.execute_expected_error_move(game, "b3")

    # Aux methods
    def execute_expected_valid_move(self, game, move_string):
        (piece_type, color, row, col) = game.parse_move(move_string)
        self.assertTrue(game.board.make_move(piece_type, color, row, col))
        game.change_current_player()

    def execute_expected_error_move(self, game, move_string):
        (piece_type, color, row, col) = game.parse_move(move_string)
        self.assertRaises(ValueError, game.board.make_move, piece_type, color, row, col)
        game.change_current_player()

    def execute_expected_invalid_move(self, game, move_string):
        (piece_type, color, row, col) = game.parse_move(move_string)
        self.assertFalse(game.board.make_move(piece_type, color, row, col))
        game.change_current_player()

    # performs a basic opening for two different boards, one manually and one via game board moves
    def classic_opening(self, game, comp_board):
        # Set board with moves
        game.player1.set_color(constants.WHITE)
        game.player2.set_color(constants.BLACK)
        self.execute_expected_valid_move(game, "e4")
        self.execute_expected_valid_move(game, "e5")
        self.execute_expected_valid_move(game, "d4")
        self.execute_expected_valid_move(game, "bb4")


        # Manually set board
        # e4
        comp_board.set_square(None, 6, 4)
        comp_board.set_square(Pawn(comp_board, constants.WHITE, 4, 4))
        # e5
        comp_board.set_square(None, 1, 4)
        comp_board.set_square(Pawn(comp_board, constants.BLACK, 3, 4))
        # d4
        comp_board.set_square(None, 6, 3)
        comp_board.set_square(Pawn(comp_board, constants.WHITE, 4, 3))
        # bb4
        comp_board.set_square(None, 0, 5)
        comp_board.set_square(Bishop(comp_board, constants.BLACK, 4, 1))




