def solution(array, n):
    array.append(n)
    array.sort()
    num = array.index(n)
    if array[num] == max(array):
        return array[num-1]
    elif array[num] == min(array):
        return array[num+1]
    else:
        comp1 = abs(array[num+1] - array[num])
        comp2 = abs(array[num-1] - array[num])
        if comp1 > comp2:
            return array[num-1]
        elif comp1 < comp2:
            return array[num+1]
        else:
            return array[num-1]