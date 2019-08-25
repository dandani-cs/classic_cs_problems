from __future__ import annotations
from typing import List, Callable, TypeVar, Tuple
from functools import reduce
from listing7_4 import Layer
from listing7_1 import sigmoid, derivative_sigmoid


T = TypeVar("T")


class Network:
	def __init__(self, layer_structure, learning_rate, activation_function = sigmoid, derivative_activation_function = derivative_sigmoid):
		if len(layer_structure) < 3:
			raise ValueError("Error, should be at least 3 layers")

		self.layers = []

		input_layer = Layer(None, layer_structure[0], learning_rate, activation_function, derivative_activation_function)
		self.layers.append(input_layer)

		for previous, num_neurons in enumerate(layer_structure[1::]):
			next_layer = Layer(self.layers[previous], num_neurons, learning_rate, activation_function, derivative_activation_function)
			self.layers.append(next_layer)


	def outputs(self, input):
		return reduce(lambda inputs, layer: layer.outputs(inputs), self.layers, input)


	def backpropagation(self, expected):
		last_layer = len(self.layers) - 1
		self.layers[last_layer].calculate_deltas_for_output_layer(expected)

		for l in range(last_layer - 1, 0, -1):
			self.layers[l].calculate_deltas_for_hidden_layer(self.layers[l + 1])


	def update_weights(self):
		for layer in self.layers[1:]:
			for neuron in layer.neurons:
				for w in range(len(neuron.weights)):
					neuron.weights[w] = neuron.weights[w] + (neuron.learning_rate * (layer.previous_layer.output_cache[w]) * neuron.delta)



	def train(self, inputs, expecteds):
		for location, xs in enumerate(inputs):
			ys = expecteds[location]
			outs = self.outputs(xs)
			#print(outs)
			self.backpropagation(ys)
			self.update_weights()


	def validate(self, inputs, expecteds, interpret_output):
		correct = 0
		# counter = 0
		for input, expected in zip(inputs, expecteds):
			#print("HJACKSBKD")
			#print("input, expected: ", input, expected)
			result = interpret_output(self.outputs(input))
			#print("result: ", result)

			if result == expected:
				correct += 1

		percentage = correct / len(inputs)
		return correct, len(inputs), percentage
			