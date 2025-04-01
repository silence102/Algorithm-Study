N = int(input())

A, B, C = 0, 0, 0

# A는 짝수 - 2
# A, B, C는 0보다 크다
# C는 B보다 2개 이상 크다

# 최소 - 2 1 3 => 6
# 최대 - 2x + 2y + c(최소 2)

count = 0

for A in range(2, N, 2):
    for B in range(1, N - A):
        C = N - A - B
        if C > 0 and C >= B + 2:
            count += 1

print(count)