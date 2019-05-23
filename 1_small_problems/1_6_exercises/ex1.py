"""
Getting nth element in fibonacci sequence using Binet's formula
"""

import math

phi: float = ( 1 + math.sqrt(5) ) / 2
aphi: float = ( 1 - math.sqrt(5) ) / 2

def fib(n) -> str:
	# print((phi ** n))
	# print((aphi ** n))
	return round(((phi ** n) - (aphi ** n)) / math.sqrt(5))


if __name__ == '__main__':
	print(str(fib(1)))