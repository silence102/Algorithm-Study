import sys
import math

M, N = map(int, sys.stdin.readline().split())

for i in range(M, N+1):
    if i < 2:
        continue
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            break
    else:
        print(i)