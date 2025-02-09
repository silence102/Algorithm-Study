import sys

def main():
    N = int(sys.stdin.readline())
    n = 10001
    arr = [0] * n

    for _ in range(N):
        num = int(sys.stdin.readline())
        arr[num] += 1

    for num in range(n):
        if arr[num] > 0:
            for _ in range(arr[num]):
                sys.stdout.write((str(num) + "\n"))

if __name__ == "__main__":
    main()