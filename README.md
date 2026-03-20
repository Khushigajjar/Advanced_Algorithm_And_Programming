# Advanced Algorithm and Programming Exercises

## Team Members
- Khushi Gajjar – Exercise 1
- Rahul Kumar Reddy Duggempudi – Exercise 2
- ZiJie HUANG – Exercise 3

---

## Exercise 1: Recursive Comment Thread Analysis

### Objective
Implement and analyze a **recursive comment system** where comments and replies form a tree structure.  
Perform operations like traversal, counting, searching, and deletion using recursion.

---

### Data Structure
Each comment is represented as a `CommentNode` containing:
- Comment ID  
- User ID  
- Content  
- Timestamp  
- Likes  
- List of replies (child nodes)  

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



## Exercise 3: Converting Recursion to Iteration

### Objective

The goal of this exercise is to understand when recursion is appropriate and how it can be converted into an iterative approach using an explicit stack. This is especially important when dealing with deep nested structures where recursion may lead to stack overflow.

---

### Implementation

In this exercise, a comment thread structure is used where each comment can have multiple replies, forming a tree-like structure.

1. **Recursive Flatten**

A recursive function is implemented to traverse the comment thread in depth-first order. The function processes the current comment first, then recursively processes all its replies.

2. **Iterative Flatten (Explicit Stack)**

The same traversal is implemented using an explicit stack. Instead of relying on the system call stack, a stack data structure is used to simulate recursion.

A simple state is introduced to track whether a node is being visited for the first time or after processing its replies. This helps maintain the correct traversal order.

3. **Counting Comments (Tail Recursion)**

A tail-recursive function is used to count the total number of comments. An accumulator is passed through recursive calls to keep track of the count.

4. **Counting Comments (Iterative Version)**

The counting logic is converted into a loop using a stack. This removes recursion entirely and provides better control over memory usage.

---

### Complexity

- **Time Complexity:** O(n)  
  Each comment is visited once.

- **Space Complexity:** O(d)  
  Where *d* is the depth of the comment tree.

---

### Conclusion

This exercise demonstrates the differences between recursive and iterative approaches. While recursion is easier to write and understand, the iterative approach is more robust for deep or complex structures.
