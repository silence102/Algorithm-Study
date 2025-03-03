from collections import deque

def bfs(start, graph, N):
    visited = [False] * (N+1)
    visited[start] = True
    queue = deque([start])        
    count = 0

    while queue:
        node = queue.popleft()

        for near in graph[node]:
           if not visited[near]:
               visited[near] = True
               queue.append(near)
               count += 1
    
    return count

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N+1)]

for _ in range(M):
    v, w = map(int, input().split())
    graph[v].append(w)
    reverse_graph[w].append(v)

result = 0

for i in range(1, N+1):
    tall = bfs(i, graph, N)
    small = bfs(i, reverse_graph, N)

    if tall + small == N - 1:
        result += 1

print(result)