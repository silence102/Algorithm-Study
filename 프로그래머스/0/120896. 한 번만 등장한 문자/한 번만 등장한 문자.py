def solution(s):
    al = [0] * 26
    answer = []
    
    for i in s:
        num = ord(i) - 97
        al[num] += 1
        
    for i in range(len(al)):
        if al[i] == 1:
            answer.append(chr(i + 97))
            
    return "".join(answer)