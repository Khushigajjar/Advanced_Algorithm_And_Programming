from __future__ import annotations
import math
from typing import Any, Iterable, List, Optional, Sequence, Tuple

HeapEntry = Tuple[int, Any, float]
Heap = List[HeapEntry]


def _swap(heap: Heap, i: int, j: int) -> None:
	heap[i], heap[j] = heap[j], heap[i]


def _heapify_up(heap: Heap, i: int) -> int:
	while i > 0:
		parent = (i - 1) // 2
		if heap[i][0] > heap[parent][0]:
			_swap(heap, i, parent)
			i = parent
		else:
			break
	return i


def _heapify_down(heap: Heap, i: int) -> None:
	while True:
		largest = i
		left = 2 * i + 1
		right = 2 * i + 2

		if left < len(heap) and heap[left][0] > heap[largest][0]:
			largest = left
		if right < len(heap) and heap[right][0] > heap[largest][0]:
			largest = right

		if largest != i:
			_swap(heap, i, largest)
			i = largest
		else:
			break


def push(heap: Heap, post_id: Any, likes: int, timestamp: float) -> None:
	entry: HeapEntry = (likes, post_id, timestamp)
	heap.append(entry)
	_heapify_up(heap, len(heap) - 1)


def pop_max(heap: Heap) -> Optional[HeapEntry]:
	if len(heap) == 0:
		return None

	max_entry = heap[0]
	heap[0] = heap[len(heap) - 1]
	heap.pop()

	if len(heap) > 0:
		_heapify_down(heap, 0)

	return max_entry


def peek_max(heap: Heap) -> Optional[HeapEntry]:
	if len(heap) == 0:
		return None
	return heap[0]


def get_top_k(heap: Heap, k: int) -> List[HeapEntry]:
	temp_heap = heap.copy()
	result: List[HeapEntry] = []

	for _ in range(min(k, len(temp_heap))):
		entry = pop_max(temp_heap)
		if entry is not None:
			result.append(entry)

	return result


def update_likes(heap: Heap, post_id: Any, new_likes: int, timestamp: float) -> None:
	for i in range(len(heap)):
		if heap[i][1] == post_id:
			heap[i] = (new_likes, post_id, timestamp)
			i = _heapify_up(heap, i)
			_heapify_down(heap, i)
			return


def size(heap: Heap) -> int:
	return len(heap)


def is_valid_heap(heap: Heap) -> bool:
	for i in range(1, len(heap)):
		parent = (i - 1) // 2
		if heap[i][0] > heap[parent][0]:
			return False
	return True


def get_height(heap: Heap) -> int:
	if len(heap) == 0:
		return 0
	return int(math.floor(math.log2(len(heap))) + 1)


def get_level_order(heap: Heap) -> List[List[HeapEntry]]:
	result: List[List[HeapEntry]] = []
	level_start = 0
	level_size = 1

	while level_start < len(heap):
		level_end = min(level_start + level_size, len(heap))
		result.append(heap[level_start:level_end])
		level_start += level_size
		level_size *= 2

	return result


class BinaryHeap:
	def __init__(self, entries: Iterable[HeapEntry] | None = None) -> None:
		self.heap: Heap = []
		if entries is not None:
			for likes, post_id, timestamp in entries:
				push(self.heap, post_id, int(likes), float(timestamp))

	def push(self, post_id: Any, likes: int, timestamp: float) -> None:
		push(self.heap, post_id, likes, timestamp)

	def pop_max(self) -> Optional[HeapEntry]:
		return pop_max(self.heap)

	def peek_max(self) -> Optional[HeapEntry]:
		return peek_max(self.heap)

	def get_top_k(self, k: int) -> List[HeapEntry]:
		return get_top_k(self.heap, k)

	def update_likes(self, post_id: Any, new_likes: int, timestamp: float) -> None:
		update_likes(self.heap, post_id, new_likes, timestamp)

	def size(self) -> int:
		return size(self.heap)

	def is_valid_heap(self) -> bool:
		return is_valid_heap(self.heap)

	def get_height(self) -> int:
		return get_height(self.heap)

	def get_level_order(self) -> List[List[HeapEntry]]:
		return get_level_order(self.heap)


def demo() -> None:
	heap: Heap = []
	push(heap, "p1", 10, 1710000000)
	push(heap, "p2", 25, 1710000100)
	push(heap, "p3", 15, 1710000200)

	print("peek_max:", peek_max(heap))
	print("top_2:", get_top_k(heap, 2))
	update_likes(heap, "p1", 30, 1710000300)
	print("pop_max:", pop_max(heap))
	print("valid:", is_valid_heap(heap))
	print("height:", get_height(heap))
	print("levels:", get_level_order(heap))


if __name__ == "__main__":
	demo()

