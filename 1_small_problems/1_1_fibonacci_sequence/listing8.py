"""
Better performing fibonacci sequence approach with old-fasinoed iteration

"""

def fib5(n: int) -> int:
	if n == 0: return n
	last: int = 0
	next: int = 1
	for i in range (1, n):
		last, next = next, last+next
		print("Loop " + str(i))
		print(last)
		print(next)
	return next


if __name__ == '__main__':
	print(fib5(5))