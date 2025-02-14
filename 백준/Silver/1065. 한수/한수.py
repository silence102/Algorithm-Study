# 한수: 각 자리 숫자가 등차수열을 이루는 수
import sys

def main():
    N = int(sys.stdin.readline())
    count = 0
    for i in range(1, N+1):
        if i < 100:
            count += 1
        else:
            num_list = list(map(int, str(i)))
            if num_list[1] - num_list[0] == num_list[2] - num_list[1]:
                count += 1
    print(count)

if __name__ == "__main__":
    main()