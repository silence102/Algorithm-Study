def solution(n):
    cnt = 1
    fact = 1
    while(fact < n):
        cnt += 1
        fact *= cnt
    if fact > n:
        cnt -= 1
    return cnt