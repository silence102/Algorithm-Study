N = int(input())

nums = list(map(int, input().split()))

count = 0
for i in nums:
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        count += 1

print(count)