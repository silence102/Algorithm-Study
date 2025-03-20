import sys
input = sys.stdin.readline

N = int(input())
ask = list(map(int, input().split()))
budget = int(input())

max_v = max(ask)

if sum(ask) <= budget:
    print(max_v)
else:
    start = 0
    end = max_v
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        total = sum(min(mid, cost) for cost in ask)

        if total <= budget:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    print(answer)