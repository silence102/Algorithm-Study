def solution(array): 
    max_num = max(array) # 1. 가장 큰 정수 값 구하기
    
    count = [0] * (max_num + 1) # 2. 0을 포함한 max 값 만큼 배열 생성
    
    for i in array: # 3. 배열의 숫자 개수 세기
        count[i] += 1
        
    mode = 0 # 4. 최빈값의 개수 구하기
    for i in count:
        if i == max(count):
            mode += 1
    
    if mode >= 2: # 5. 최빈값이 여러개 이면 -1, 한개 이면 최빈값을 출력
        return -1
    else:
        return count.index(max(count))