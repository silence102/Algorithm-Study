def solution(my_string):
    answer = ''
    aeiou = ['a','e','i','o','u']
    
    for i in my_string:
        if i in aeiou:
            continue
        else:
            answer += i
    return answer