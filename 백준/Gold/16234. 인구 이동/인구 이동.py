# 인구 이동

'''
N x N 크기 땅/ 각 칸에 국가가 존재
인접한 국가 간의 인구 차이가 L명 이상 R명 이하인 경우 국경을 오픈
하루 동안은 서로 연합

연합을 이루고 있는 각 칸의 인구수 : 연합의 인구수 / 칸 수
이후 연합 해체하고 국경선 닫음
'''
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(s1, s2, visited):
    queue = deque()
    queue.append((s1, s2))
    union = [(s1, s2)]
    visited[s1][s2] = True
    
    total = matrix[s1][s2]
    count = 1
    # bfs로 최대로 먼저 방문 해보고 그 연합국에 대한 정보 갱신 가능

    # 그 외 방문하지 않은 곳 부터 다시 시작?

    while queue:
        r, c = queue.popleft()
        
        for k in range(4):

            di = r + dr[k]
            dj = c + dc[k]

            if 0 <= di < N and 0 <= dj < N and not visited[di][dj]:

                if L <= abs(matrix[r][c] - matrix[di][dj]) <= R:

                    visited[di][dj] = True

                    total += matrix[di][dj]
                    
                    count += 1
                    
                    queue.append((di, dj))
                    union.append((di, dj))

    if count == 1:
        return False

    population = total // count

    for i, j in union:
        matrix[i][j] = population
    
    return count
            


N, L, R = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

migration = 0

while True:
    changed = False
    visited = [[False] * (N) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]: 
                change = bfs(i, j, visited)
                if change:
                    changed = True

    if not changed:
        break

    migration += 1

print(migration)