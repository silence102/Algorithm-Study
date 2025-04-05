N = int(input())

k_melon = [tuple(map(int, input().split())) for _ in range(6)]

max_width = 0
max_height = 0
max_width_idx = 0
max_height_idx = 0

for i in range(6):
    d, l = k_melon[i]
    if d == 1 or d == 2:
        if l > max_width:
            max_width = l
            max_width_idx = i
    else:
        if l > max_height:
            max_height = l
            max_height_idx = i

big = max_width * max_height

small_idx1 = (max_width_idx + 3) % 6
small_idx2 = (max_height_idx + 3) % 6 

small = k_melon[small_idx1][1] * k_melon[small_idx2][1]

print((big-small) * N)