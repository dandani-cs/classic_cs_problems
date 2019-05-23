"""
Adding counter to search algorithms to compare performances
"""


from listing2_9ex import dfs, bfs, astar, node_to_path, Node
from listing2_10 import Maze, manhattan_distance
from statistics import mean


dfs_performance = []
bfs_performance = []
astar_performace = []

for i in range(100):
	m = Maze()
	solution1, dfs_counter = dfs(m.start, m.goal_test, m.successors)
	dfs_performance.append(dfs_counter)
	solution2, bfs_counter = bfs(m.start, m.goal_test, m.successors)
	bfs_performance.append(bfs_counter)
	distance = manhattan_distance(m.goal)
	solution3, astar_counter = astar(m.start, m.goal_test, m.successors, distance)
	astar_performace.append(astar_counter)
print("DFS average: " + str(mean(dfs_performance)))
print("BFS average: " + str(mean(bfs_performance)))
print("A* average: " + str(mean(astar_performace)))


# solution2