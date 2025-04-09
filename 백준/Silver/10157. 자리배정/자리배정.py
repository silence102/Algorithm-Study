import sys
input = sys.stdin.readline

# N: 가로, M: 세로
N, M = map(int, input().split())
target = int(input())

# 예외 처리 해줄 수 있는 조건을 우선 처리
if target > N * M:
    print(0)
    exit()

matrix = [[0] * N for _ in range(M)]

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
d = 0

# 좌표를 이해하는 방식에서 조금 어려움이 있었음
# 문제에서는 X축 Y축의 위치를 요구하고 있었으므로 인덱스의 개념과는 반대로 생각하고 값이 0이 아닌 1부터 시작함을 인지하고 접근해야 함.

r, c = M - 1, 0
matrix[r][c] = 1

# 설마 답이 1인 경우를 놓쳤던 건가..?
if target == 1:
    print(f"{c + 1} {M - r}")
    exit()

for i in range(2, N * M + 1):
    di = r + dr[d]
    dj = c + dc[d]

    if 0 <= di < M and 0 <= dj < N and not matrix[di][dj]:
        r, c = di, dj
        matrix[di][dj] = i
    
    else:
        # 방향을 한번 바꾸는 걸로는 안될 수도 있으니 여러번 바꿔볼 수 있도록 변경
        for _ in range(4):
            d = (d + 1) % 4
            di = r + dr[d]
            dj = c + dc[d]
            
            if 0 <= di < M and 0 <= dj < N and not matrix[di][dj]:
                r, c = di, dj
                matrix[r][c] = i
                break
    
    if i == target:
        print(f"{c + 1} {M - r}")
        break