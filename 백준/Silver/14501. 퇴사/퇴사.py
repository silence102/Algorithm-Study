def recur(time, total):
    global max_value
    if time > N:
        return
    
    if time == N:
        max_value = max(max_value, total)
        return
    
    T, P = schedule[time]
    
    if time + T <= N:
        recur(time + T, total + P)

    recur(time + 1, total)

N = int(input())

schedule = []
for _ in range(N):
    T, P = map(int, input().split())
    schedule.append((T,P))

max_value = 0
recur(0, 0)
print(max_value)