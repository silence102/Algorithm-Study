N, K = map(int, input().split())

coins = []
result = 0

for _ in range(N):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse=True)

for i in coins:
    if K // i > 0:
        result += K // i
        K %= i

print(result)