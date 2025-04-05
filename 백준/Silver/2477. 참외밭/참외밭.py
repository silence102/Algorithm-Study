N = int(input())

k_melon = []
for _ in range(6):
    d, l = map(int, input().split())
    k_melon.append((d, l))

total1 = []
total2 = []

sort_k = sorted(k_melon, key=lambda x:x[1], reverse=True)
total1.append(sort_k[0])

if sort_k[0][0] == 1 or sort_k[0][0] == 2:
    for i in range(1,6):
        if sort_k[i][0] == 3 or sort_k[i][0] == 4:
            total1.append(sort_k[i])
            break
else:
    for i in range(1,6):
        if sort_k[i][0] == 1 or sort_k[i][0] == 2:
            total1.append(sort_k[i])
            break

for i in range(6):
    if k_melon[i] in total1:
        total2.append(k_melon[(i + 3) % 6])

total1 = total1[0][1] * total1[1][1]

total2 = total2[0][1] * total2[1][1]

print((total1 - total2) * N)