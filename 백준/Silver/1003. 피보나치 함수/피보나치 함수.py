T = int(input())

for _ in range(T):
    N = int(input())
    dp = [(0, 0, 0)] * (N + 1)
    if N >= 1:
        dp[0] = (0, 1, 0)
        dp[1] = (1, 0, 1)
    else:
        dp[0] = (0, 1, 0)
        print(dp[0][1], dp[0][2])
        continue

    for i in range(2, N+1):
        if dp[i] == (0, 0, 0):
            a, b = dp[i-1], dp[i-2]
            dp[i] = (a[0]+b[0], a[1]+b[1], a[2]+b[2])

    print(dp[N][1], dp[N][2])