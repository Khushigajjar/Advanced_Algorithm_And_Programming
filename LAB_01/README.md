
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

Exercise 4 – Polynomial Evaluation (Horner’s Method)
Objective

Evaluate a polynomial at a given value using Horner’s method instead of the naive power-based approach.

Approach

The polynomial is evaluated starting from the highest-degree coefficient.

Instead of computing powers of x separately, the algorithm repeatedly multiplies the accumulated result by x and adds the next coefficient.

This reduces the number of arithmetic operations and avoids repeated exponentiation.

Complexity Analysis

Let n be the degree of the polynomial.

Each coefficient is processed exactly once.

Time Complexity: O(n)
Space Complexity: O(1) (only one variable is used to store the intermediate result)

Compared to the naive approach, which may require repeated power calculations and up to O(n²) operations, Horner’s method provides a linear-time improvement.

Edge Cases Tested

Constant polynomial
Empty coefficient list
All zero coefficients
Evaluation at x = 0
Large degree polynomials

Exercise 5 – Array Rotation Optimization
Objective

Rotate an array to the right by k positions using an in-place method with constant extra space.

Approach

The reverse method is used for optimal performance:

Compute k mod n to handle cases where k is larger than the array length.

Reverse the entire array.

Reverse the first k elements.

Reverse the remaining elements.

This results in the desired rotated array without using additional memory.

Complexity Analysis

Let n be the length of the array.

Each element is moved a constant number of times through the reverse operations.

Time Complexity: O(n)
Space Complexity: O(1)

The algorithm achieves optimal time complexity for array rotation.

Edge Cases Tested

Empty array
Single-element array
k = 0
k greater than array length
Small arrays with k = 1
Large arrays

Exercise 6 – First Unique Character Finder
Objective

Find the index of the first non-repeating character in a string using linear time complexity.

Approach

A dictionary is used to count the frequency of each character.

The algorithm performs two passes:

First pass: count occurrences of each character.

Second pass: return the index of the first character with frequency equal to 1.

If no such character exists, return -1.

Complexity Analysis

Let n be the length of the string.

Each character is processed at most twice.

Time Complexity: O(n)
Space Complexity: O(n) (dictionary stores character frequencies)

The use of a hash table ensures constant-time lookup on average.

Edge Cases Tested

Empty string
Single-character string
All characters repeated
Unique character at beginning
Unique character at end
Long strings with repeated patterns

Conclusion

Exercises 4, 5, and 6 further reinforced core algorithmic principles:

• Efficient mathematical computation using algebraic transformation (Horner’s method)
• In-place array manipulation using reversal techniques
• Hash table usage for frequency-based pattern detection

All implementations were tested with representative edge cases.
The complexity analysis confirms that each solution achieves optimal asymptotic efficiency for its problem constraints.
