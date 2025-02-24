import sys

def stack_push(x):
    stack.append(x)

def stack_pop():
    if not stack:
        return -1
    return stack.pop()

def stack_size():
    return len(stack)

def is_empty():
    return int(not stack)

def stack_top():
    if not stack:
        return -1
    return stack[-1]

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    input = sys.stdin.readline
    order = input().split()

    if order[0] == "push":
        stack_push(order[1])
    elif order[0] == "top":
        print(stack_top())
    elif order[0] == "pop":
        print(stack_pop())
    elif order[0] == "empty":
        print(is_empty())
    elif order[0] == "size":
        print(stack_size())