"""
running tests for tic tac toe minimax algorithm
tictactoe_tests.py
"""

import unittest
from typing import List
from listing8_8 import find_best_move
from listing8_2 import TTTPiece, TTTBoard
from listing8_1 import Move 

class TTTMinimaxTestCase(unittest.TestCase):
	def test_easy_position(self):
		to_win_easy_position = [TTTPiece.X, TTTPiece.O, TTTPiece.X,
		TTTPiece.X, TTTPiece.E, TTTPiece.O,
		TTTPiece.E, TTTPiece.E, TTTPiece.O
		]
		test_board1 = TTTBoard(to_win_easy_position, TTTPiece.X)
		answer1 = find_best_move(test_board1)
		self.assertEqual(answer1, 6)


	def test_block_position(self):
		to_block_position = [TTTPiece.X, TTTPiece.E, TTTPiece.E,
		TTTPiece.E, TTTPiece.E, TTTPiece.O,
		TTTPiece.E, TTTPiece.X, TTTPiece.O
		]
		test_board2 = TTTBoard(to_block_position, TTTPiece.X)
		answer2 = find_best_move(test_board2)
		self.assertEqual(answer2, 2)


	def test_hard_position(self):
		to_win_hard_positon = [TTTPiece.X, TTTPiece.E, TTTPiece.E,
		TTTPiece.E, TTTPiece.E, TTTPiece.O,
		TTTPiece.O, TTTPiece.X, TTTPiece.E
		]
		test_board3 = TTTBoard(to_win_hard_positon, TTTPiece.X)
		answer3 = find_best_move(test_board3)
		self.assertEqual(answer3, 1)


if __name__ == "__main__":
	unittest.main()