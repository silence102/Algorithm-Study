def solution(i, j, k):
    sentence = ''
    result = 0
    for i in range(i,j+1):
        sentence += str(i)
    for i in sentence:
        if i == str(k):
            result += 1
    return result