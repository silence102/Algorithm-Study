# 카드 합 21 이하에서 가장 큰 최대 합 만드는 게임
def black_jack(x, total):
    global answer
    if total > M:
        return

    if x == 3:
        if total <= M:
            answer = max(answer, total)
        return
    
    for i in range(N):
        if visited[i]:
            continue

        visited[i] = 1
        black_jack(x+1, total + card[i])
        visited[i] = 0

N, M = map(int, input().split())

card = list(map(int, input().split()))

answer = 0
visited = [0] * (N + 1)
black_jack(0, 0)
print(answer)