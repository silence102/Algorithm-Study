# 런타임 에러 1 - 불필요한 연산 제거, bfs 내에서 순회하면서 물고기 위치 기록 및 로직 처리
#             - 불필요한 초기값 반복 제거, 로직 단순화 -> 도움

import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

def bfs(s1, s2, shark):
    visited = [[-1] * N for _ in range(N)]
    queue = deque()
    queue.append((s1, s2))
    visited[s1][s2] = 0
    fish_list = []

    while queue:
        r, c = queue.popleft()
        
        for k in range(4):
            di = r + dr[k]
            dj = c + dc[k]

            if 0 <= di < N and 0 <= dj < N and visited[di][dj] == -1:
                if matrix[di][dj] <= shark:
                    visited[di][dj] = visited[r][c] + 1
                
                    if 0 < matrix[di][dj] < shark:
                        fish_list.append((visited[di][dj], di, dj))
                    queue.append((di, dj))
                
    if not fish_list:
        return None
    fish_list.sort()
    return fish_list[0]

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            s1, s2 = i, j
            matrix[i][j] = 0

shark = 2
mom_call = 0
ate = 0

while True:
    result = bfs(s1, s2, shark)

    if not result:
        break
    
    dist, r, c = result
    mom_call += dist
    ate += 1
    matrix[r][c] = 0
    s1, s2 = r, c

    if ate == shark:
        shark += 1
        ate = 0

print(mom_call)