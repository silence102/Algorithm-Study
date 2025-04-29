N = int(input())

if N // 4 > 1:
    text = ["long"] * 1 * (N // 4)
else:
    text = ["long"] * 1
    
print(*text, "int")