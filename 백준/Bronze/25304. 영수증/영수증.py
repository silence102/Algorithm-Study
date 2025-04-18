Total = int(input())

N = int(input())

sum_product = 0
for _ in range(N):
    price, count = map(int, input().split())
    sum_product += (price * count)
    
if Total == sum_product:
    print("Yes")
else:
    print("No")