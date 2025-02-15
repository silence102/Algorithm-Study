import sys
input = sys.stdin.readline

def main(arr, key):
    start, end = 0, len(arr) - 1

    while start <= end:
        middle = (start + end) // 2
        if key == arr[middle]:
            return True
        elif key > arr[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return False

if __name__ == "__main__":
    N = int(input())
    n_arr = list(map(int, input().split()))
    n_arr.sort()
    M = int(input())
    m_arr = list(map(int, input().split()))

    for key in m_arr:
        if main(n_arr, key):
            print(1)
        else:
            print(0)