from networkx import nodes


ex-1


FUNCTION is_valid_invitation(invited, graph):
    FOR i FROM 0 TO len(invited) - 1:
        FOR j FROM i+1 TO len(invited) - 1:
            u <- invited[i]
            v <- invited[j]
            IF v IN graph[u]:   
                RETURN False
    RETURN True


FUNCTION find_max_invitations_exact(graph):
    best <- [0, []]      

    FUNCTION backtrack(candidates, current):
        IF len(current) + len(candidates) ≤ best[0]:
            RETURN

        IF candidates is EMPTY:
            IF len(current) > best[0]:
                best <- [len(current), COPY(current)]
            RETURN

        node <- candidates[0]
        remaining <- candidates[1:]

      
        new_candidates <- [v FOR v IN remaining IF v NOT IN graph[node]]
        backtrack(new_candidates, current + [node])

      
        backtrack(remaining, current)

    nodes <- LIST of all node IDs in graph
    backtrack(nodes, [])
    RETURN best



FUNCTION find_max_invitations_greedy(graph):
    remaining <- COPY of all nodes
    invited <- []

    WHILE remaining is NOT EMPTY:
        node <- node in remaining with MIN degree in subgraph(remaining)
        invited.APPEND(node)

        to_remove <- {node} ∪ {v FOR v IN graph[node] IF v IN remaining}
        remaining <- remaining 

    RETURN (len(invited), invited)