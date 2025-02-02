import sys

def main():
    a, b, c, d, e = map(int, sys.stdin.readline().split())
    total = a**2 + b**2 + c**2 + d**2 + e**2
    code = total % 10
    print(code)
    
if __name__ == "__main__":
    main()