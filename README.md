# Advanced Algorithm and Programming Exercises

## Team Members

- Khushi Gajjar – Exercise 1
- Rahul Kumar Reddy Duggempudi – Exercise 2
- ZiJie HUANG – Exercise 3 + Final integration question

---

## Exercise 2: Conflict-Free Labeling – User Categorization (Ref. Graph Coloring)

This exercise models user categorization as a **graph coloring** problem:

- Each user is a **node**.
- Each conflict/relationship is an **edge**.
- A **label** (color) is an integer assigned to each node.
- A labeling is **conflict-free** if no edge connects two nodes with the same label.

Graph representation used in code:

- `graph`: adjacency list (dictionary) where `graph[u]` is the list of neighbors of node `u`.
- `labeling`: list where `labeling[u]` is the label for node `u` (and `-1` means unassigned).

Implemented operations (see Exercise2_Conflict-Free_Labeling.py):

- `is_valid_labeling(labeling, graph)`
- `assign_labels(k, graph, node, labeling)`
- `find_min_labels(graph)`

---


