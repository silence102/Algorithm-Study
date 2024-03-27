def solution(numbers):
    numbers.sort()
    comp1 = numbers[0] * numbers[1]
    comp2 = numbers[-1] * numbers[-2]
    if comp1 > comp2:
        return comp1
    else:
        return comp2