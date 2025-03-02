N = int(input())

max_big = N // 5
count_bag = 0

for k in range(max_big, -1, -1):
    M = N - 5*k
    if M % 3 == 0:
        count_bag += M // 3
        count_bag += k
        break
else:
    count_bag = -1

print(count_bag)