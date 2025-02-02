import sys

def main():
    a, b = map(int, sys.stdin.readline().split())
    result = (a + b) * (a - b)
    print(result)

if __name__ == "__main__":
    main()