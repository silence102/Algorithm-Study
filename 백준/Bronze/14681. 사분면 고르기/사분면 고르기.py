import sys

def main():
    A = int(sys.stdin.readline())
    B = int(sys.stdin.readline())
    
    if A > 0 and B > 0:
        print("1")
    elif A < 0 and B > 0:
        print("2")
    elif A < 0 and B < 0:
        print("3")
    elif A > 0 and B < 0:
        print("4")   

if __name__ == "__main__":
    main()