def bfs(n):
    queue = []
    queue.append(n)
    visited[n] = True

    while queue:
        v = queue.pop(0)
        for w in tree[v]:
            if not visited[w]:
                parent[w] = v
                visited[w] = True
                queue.append(w)

N = int(input())

tree = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
parent = [0] * (N + 1)

for _ in range(N-1):
    v, w = map(int, input().split())
    tree[w].append(v)
    tree[v].append(w)

bfs(1)

for i in range(2, N + 1):
    print(parent[i])