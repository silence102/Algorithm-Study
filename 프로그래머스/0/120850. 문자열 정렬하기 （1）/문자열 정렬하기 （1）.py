def solution(my_string):
    answer = []
    for i in my_string:
        for j in range(10):
            if i == str(j):
                answer.append(int(i))
    answer.sort()
    return answer