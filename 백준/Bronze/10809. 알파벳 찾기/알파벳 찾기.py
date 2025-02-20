S = input()

a_list = [chr(i) for i in range(ord('a'), ord('z')+1)]

for i in a_list:
    print(S.find(i), end=" ")