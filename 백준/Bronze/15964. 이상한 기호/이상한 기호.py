import sys

def main():
    A, B  = map(int, sys.stdin.readline().split())
    result = (A+B)*(A-B)
    print(result)

if __name__ == "__main__":
    main()