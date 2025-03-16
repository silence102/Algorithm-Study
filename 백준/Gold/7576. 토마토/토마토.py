import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < M and tomato[x][y] == 0

def bfs():
    queue = deque(to_info)

    while queue:
        r, c = queue.popleft()    
        for k in range(4):
            di = r + dr[k]
            dj = c + dc[k]
            if is_valid(di, dj):
                queue.append((di, dj))
                tomato[di][dj] = tomato[r][c] + 1

    answer = 0
    for i in tomato:
        answer = max(answer, max(i))
        if 0 in i:
            return -1
    
    return answer - 1


M, N = map(int, sys.stdin.readline().split())

tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

to_info = []
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            to_info.append((i, j))

print(bfs())