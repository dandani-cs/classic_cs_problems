"""
Creating a Direct edge for digraph support
"""

from __future__ import annotations
from listing4_1 import Edge
from dataclasses import dataclass


@dataclass
class DirectEdge(Edge):
	def reversed(self):
		raise Exception("Direct edge cannot be reversed")


	def __str__(self):
		return f"{self.u} -> {self.v}"