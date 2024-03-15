def solution(order):
    answer = 0
    game = [3, 6, 9]
    for i in str(order):
        if int(i) in game:
            answer += 1
    return answer