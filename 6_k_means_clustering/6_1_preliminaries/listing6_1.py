"""
Calculating for z-scores
"""

from __future__ import annotations
from typing import TypeVar, Generic, List, Sequence
from copy import deepcopy
from functools import partial
from random import uniform
from statistics import mean, pstdev
from dataclasses import dataclass 
from listing6_2 import DataPoint

def zscores(original):
	avg = mean(original)
	std = pstdev(original)
	if std == 0:
		return [0] * len(original)

	return [(x - avg) / std for x in original]