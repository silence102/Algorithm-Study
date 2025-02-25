import sys

N = int(sys.stdin.readline().strip())

set_words = set()
for _ in range(N):
    set_words.add((sys.stdin.readline().strip()))
    
words = list(set_words)
n = len(words)

# 정렬 함수(sort(), sorted())는 튜플의 첫 번째 요소를 우선 정렬
# 만약 첫 번째 요소가 같다면 두 번째 요소로 정렬하는 방식
words.sort(key = lambda x: (len(x), x) )

sys.stdout.write("\n".join(words))