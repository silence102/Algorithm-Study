N, M = map(int, input().split())

if N < M:
    num1, num2 = M, N
else:
    num1, num2 = N, M

while num2 != 0:
    num1, num2 = num2, num1 % num2

G = num1
L = (N // G) * (M // G) * G

print(G)
print(L)