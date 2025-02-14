import sys

def main():
    T = int(sys.stdin.readline())

    for _ in range(T):
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
        
if __name__ == "__main__":
    main()