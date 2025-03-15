# 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M
N, M = map(int, input().split())

listen = set()
watch = set()

for _ in range(N):
    name = input()
    listen.add(name)

for _ in range(M):
    name = input()
    watch.add(name)

answer = list(listen & watch)
answer.sort()

print(len(answer))
for i in range(len(answer)):
    print(answer[i])