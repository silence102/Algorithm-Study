import sys
import heapq

N = int(sys.stdin.readline())

heap = []
for _ in range(N):
    X = int(sys.stdin.readline())
    
    if X != 0:
        heapq.heappush(heap, X)
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))