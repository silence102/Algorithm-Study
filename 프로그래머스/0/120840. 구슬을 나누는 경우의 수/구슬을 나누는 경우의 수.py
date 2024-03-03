def solution(balls, share):
    num1 = 1;
    num2 = 1;
    num3 = 1;
    
    for i in range(2, balls+1):
        num1 *= i
    for i in range(2, (balls-share)+1):
        num2 *= i
    for i in range(2, share+1):
        num3 *= i
        
    return num1 / (num2 * num3)
