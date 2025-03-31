N, M, K = map(int, input().split())

max_team = min(N//2, M)

remain = N + M - K

print(min(remain // 3, max_team))