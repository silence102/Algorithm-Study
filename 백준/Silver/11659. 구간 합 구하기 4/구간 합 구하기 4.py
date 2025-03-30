import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))

sum_list = [0]
for num in nums:
    sum_list.append(sum_list[-1] + num)

for _ in range(M):
    s, e = map(int, input().split())

    print(sum_list[e] - sum_list[s-1])