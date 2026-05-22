from __future__ import annotations

from typing import Iterable, List, Sequence, Tuple


def is_within_budget(selection: Iterable[int], costs: Sequence[int], budget: int) -> bool:
    total = 0
    for i in selection:
        total += costs[i]
        if total > budget:
            return False
    return total <= budget


def maximize_reach_exact(
    budget: int, costs: Sequence[int], reaches: Sequence[int]
) -> Tuple[int, List[int]]:
    n = len(costs)
    prev = [0] * (budget + 1)
    take = [bytearray(budget + 1) for _ in range(n)]

    for i in range(n):
        c = costs[i]
        r = reaches[i]
        curr = prev[:]  # dp row for first i+1 items

        for b in range(c, budget + 1):
            cand = prev[b - c] + r
            if cand > curr[b]:
                curr[b] = cand
                take[i][b] = 1

        prev = curr

    selected: List[int] = []
    b = budget
    for i in range(n - 1, -1, -1):
        if take[i][b]:
            selected.append(i)
            b -= costs[i]
    selected.reverse()
    return prev[budget], selected


def maximize_reach_greedy(
    budget: int, costs: Sequence[int], reaches: Sequence[int]
) -> Tuple[int, List[int]]:
    def ratio(i: int) -> float:
        c = costs[i]
        if c == 0:
            return float("inf") if reaches[i] > 0 else 0.0
        return reaches[i] / c

    order = sorted(range(len(costs)), key=ratio, reverse=True)

    total_cost = 0
    total_reach = 0
    selected: List[int] = []

    for i in order:
        if total_cost + costs[i] <= budget:
            selected.append(i)
            total_cost += costs[i]
            total_reach += reaches[i]

    return total_reach, selected


def _total_cost(selection: Iterable[int], costs: Sequence[int]) -> int:
    return sum(costs[i] for i in selection)


def _total_reach(selection: Iterable[int], reaches: Sequence[int]) -> int:
    return sum(reaches[i] for i in selection)


def _run_test(name: str, budget: int, costs: Sequence[int], reaches: Sequence[int]) -> None:
    exact_reach, exact_sel = maximize_reach_exact(budget, costs, reaches)
    greedy_reach, greedy_sel = maximize_reach_greedy(budget, costs, reaches)

    print(name)
    print("Budget:", budget)
    print("Costs:", list(costs))
    print("Reaches:", list(reaches))

    print(
        "Exact  : reach=", exact_reach,
        ", cost=", _total_cost(exact_sel, costs),
        ", selected=", exact_sel,
        ", valid=", is_within_budget(exact_sel, costs, budget),
        sep=""
    )
    print(
        "Greedy : reach=", greedy_reach,
        ", cost=", _total_cost(greedy_sel, costs),
        ", selected=", greedy_sel,
        ", valid=", is_within_budget(greedy_sel, costs, budget),
        sep=""
    )
    print()


if __name__ == "__main__":
    # Test 1: Simple case (greedy usually matches exact)
    _run_test(
        "Test 1: Simple",
        budget=7,
        costs=[3, 4, 2],
        reaches=[4, 5, 3],
    )

    # Test 2: Counterexample where greedy by ratio fails
    _run_test(
        "Test 2: Greedy fails counterexample",
        budget=10,
        costs=[6, 5, 5],
        reaches=[60, 49, 49],
    )

    # Test 3: Larger small instance
    _run_test(
        "Test 3: Medium",
        budget=15,
        costs=[12, 2, 1, 4, 1],
        reaches=[4, 2, 2, 10, 1],
    )

    # Test 4: Another comparison instance
    _run_test(
        "Test 4: Another",
        budget=9,
        costs=[5, 4, 6, 3],
        reaches=[10, 8, 12, 6],
    )
