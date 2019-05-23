"""
Comparing performances of binary and linear search
Uses timeit module; does not work

"""
import timeit
import random
from time import sleep


def linear_search(collection, key_item):
	for i in collection:
		if i == key_item:
			return True
	return False

def binary_search(collection, key_item):
	low = 0
	high = len(collection) - 1
	while low <= high:
		mid = (low + high) // 2
		if collection[mid] < key_item:
			low = mid + 1
			# print(low)
		elif collection[mid] > key_item:
			high = mid - 1
			# print(high)
		else: 
			return True

		# sleep(10)

	return False

def wrapper(func, *args, **kwargs):
	def wrapped():
		return func(*args, **kwargs)
	return wrapped

if __name__ == '__main__':
	# setup = """
	# sequence = [x for x in range(1, 1000001)]
	# key = random.randint(1, 1000001)


	# """
	sequence = [x for x in range(1, 1000001)]
	# for x in sequence:
	# 	print(x)
	key = random.randint(1, 1000001)
	print("generated sequence")
	print(linear_search(sequence, key))
	linear_time = timeit.timeit("linear_search(sequence, key)", setup="from __main__ import linear_search, key, sequence")
	# linear_wrapped = "linear_search(sequence, key)"
	# linear_wrapped = wrapper(linear_search, sequence, key)
	# binary_wrapped = wrapper(binary_search, sequence, key)
	# linear_time = timeit.timeit(linear_wrapped)
	print(linear_time)
	# # print(str(key))
	# # print(binary_search(sequence, key))
	# print(timeit.timeit(binary_wrapped))
