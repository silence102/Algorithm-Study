import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque()

for _ in range(N):
    age, name = input().split()
    queue.append((int(age), name))

# sorted 리스트 형변환과 deque로 다시 형변환 하는 방식을 학습함
queue = deque(sorted(queue, key= lambda x: x[0]))

while queue:
    print(*queue.popleft())