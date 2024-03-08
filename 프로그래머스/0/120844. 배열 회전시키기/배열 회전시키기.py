def solution(numbers, direction):
    answer = [0] * len(numbers)
    for i in range(len(numbers)):
        if direction == "right":
            answer[i] = numbers[i-1]
        elif i == (len(numbers)-1) and direction == "left":
            answer[-1] = numbers[0]
        else:
            answer[i] = numbers[i+1]
    return answer 