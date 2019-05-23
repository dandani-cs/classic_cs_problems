"""
Searching for DNA nucleotides

"""

from enum import IntEnum
from typing import Tuple, List


Nucleotide = IntEnum("Nucleotide", ("A", "C", "G", "T"))

# Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
# Gene = List [Codon]

def str_to_gene(s):
	gene = []
	for i in range(0, len(s), 3):
		if (i + 2) >= len(s):
			return gene
		codon = (Nucleotide[s[i]], 
			Nucleotide[s[i + 1], 
			Nucleotide[s[i + 2]]])
		gene.append(codon)
	return gene # is this still necessary?


def linear_search(gene, key_codon):
	for codon in gene:
		if codon == key_codon:
			return True
	return False

def binary_search(gene, key_codon):
	low = 0
	high = len(gene) - 1
	while low <= high:
		mid = (low + high) // 2
		if gene[mid] < key_codon:
			low = mid + 1
		elif gene[mid] > key_codon:
			high = mid - 1
		else:
			return True
	return False