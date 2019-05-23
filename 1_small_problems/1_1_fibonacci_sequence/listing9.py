"""
Space-saving iteration method of Fibonacci sequence using generators

"""

from typing import Generator

def fib6(n):
	yield 0
	if n > 0: yield 1
	last: int = 0
	next: int = 1
	for i in range (1, n):
		last, next = next, last+next
		yield next

if __name__ == '__main__':
	for i in fib6(5):
		print(i)