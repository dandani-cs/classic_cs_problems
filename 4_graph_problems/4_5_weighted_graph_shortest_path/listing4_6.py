"""
Creates a weighted edge as subclass of edge class
"""

from __future__ import annotations
from dataclasses import dataclass
from listing4_1 import Edge 


@dataclass
class WeightedEdge(Edge):
	weight: int


	def reversed(self):
		return WeightedEdge(self.v, self.u, self.weight)


	def __lt__(self, other):
		return self.weight < other.weight


	def __str__(self):
		return f"{self.u} {self.weight}> {self.v}"

