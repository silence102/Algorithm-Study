def solution(n):
    answer = 1 # 피자 한판
    while (answer * 6) % n != 0: # 사람 수로 나눈 나머지가 0이면 정답, 
        answer += 1 # 아니면 피자 한판 더해서 반복
    return answer    