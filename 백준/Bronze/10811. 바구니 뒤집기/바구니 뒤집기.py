N, M = map(int, input().split())

nums = [0] + list(range(1, N + 1))

for _ in range(M):
    i, j = map(int, input().split())
    
    nums = nums[:i] + nums[j:i-1:-1] + nums[j+1:]

print(*nums[1:])