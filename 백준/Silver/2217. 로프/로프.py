import sys

def main():
    N = int(sys.stdin.readline())
    arr = []

    for _ in range(N):
        num = int(sys.stdin.readline())
        arr.append(num)

    arr.sort()

    max_w = 0
    for i in range(N):
        max_w = max(max_w, arr[i] * (N - i))

    sys.stdout.write(str(max_w))


if __name__ == "__main__":
    main()