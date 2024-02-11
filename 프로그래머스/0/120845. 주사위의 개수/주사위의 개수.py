def solution(box, n):
    answer = 1
    for i in box:
        print(i / n)
        answer *= i // n
    return answer