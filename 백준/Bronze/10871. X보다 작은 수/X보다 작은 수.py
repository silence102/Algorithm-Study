import sys

def main():
    N, X = map(int, sys.stdin.readline().split())
    arr = list(map(int, input().split()))

    for i in range(N):
        if arr[i] < X:
            print(arr[i], end=" ")

if __name__ == "__main__":
    main()