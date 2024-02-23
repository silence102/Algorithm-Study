def solution(n):
    numList = []
    num = 0
    
    for i in range(0,n+1,2):
        numList.append(i)
    for i in numList:
        num += i
    return num