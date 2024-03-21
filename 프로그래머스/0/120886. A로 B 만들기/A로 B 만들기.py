def solution(before, after):
    compare1 = []
    compare2 = []
    for i in before:
        compare1.append(i)
    for i in after:
        compare2.append(i)
    compare1.sort()
    compare2.sort()
    if compare1 == compare2:
        return 1
    else: 
        return 0
