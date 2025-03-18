import sys
import heapq

input = sys.stdin.readline

max_heap = []

N = int(input())

for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(max_heap, -x)
    else:
        if max_heap:
            print(-heapq.heappop(max_heap))
        else:
            print(0)