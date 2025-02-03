import sys

def main():
    A, B = map(int, sys.stdin.readline().split())
    result1 = A + B
    result2 = A - B
    result3 = A * B
    result4 = A // B
    result5 = A % B
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
    
if __name__ == "__main__":
    main()