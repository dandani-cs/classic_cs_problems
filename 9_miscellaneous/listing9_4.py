"""
travelling salesman bruteforce method
tsp.py
"""

from typing import Dict, List, Iterable, Tuple
from itertools import permutations

vt_distances: Dict[str, Dict[str, int]] = {
    "Rutland":
        {"Burlington": 67,
         "White River Junction": 46,
         "Bennington": 55,
         "Brattleboro": 75},
    "Burlington":
        {"Rutland": 67,
         "White River Junction": 91,
         "Bennington": 122,
         "Brattleboro": 153},
    "White River Junction":
        {"Rutland": 46,
         "Burlington": 91,
         "Bennington": 98,
         "Brattleboro": 65},
    "Bennington":
        {"Rutland": 55,
         "Burlington": 122,
         "White River Junction": 98,
         "Brattleboro": 40},
    "Brattleboro":
        {"Rutland": 75,
         "Burlington": 153,
         "White River Junction": 65,
         "Bennington": 40}
}

vt_cities = vt_distances.keys()
city_permutations = permutations(vt_cities)

# for n in city_permutations:
#     print(n)

tsp_paths = [c + (c[0],) for c in city_permutations]


if __name__ == '__main__':
    best_path: Tuple[str, ...]
    min_distance = 9999999999
    for path in tsp_paths:
        distance = 0
        last = path[0]
        for next in path[1:]:
            distance += vt_distances[last][next]
            last = next
        if distance < min_distance:
            best_path = path
            min_distance = distance

    print(f"Shortest path: {best_path} in {min_distance} miles.")