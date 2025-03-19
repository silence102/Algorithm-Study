def make_set(x):
    parents = [i for i in range(x + 1)]
    return parents

def find_set(x):
    if x == parent[x]:
        return x
    return find_set(parent[x])

def union_set(o, x, y):
    boss_x = find_set(x)
    boss_y = find_set(y)
    # 동맹 시그널
    if o == 1:
        # 같은 동맹국 또는 속국일 때
        if boss_x == boss_y:
            return
        # 동맹 후 - 큰 규모 국가에 몰아주기
        if world[boss_x] > world[boss_y]:
            world[boss_x] += world[boss_y]
            parent[boss_y] = boss_x
            world[boss_y] = 0
        else:
            world[boss_y] += world[boss_x]
            parent[boss_x] = boss_y
            world[boss_x] = 0

    # 전쟁 시그널
    if o == 2:
        # 아군과는 싸울 수 없음
        if boss_x == boss_y:
            return

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

# 국가의수 M, 기록의 수 M
N, M = map(int, input().split())

parent = make_set(N)

world = [0]
for _ in range(N):
    country = int(input())
    world.append(country)

for _ in range(M):
    # O = 1 (동맹), O = 2 (전쟁), P, Q 는 대상 국가
    O, P, Q = map(int, input().split())
    union_set(O, P, Q)

remain_country = []
# remain_country = set()
remain_power = []

# for i in range(1, N+1): 
#     con_num = find_set(parent[i])
#     remain_country.add(con_num)

for i in world:
    if i != 0:
        remain_country.append(i)

for j in remain_country:
    remain_power.append(j)

remain_power.sort()

print(len(remain_country))
print(*remain_power)