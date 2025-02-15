def main(N):
    if N < 2:
        return N
    a, b = 0, 1
    for _ in range(2, N+1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    N = int(input())
    print(main(N))