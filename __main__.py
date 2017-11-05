from sample.game.chess_game import ChessGame


def main():
    while True:
        response = input("Would you like to flip the board (y/n)")
        if response.lower().__eq__("y"):
            flip_board = True
            break
        if response.lower().eq("n"):
            flip_board = False
            break

    game = ChessGame(flip_board)
    game.start()


if __name__ == "__main__":
    main()


