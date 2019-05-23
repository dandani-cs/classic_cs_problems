"""
Solves Towers of Hanoi puzzle using stacks and type hints

"""

from typing import TypeVar, Generic, List
T = TypeVar("T")

class Stack(Generic[T]):

	def __init__(self, name):
		self.name = name
		self._container: List[T] = []


	def push(self, item):
		self._container.append(item)

	
	def pop(self):
		return self._container.pop()


	def __repr__(self):
		return repr(self._container)


def hanoi(begin, end, temp, n):
	print("n: {}, begin: {}, temp: {}, end: {}".format(str(n), begin.name, temp.name, end.name))
	if n == 1:
		begin_item = begin.pop()
		end.push(begin_item)
		print("Pushing {} from {} in {}".format(begin_item, begin.name, end.name))
	else:
		
		hanoi(begin, temp, end, n - 1) #a, b, c
		hanoi(begin, end, temp, 1) # a, c, b
		hanoi(temp, end, begin, n - 1) # b, c, a


if __name__ == '__main__':
	num_disc = 3
	tower_a = Stack("a")
	tower_b = Stack("b")
	tower_c = Stack("c")

	for i in range(1, num_disc + 1):
		tower_a.push(i)

	hanoi(tower_a, tower_c, tower_b, num_disc)
	print(tower_a)
	print(tower_b)
	print(tower_c)