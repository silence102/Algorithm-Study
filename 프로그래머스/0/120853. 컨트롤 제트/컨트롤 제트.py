def solution(s):
    answer = 0
    num = 0
    s = s.split(" ")
    for i in s:
        if i == "Z":
            answer -= num
        else:
            answer += int(i)
            num = int(i)
    return answer