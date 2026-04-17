# Advanced Algorithm and Programming Exercises

## Team Members
- Khushi Gajjar – Exercise 1 + Final integration question
- Rahul Kumar Reddy Duggempudi – Exercise 2
- ZiJie HUANG – Exercise 3

### Exercise 1: Divide & Conquer – Spatial Splitting  
## Objective: 
Implement recursive functions that split a 2D space into smaller regions.

## Algorithm
Start with the full region, compute point density, and recursively split into four quadrants until the minimum region size is reached.

## Complexity
**Time:** O(n × (W / min_size)²), worst case O(n²)  
**Space:** O(log(W / min_size)) 

## Exercise 2 — Fractal Drawing (Recursive Shapes)

What is implemented:
- draw_sierpinski(canvas, x, y, size, depth)
- draw_tree(canvas, x, y, length, angle, depth)
- fractal_dimension(fractal_image, box_sizes)
- count_nonempty_boxes(image, box_size)

Complexity analysis answers:
1) Sierpiński (depth 5): 3^5 = 243 small triangles
2) Fractal dimension: straight line = 1, filled square = 2 (Sierpiński = 1.585)
