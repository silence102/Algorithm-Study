def find_pair(pairs):
    stack = []

    for i in range(len(pairs)):
        if pairs[i] == "(":
            stack.append(pairs[i])
        elif pairs[i] == ")":
            if not stack:
                return False
            stack.pop()

    return not stack

N = int(input())

for _ in range(N):
    braket = list(input())
    print("YES" if find_pair(braket) else "NO")