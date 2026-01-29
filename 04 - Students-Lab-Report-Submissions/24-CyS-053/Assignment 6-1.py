from collections import deque

graph = {
    0:[1,2],
    1:[3,4],
    2:[5,6],
    3:[],
    4:[],
    5:[],
    6:[]
}

def bfs(start):
    visited=[]
    q=deque([start])
    s={start}
    while q:
        n=q.popleft()
        visited.append(n)
        for x in graph[n]:
            if x not in s:
                s.add(x)
                q.append(x)
    return visited

def dfs(start):
    visited=[]
    stack=[start]
    s={start}
    while stack:
        n=stack.pop()
        visited.append(n)
        for x in reversed(graph[n]):
            if x not in s:
                s.add(x)
                stack.append(x)
    return visited

print("BFS:", bfs(0))
print("DFS:", dfs(0))
