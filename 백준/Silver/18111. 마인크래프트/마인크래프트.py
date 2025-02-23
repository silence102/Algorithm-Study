# N: 집터 세로, M: 집터 가로, B: 인벤토리 블럭 개수
N, M, B = map(int, input().split())

# 땅 높이 정보/ 0 <= 땅 높이 <= 256
ground = [list(map(int, input().split())) for _ in range(N)]

# 최고, 최저 값 구하기
max_g = 0
min_g = 256

# 카운팅
counting = [0] * 257 

for i in range(N):
    for j in range(M):
        height = ground[i][j]
        counting[height] += 1
        max_g = max(max_g, height)
        min_g = min(min_g, height)        

best_time = float('inf')
best_height = 0

# 평탄화 가능한 범위 모두 탐색
for level in range(min_g, max_g+1):
    remove_blocks = 0
    add_blocks = 0

    # 목표 높이와 값을 가진 다른 높이 비교
    for height in range(257):
        if counting[height] > 0:

            # 비교 후 목표 높이 보다 높으면 제거해야할 개수 추가
            if height > level:
                remove_blocks += (height - level) * counting[height]
            # 비교 후 목표 높이 보다 낮으면 추가해야할 개수 추가
            elif height < level:
                add_blocks += (level - height) * counting[height]

    # 추가 해야 하는 개수 보다 가지고 있는 개수가 크거나 같아야 하는 조건
    if remove_blocks + B >= add_blocks:
        time = (remove_blocks * 2) + add_blocks

        # 시간 짧은거 우선, 값이 같으면 더 높은 값 갱신신
        if time < best_time or (time == best_time and level > best_height):
            best_time = time
            best_height = level

# 시간, 높이 정답 출력
print(best_time, best_height)