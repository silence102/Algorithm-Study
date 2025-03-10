# 11723. 집합

# add x
# remove x
# check x
# toggle x
# all
# empty

import sys

N = int(sys.stdin.readline())

S = set()

for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == "add":
        S.add(int(order[1]))
    elif order[0] == "remove":
        S.discard(int(order[1]))
    elif order[0] == "check":
        if int(order[1]) in S:
            print(1)
        else:
            print(0)
    elif order[0] == "toggle":
        if int(order[1]) in S:
            S.remove(int(order[1]))
        else:
            S.add(int(order[1]))
    elif order[0] == "all":
        S.update(range(1, 21))
    elif order[0] == "empty":
        S.clear()