import sys


def init(left, right, node):
    if left == right:
        segment_tree[node] = arr[left]
        return segment_tree[node]

    mid = (left + right) // 2
    segment_tree[node] = (init(left, mid, node * 2) + init(mid + 1, right, node * 2 + 1))
    return segment_tree[node]


def update(idx, value, node, node_left, node_right):
    if idx < node_left or idx > node_right:
        return segment_tree[node]
    if node_left == node_right:
        segment_tree[node] = value
        return segment_tree[node]
    mid = (node_left + node_right) // 2
    segment_tree[node] = update(idx, value, node * 2, node_left, mid) + update(idx, value, node * 2 + 1, mid + 1,
                                                                               node_right)
    return segment_tree[node]


def query(left, right, node, node_left, node_right):
    if left > node_right or right < node_left:
        return 0
    elif left <= node_left and node_right <= right:
        return segment_tree[node]

    mid = (node_left + node_right) // 2
    return query(left, right, node * 2, node_left, mid) + query(left, right, node * 2 + 1, mid + 1, node_right)


N, Q = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
segment_tree = [0] * (4 * N)
init(0, N-1, 1)
for _ in range(Q):
    x, y, a, b = map(int, sys.stdin.readline().split())
    if x > y:
        x, y = y, x
    print(query(x-1, y-1, 1, 0, N-1))
    update(a-1, b, 1, 0, N-1)
