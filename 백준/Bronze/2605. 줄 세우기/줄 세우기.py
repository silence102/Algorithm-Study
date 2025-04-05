from collections import deque

N = int(input())

number = list(map(int, input().split()))

students = [i for i in range(1,N+1)]

for i in range(N):
    if number[i] > 0:
        num = number[i]
        queue = deque(students[i-num:i+1])
        temp = queue.pop()
        queue.appendleft(temp)
        students = students[:i-num] + list(queue) + students[i+1:]

print(*students)