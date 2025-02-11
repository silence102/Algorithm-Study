import sys

def main():
    input = sys.stdin.readline
    ouput = sys.stdout.write
    T = int(input().rstrip())

    for tc in range(1, T + 1):
        A, B = map(int, input().split())
        answer = A + B
        ouput(str(answer) + "\n")


if __name__ == "__main__":
    main()