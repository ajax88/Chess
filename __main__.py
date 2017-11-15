from sample.game.chess_game import ChessGame
import os


def main():
    while True:
        os.system('clear')
        print_title()
        response = input("Would you like to flip the board (y/n)")
        if response.lower() == "y":
            flip_board = True
            break
        if response.lower() == "n":
            flip_board = False
            break

    game = ChessGame(flip_board)
    game.start()

def print_title():
    print("  /$$$$$$  /$$                                   ")
    print(" /$$__  $$| $$                                   ")
    print("| $$  \__/| $$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$$")
    print("| $$      | $$__  $$ /$$__  $$ /$$_____//$$_____/")
    print("| $$      | $$  \ $$| $$$$$$$$|  $$$$$$|  $$$$$$ ")
    print("| $$    $$| $$  | $$| $$_____/ \____  $$\____  $$")
    print("|  $$$$$$/| $$  | $$|  $$$$$$$ /$$$$$$$//$$$$$$$/")
    print(" \______/ |__/  |__/ \_______/|_______/|_______/ ")
    print("\n")
    print("             Alex Jackson & Katie Hoskins        ")
    print("                    Fall 2017                    ")
    print("\n")
    print("\n")


if __name__ == "__main__":
    main()


