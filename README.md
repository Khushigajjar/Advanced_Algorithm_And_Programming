# Advanced Algorithm and Programming Exercises

## Team Members
- Khushi Gajjar – Exercise 1
- Rahul Kumar Reddy Duggempudi – Exercise 2
- ZiJie HUANG – Exercise 3

---

## Exercise 1: Binary Tree Representation of Content Categories 

### Objective

---

### Data Structure
Each comment is represented as a `CategoryNode` containing:
- category ID  
- name 
- post_count  
- left  
- right  
- parent  

---

### Algorithms

1. **Display Thread**  
   Recursively prints comments with indentation to show hierarchy  

2. **Count Total Comments**  
   Counts all comments including replies  

3. **Total Likes**  
   Computes total likes across the thread  

4. **Find Deepest Reply**  
   Finds maximum nesting depth  

5. **Search by User**  
   Returns all comments by a specific user  

6. **Contains Keyword**  
   Checks if a keyword exists in any comment  

7. **Delete Comment**  
   Removes a comment and all its replies (cascade deletion)  

---


### Complexity

- **Time Complexity:** O(n)  
  Each comment is visited once  

- **Space Complexity:** O(H)  
  H = depth of recursion (nesting level)  

---

### Conclusion
This exercise demonstrates the use of recursion on tree structures. 

---

## Exercise 2: Tree Traversals for Content Processing

### Objective
Implement the three classic binary tree traversals (in-order, pre-order, post-order) to process category data in different orders for exporting, searching, and aggregating metrics.

---

### Data Structure
Each category is represented as a `CategoryNode` containing:
- category ID
- name
- post_count
- left
- right
- parent

---

### Algorithms

1. **In-order Collect**  
   Returns a list of category names in in-order sequence (Left → Root → Right)

2. **In-order Accumulate Posts**  
   Traverses in-order and builds a running total of `post_count`

3. **In-order Find k-th**  
   Finds the k-th category in in-order order (1-indexed)

4. **Pre-order Export**  
   Produces a formatted tree representation (indented by depth) for storage/transmission

5. **Pre-order Copy**  
   Creates a deep copy of the entire tree (preserves structure and parent links)

6. **Pre-order Serialize**  
   Converts the tree into a single string using pre-order tokens (with `#` for nulls)

7. **Post-order Total Posts**  
   Computes total posts for a category including all of its subcategories (children first)

8. **Post-order Average Depth**  
   Calculates the average depth of leaf categories

9. **Post-order Collect Leaves**  
   Collects all leaf categories (nodes with no children)

10. **Find Most Popular Category**  
   Returns the category name with the highest `post_count` (category itself only)

11. **Category With Most Subcategories**  
   Returns the category with the most direct children (left/right)

---

### Complexity

- **Time Complexity:** O(n)  
  Each traversal visits every node once

- **Space Complexity:** O(H)  
  H = height of the tree due to recursion

---

### Conclusion
This exercise shows how traversal order changes what you can compute efficiently: in-order is useful for sorted/structured listing, pre-order is helpful for exporting the structure, and post-order is best for bottom-up aggregation.
