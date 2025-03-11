N = int(input())

waiting = list(map(int, input().split()))

waiting.sort()

total = 0
temp = 0
for i in range(N):
    temp += waiting[i]
    total += temp

print(total)