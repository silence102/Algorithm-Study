def makesum(n):
    for i in range(1, n):
        num = i + sum(int(j) for j in str(i))   
        if num == N:
            print(i)
            return
    print(0)

N = int(input())
makesum(N)    