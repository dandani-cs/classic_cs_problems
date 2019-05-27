"""
Solving the eight queens problem
"""

from listing3_1 import Constraint, CSP
from typing import Dict, List, Optional

class QueensConstraint(Constraint):
	
	def __init__(self, columns):
		super().__init__(columns)
		self.columns = columns


	def satisfied(self, assignment):
		for qc1, qr1 in assignment.items():
			for qc2 in range(qc1 + 1, len(self.columns) + 1):
				if qc2 in assignment:
					qr2 = assignment[qc2]
					if qr1 == qr2:
						return False
					if abs(qc1 - qc2) == abs(qr1 - qr2):
						return False
		return True



if __name__ == '__main__':
	columns = [1, 2, 3, 4, 5, 6, 7, 8]
	rows = {}
	for column in columns:
		rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]

	csp = CSP(columns, rows)
	csp.add_constraint(QueensConstraint(columns))
	solution = csp.backtracking_search()
	if solution is None:
		print("No solution")

	else:
		print(solution)

