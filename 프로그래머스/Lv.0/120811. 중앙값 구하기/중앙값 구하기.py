def solution(array):
    array.sort()
    mid_len = len(array) // 2 + 1
    answer = array[mid_len-1]
    return answer