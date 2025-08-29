def solution(numbers):
    alpha_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, w in enumerate(alpha_list):
        numbers = numbers.replace(w, str(i))
    return int(numbers)