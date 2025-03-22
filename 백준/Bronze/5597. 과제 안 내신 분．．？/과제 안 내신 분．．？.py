num = [0] * 31
for _ in range(28):
    N = int(input())
    num[N] += 1
    
for i in range(1, len(num)):
    if num[i] == 0:
        print(i)
    