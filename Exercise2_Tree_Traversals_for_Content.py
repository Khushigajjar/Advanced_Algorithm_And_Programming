from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class CategoryNode:
	category_id: int
	name: str
	post_count: int
	left: Optional["CategoryNode"] = None
	right: Optional["CategoryNode"] = None
	parent: Optional["CategoryNode"] = None


# In-order (Left -> Root -> Right)


def in_order_collect(node: Optional[CategoryNode]) -> list[str]:
	result: list[str] = []
	if node is None:
		return result

	result.extend(in_order_collect(node.left))
	result.append(node.name)
	result.extend(in_order_collect(node.right))
	return result


def in_order_accumulate_posts(node: Optional[CategoryNode], running_total: int = 0) -> int:
	if node is None:
		return running_total

	running_total = in_order_accumulate_posts(node.left, running_total)
	running_total += node.post_count
	running_total = in_order_accumulate_posts(node.right, running_total)
	return running_total


def in_order_find_kth(node: Optional[CategoryNode], k: int) -> Optional[str]:
	if k < 1:
		raise ValueError("k must be >= 1 (1-indexed)")

	counter = 0

	def helper(current: Optional[CategoryNode]) -> Optional[str]:
		nonlocal counter
		if current is None:
			return None

		left_result = helper(current.left)
		if left_result is not None:
			return left_result

		counter += 1
		if counter == k:
			return current.name

		return helper(current.right)

	return helper(node)


# Pre-order (Root -> Left -> Right)


def pre_order_export(node: Optional[CategoryNode], depth: int = 0) -> str:
	if node is None:
		return ""

	lines: list[str] = []

	def helper(current: Optional[CategoryNode], current_depth: int) -> None:
		if current is None:
			return
		indentation = "  " * current_depth
		lines.append(f"{indentation}{current.name}({current.post_count})")
		helper(current.left, current_depth + 1)
		helper(current.right, current_depth + 1)

	helper(node, depth)
	return "\n".join(lines)


def pre_order_copy(node: Optional[CategoryNode], parent: Optional[CategoryNode] = None) -> Optional[CategoryNode]:
	if node is None:
		return None

	new_node = CategoryNode(
		category_id=node.category_id,
		name=node.name,
		post_count=node.post_count,
		parent=parent,
	)
	new_node.left = pre_order_copy(node.left, parent=new_node)
	new_node.right = pre_order_copy(node.right, parent=new_node)
	return new_node


def pre_order_serialize(node: Optional[CategoryNode]) -> str:
	if node is None:
		return "#"

	token = f"{node.name}({node.post_count})"
	return f"{token}|{pre_order_serialize(node.left)}|{pre_order_serialize(node.right)}"


# Post-order (Left -> Right -> Root)


def post_order_total_posts(node: Optional[CategoryNode]) -> int:
	if node is None:
		return 0

	left_total = post_order_total_posts(node.left)
	right_total = post_order_total_posts(node.right)
	return left_total + right_total + node.post_count


def post_order_average_depth(node: Optional[CategoryNode]) -> float:
	total_depth, count = _avg_depth_helper(node, 0)
	if count == 0:
		return 0.0
	return total_depth / count


def _avg_depth_helper(node: Optional[CategoryNode], current_depth: int) -> tuple[int, int]:
	if node is None:
		return 0, 0

	if node.left is None and node.right is None:
		return current_depth, 1

	left_depth_sum, left_count = _avg_depth_helper(node.left, current_depth + 1)
	right_depth_sum, right_count = _avg_depth_helper(node.right, current_depth + 1)
	return left_depth_sum + right_depth_sum, left_count + right_count


def post_order_collect_leaves(node: Optional[CategoryNode]) -> list[str]:
	result: list[str] = []
	if node is None:
		return result

	result.extend(post_order_collect_leaves(node.left))
	result.extend(post_order_collect_leaves(node.right))
	if node.left is None and node.right is None:
		result.append(node.name)
	return result




def find_most_popular_category(node: Optional[CategoryNode]) -> Optional[str]:
	best_name, _best_count = _find_most_popular_category(node, best_name=None, best_count=None)
	return best_name


def _find_most_popular_category(
	node: Optional[CategoryNode],
	best_name: Optional[str],
	best_count: Optional[int],
) -> tuple[Optional[str], Optional[int]]:
	if node is None:
		return best_name, best_count

	if best_count is None or node.post_count > best_count:
		best_name = node.name
		best_count = node.post_count

	best_name, best_count = _find_most_popular_category(node.left, best_name, best_count)
	best_name, best_count = _find_most_popular_category(node.right, best_name, best_count)
	return best_name, best_count


def category_with_most_subcategories(node: Optional[CategoryNode]) -> Optional[str]:
	if node is None:
		return None

	best_name: Optional[str] = None
	best_children: Optional[int] = None
	best_name, best_children = _category_with_most_subcategories(node.left, best_name, best_children)
	best_name, best_children = _category_with_most_subcategories(node.right, best_name, best_children)
	return best_name


def _category_with_most_subcategories(
	node: Optional[CategoryNode],
	best_name: Optional[str],
	best_children: Optional[int],
) -> tuple[Optional[str], Optional[int]]:
	if node is None:
		return best_name, best_children

	child_count = 0
	if node.left is not None:
		child_count += 1
	if node.right is not None:
		child_count += 1

	if best_children is None or child_count > best_children:
		best_name = node.name
		best_children = child_count

	best_name, best_children = _category_with_most_subcategories(node.left, best_name, best_children)
	best_name, best_children = _category_with_most_subcategories(node.right, best_name, best_children)
	return best_name, best_children


def _build_example_tree() -> CategoryNode:
	technology = CategoryNode(1, "Technology", 150)
	programming = CategoryNode(2, "Programming", 85, parent=technology)
	design = CategoryNode(3, "Design", 65, parent=technology)
	technology.left = programming
	technology.right = design

	python = CategoryNode(4, "Python", 42, parent=programming)
	java = CategoryNode(5, "Java", 30, parent=programming)
	programming.left = python
	programming.right = java

	django = CategoryNode(6, "Django", 18, parent=python)
	flask = CategoryNode(7, "Flask", 12, parent=python)
	python.left = django
	python.right = flask

	ui_ux = CategoryNode(8, "UI/UX", 38, parent=design)
	graphics = CategoryNode(9, "Graphics", 22, parent=design)
	design.left = ui_ux
	design.right = graphics

	return technology


if __name__ == "__main__":
	root = _build_example_tree()

	print("In-order:")
	print(" -> ".join(in_order_collect(root)))
	print("Total posts (accumulate):", in_order_accumulate_posts(root))
	print("6th (in-order):", in_order_find_kth(root, 6))

	print("\nPre-order export:")
	print(pre_order_export(root))
	print("\nPre-order serialize:")
	print(pre_order_serialize(root))

	print("\nTotal posts (post-order):", post_order_total_posts(root))
	print("Average leaf depth:", post_order_average_depth(root))
	print("Leaves:", post_order_collect_leaves(root))

	print("\nMost popular:", find_most_popular_category(root))
	print("Most subcategories:", category_with_most_subcategories(root))

