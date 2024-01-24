def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '0': 
            answer = answer + '5'
        elif i == '2':
            answer = answer + '0'
        elif i == "5":
            answer = answer + '2'
    return answer