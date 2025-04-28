H, M = map(int, input().split())
cook = int(input())


if M + cook >= 60:
    hour = (M + cook) // 60
    minutes = (M + cook) % 60
else:
    hour = 0
    minutes = (M + cook)

if (H + hour) >= 24:
    print(f"{(H + hour) % 24} {minutes}")
else:
    print(f"{H + hour} {minutes}")