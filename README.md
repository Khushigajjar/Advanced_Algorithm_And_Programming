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

## Exercise 2: Recursive Content Aggregation with Divide and Conquer

Author: Rahul Kumar Reddy Duggempudi

### Objective
Implement and analyze **divide-and-conquer engagement analytics** for a list of posts.  
Compute max, total, average, threshold-based counts, sort by engagement using merge sort, and detect peak hour using recursion.  

Python File: `Recursive_Content_Aggregation_with_Divide_Conquer.py`

---

### Data Structure
Each post is represented as a `Post` containing:
- Post ID  
- User ID  
- Content preview  
- Timestamp  
- Likes  
- Comments  
- Shares  
- Engagement score: `(likes × 1) + (comments × 2) + (shares × 3)`  

---

### Algorithms

1. **Maximum Engagement**  
   Finds the maximum engagement score using divide and conquer (`max_engagement`)  

2. **Total Engagement**  
   Recursively sums engagement scores (`sum_engagement`)  

3. **Average Engagement**  
   Computes average as total / number of posts (`average_engagement`)  

4. **Count Above Threshold**  
   Counts posts with engagement score greater than a threshold (`count_above_threshold`)  

5. **Merge Sort by Engagement**  
   Sorts posts in descending order of engagement (`merge_sort_by_engagement`, `merge`)  

6. **Peak Hour (Binary Search Style)**  
   Finds the peak index in hourly likes data (`find_peak_hour`)  

---

### Complexity

1. **Time Complexity of `max_engagement`: O(n)**  
   Proof (recurrence): `T(1) = O(1)`, `T(n) = 2T(n/2) + O(1)` (two halves + one comparison).  
   This solves to `T(n) = Θ(n)` (so the time complexity is `O(n)`).  

2. **Merge sort vs insertion sort for 10,000 posts**  
   - Merge sort: `O(n log n)` = `10,000 × log2(10,000)` = `10,000 × 13.29` ≈ `133,000` (order of magnitude)  
   - Insertion sort (worst case): `O(n²)` = `10,000 × 9,999 / 2` = `50,000,000`  
   Merge sort is much faster for random/unsorted data; insertion sort is only competitive when data is nearly sorted.  

3. **Recursion depth of merge sort on n elements**  
   The array is halved until size 1, so recursion depth is about `floor(log2(n)) + 1` (i.e., `Θ(log n)`).  

4. **Why `find_peak_hour` uses binary-search style recursion**  
   We can discard half the range based on `likes[mid]` vs `likes[mid+1]`.  
   This only works when the array is **unimodal** (non-decreasing up to a single peak, then non-increasing).  
   Time complexity is `O(log n)` with recursion depth `O(log n)`.  

---

### Conclusion
This exercise demonstrates divide-and-conquer recursion on arrays for analytics, sorting, and peak detection.  

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
