import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    arr_n = list(map(int, input().split()))
    arr_n.sort()

    M = int(input())
    arr_m = list(map(int, input().split()))

    for i in range(M):
        start = 0
        end = N - 1
        while start <= end:
            middle = (start + end) // 2
            if arr_n[middle] == arr_m[i]:
                print(1, end=" ")
                break
            elif arr_n[middle] > arr_m[i]:
                end = middle - 1
            else:
                start = middle + 1
        else:
            print(0, end=" ")


if __name__ == "__main__":
    main()