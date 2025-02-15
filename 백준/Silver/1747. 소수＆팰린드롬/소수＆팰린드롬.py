def is_pal(i):
    pal = str(i)
    return pal == pal[::-1]

import sys
N = int(sys.stdin.readline())
for i in range(N, 1003002):
    # 소수는 1과 자기 자신으로 만 나누어지는 수
    # 1은 소수가 아님 
    if i == 1:
        continue

    if is_pal(i):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
            break