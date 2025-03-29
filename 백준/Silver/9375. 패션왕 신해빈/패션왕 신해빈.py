T = int(input())

for _ in range(T):
    N = int(input())

    kinds = {}
    for i in range(N):
        item, kind = input().split()

        if kind in kinds:
            kinds[kind] += 1
        else:
            kinds[kind] = 1
    
    answer = 1
    for j in kinds:
        answer *= kinds[j] + 1
    
    print(answer - 1)