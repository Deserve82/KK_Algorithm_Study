import sys


def update(idx, value, node, node_left, node_right):
    if idx < node_left or idx > node_right:
        return segment_tree[node]
    if node_left == node_right:
        segment_tree[node] += value
        return segment_tree[node]
    mid = (node_left + node_right) // 2
    segment_tree[node] = update(idx, value, node * 2, node_left, mid) + update(idx, value, node * 2 + 1, mid+1, node_right)
    return segment_tree[node]


def query(left, right, node, node_left, node_right):
    if left > node_right or right < node_left:
        return 0
    elif left <= node_left and node_right <= right:
        return segment_tree[node]

    mid = (node_left + node_right) // 2
    return query(left, right, node * 2, node_left, mid) + query(left, right, node * 2 + 1, mid+1, node_right)


N, Q = map(int, sys.stdin.readline().split())
arr = [0] * N
segment_tree = [0] * (4 * N)
for _ in range(Q):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(b-1, c, 1, 0, N-1)
    else:
        print(query(b-1, c-1, 1, 0, N-1))
