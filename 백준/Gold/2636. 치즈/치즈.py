import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    visited = [[0] * N for _ in range(M)]
    queue = deque()
    melt = set()

    queue.append((0, 0))
    visited[0][0] = 1

    while queue:
        r, c = queue.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            di = r + dr
            dj = c + dc

            if 0 <= di < M and 0 <= dj < N:
                if not visited[di][dj]: 
                    visited[di][dj] = 1
                    if not matrix[di][dj]:
                        queue.append((di, dj))
                    elif matrix[di][dj]:
                        melt.add((di, dj))

    if not melt:
        return 0
    
    for x, y in melt:
        matrix[x][y] = 0

    return len(melt)


M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]

step = 0
last_cheese = 0

while True:
    end = bfs()

    if end == 0:
        break

    last_cheese = end
    step += 1

print(step)
print(last_cheese)