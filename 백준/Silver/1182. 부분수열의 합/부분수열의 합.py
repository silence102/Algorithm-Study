N, S = map(int, input().split())

numbers = list(map(int, input().split()))

# 부분수열의 합이 S가 되는 경우의 수: 부분집합 계산

# 2**N 개의 경우가 존재
result = 0
for i in range(1, 1 << N):
    subset = []
    for j in range(N):
        if i & (1 << j):
            subset.append(numbers[j])

    if sum(subset) == S:
        result += 1

print(result)