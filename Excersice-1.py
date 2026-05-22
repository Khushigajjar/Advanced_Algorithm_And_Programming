from itertools import combinations
import time

def is_valid_coverage(selected_users, graph):
    covered = set()
    for u in selected_users:
        covered.add(u)
        for v in graph[u]:
            covered.add(v)
    for u in graph:
        if u not in covered:
            return False
    return True

def find_minimum_coverage(graph, N):
    best_size = N + 1
    best_set = []
    for r in range(N + 1):
        for S in combinations(range(N), r):
            if is_valid_coverage(S, graph):
                if len(S) < best_size:
                    best_size = len(S)
                    best_set = list(S)
    return (best_size, best_set)

def find_fast_coverage(graph, N):
    uncovered = set(range(N))
    selected = set()
    while uncovered:
        best_node = -1
        best_count = -1
        for u in range(N):
            count = 0
            if u in uncovered:
                count += 1
            for v in graph[u]:
                if v in uncovered:
                    count += 1
            if count > best_count:
                best_count = count
                best_node = u
        selected.add(best_node)
        uncovered.discard(best_node)
        for v in graph[best_node]:
            uncovered.discard(v)
    return (len(selected), selected)



# Test 1: Star graph (1 center connected to all)
graph1 = {
    0: [1, 2, 3, 4],
    1: [0],
    2: [0],
    3: [0],
    4: [0]
}
N1 = 5
size_min1, set_min1 = find_minimum_coverage(graph1, N1)
size_fast1, set_fast1 = find_fast_coverage(graph1, N1)
print("Test 1: Star Graph")
print(f"Minimum coverage : size={size_min1}, set={set_min1}")
print(f"Greedy  coverage : size={size_fast1}, set={set_fast1}")
print(f"Greedy valid? {is_valid_coverage(set_fast1, graph1)}")
print()

# Test 2: Path graph  0-1-2-3-4
graph2 = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2, 4],
    4: [3]
}
N2 = 5
size_min2, set_min2 = find_minimum_coverage(graph2, N2)
size_fast2, set_fast2 = find_fast_coverage(graph2, N2)
print("Test 2: Path Graph")
print(f"Minimum coverage : size={size_min2}, set={set_min2}")
print(f"Greedy  coverage : size={size_fast2}, set={set_fast2}")
print(f"Greedy valid? {is_valid_coverage(set_fast2, graph2)}")
print()

# Test 3: Complete graph (everyone is friends with everyone)
graph3 = {
    0: [1, 2, 3],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [0, 1, 2]
}
N3 = 4
size_min3, set_min3 = find_minimum_coverage(graph3, N3)
size_fast3, set_fast3 = find_fast_coverage(graph3, N3)
print("Test 3: Complete Graph")
print(f"Minimum coverage : size={size_min3}, set={set_min3}")
print(f"Greedy  coverage : size={size_fast3}, set={set_fast3}")
print(f"Greedy valid? {is_valid_coverage(set_fast3, graph3)}")
print()

# Test 4: Disconnected graph (two separate components)

graph4 = {
    0: [1],
    1: [0, 2],
    2: [1],
    3: [4],
    4: [3]
}
N4 = 5
size_min4, set_min4 = find_minimum_coverage(graph4, N4)
size_fast4, set_fast4 = find_fast_coverage(graph4, N4)
print("Test 4: Disconnected Graph")
print(f"Minimum coverage : size={size_min4}, set={set_min4}")
print(f"Greedy  coverage : size={size_fast4}, set={set_fast4}")
print(f"Greedy valid? {is_valid_coverage(set_fast4, graph4)}")
print()

# Test 5: Single node (trivial)

graph5 = {0: []}
N5 = 1
size_min5, set_min5 = find_minimum_coverage(graph5, N5)
size_fast5, set_fast5 = find_fast_coverage(graph5, N5)
print("Test 5: Single Node")
print(f"Minimum coverage : size={size_min5}, set={set_min5}")
print(f"Greedy  coverage : size={size_fast5}, set={set_fast5}")
print(f"Greedy valid? {is_valid_coverage(set_fast5, graph5)}")
print()



