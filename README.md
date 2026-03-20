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

---

## Exercise 2: Recursive Content Aggregation with Divide and Conquer

**Team Member:** Rahul Kumar Reddy Duggempudi

### Objective
Implement divide-and-conquer analytics over an array of posts using recursion.
Compute maximum, total, average, and threshold-based counts of engagement, then sort posts by engagement using recursive merge sort.
Also, find the peak hour from hourly engagement data using binary-search style recursion.

Implementation: `Recursive_Content_Aggregation_with_Divide_Conquer.py`

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
- Engagement score, computed as:
   - `engagement_score = (likes × 1) + (comments × 2) + (shares × 3)`

---

### Algorithms

1. **Maximum Engagement** (`max_engagement`)
    Returns the maximum engagement score in `posts[left..right]`.

2. **Total and Average Engagement** (`sum_engagement`, `average_engagement`)
    Computes total engagement via recursion and derives the average.

3. **Count Above Threshold** (`count_above_threshold`)
    Counts how many posts have engagement score strictly greater than a given threshold.

4. **Merge Sort by Engagement** (`merge_sort_by_engagement`, `merge`)
    Recursively sorts posts in descending order by engagement score.

5. **Peak Hour Analysis** (`find_peak_hour`)
    Finds the hour index with the highest engagement in a unimodal hourly array.

---

### Complexity (Answers)

1) **Time complexity of recursive `max_engagement` (prove it)**

- Let $n = (right - left + 1)$ be the number of posts.
- The recurrence is:
   - $T(1) = O(1)$
   - $T(n) = 2T(n/2) + O(1)$ (two recursive calls + constant-time comparison)
- By Master Theorem: $a=2, b=2, f(n)=O(1)$ and $n^{\log_b a}=n$.
   Therefore $T(n)=\Theta(n)$.

So the time complexity is **O(n)**.

2) **Merge sort (O(n log n)) vs insertion sort (O(n²)) for 10,000 posts**

- Merge sort does about $n\log_2 n$ work:
   - $10{,}000\log_2(10{,}000) \approx 10{,}000 \times 13.29 \approx 133{,}000$ (order of magnitude)
- Insertion sort worst case does about $n(n-1)/2$ work:
   - $10{,}000 \times 9{,}999 / 2 \approx 50{,}000{,}000$

For 10,000 posts, merge sort is dramatically faster on unsorted/random data.
Insertion sort is only competitive when the input is already nearly sorted.

3) **Recursion depth for merge sort on n elements**

Each recursive level halves the problem size until 1 element remains.
The maximum recursion depth is:
- $\lfloor\log_2(n)\rfloor + 1$ (equivalently, $\Theta(\log n)$)

4) **Why `find_peak_hour` works like binary search; required property**

We can discard half the search range because the comparison `likes[mid]` vs `likes[mid+1]` tells which side must contain the peak.
This is only guaranteed when the hourly array is **unimodal**:
- non-decreasing up to a single peak, then non-increasing afterward.

Under this property:
- If `likes[mid] < likes[mid+1]`, you are on the rising slope, so the peak is to the right.
- Otherwise, you are on the falling slope (or at a plateau), so the peak is to the left (including mid).

This gives **O(log n)** time and **O(log n)** recursion depth.

---

### Conclusion
This exercise demonstrates divide-and-conquer recursion on arrays: splitting the input, combining results, and using merge sort to order posts by engagement.