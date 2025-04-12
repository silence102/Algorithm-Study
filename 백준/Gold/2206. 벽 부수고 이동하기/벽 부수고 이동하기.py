# 시간 초과 2

# 3차원 배열을 활용해서 상태를 관리하는 방식에 대해서 학습
# bfs의 특성상 최단 거리의 방문을 우선 처리함
# 이로 인해 벽을 부순 경우와 부수지 않은 경우의 최단 거리 갱신이 가능

import sys
input = sys.stdin.readline

from collections import deque

def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1

    while queue:
        r, c, broke = queue.popleft()
        
        if r == N-1 and c == M-1:
            return visited[r][c][broke]
        
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            di = r + dr
            dj = c + dc

            if 0 <= di < N and 0 <= dj < M:

                if not matrix[di][dj] and not visited[di][dj][broke]:
                    visited[di][dj][broke] = visited[r][c][broke] + 1
                    queue.append((di,dj,broke))

                elif matrix[di][dj] and not broke and not visited[di][dj][1]:
                    visited[di][dj][1] = visited[r][c][broke] + 1
                    queue.append((di, dj, 1))

    return -1


# N 세로, M 가로
N, M = map(int, input().split())

matrix = [list(map(int, input().strip())) for _ in range(N)]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

print(bfs())