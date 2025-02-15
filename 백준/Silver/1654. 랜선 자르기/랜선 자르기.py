K, N = map(int, input().split())
K_arr = [int(input()) for _ in range(K)]    

max_len = 0
start, end = 1, max(K_arr)
while start <= end:
    middle = (start + end) // 2
    lan_cable = 0
    for i in range(K):
        lan_cable += K_arr[i] // middle
    if lan_cable >= N:
        max_len = middle
        start = middle + 1 
    else:
        end = middle - 1
print(max_len)