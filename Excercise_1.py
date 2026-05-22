def is_valid_invitation(invited, graph):
    for i in range(len(invited)):
        for j in range(i + 1, len(invited)):
            u = invited[i]
            v = invited[j]
            if v in graph[u]:
                return False
    return True


def find_max_invitations_exact(graph):
    best = [0, []]

    def backtrack(candidates, current):
        nonlocal best

        if len(current) + len(candidates) <= best[0]:
            return

        if not candidates:
            if len(current) > best[0]:
                best = [len(current), current.copy()]
            return

        node = candidates[0]
        remaining = candidates[1:]

        new_candidates = [v for v in remaining if v not in graph[node]]

        backtrack(new_candidates, current + [node])
        backtrack(remaining, current)

    nodes = list(graph.keys())
    backtrack(nodes, [])

    return best


def find_max_invitations_greedy(graph):
    remaining = set(graph.keys())
    invited = []

    while remaining:
        node = min(remaining, key=lambda x: len([v for v in graph[x] if v in remaining]))
        invited.append(node)
        to_remove = {node} | {v for v in graph[node] if v in remaining}
        remaining = remaining - to_remove

    return len(invited), invited



