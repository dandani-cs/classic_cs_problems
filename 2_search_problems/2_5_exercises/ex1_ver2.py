"""
Comparing performances of binary and linear search
Using time.time 

"""
import random
from time import sleep, time

sequence = [x for x in range(1, 1000001)]
key = random.randint(1, 1000001)

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

def functimer(func, *args):
	start = time()
	func(*args)
	end = time()

	return end - start


if __name__ == '__main__':

	sequence = [x for x in range(1, 1000001)]
	
	key = random.randint(1, 1000001)

	linear_performance = functimer(linear_search, sequence, key)
	binary_performance = functimer(binary_search, sequence, key)
	print("Linear search: " + str(linear_performance))
	print("Binary search: " + str(binary_performance))
	print("Difference: " + str(linear_performance - binary_performance))

	
