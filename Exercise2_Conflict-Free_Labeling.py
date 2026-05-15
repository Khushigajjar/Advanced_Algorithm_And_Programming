def _graph_nodes(graph):
	if isinstance(graph, dict):
		return list(graph.keys())
	return list(range(len(graph)))


def _graph_size(graph):
	return len(_graph_nodes(graph))


def _graph_neighbors(graph, node):
	if isinstance(graph, dict):
		return graph.get(node, [])
	return graph[node]


def _graph_edges(graph):
	edges = set()
	for u in _graph_nodes(graph):
		for v in _graph_neighbors(graph, u):
			if u == v:
				continue
			a, b = (u, v) if u < v else (v, u)
			edges.add((a, b))
	return edges


def is_valid_labeling(labeling, graph):
	"""Return True if no adjacent nodes share the same (assigned) label.

	Note: Unassigned nodes should use -1 and are ignored in the check.
	"""
	for (u, v) in _graph_edges(graph):
		if labeling[u] != -1 and labeling[v] != -1 and labeling[u] == labeling[v]:
			return False
	return True


def assign_labels(k, graph, node, labeling):
	"""Backtracking k-coloring.

	labeling is modified in-place; returns True if a coloring is found.
	"""
	n = _graph_size(graph)
	if node == n:
		return True

	for color in range(k):
		labeling[node] = color

		valid = True
		for neighbor in _graph_neighbors(graph, node):
			if 0 <= neighbor < n and labeling[neighbor] == color:
				valid = False
				break

		if valid:
			if assign_labels(k, graph, node + 1, labeling):
				return True

		labeling[node] = -1

	return False


def find_min_labels(graph):
	"""Find the minimum number of labels needed and one valid labeling."""
	n = _graph_size(graph)
	labeling = [-1] * n

	k = 1
	while k <= n:
		labeling = [-1] * n
		success = assign_labels(k, graph, 0, labeling)
		if success:
			return (k, labeling)
		k += 1

	return (n, labeling)


graph1 = {
	0: [1, 2, 3, 4],
	1: [0],
	2: [0],
	3: [0],
	4: [0],
}
min_k1, labeling1 = find_min_labels(graph1)
print("Test 1: Star Graph")
print(f"Minimum labels k={min_k1}, labeling={labeling1}")
print(f"Valid? {is_valid_labeling(labeling1, graph1)}")
print()


graph2 = {
	0: [1],
	1: [0, 2],
	2: [1, 3],
	3: [2, 4],
	4: [3],
}
min_k2, labeling2 = find_min_labels(graph2)
print("Test 2: Path Graph")
print(f"Minimum labels k={min_k2}, labeling={labeling2}")
print(f"Valid? {is_valid_labeling(labeling2, graph2)}")
print()


graph3 = {
	0: [1, 2, 3],
	1: [0, 2, 3],
	2: [0, 1, 3],
	3: [0, 1, 2],
}
min_k3, labeling3 = find_min_labels(graph3)
print("Test 3: Complete Graph K4")
print(f"Minimum labels k={min_k3}, labeling={labeling3}")
print(f"Valid? {is_valid_labeling(labeling3, graph3)}")
print()


graph4 = {
	0: [1],
	1: [0, 2],
	2: [1],
	3: [4],
	4: [3],
}
min_k4, labeling4 = find_min_labels(graph4)
print("Test 4: Disconnected Graph")
print(f"Minimum labels k={min_k4}, labeling={labeling4}")
print(f"Valid? {is_valid_labeling(labeling4, graph4)}")
print()

