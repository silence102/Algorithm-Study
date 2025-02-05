import sys

def main():
    A, B = map(int, sys.stdin.readline().split())
    if A > B:
        print(">")
    elif A < B:
        print("<")
    elif A == B:
        print("==")

if __name__ == "__main__":
    main()