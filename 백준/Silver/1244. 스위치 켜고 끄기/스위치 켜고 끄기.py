N = int(input())

switch = list(map(int, input().split()))

P = int(input())

for p in range(P):
    G, C = map(int, input().split())

    if G == 1:
        for i in range(C-1, N, C):
            switch[i] = (switch[i] + 1) % 2
    else:
        C = C - 1    
        switch[C] = (switch[C] + 1) % 2
        for i in range(1, N // 2 + 1):
            if 0 <= C-i and C+i < N:
                if switch[C-i] == switch[C+i]:
                    switch[C-i] = (switch[C-i] + 1) % 2
                    switch[C+i] = (switch[C+i] + 1) % 2
                else:
                    break

for i in range(len(switch)):
    if i % 20 == 0 and i != 0:
        print()
    print(switch[i], end=" ")
