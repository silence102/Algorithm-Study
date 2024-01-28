answer = []
def solution(my_string):
    for i in my_string:
        answer.append(i)
    return "".join(answer[::-1])
     
