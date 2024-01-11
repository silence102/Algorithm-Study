import math 
def solution(numer1, denom1, numer2, denom2):  
    denom = denom1 * denom2
    numer = (numer1 * denom2) + (numer2 * denom1) 
    getgcd = math.gcd(numer, denom)
    numer = numer // getgcd
    denom = denom // getgcd
    answer = [numer, denom]
    return answer
# from fractions import Fraction
# def solution(num1,den1,num2,den2):
#     answer = Fraction(num1,den1) + Fraction(num2,den2)
#     return [(answer.numerator),(answer.denominator) ]
    
