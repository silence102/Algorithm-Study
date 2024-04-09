def solution(array, height):
    tall = []
    for i in array:
        if i > height:
            tall.append(i)            
    return len(tall)