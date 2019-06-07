"""
Creating a framework for graph problems
"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Edges:
	u: int
	v: int


	def reversed(self):
		return Edge(self.u, self.v)


	def __str__(self):
		return f"{self.u} -> {self.v}"

		
