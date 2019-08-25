"""
code for Tic Tac Toe
tictactoe.py
"""

from __future__ import annotations
from typing import List
from enum import Enum 
from listing8_1 import Piece, Board, Move


class TTTPiece(Piece, Enum):
	X = "X"
	O = "O"
	E = " "


	@property
	def opposite(self):
		if self == TTTPiece.X:
			return TTTPiece.O
		elif self == TTTPiece.O:
			return TTTPiece.X
		else:
			return TTTPiece.E

	def __str__(self):
		return self.value


class TTTBoard(Board):
	def __init__(self, position = [TTTPiece.E] * 9, turn = TTTPiece.X):
		self.position = position
		self._turn = turn


	@property
	def turn(self):
		return self._turn


	def move(self, location):
		temp_position = self.position.copy()
		temp_position[location] = self._turn
		return TTTBoard(temp_position, self._turn.opposite)


		
	
	