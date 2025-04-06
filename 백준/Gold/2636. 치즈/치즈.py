from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(s1, s2, step, total):
    visited = [[0] * N for _ in range(M)]
    queue = deque()
    cheese = set()
    queue.append((s1, s2))
    visited[s1][s2] = 1

    while queue:
        r, c = queue.popleft()

        for k in range(4):
            di = r + dr[k]
            dj = c + dc[k]

            if 0 <= di < M and 0 <= dj < N and not visited[di][dj] and not matrix[di][dj]:
                visited[di][dj] = 1
                queue.append((di, dj))
            elif 0 <= di < M and 0 <= dj < N and not visited[di][dj] and matrix[di][dj]:
                cheese.add((di, dj))

    melt = []
    cheese = deque(cheese)
    remain = len(cheese)

    while cheese:
        r, c = cheese.popleft()

        for k in range(4):
            di = r + dr[k]
            dj = c + dc[k]

            if visited[di][dj]:
                melt.append((r,c))
                break
    
    if not melt:
        return [step, total]
    
    for i in melt:
        matrix[i[0]][i[1]] = 0

    return bfs(0, 0, step + 1, remain)



M, N = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(M)]

result = bfs(0, 0, 0, 0)

print(result[0])
print(result[1])