scale = list(map(int, input().split()))

ascending = list(i for i in range(1, 9))
descending = list(i for i in range(8, 0, -1))

if scale == ascending:
    print("ascending")
elif scale == descending:
    print("descending")
else:
    print("mixed")