"""
Own rendition of the circuit board layout 
"""

from typing import NamedTuple, List, Dict, Optional
from listing3_1 import CSP, Constraint

class GridLocation(NamedTuple):
	row: int
	col: int


def generate_grid(rows, columns):
	return [[" " for c in range(columns)] for r in range(rows)]


def display_grid(grid):
	for row in grid:
		print("".join(row))


def generate_domain(part, grid):
	domain = []
	grid_height = len(grid)
	grid_width = len(grid[0])
	part_height, part_width = part

	for row in range(grid_height):
		for col in range(grid_width):
			cols_left = range(col, col + part_width)
			rows_left = range(row, row + part_height)

			if col + part_width <= grid_width and row + part_height <= grid_height:
				domain.append([GridLocation(r, c) for c in cols_left for r in rows_left])

			if row + part_width <= grid_height and col + part_height <= grid_width:
				domain.append([GridLocation(r, c) for r in rows_left for c in cols_left ])


	return domain


class CircuitBoardConstraint(Constraint):
	def __init__(self, parts):
		super().__init__(parts)
		self.parts = parts


	def satisfied(self, assignment):
		all_locations = [locs for values in assignment.values() for locs in values]

		return len(set(all_locations)) == len(all_locations)



if __name__ == '__main__':
	grid = generate_grid(9, 9)
	parts = [(4, 3), (2,4)]
	locations = {}
	for part in parts:
		locations[part] = generate_domain(part, grid)

	csp = CSP(parts, locations)
	csp.add_constraint(CircuitBoardConstraint(parts))
	solution = csp.backtracking_search()
	if solution is None:
		print("No solution")
	else:
		# print(solution)
		for grid_locations in solution.values():

			for row, col in grid_locations:
				grid[row][col] = "X"


		display_grid(grid)









