# 시간 초과 4

# R, C 의 크기가 20이나 되는 점, in 연산이 시간 복잡도가 O(N)인 점, 알파벳이 가지는 특성
# 비트 마스크 표현 방식 - 어렵긴 한데 조금씩 배우는 중

import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, visited, cnt):
    global answer
    # 마지막 가지에서 더 이상 나아가지 않게 처리
    if cnt == 26:
        answer = 26
        return

    # 현재 까지의 위치와 방문 기록을 set()에 입력해두고 중복이 없도록 관리
    state = (r, c, visited)
    if state in visited_set:
        return
    
    visited_set.add(state)

    answer = max(answer, cnt)

    for k in range(4):
        di = r + dr[k]
        dj = c + dc[k]
        
        if 0 <= di < R and 0 <= dj < C:
            index = ord(matrix[di][dj])-65
            if not visited & (1 << index):
                dfs(di, dj, visited | (1 << index), cnt + 1)         

# R 세로, C 가로
R, C = map(int, input().split())

matrix = [input() for _ in range(R)]

start_index = ord(matrix[0][0])-65
visited_set = set()

answer = 0
dfs(0, 0, 1 << start_index, 1)
print(answer)