import sys


def init(left, right, node):
    if left == right:
        segment_tree[node] = arr[left]
        return segment_tree[node]

    mid = (left + right) // 2
    segment_tree[node] = init(left, mid, node * 2) + init(mid + 1, right, node * 2 + 1)
    return segment_tree[node]


def query(left, right, node, node_left, node_right):
    if right < node_left or left > node_right:
        return 0
    if left <= node_left and node_right <= right:
        return segment_tree[node]

    mid = (node_left + node_right) // 2
    return query(left, right, node * 2, node_left, mid) + query(left, right, node * 2 + 1, mid + 1,
                                                                node_right)


def update(idx, val, node, node_left, node_right):
    if node_left > idx or node_right < idx:
        return segment_tree[node]
    if node_left == node_right:
        segment_tree[node] = val
        return segment_tree[node]

    mid = (node_left + node_right) // 2
    segment_tree[node] = update(idx, val, node * 2, node_left, mid) + update(idx, val, node * 2 + 1, mid + 1,
                                                                             node_right)
    return segment_tree[node]


N, M, Q = map(int, input().split())
arr = []
segment_tree = [0] * (N * 4)
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
init(0, N - 1, 1)
for _ in range(M + Q):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(b - 1, c, 1, 0, N - 1)
    else:
        print(query(b - 1, c - 1, 1, 0, N - 1))
