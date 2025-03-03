import sys

# N: 세로 M: 가로
N, M = map(int, sys.stdin.readline().split())

# 테트로미노 보드 N * M
tetromino = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 최대 합
max_sum = 0

max_val = max(map(max, tetromino))

visited = [[False] * M for _ in range(N)]

# r,c: 시작 좌표 depth: 테트로미노는 4칸, total: 총합
def dfs(r, c, depth, total):
    global max_sum

    if total + (4 - depth) * max_val <= max_sum:
        return

    if depth == 4:
        max_sum = max(max_sum, total)
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
           visited[nr][nc] = True
           dfs(nr, nc, depth + 1, total + tetromino[nr][nc])
           visited[nr][nc] = False

def check_oh_shapes(r, c):
    """ 'ㅗ', 'ㅜ', 'ㅏ', 'ㅓ' 모양 처리 """
    global max_sum
    shapes = [
        [(0, 0), (0, 1), (0, 2), (-1, 1)],  # ㅗ
        [(0, 0), (0, 1), (0, 2), (1, 1)],   # ㅜ
        [(0, 0), (1, 0), (2, 0), (1, -1)],  # ㅓ
        [(0, 0), (1, 0), (2, 0), (1, 1)],   # ㅏ
    ]

    for shape in shapes:
        total = 0
        is_valid = True
        for x, y in shape:
            di, dj = r + x, c + y
            if 0 <= di < N and 0 <= dj < M:
                total += tetromino[di][dj]
            else:
                is_valid = False
                break
        if is_valid:
            max_sum = max(max_sum, total)

for i in range(N):
    for j in range(M):
        # DFS 탐색     
        visited[i][j] = True
        dfs(i, j, 1, tetromino[i][j])
        visited[i][j] = False

        # 'ㅗ' 모양 체크
        check_oh_shapes(i, j)

print(max_sum)