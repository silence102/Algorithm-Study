import math

def solution(n):
    square_root = math.sqrt(n)
    square_number = square_root ** 2
    
    if square_root % 1 == 0:
        return 1
    else:
        return 2