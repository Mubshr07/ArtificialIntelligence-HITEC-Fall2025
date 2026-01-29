from heapq import heappush, heappop
graph = {
    'a': {'b':9, 'c':4, 'd':7},
    'b': {'e':11},
    'c': {'e':17, 'f':12},
    'd': {'f':14},
    'e': {'z':5},
    'f': {'z':9},
    'z': {}
}
h = {
    'a':21, 'b':14, 'c':18, 'd':18,
    'e':5,  'f':8,  'z':0
}
def best_first_search(start, goal):
    open_list = []
    heappush(open_list, (h[start], start))
    visited = set()
    parent = {start: None}
    while open_list:
        _, node = heappop(open_list)
        print("Expanding:", node)
        if node == goal:
            break
        visited.add(node)
        for neigh in graph[node]:
            if neigh not in visited:
                parent[neigh] = node
                heappush(open_list, (h[neigh], neigh))
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
        print("Current Beam Level:", level)
        if goal in level:
            break
        candidates = []
        for node in level:
            for neigh in graph[node]:
                candidates.append((h[neigh], neigh, node))
        candidates.sort(key=lambda x: x[0])
        next_level = []
        for i in range(min(k, len(candidates))):
            h_val, child, par = candidates[i]
            parent[child] = par
            next_level.append(child)
        level = next_level
    path = []
    cur = goal
    while cur:
        path.append(cur)
        cur = parent.get(cur)
    return path[::-1]
print("\n==== Best-First Search ====")
bfs_path = best_first_search('a', 'z')
print("Best-First Search Path:", bfs_path)
print("\n==== Beam Search (k = 2) ====")
beam_path = beam_search('a', 'z', k=2)
print("Beam Search Path:", beam_path)
