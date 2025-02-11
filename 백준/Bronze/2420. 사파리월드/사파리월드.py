import sys

def main():
    A, B = map(int, sys.stdin.readline().split())
    if A > 0 and B > 0:
        print(abs(A - B))
    elif A > 0 and B < 0:
        print(A + abs(B))
    elif A < 0 and B > 0:
        print(B + abs(A))
    else:
        print(abs(A - B))

if __name__ == "__main__":
    main()