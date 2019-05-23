"""
Maze solving program
"""

from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
from listing2-9 import dfs, bfs, node_to_path, astar, Node

T = Type

class Cell(str, Enum):
	EMPTY = " "
	BLOCKED = "X"
	START = "S"
	GOAL = "G"
	PATH = "*"


class MazeLocation(NamedTuple):
	row: int
	col: int


class Maze:
	def __init__(self, row = 10, col = 10, sparseness = 0.2, start = MazeLocation(0, 0), goal = MazeLocation(9, 9)):
		self._row = row
		self._col = col
		self.start = start
		self.goal = goal

		self._grid = [[Cell.EMPTY for c in range(col)] for r in range(row)]

		self._randomly_fill(row, col, sparseness)

		self._grid[start.row][start.col] = Cell.START
		self._grid[goal.row][goal.col] = Cell.GOAL


	def _randomly_fill(self, row, col, sparseness):
		for row in range(row):
			for col in range(col):
				if random.uniform(0, 1.0) < sparseness:
					self._grid[row][col] = Cell.BLOCKED

					
	def __str__(self):
		output = ""
		for row in self._grid:
			output += "".join([c.value for c in row]) + "\n"
		return output


	def goal_test(self, ml):
		return ml == self.goal

	def successors(self, ml):
		locations = []
		if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.col] != Cell.BLOCKED:
			locations.append(MazeLocation(ml.row + 1, ml.column))
		if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.col] != Cell.BLOCKED:
			locations.append(MazeLocation(ml.row - 1, ml.column))
		if ml.col + 1 < self._col and self._grid[ml.row][ml.col + 1] != Cell.BLOCKED:
			locations.append(MazeLocation(ml.row, ml.col + 1))
		if ml.col - 1 >= 0 and self._grid[ml.row][ml.col - 1] != Cell.BLOCKED:
			locations.append(MazeLocation(ml.row, ml.col - 1))

		return locations



	def mark(self, path):
		for maze_location in path:
			self._grid[maze_location.row][maze_location.col] = Cell.PATH
		self._grid[self.start.row][self.start.col] = Cell.START
		self._grid[self.goal.row][self.goal.col] = Cell.GOAL


	def clear(self, path):
		for maze_location in path:
			self._grid[maze_location.row][maze_location.col] = Cell.EMPTY
		self._grid[self.start.row][self.start.col] = Cell.START
		self._grid[self.goal.row][self.goal.col] = Cell.GOAL



if __name__ == '__main__':
	m = Maze()
	print(m)
	solution1 = dfs(m.start, m.goal_test, m.successors)
	if solution1 is None:
		print("No solution for dfs")

	else:
		path1 = node_to_path(solution1)
		m.mark(path1)
		print(m)
		m.clear(path1)