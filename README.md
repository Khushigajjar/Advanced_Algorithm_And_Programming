# Advanced Algorithm and Programming Exercises

## Team Members
- Khushi Gajjar – Exercise 1
- Rahul Kumar Reddy Duggempudi – Exercise 2
- ZiJie HUANG – Exercise 3

---

## Exercise 1: Graph Representations for Social Networks


Implements a `SocialGraph` structure using both **adjacency matrix** and **adjacency linked list** representations simultaneously.

## Operations
- `add_friendship(u, v)` / `remove_friendship(u, v)` — add or remove edge
- `are_friends(u, v)` — check connection
- `get_friends(u)` / `get_degree(u)` — neighbor info
- `get_num_users()` / `get_num_edges()` — graph size
- `is_complete_graph()` / `graph_density()` / `degree_distribution()` — graph properties
- `matrix_to_list()` / `list_to_matrix()` — convert between representations

## Complexity Highlights

| Operation | Matrix | List |
|---|---|---|
| `are_friends` | O(1) | O(deg(u)) |
| `get_friends` | O(n) | O(deg(u)) |
| `add/remove` | O(1) | O(deg(u)) |

## Space (1B users, avg degree 150)
| Representation | Memory |
|---|---|
| Adjacency Matrix | ~125 PB |
| Adjacency List | ~3.6 TB |



---

## Exercise 2: Graph Traversals (DFS) for Social Network Analysis

- Implementation file: `Exercise2_Graph_Traversals.py`
- Includes:

  - Recursive DFS and iterative DFS (stack)
  - Connected components + connectivity check
  - Path existence (`has_path`) and path reconstruction (`find_path`)
  - Simple traversal-based analytics (component sizes, largest component, isolated users)
```

