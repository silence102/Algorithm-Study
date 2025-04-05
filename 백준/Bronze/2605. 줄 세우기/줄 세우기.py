N = int(input())
number = list(map(int, input().split()))

students = []

for i in range(N):
    students.insert(i - number[i], i + 1)

print(*students)