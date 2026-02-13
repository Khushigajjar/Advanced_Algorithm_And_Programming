
All implementations for this lab are located inside the `LAB_01` folder.

---

# Exercise 1 – Integer Mirror (Digit Reversal)

### Objective
Reverse the digits of a non-negative integer using only mathematical operations (`+`, `-`, `*`, `div`, `mod`) without converting the number to a string.

### Approach
The algorithm extracts the last digit using modulo, appends it to a new number after multiplying the current result by 10, and removes the last digit using integer division. This process continues until all digits are processed.

### Complexity Analysis
- Let **d** be the number of digits.
- Each digit is processed once.
- Time Complexity: **O(log n)** (since digits ≈ log₁₀(n))
- Space Complexity: **O(1)**

### Edge Cases Tested
- `0`
- Single-digit numbers
- Numbers with trailing zeros (e.g., 400 → 4)
- Large integers

---

# Exercise 2 – Balanced Symbol Checker

### Objective
Determine whether a string containing the symbols `()`, `[]`, `{}` is properly balanced using a stack data structure.

### Approach
Opening symbols are pushed onto a stack.  
Closing symbols are matched with the top element of the stack using the LIFO principle.  
If a mismatch occurs or the stack is not empty at the end, the string is not balanced.

### Complexity Analysis
- Let **n** be the length of the string.
- Each character is processed once.
- Time Complexity: **O(n)**
- Space Complexity: **O(n)** (worst case: all opening symbols)

### Edge Cases Tested
- Empty string
- Only opening symbols
- Only closing symbols
- Incorrect nesting (e.g., `([)]`)
- Deeply nested valid input

---

# Exercise 3 – Merge Overlapping Intervals

### Objective
Given a list of intervals, merge all overlapping intervals and return a list of non-overlapping intervals covering the same ranges.

### Approach
The intervals are first sorted by their starting value.  
The algorithm then scans the sorted list and merges intervals whenever an overlap is detected.

### Complexity Analysis
- Sorting requires **O(n log n)** comparisons.
- Merging requires a single linear scan.
- Total Time Complexity: **O(n log n)**
- Space Complexity: **O(n)**

### Edge Cases Tested
- Empty list
- Single interval
- Fully overlapping intervals
- Boundary overlaps (e.g., `[1,4]` and `[4,5]`)
- Already sorted and unsorted inputs

---

# Conclusion

This lab focused on revising fundamental algorithmic techniques including:
- Arithmetic-based digit manipulation
- Stack-based pattern matching
- Sorting and interval merging strategies

Each solution was implemented and tested with various edge cases to ensure correctness and efficiency. The complexity analysis confirms that all solutions achieve optimal asymptotic performance for their respective approaches.