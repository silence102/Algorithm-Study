# DFS + BFS

def dfs(s):
    ans_dfs.append(s)
    visited[s] = True

    for n in graph[s]:
        if not visited[n]:
            dfs(n)

def bfs(s):
    queue = []
    ans_bfs.append(s)
    queue.append(s)
    visited[s] = True

    while queue:
        c = queue.pop(0)
        for n in graph[c]:
            if not visited[n]:
                visited[n] = True
                ans_bfs.append(n)
                queue.append(n)

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    v, w = map(int, input().split())

    graph[v].append(w)
    graph[w].append(v)

for arr in graph:
    arr.sort()

ans_dfs = []
visited = [False] * (N + 1)
dfs(V)
print(*ans_dfs)

visited = [False] * (N + 1)
ans_bfs = []
bfs(V)
print(*ans_bfs)