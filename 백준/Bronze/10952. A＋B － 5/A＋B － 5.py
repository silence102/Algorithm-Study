import sys

def main():
    while 1:
        A, B = map(int, sys.stdin.readline().split())
        if A == 0 and B == 0:
            break
        print(A + B)

if __name__ == "__main__":
    main()