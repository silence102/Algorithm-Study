N, M = map(int, input().split())


arr1 = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(N)]

arr3 = list(zip(arr1, arr2))
answer = []

for i in range(len(arr3)):
    temp = []
    for j in range(M):
        sum_arr = arr3[i][0][j] + arr3[i][1][j]
        temp.append(sum_arr)
    answer.append(temp)

for i in answer:
    print(*i)