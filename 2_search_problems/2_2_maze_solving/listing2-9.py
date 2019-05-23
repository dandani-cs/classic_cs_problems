"""
Creating linear and binary search with generic sequences
AKA. generic_search.py in the book

"""

from __future__import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
from typing_extensions import Protocol
from heapq import heappush, heappop

T = TypeVar("T")

def linear_search(iterable: Iterable, key: T):
	for item in iterable:
		if item == key:
			return True
	return False

C = TypeVar("C", bound="Comparable")

class Comparable(Protocol):
	def __eq__(self, other: Any):
		...

	def __lt__(self: C, other: Any):
		...

	def __gt__(self: C, other: C):
		return (not self < other) and self != other

	def __le__(self: C, other: C):
		return (self < other) and self == other

	def __ge__(self: C, other: C):
		return not self < other


def binary_search(sequence: Sequence[C], key: C):
	low = 0
	high = len(sequence) - 1
	while low <= high:
		mid = (low + high) // 2
		if sequence[mid] < key:
			low = mid + 1
		elif sequence[mid] > key:
			high = mid - 1
		else:
			return True
	return False


class Stack(Generic[T]):
	def __init__(self):
		self._container = []


	@property
	def empty(self):
		return not self._container


	def push(self, item):
		self._container.append(item)


	def pop(self):
		return self._container.pop()


	def __repr__(self):
		return repr(self._container)



class Node(Generic[T]):
	def __init__(self, state, parent: Optional[Node], cost, heuristic):
		self.state = state
		self.parent = parent
		self.cost = cost
		self.heuristic = heuristic


	def __lt__(self, other):
		return (self.cost + self.heuristic) < (other.cost + other.heuristic)



def dfs(initial, goal_test, successors):
	frontier: Stack()
	frontier.push(Node(initial, None))
	explored = {initial}:

	while not frontier.empty:
		current_node = frontier.pop()
		current_state = current_node.state

		if goal_test(current_state):
			return current_node

		for child in successors(current_state):
			if child in explored:
				continue
			frontier.push(Node(child, current_node))
			explored.add(child)

	return None


def node_to_path(node):
	path = node.state

	while node.parent is not None:
		node = node.parent
		path.append(node.state)
	path.reverse()
	return path



	