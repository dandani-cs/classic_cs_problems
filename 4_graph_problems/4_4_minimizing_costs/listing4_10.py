"""
Creating the minimum spanning tree solution
"""
from typing import TypeVar, List, Optional
from listing4_7 import WeightedGraph
from listing4_6 import WeightedEdge
from listing4_9 import PriorityQueue

V = TypeVar("V")


def total_weight(wp):
	return sum([e.weight for e in wp])


def mst(wg, start = 0):
	if start > (wg.vertex_count) or start < 0:
		return None
	result = []
	pq = PriorityQueue()
	visited = [False] * wg.vertex_count


	def visit(index):
		visited[index] = True
		for edge in wg.edges_for_index(index):
			if not visited[edge.v]:
				pq.push(edge)

	visit(start)

	while not pq.empty:
		edge = pq.pop()
		if visited[edge.v]:
			continue

		result.append(edge)
		visit(edge.v)


	return result


def print_weighted_path(wg, wp):
	for edge in wp:
		print(f"{wg.vertex_at(edge.u)} {edge.weight}> {wg.vertex_at(edge.v)}")
		print(f"Total weight: {total_weight(wp)}")



if __name__ == '__main__':
	city_graph2: WeightedGraph[str] = WeightedGraph(["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston", "New York", "Atlanta", "Miami", "Dallas", "Houston", "Detroit", "Philadelphia", "Washington"])

	city_graph2.add_edge_by_vertices("Seattle", "Chicago", 1737)
	city_graph2.add_edge_by_vertices("Seattle", "San Francisco", 678)
	city_graph2.add_edge_by_vertices("San Francisco", "Riverside", 386) 
	city_graph2.add_edge_by_vertices("San Francisco", "Los Angeles", 348) 
	city_graph2.add_edge_by_vertices("Los Angeles", "Riverside", 50) 
	city_graph2.add_edge_by_vertices("Los Angeles", "Phoenix", 357) 
	city_graph2.add_edge_by_vertices("Riverside", "Phoenix", 307) 
	city_graph2.add_edge_by_vertices("Riverside", "Chicago", 1704) 
	city_graph2.add_edge_by_vertices("Phoenix", "Dallas", 887) 
	city_graph2.add_edge_by_vertices("Phoenix", "Houston", 1015) 
	city_graph2.add_edge_by_vertices("Dallas", "Chicago", 805) 
	city_graph2.add_edge_by_vertices("Dallas", "Atlanta", 721) 
	city_graph2.add_edge_by_vertices("Dallas", "Houston", 225) 
	city_graph2.add_edge_by_vertices("Houston", "Atlanta", 702) 
	city_graph2.add_edge_by_vertices("Houston", "Miami", 968) 
	city_graph2.add_edge_by_vertices("Atlanta", "Chicago", 588) 
	city_graph2.add_edge_by_vertices("Atlanta", "Washington", 543) 
	city_graph2.add_edge_by_vertices("Atlanta", "Miami", 604) 
	city_graph2.add_edge_by_vertices("Miami", "Washington", 923) 
	city_graph2.add_edge_by_vertices("Chicago", "Detroit", 238) 
	city_graph2.add_edge_by_vertices("Detroit", "Boston", 613) 
	city_graph2.add_edge_by_vertices("Detroit", "Washington", 396) 
	city_graph2.add_edge_by_vertices("Detroit", "New York", 482) 
	city_graph2.add_edge_by_vertices("Boston", "New York", 190) 
	city_graph2.add_edge_by_vertices("New York", "Philadelphia", 81) 
	city_graph2.add_edge_by_vertices("Philadelphia", "Washington", 123)

	result = mst(city_graph2)

	if result is None:
		print("No solution!")
	else:
		print_weighted_path(city_graph2, result)