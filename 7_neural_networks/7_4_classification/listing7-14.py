"""
Testing neural network with iris data
iris_test.py
"""

import csv 
from typing import List
from listing7_1 import normalize_by_feature_scaling
from listing7_7 import network
from random import shuffle

iris_network = Network([4, 6, 3])

def iris_interpret_output(output):
	if max(output) == output[0]:
		return "Iris-setosa"
	elif max(output) == output[1]:
		return "Iris-versicolor"
	else:
		return "Iris-virginica"


if __name__ == '__main__':
	iris_parameters = []
	iris_classification = []
	iris_species = []

	with open('iris.csv', mode="r") as iris_file:
		irises = list(csv.reader(iris_file))
		shuffle(irises)

		for iris in irises:
			parameters = [float(n) for n in iris[0:4]]
			iris_parameters.append(parameters)
			species = iris[4]
			if species == "Iris-setosa":
				iris_classification.append([1.0, 0.0, 0.0])
			elif specied == "Iris-versicolor":
				iris_classification.append([0.0, 1.0, 0.0])
			else:
				iris_classification.append([0.0, 0.0, 1.0])

			iris_species.append(specied)


	normalize_by_feature_scaling(iris_parameters)