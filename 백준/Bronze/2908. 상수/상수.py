N, M = map(str, input().split())

if int(N[::-1]) >= int(M[::-1]):
    print(N[::-1])
else:
    print(M[::-1])