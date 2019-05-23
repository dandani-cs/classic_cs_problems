"""
Missionaries and Cannibals problem 

"""

from __future__ import annotations
from typing import List, Optional
from listing2_9 import bfs, Node, node_to_path
from time import sleep

MAX_NUM = 3

class MCState:
	def __init__(self, missionaries, cannibals, boat):
		self.wm = missionaries
		self.wc = cannibals
		self.em = MAX_NUM - self.wm
		self.ec = MAX_NUM - self.wc

		self.boat = boat


	def __str__(self):
		return ("""On the west bank, there are {} missionaries and {} cannibals.
			On the east bank, there are {} missionaries and {} cannibals. 
			The boat is on the {} bank.
			""".format(self.wm, self.wc, self.em, self.ec, ("west" if self.boat else "east")))


	def goal_test(self):
		# print("starting goal_test")
		return self.is_legal and self.em == MAX_NUM and self.ec == MAX_NUM


	@property
	def is_legal(self):
		if (self.wm < self.wc):
			if self.wm > 0:
				# print("west is less")
				return False
		if (self.em < self.ec):
			if self.em > 0:
				# print("east is less")
				return False
		return True


	def successors(self):
		sucs = []
		if self.boat:
			if self.wm > 1:
				sucs.append(MCState(self.wm - 2, self.wc, not self.boat))
			if self.wm > 0:
				sucs.append(MCState(self.wm - 1, self.wc, not self.boat))
			if self.wc > 1:
				sucs.append(MCState(self.wm, self.wc - 2, not self.boat))
			if self.wc > 0:
				sucs.append(MCState(self.wm, self.wc - 1, not self.boat))
			if (self.wc > 0) and (self.wm > 0):
				sucs.append(MCState(self.wm - 1, self.wc - 1, not self.boat))

		else:
			if self.em > 1:
				sucs.append(MCState(self.wm + 2, self.wc, not self.boat))
			if self.em > 0:
				sucs.append(MCState(self.wm + 1, self.wc, not self.boat))
			if self.ec > 1:
				sucs.append(MCState(self.wm, self.wc + 2, not self.boat))
			if self.ec > 0:
				sucs.append(MCState(self.wm, self.wc + 1, not self.boat))
			if (self.ec > 0) and (self.em > 0):
				sucs.append(MCState(self.wm + 1, self.wc + 1, not self.boat))

		# for x in sucs:
		# 	if not x.is_legal:
		# 		print(x)
		# 	else:
		# 		print("legal")
		# 		print(x)
		# sleep(60)		
		return [x for x in sucs if x.is_legal]



def display_solution(path):
	if len(path) == 0:
		return

	old_state = path[0]
	print(old_state)
	for current_state in path[1:]:
		if current_state.boat:
			print("{} missionaries and {} cannibals have moved from east to west bank.".format(old_state.em - current_state.em, old_state.ec - current_state.ec))
		else:
			print("{} missionaries and {} cannibals have moved from west to east bank.".format(old_state.wm - current_state.wm, old_state.wc - current_state.wc))
		print(current_state)
		old_state = current_state


if __name__ == '__main__':
	start = MCState(MAX_NUM, MAX_NUM, True)
	# print(start)
	solution = bfs(start, MCState.goal_test, MCState.successors)

	if solution is None:
		print("No solution")
	else:
		path = node_to_path(solution)
		display_solution(path)