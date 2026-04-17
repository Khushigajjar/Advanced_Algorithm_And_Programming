# Advanced Algorithm and Programming Exercises

## Team Members
- Khushi Gajjar – Exercise 1
- Rahul Kumar Reddy Duggempudi – Exercise 2
- ZiJie HUANG – Exercise 3

---
### Exercise 1:  Divide & Conquer – Spatial Splitting
## Objective
Implement recursive functions that split a 2D space into smaller regions. 

## Algorithm
Start with the full region, compute point density, and recursively split into four quadrants until the minimum region size is reached.

## Complexity
**Time:** O(n × (W / min_size)²), worst case O(n²)  
**Space:** O(log(W / min_size))