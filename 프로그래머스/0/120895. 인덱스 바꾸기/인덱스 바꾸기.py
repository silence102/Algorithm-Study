def solution(my_string, num1, num2):
    answer = []
    result = ""
    change_num = 0
    for i in my_string:
        answer.append(i)
    change_num = answer[num1]
    answer[num1] = answer[num2]
    answer[num2] = change_num
    for i in answer:
        result += i
    return result
