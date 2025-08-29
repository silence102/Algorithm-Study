def solution(my_string):
    total = 0
    num = ""
    sign = 1
    
    for i in my_string:
        if i.isdigit():
            num += i
        elif i in "+-":
            if num:
                total += sign * int(num)
                num = ""
            sign = 1 if i == "+" else -1
        else:
            pass
        
    if num:
        total += sign * int(num)
    return total