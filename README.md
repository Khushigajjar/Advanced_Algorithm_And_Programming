# Exercise 2: Viral Message Timing (0/1 Knapsack)

Each user `i` has:

- `costs[i]` (integer)
- `reaches[i]` (integer)

Goal: choose a subset `S` to maximize total reach with `sum(costs[i] for i in S) <= budget`.

## Functions

- `maximize_reach_exact(budget, costs, reaches)`
  - Exact 0/1 knapsack (DP)
  - Returns `(max_reach, selected_users_list)`
  - Time: `O(N × budget)`

- `is_within_budget(selection, costs, budget)`
  - Checks if a selection is within budget
  - Time: `O(N)` (or `O(k)` for `k` selected users)

- `maximize_reach_greedy(budget, costs, reaches)`
  - Greedy by ratio `reach/cost`
  - Returns `(reach, selected_users)`
  - Time: `O(N log N)`

## Built-in tests in the file

- **Test 1: Simple** — small instance
- **Test 2: Greedy fails counterexample** — budget=10, (6,60) vs (5,49)+(5,49)
- **Test 3: Medium** — slightly larger instance
- **Test 4: Another** — another small comparison
