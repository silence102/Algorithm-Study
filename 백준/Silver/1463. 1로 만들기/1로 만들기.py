# DP 사용
N = int(input())

# N 크기 만큼 DP 배열 생성
dp = [0] * (N + 1)

# 미리 반복문을 통해 DP 배열의 값을 채워둠 - 작은 값부터 차곡차곡 값을 채워 나감
for i in range(2, N + 1):
    # 3가지 방식의 경우의 수를 구하고 최솟값을 DP에 저장
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

# 정답 출력
print(dp[N])