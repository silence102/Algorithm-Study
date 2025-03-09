# 전위 순회, 중위 순회, 후위 순회 출력하는 프로그램 작성
def pre_order(v, pre):
    pre += v
    if tree[v][0] != '.':
        pre = pre_order(tree[v][0], pre)
    if tree[v][1] != '.':
        pre = pre_order(tree[v][1], pre)

    return pre

def in_order(v, in_o):
    if tree[v][0] != '.':
        in_o = in_order(tree[v][0], in_o)
    in_o += v
    if tree[v][1] != '.':
        in_o = in_order(tree[v][1], in_o)

    return in_o

def post_order(v, post):
    if tree[v][0] != '.':
        post = post_order(tree[v][0], post)
    if tree[v][1] != '.':
        post = post_order(tree[v][1], post)
    post += v

    return post

# N개의 이진 트리 노드
N = int(input())

tree = {}
for _ in range(N):
    # V: 부모 노드, L: 왼쪽 자식, R: 오른쪽 자식
    V, L, R = input().split()
    tree[V] = [L, R]

print(pre_order("A", ""))
print(in_order("A", ""))
print(post_order("A", ""))