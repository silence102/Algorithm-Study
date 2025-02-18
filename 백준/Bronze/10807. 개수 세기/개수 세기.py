N = int(input())

arr = list(map(int, input().split()))

v = int(input())

count = 0
for i in range(N):
    if v == arr[i]:
        count += 1

print(count)