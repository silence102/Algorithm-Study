def dfs(s):
    global answer
    visited[s] = True
    answer += 1

    for n in graph[s]:
        if not visited[n]:
            dfs(n)        

N = int(input())    
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

answer = 0 
visited = [False] * (N + 1) 
dfs(1)

print(f"{answer-1}")