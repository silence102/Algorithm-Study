N = int(input())

coordinate = []
for _ in range(N):
    (f, s) = map(int, input().split())
    coordinate.append((f, s))

coordinate.sort(key = lambda x: (x[0], x[1]))

for coor in coordinate:
    print(f"{coor[0]} {coor[1]}")