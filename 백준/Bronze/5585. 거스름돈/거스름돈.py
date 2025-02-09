import sys

def main():
    price = int(sys.stdin.readline())
    change = 1000 - price
    JOI = [500, 100, 50, 10, 5, 1]
    count = 0

    for i in JOI:
        count += (change // i)
        change %= i
    
    print(count)

if __name__ == "__main__":
    main()