def solution(n, k):
    cost = (12000*n + 2000*k)
    answer = cost - (n//10)*2000
    return answer