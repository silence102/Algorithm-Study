N1 = int(input())
N2 = list(map(int, input()))

total = 0
for i in range(len(N2)):
    total += N1 * N2[-i-1] * int('1' + ('0'*i))
    print(N1 * N2[-i-1])
print(total)