def solution(price):
    if price >= 500000:
        answer =  price - (price * (20 / 100))
    elif price >= 300000:
        answer = price - (price * (10 / 100))
    elif price >= 100000:
        answer = price - (price * (5 / 100))
    else:
        answer = price
    return int(answer)