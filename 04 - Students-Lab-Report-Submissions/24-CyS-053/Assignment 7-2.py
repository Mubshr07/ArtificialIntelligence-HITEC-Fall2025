from heapq import heappush, heappop
graph = {
    'S': {'A':4, 'B':10, 'C':11},
    'A': {'B':8, 'D':5},
    'B': {'D':15, 'C':8},
    'C': {'D':2, 'E':20},
    'D': {'H':16, 'I':20, 'F':1},
    'E': {'G':19},
    'F': {'G':13},
    'H': {'I':1, 'J':2},
    'I': {'J':5, 'G':13},
    'J': {'K':7},
    'K': {'G':16},
    'G': {}
}
h = {
    'S':7, 'A':8, 'B':6, 'C':5,
    'D':5, 'E':3, 'F':3, 'H':7,
    'I':4, 'J':5, 'K':3, 'G':0
}
def best_first_search(start, goal):
    pq = []
    heappush(pq, (h[start], start))
    visited = set()
    parent = {start: None}
    while pq:
        _, node = heappop(pq)
        print("Expanding:", node)

        if node == goal:
            break
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                parent[nbr] = node
                heappush(pq, (h[nbr], nbr))
    path = []
    cur = goal
    while cur:
        path.append(cur)
        cur = parent.get(cur)
    return path[::-1]
def beam_search(start, goal, k):
    level = [start]
    parent = {start: None}

    while level:
        print("Beam Level:", level)
        if goal in level:
            break
        candidates = []
        for node in level:
            for nbr in graph[node]:
                candidates.append((h[nbr], nbr, node))
        candidates.sort()
        chosen = candidates[:k]
        next_level = []
        for hval, child, par in chosen:
            parent[child] = par
            next_level.append(child)
        level = next_level
    path = []
    cur = goal
    while cur:
        path.append(cur)
        cur = parent.get(cur)
    return path[::-1]
def a_star(start, goal):
    pq = []
    heappush(pq, (h[start], 0, start))  
    parent = {start: None}
    g_cost = {start: 0}
    visited = set()
    while pq:
        f, g, node = heappop(pq)
        print("Expanding:", node)

        if node == goal:
            break
        visited.add(node)

        for nbr in graph[node]:
            cost = g + graph[node][nbr]
            if nbr not in g_cost or cost < g_cost[nbr]:
                g_cost[nbr] = cost
                f_new = cost + h[nbr]
                parent[nbr] = node
                heappush(pq, (f_new, cost, nbr))
    path = []
    cur = goal
    while cur:
        path.append(cur)
        cur = parent.get(cur)
    return path[::-1]
print("\n===== Best First Search =====")
path1 = best_first_search("S", "G")
print("BFS Path:", path1)
print("\n===== Beam Search (k=2) =====")
path2 = beam_search("S", "G", k=2)
print("Beam Path:", path2)
print("\n===== A* Search =====")
path3 = a_star("S", "G")
print("A* Path:", path3)
