T = int(input())

for tc in range(1, T+1):
    OX = input()
    total = 0
    count = 0
    for i in range(len(OX)):
        if OX[i] == "O":
            count += 1
            total += count
        else:
            count = 0
    print(total)