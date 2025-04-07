N, K = map(int, input().split())

students_info = [0] * 13
for _ in range(N):
    g, c = map(int, input().split())
    if g == 0:
        idx = 2 * c - 1
    else:
        idx = 2 * c

    students_info[idx] += 1
answer = 0
for i in range(len(students_info)):
    if students_info[i] > K:
        if students_info[i] % K > 0:
            answer += students_info[i] // K + 1
        else:
            answer += students_info[i] // K
    elif 0 < students_info[i] <= K:
        answer += 1

print(answer)