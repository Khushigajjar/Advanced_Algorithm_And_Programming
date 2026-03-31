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