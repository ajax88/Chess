from sample.player.abstract_player import Player
from sample.helpers import constants


class ChessPlayer(Player):
    def __init__(self, name, board, color):
        super().__init__(name)
        self.colors = [constants.WHITE, constants.BLACK]
        self.board = board
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        color = str(color).lower()
        if not self.colors.__contains__(color):
            raise ValueError("Player color must be either white or black.")
        else:
            self.color = color

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
