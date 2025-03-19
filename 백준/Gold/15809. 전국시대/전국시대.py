import sys
input = sys.stdin.readline

def main():
    # 국가의수 M, 기록의 수 M
    N, M = map(int, input().split())

    parent = [i for i in range(N + 1)]

    world = [0] + [int(input()) for _ in range(N)]

    for _ in range(M):
        # O = 1 (동맹), O = 2 (전쟁), P, Q 는 대상 국가
        O, P, Q = map(int, input().split())
        boss_x = find_set(P, parent)
        boss_y = find_set(Q, parent)

        if O == 1:
            # 동맹 후 - 큰 규모 국가에 몰아주기
            if boss_x > boss_y:
                world[boss_x] += world[boss_y]
                parent[boss_y] = boss_x
                world[boss_y] = 0
            else:
                world[boss_y] += world[boss_x]
                parent[boss_x] = boss_y
                world[boss_x] = 0

        # 전쟁 시그널
        else:
            # 주전 국 간의 규모 비교 3가지 경우
            if world[boss_x] > world[boss_y]:
                world[boss_x] -= world[boss_y]
                world[boss_y] = 0
                parent[boss_y] = boss_x
            elif world[boss_x] < world[boss_y]:
                world[boss_y] -= world[boss_x]
                world[boss_x] = 0
                parent[boss_x] = boss_y
            else:
                world[boss_x], world[boss_y] = 0, 0
                parent[boss_x] = 0
                parent[boss_y] = 0 

    remain_country = []
    remain_power = []

    for i in world:
        if i != 0:
            remain_country.append(i)

    for j in remain_country:
        remain_power.append(j)

    remain_power.sort()

    print(len(remain_country))
    print(*remain_power)

def find_set(x, parent):
    if parent[x] == x:
            return x
    parent[x] = find_set(parent[x], parent)
    return parent[x]

if __name__ == "__main__":
    main()