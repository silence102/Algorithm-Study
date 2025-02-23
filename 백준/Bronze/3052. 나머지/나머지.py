count = set()
for _ in range(10):
    N = int(input())
    count.add(N % 42)

print(len(count))