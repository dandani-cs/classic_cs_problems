"""
phone number mnemonics
"""
from typing import Dict, Tuple, Iterable, List
from itertools import product
import enchant

phone_mapping = {"1": ("1",),
                 "2": ("a", "b", "c"),
                 "3": ("d", "e", "f"),
                 "4": ("g", "h", "i"),
                 "5": ("j", "k", "l"),
                 "6": ("m", "n", "o"),
                 "7": ("p", "q", "r", "s"),
                 "8": ("t", "u", "v"),
                 "9": ("w", "x", "y", "z"),
                 "0": ("0",)}

def possible_mnemonics(phone_no):
	letter_tuples = []
	for digit in phone_no:
		letter_tuples.append(phone_mapping.get(digit, (digit, )))
		# print(digit, letter_tuples)
	return product(*letter_tuples)


if __name__ == '__main__':
	true_mnemonic = []
	d = enchant.Dict("en_US")
	phone_no = input("Enter a phone_no: ")
	print("Here are potential mnemonics:")
	for mnemonic in possible_mnemonics(phone_no):
		if d.check("".join(mnemonic)):
			true_mnemonic.append("".join(mnemonic))

	print(true_mnemonic)