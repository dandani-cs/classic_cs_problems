"""
Calculating pi using the Leibniz formula and rote conversion

"""

def calculating_pi(n):
	pi = 0.0
	numerator = 4.0
	denominator = 1.0
	operation = 1.0

	for _ in range(n):
		pi += operation * (numerator / denominator)
		denominator += 2.0
		operation *= -1.0

	return pi

if __name__ == '__main__':
	print(calculating_pi(100000))