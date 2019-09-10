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

	@property
	def legal_moves(self):
		return [Move(l) for l in range(len(self.position)) if self.position[l] == TTTPiece.E]


	@property 
	def is_win(self):
		return self.position[0] == self.position[1] and self.position[0] == self.position[2] and self.position[0] != TTTPiece.E or \
        self.position[3] == self.position[4] and self.position[3] == self.position[5] and self.position[3] != TTTPiece.E or \
        self.position[6] == self.position[7] and self.position[6] == self.position[8] and self.position[6] != TTTPiece.E or \
        self.position[0] == self.position[3] and self.position[0] == self.position[6] and self.position[0] != TTTPiece.E or \
        self.position[1] == self.position[4] and self.position[1] == self.position[7] and self.position[1] != TTTPiece.E or \
        self.position[2] == self.position[5] and self.position[2] == self.position[8] and self.position[2] != TTTPiece.E or \
        self.position[0] == self.position[4] and self.position[0] == self.position[8] and self.position[0] != TTTPiece.E or \
        self.position[2] == self.position[4] and self.position[2] == self.position[6] and self.position[2] != TTTPiece.E	
	
	def evaluate(self, player):
		if self.is_win and self.turn == player:
			return -1
		elif self.is_win and self.turn != player:
			return 1
		else:
			return 0


	def __repr__(self):
		return f"""\t\t {self.position[0]}|{self.position[1]}|{self.position[2]}
		{self.position[3]}|{self.position[4]}|{self.position[5]}
		{self.position[6]}|{self.position[7]}|{self.position[8]}
		"""


		
	
	