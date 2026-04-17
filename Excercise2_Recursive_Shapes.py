from __future__ import annotations
import math
import tkinter as tk
from typing import Iterable, List, Sequence

def draw_line(canvas: tk.Canvas, x1: float, y1: float, x2: float, y2: float, *, width: int = 1) -> None:
	canvas.create_line(x1, y1, x2, y2, width=width)


def draw_filled_triangle(
	canvas: tk.Canvas,
	x: float,
	y: float,
	size: float,
	*,
	fill: str = "black",
	outline: str | None = None,
) -> None:
	x1, y1 = x + size / 2.0, y
	x2, y2 = x, y + size
	x3, y3 = x + size, y + size
	canvas.create_polygon(
		x1,
		y1,
		x2,
		y2,
		x3,
		y3,
		fill=fill,
		outline=outline if outline is not None else fill,
	)


def draw_sierpinski(canvas: tk.Canvas, x: float, y: float, size: float, depth: int) -> None:
	if depth == 0:
		draw_filled_triangle(canvas, x, y, size)
		return

	half = size / 2.0

	draw_sierpinski(canvas, x, y, half, depth - 1)
	draw_sierpinski(canvas, x + half, y, half, depth - 1)
	draw_sierpinski(canvas, x + half / 2.0, y + half, half, depth - 1)


def draw_tree(canvas: tk.Canvas, x: float, y: float, length: float, angle: float, depth: int) -> None:
	angle_radians = math.radians(angle)
	x2 = x + length * math.cos(angle_radians)
	y2 = y + length * math.sin(angle_radians)
	draw_line(canvas, x, y, x2, y2)

	if depth == 0:
		return

	next_length = length * (2.0 / 3.0)
	draw_tree(canvas, x2, y2, next_length, angle + 30.0, depth - 1)
	draw_tree(canvas, x2, y2, next_length, angle - 30.0, depth - 1)


BoolGrid = List[List[bool]]


def _as_bool_grid(fractal_image) -> BoolGrid:
	if isinstance(fractal_image, list):
		if not fractal_image:
			return []
		if isinstance(fractal_image[0], list):
			return fractal_image  # assume already a BoolGrid

	if hasattr(fractal_image, "size") and hasattr(fractal_image, "getpixel"):
		width, height = fractal_image.size
		try:
			img = fractal_image.convert("L")
		except Exception:
			img = fractal_image

		grid = [[False for _ in range(width)] for _ in range(height)]
		for y in range(height):
			row = grid[y]
			for x in range(width):
				try:
					px = img.getpixel((x, y))
				except Exception:
					px = 0

				if isinstance(px, tuple):
					row[x] = any(channel != 0 for channel in px)
				else:
					row[x] = px != 0
		return grid

	raise TypeError("Unsupported fractal_image type")


def count_nonempty_boxes(fractal_image, box_size: int) -> int:
	if box_size <= 0:
		raise ValueError("box_size must be > 0")

	grid = _as_bool_grid(fractal_image)
	if not grid or not grid[0]:
		return 0

	height = len(grid)
	width = len(grid[0])
	rows = height // box_size
	cols = width // box_size

	count = 0
	for r in range(rows):
		y0 = r * box_size
		y1 = y0 + box_size
		for c in range(cols):
			x0 = c * box_size
			x1 = x0 + box_size

			nonempty = False
			for yy in range(y0, y1):
				row = grid[yy]
				for xx in range(x0, x1):
					if row[xx]:
						nonempty = True
						break
				if nonempty:
					break

			if nonempty:
				count += 1

	return count


def _linear_fit_slope(xs: Sequence[float], ys: Sequence[float]) -> float:
	if len(xs) != len(ys) or len(xs) < 2:
		raise ValueError("Need at least two (x, y) points")

	mean_x = sum(xs) / len(xs)
	mean_y = sum(ys) / len(ys)
	var_x = sum((x - mean_x) ** 2 for x in xs)
	if var_x == 0:
		raise ValueError("All x values are identical; cannot fit a line")

	cov_xy = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
	return cov_xy / var_x


def fractal_dimension(fractal_image, box_sizes: Iterable[int]) -> float:
	counts: List[int] = []
	log_inv_sizes: List[float] = []

	for box_size in box_sizes:
		c = count_nonempty_boxes(fractal_image, int(box_size))
		if c <= 0:
			continue
		counts.append(c)
		log_inv_sizes.append(math.log(1.0 / float(box_size)))

	if len(counts) < 2:
		raise ValueError("Not enough data to estimate a dimension")

	log_counts = [math.log(float(c)) for c in counts]
	return _linear_fit_slope(log_inv_sizes, log_counts)


def demo_window() -> None:
	root = tk.Tk()
	root.title("Exercise 2 - Recursive Shapes")

	canvas = tk.Canvas(root, width=900, height=450, bg="white")
	canvas.pack(fill="both", expand=True)

	draw_sierpinski(canvas, x=30, y=30, size=360, depth=6)
	draw_tree(canvas, x=680, y=410, length=140, angle=-90, depth=8)

	root.mainloop()


if __name__ == "__main__":
	demo_window()

