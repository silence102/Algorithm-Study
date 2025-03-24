T = int(input())


for tc in range(1, T + 1):
    N = int(input())

    dp = [0] * (N + 1)

    dp[0] = 1

    if N >= 3:
        dp[1] = 1
        dp[2] = 2
        for i in range(3, N + 1):
            if dp[i] == 0:
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[N])
    else:
        if N == 1:
            print(1)
        elif N == 2:
            print(2)
        else:
            print(dp[N])
