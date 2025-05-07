# 1. 부르는 번호들을 순차적으로 순서대로 딕셔너리에 저장
# 2. 딕셔너리에 저장된 값들로 현재 빙고판의 rank 기반 순서를 기록
# 3. 이를 활용해 순서대로 새로운 마크를 표시

# 4. 매번 가로, 새로, 대각선을 확인하고 3빙고가 되면 종료 <- 이 부분 도움받음
# + 25 반복을 도는 아이디어, all

matrix = [list(map(int, input().split())) for _ in range(5)]

say_num = [list(map(int, input().split())) for _ in range(5)]

counting = {}
for i in range(5):
    for j in range(5):
        counting[say_num[i][j]] = (j + 1) + (5 * i)

for i in range(5):
    for j in range(5):
        matrix[i][j] = counting[matrix[i][j]]

called = [[False] * 5 for _ in range(5)]

for step in range(1, 26):

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == step:
                called[i][j] = True

    bingo = 0

    for row in called:
        if all(row):
            bingo += 1

    for col in range(5):
        if all(called[row][col] for row in range(5)):
            bingo += 1

    if all(called[i][i] for i in range(5)):
        bingo += 1

    if all(called[i][4 - i] for i in range(5)):
        bingo += 1

    if bingo >= 3:
        print(step)
        break

# 빙고 3줄이 완성되는 타이밍은?