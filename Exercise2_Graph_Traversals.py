from __future__ import annotations
from collections.abc import Iterable
from typing import Any

Graph = dict[Any, list[Any]]

def _require_user_in_graph(graph: Graph, user: Any) -> None:
	if user not in graph:
		raise KeyError(f"User {user!r} is not present in the graph")

def neighbors(graph: Graph, user: Any) -> list[Any]:
	_require_user_in_graph(graph, user)
	return graph[user]

def dfs_recursive(graph: Graph, start_user: Any) -> list[Any]:
	_require_user_in_graph(graph, start_user)
	visited: set[Any] = set()
	result: list[Any] = []

	def dfs(u: Any) -> None:
		visited.add(u)
		result.append(u)
		for v in neighbors(graph, u):
			if v not in visited:
				dfs(v)

	dfs(start_user)
	return result

def dfs_iterative(graph: Graph, start_user: Any) -> list[Any]:
	_require_user_in_graph(graph, start_user)
	visited: set[Any] = set()
	stack: list[Any] = [start_user]
	result: list[Any] = []

	while stack:
		u = stack.pop()
		if u in visited:
			continue

		visited.add(u)
		result.append(u)

		for v in reversed(neighbors(graph, u)):
			if v not in visited:
				stack.append(v)

	return result


def find_connected_components(graph: Graph) -> list[list[Any]]:
	visited: set[Any] = set()
	components: list[list[Any]] = []

	for user in graph:
		if user in visited:
			continue

		component: list[Any] = []
		stack: list[Any] = [user]

		while stack:
			u = stack.pop()
			if u in visited:
				continue

			visited.add(u)
			component.append(u)

			for v in reversed(neighbors(graph, u)):
				if v not in visited:
					stack.append(v)

		components.append(component)

	return components


def is_connected(graph: Graph) -> bool:
	if not graph:
		return True
	return len(find_connected_components(graph)) == 1


def has_path(graph: Graph, start_user: Any, target_user: Any) -> bool:
	_require_user_in_graph(graph, start_user)
	_require_user_in_graph(graph, target_user)
	visited: set[Any] = set()

	def dfs(u: Any) -> bool:
		if u == target_user:
			return True
		visited.add(u)
		for v in neighbors(graph, u):
			if v not in visited and dfs(v):
				return True
		return False

	return dfs(start_user)


def find_path(graph: Graph, start_user: Any, target_user: Any) -> list[Any]:
	_require_user_in_graph(graph, start_user)
	_require_user_in_graph(graph, target_user)
	visited: set[Any] = set()
	path: list[Any] = []

	def dfs(u: Any) -> bool:
		visited.add(u)
		path.append(u)

		if u == target_user:
			return True

		for v in neighbors(graph, u):
			if v not in visited and dfs(v):
				return True

		path.pop()
		return False

	return path if dfs(start_user) else []


def get_connected_components_sizes(graph: Graph) -> list[int]:
	return [len(component) for component in find_connected_components(graph)]


def find_largest_component(graph: Graph) -> list[Any]:
	components = find_connected_components(graph)
	if not components:
		return []
	return max(components, key=len)


def find_isolated_users(graph: Graph) -> list[Any]:
	return [user for user, nbrs in graph.items() if len(nbrs) == 0]


def add_user(graph: Graph, user: Any) -> None:
	graph.setdefault(user, [])


def add_friendship(graph: Graph, user_a: Any, user_b: Any) -> None:
	add_user(graph, user_a)
	add_user(graph, user_b)

	if user_b not in graph[user_a]:
		graph[user_a].append(user_b)
	if user_a not in graph[user_b]:
		graph[user_b].append(user_a)

def add_friendships(graph: Graph, edges: Iterable[tuple[Any, Any]]) -> None:
	for a, b in edges:
		add_friendship(graph, a, b)


if __name__ == "__main__":
	social_graph: Graph = {}
	add_friendships(
		social_graph,
		[
			("Asha", "Bilal"),
			("Bilal", "Carmen"),
			("Carmen", "Daria"),
			("Asha", "Eshan"),
			("Farah", "Gio"),
		],
	)
	add_user(social_graph, "Hyejin")

	start = "Asha"
	print("DFS (recursive) from", start, ":", dfs_recursive(social_graph, start))
	print("DFS (iterative) from ", start, ":", dfs_iterative(social_graph, start))

	components = find_connected_components(social_graph)
	print("Connected components:", components)
	print("Component sizes:", get_connected_components_sizes(social_graph))
	print("Largest component:", find_largest_component(social_graph))
	print("Isolated users:", find_isolated_users(social_graph))
	print("Graph is connected?", is_connected(social_graph))

	print("Has path Asha -> Daria?", has_path(social_graph, "Asha", "Daria"))
	print("Has path Asha -> Gio?  ", has_path(social_graph, "Asha", "Gio"))
	print("Path Asha -> Daria:", find_path(social_graph, "Asha", "Daria"))
	print("Path Asha -> Gio:  ", find_path(social_graph, "Asha", "Gio"))
