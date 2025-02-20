max_num = 0
max_idx = 0
for i in range(1, 10):
    N = int(input())
    if N > max_num:
        max_num = N
        max_idx = i

print(max_num)
print(max_idx)