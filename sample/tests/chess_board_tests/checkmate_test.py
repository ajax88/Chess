import unittest
from sample.game.chess_game import ChessGame
from sample.helpers import constants


class TestCheckMate(unittest.TestCase):
    def test_fools_mate(self):
        game = ChessGame(False, True)
        game.player1.set_color(constants.WHITE)
        game.player2.set_color(constants.BLACK)
        
        execute_move(game, "e4")
        self.assertFalse(game.board.in_checkmate(constants.BLACK))
        self.assertFalse(game.board.in_checkmate(constants.WHITE))
        execute_move(game, "g5")
        self.assertFalse(game.board.in_checkmate(constants.BLACK))
        self.assertFalse(game.board.in_checkmate(constants.WHITE))
        execute_move(game, "d4")
        self.assertFalse(game.board.in_checkmate(constants.BLACK))
        self.assertFalse(game.board.in_checkmate(constants.WHITE))
        execute_move(game, "f6")
        self.assertFalse(game.board.in_checkmate(constants.BLACK))
        self.assertFalse(game.board.in_checkmate(constants.WHITE))
        execute_move(game, "qh5")
        self.assertTrue(game.board.in_checkmate(constants.BLACK))
        self.assertFalse(game.board.in_checkmate(constants.WHITE))


def execute_move(game, move_string):
    (piece_type, color, row, col, letter, num) = game.parse_move(move_string)
    game.board.make_move(piece_type, color, row, col)
    game.change_current_player()

