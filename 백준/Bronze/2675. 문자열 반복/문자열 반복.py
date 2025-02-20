T = int(input())

for tc in range(1, T+1):
    N, word = input().split()

    new_word = ""
    for i in word:
        new_word += (i * int(N))
    print(new_word)