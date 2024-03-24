def solution(num_list, n):
    cnt = 0
    numbers = []
    answer = []
    for i in range(len(num_list)):
        numbers.append(num_list[i])
        cnt += 1
        if cnt == n:
            answer.append(numbers)
            cnt = 0
            numbers = []
    return answer