# 함부로 전역 변수로 visited를 선언하지 말자

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(s1, s2):
    global answer
    stack = []
    stack.append((s1,s2))
    visited.add((s1, s2))

    while stack:
        r, c = stack.pop()

        for k in range(4):
            di = r + dr[k]
            dj = c + dc[k]

            if 0 <= di < N and 0 <= dj < M and matrix[di][dj] and (di, dj) not in visited:
                visited.add((di, dj))
                stack.append((di, dj))
    
    answer += 1


T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())

    cabbage = []
    matrix = [[0] * M for _ in range(N)]

    for _ in range(K):
        Y, X = map(int, input().split())
        matrix[X][Y] = 1
        cabbage.append((X, Y))
        
    visited = set()
    answer = 0
    for i in cabbage:
        r, c = i[0], i[1]
        if (r, c) not in visited:
            dfs(r, c)

    print(answer)