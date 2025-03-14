import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dogam = {

}

for i in range(1, N + 1):
    monster = input().strip()
    dogam[i] = monster
    dogam[monster] = i

for j in range(M):
    order = input().strip()
    if order.isdecimal():
        print(dogam[int(order)])
    else:
        print(dogam[order])