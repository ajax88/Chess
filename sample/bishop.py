from sample.chesspiece import ChessPiece

class Bishop(ChessPiece):
    def __init__(self, board, color, row, col):
        super().__init__(board, color, row, col)
        self.name = 'b'

    def move(self, to_row, to_col):
        pass