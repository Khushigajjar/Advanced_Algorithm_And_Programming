# Advanced Algorithm and Programming Exercises

## Team Members
- Khushi Gajjar – Exercise 1 + Final integration question
- Rahul Kumar Reddy Duggempudi – Exercise 2
- ZiJie HUANG – Exercise 3 + Final integration question

## Exercise 1: Binary Search Trees – User Search & Friend-of-Friend Suggestions 

Objective: Implement a BST to manage user profiles by user_id and efficiently find friends-of-friends for friend recommendations. 

## Exercise 2: Binary Heap – Trending Posts Feed

This exercise implements a max-heap for trending posts. Each heap entry is stored as:

Implemented this functions:
- insert() - O(n)
- find() - O(n)
- inorder_traversal() -O(n)
- delete() - O(n)
- suggest_friends() - O(k·f·n)
- get_height() - O(n)
- is_balanced() - O(n²)
- get_leaf_count() - O(n)


- `(likes, post_id, timestamp)`

Implemented operations (see `Exercise2_BinaryHeap.py`):

- `push(post_id, likes, timestamp)`
- `pop_max()`
- `peek_max()`
- `get_top_k(k)`
- `update_likes(post_id, new_likes, timestamp)`
- `size()`
- `is_valid_heap()`
- `get_height()`
- `get_level_order()`

```

