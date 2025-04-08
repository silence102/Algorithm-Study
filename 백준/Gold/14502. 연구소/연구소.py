# 연구소

from collections import deque

def bfs():
    queue = deque(virus)
    # 얕은 복사로 인해서 초기 시도를 제외하고는 lab의 기존 형태가 훼손되었던 문제가 있었음 -> 적절한 복사와 초기화가 이루어져야 했으나 백트래킹 만으로 초기화가 될 수 있었던 오류가 있었음.
    visited = [i[:] for i in lab]
    
    while queue:
        r, c = queue.popleft()
        
        for i, j in [(-1,0), (1,0), (0,-1),(0,1)]:
            di = r + i
            dj = c + j

            if 0 <= di < N and 0 <= dj < M and not visited[di][dj]:
                visited[di][dj] = 2
                queue.append((di, dj))

    total = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                total += 1
                
    return total

def back(cnt):
    
    global answer
    if cnt == 3:
        result = bfs()
        answer = max(answer, result)
        return

    for i in range(N):
        for j in range(M):
            if not lab[i][j]:
                lab[i][j] = 1
                back(cnt + 1)
                lab[i][j] = 0


# N: 가로, M: 세로
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# BFS로 바이러스 위치에서 번지기 시작해서 최종 남은 안전지대 구하기
# 벽 3개를 임의로 세워서 각각의 BFS 실행 후 최대 안전지대 값 갱신
# 어려운 점: 3개의 임의의 벽을 어떤 기준으로 세워줄 수 있는지가 관건

# 1. 바이러스 위치 파악
virus = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            virus.append((i, j))

# 2. 임의의 위치에 벽 3개 세운 후 바이러스 퍼진 결과 시뮬레이션
answer = 0 
back(0)
print(answer)