from context import sample
from sample.board import Board

import unittest

class TestBoardMethods(unittest.TestCase):

    def test_set_get_square(self):
    	print("Testing initialization of int board.")

    	board = sample.board.Board(5, 10, int)
    	self.assertEqual(board.get_square(1, 2), None)

    	print("Success.")

    def test_wrong_square_type(self):
    	print("Testing exception raise with wrong type.")

    	board = Board(8, 8, int)
    	with (self.assertRaises(ValueError)):
    	   board.set_square(1, 2, 's')

    	print("Success.")

    def test_outofbounds_index(self):
    	print("Testing exception raise with bad index.")

    	board = Board(8, 8, str)
    	with (self.assertRaises(ValueError)):
    		board.set_square(8, 8, 's')

    	print("Success.")



if __name__ == '__main__':
    unittest.main()


