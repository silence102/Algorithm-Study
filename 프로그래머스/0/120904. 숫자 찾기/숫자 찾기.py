def solution(num, k):
    sum = 1
    for i in str(num):
        if i == str(k):
            return sum
        sum += 1
    return -1
            