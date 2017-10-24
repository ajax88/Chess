from sample.board.board import Board
import unittest


class TestBoardMethods(unittest.TestCase):
    def test_set_get_square(self):
        print("Testing initialization of int board.")

        board = Board(5, 10)
        self.assertEqual(board.get_square(1, 2), None)

        print("Success.")

    def test_outofbounds_index(self):
        print("Testing exception raise with bad index.")

        board = Board(8, 8)
        with (self.assertRaises(ValueError)):
            board.set_square(8, 8, 's')

        print("Success.")


if __name__ == '__main__':
    unittest.main()
