import sys

def main():
    A, B, C = map(int, sys.stdin.readline().split())
    result = A + B + C
    print(result)
    
if __name__ == "__main__":
    main()