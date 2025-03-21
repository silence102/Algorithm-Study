N, M = map(int, input().split())

memo = {}

for _ in range(N):
    site, pw = input().split()
    memo[site] = pw

for _ in range(M):
    find = input()
    print(memo[find])