import heapq

graph = {
    'A': [('B',3), ('C',4)],
    'B': [('D',2), ('E',6)],
    'C': [('I',5), ('E',3), ('J',9), ('G',12)],
    'D': [('H',4)],
    'E': [('H',5)],
    'F': [('C',7), ('I',8)],
    'H': [('J',2)],
    'I': [('J',3)],
    'J': [],
    'G': [('J',4)]
}

def ucs(start, goal):
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return cost, path

        for nxt, c in graph[node]:
            if nxt not in visited:
                heapq.heappush(pq, (cost + c, nxt, path + [nxt]))

    return None

cost, path = ucs('A', 'J')
print("UCS Path:", path)
print("Total Cost:", cost)
