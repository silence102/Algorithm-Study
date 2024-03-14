def solution(my_string):
    answer = []
    for i in my_string:
        answer.append(i.lower())
    answer.sort()
    return ''.join(answer)