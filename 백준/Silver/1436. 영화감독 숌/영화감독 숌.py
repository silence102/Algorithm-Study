N = int(input())

num = 666
movie = 0
while True:
    if '666' in str(num):
        movie += 1
    if movie == N:
        print(num)
        break
    num += 1