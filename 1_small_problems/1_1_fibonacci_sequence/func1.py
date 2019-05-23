"""
Recursion simple example

Loops from 1 to 10
"""


def func1(x):
	if x > 10:
		return x
	return func1(x + 1)

if __name__ == '__main__':
	print(func1(0))