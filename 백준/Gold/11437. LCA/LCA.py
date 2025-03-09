# LCA - 그래프, 트리, 최소 공통 조상 문제
import sys
from collections import deque
'''
2 <= N <= 50000개의 정점 트리
각 정점은 1 ~ N 번까지 번호 매겨짐 / 루트가 1번
두 노드의 쌍 1 <= M <= 10000의 가장 가까운 공통 조상 번호 출력
'''

# 트리를 순회하며 각 노드의 부모들을 리스트에 저장
def bfs(v):
    # visited = [False] * (N + 1)
    queue = deque([v])
    depth[v] = 1
    
    while queue:
        node = queue.popleft()
        for w in tree[node]:
            if depth[w] == 0:
                # visited[w] = True
                depth[w] = depth[node] + 1
                parent[w] = node
                queue.append(w)

def find_anc(v1, v2):
    # 개념적으로는 본인을 조상 노드에 포함하지 않지만 LCA 문제 케이스에서는 본인을 포함
    
    # 두 정점 깊이 비교/ v1 이 더 깊도록 설정
    if depth[v1] < depth[v2]:
        v1, v2 = v2, v1

    while depth[v1] > depth[v2]:
        v1 = parent[v1]

    while v1 != v2:
        v1 = parent[v1]
        v2 = parent[v2]

    return v1
    # anc = []
    # anc.append(v)
    # while parent[v] != 0:
    #     anc.append(parent[v])
    #     v = parent[v]

    # return anc

# def get_result(anc1, anc2):
#     anc1 = set(anc1)
#     for i in anc2:
#         if i in anc1:
#             return i

N = int(sys.stdin.readline())

tree = [[] for _ in range(N+1)]
# 모든 노드의 부모는 하나만 존재
parent = [0] * (N + 1)
depth = [0] * (N + 1)

# 주어지는 정보 중 누가 부모 노드이고 자식 노드인지 알 수 없음 -> 양방향 입력
for _ in range(N-1):
    v1, v2 = map(int, sys.stdin.readline().split())
    tree[v1].append(v2)
    tree[v2].append(v1)

# 주어지는 두 정점 중 어느 것이 부모인지 알 수 없음 -> bfs
bfs(1)

M = int(sys.stdin.readline())
for _ in range(M):
    v3, v4 = map(int, sys.stdin.readline().split())

    print(find_anc(v3, v4))