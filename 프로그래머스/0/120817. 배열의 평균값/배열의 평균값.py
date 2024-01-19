def solution(numbers):
    sum_num = 0
    for i in numbers:
        sum_num += i
    answer = sum_num / len(numbers)
    return answer