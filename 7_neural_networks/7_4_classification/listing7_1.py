""" Preliminary files and functions for neural networks
util.py
"""

from typing import List
from math import exp

def dot_product(xs, ys):
	return sum(x * y for x, y in zip(xs, ys))


def sigmoid(x):
	return 1.0 / (1.0 + exp(-x))


def derivative_sigmoid(x):
	sig = sigmoid(x)
	return sig * (1 - sig)


def normalize_by_feature_scaling(dataset):
	for col_num in range(len(dataset[0])):
		column = [row[col_num] for row in dataset]
		minimum = min(column)
		maximum = max(column)
		for row_num in range(len(dataset)):
			dataset[row_num][col_num] = ( dataset[row_num][col_num] - minimum ) / ( maximum - minimum )

			


