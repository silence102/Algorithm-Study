from math import prod

count = [0] * 10

nums = []
for _ in range(3):
    nums.append(int(input()))

product = prod(nums)
for i in str(product):
    count[int(i)] += 1

for j in count:
    print(j)