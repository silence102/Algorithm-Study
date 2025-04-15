# 두 종단을 구하는 방법: bfs로 끝값 찾고 한번더 bfs로 끝값 찾는게 포인트

# 틀림 1 -> 마지막에 queue에 들어간 값이 가장 큰 값이라고 생각하는 오류를 범함 -> 최대 값 갱신으로 변경
# 틀림 2 -> 두 종단 값의 거리가 가장 먼 값의 최단 거리를 종단 값들 중 최소 거리로 오해함
# 틀림 3 -> -1 초기화 문제 등 몇몇 예상 못한 부분이 있을거라 판단 -> 완탐 구현으로 변경

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(s1, s2):
    visited = [[-1] * M for _ in range(N)]
    visited[s1][s2] = 0

    queue = deque()
    queue.append((s1, s2))
    
    max_dist = 0

    while queue:
        r, c = queue.popleft()

        for k in range(4):
            di = r + dr[k]
            dj = c + dc[k]

            if 0 <= di < N and 0 <= dj < M and visited[di][dj] == -1 and matrix[di][dj] != "W":
                visited[di][dj] = visited[r][c] + 1
                max_dist = max(max_dist, visited[di][dj])
                queue.append((di, dj))

    return max_dist

N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'L':
            dist = bfs(i, j)
            answer = max(answer, dist)

print(answer)