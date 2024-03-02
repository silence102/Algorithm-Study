def solution(hp):
    answer = 0
    while (hp > 0):
        if (hp // 5) != 0:
            answer += (hp // 5)
            hp = hp % 5
        elif (hp // 3) != 0:
            answer += (hp // 3)
            hp = hp % 3
        elif (hp // 1) != 0:
            answer += (hp // 1)
            hp = 0     
    return answer
        