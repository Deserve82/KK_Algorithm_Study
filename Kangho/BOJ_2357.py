import sys


def init_min(left, right, node):
    if left == right:
        min_range[node] = arr[left]
        return min_range[node]
    mid = (left+right) // 2
    min_range[node] = min(init_min(left, mid, node * 2), init_min(mid+1, right, node * 2 + 1))
    return min_range[node]


def init_max(left, right, node):
    if left == right:
        max_range[node] = arr[left]
        return max_range[node]

    mid = (left + right) // 2
    max_range[node] = max(init_max(left, mid, node * 2), init_max(mid+1, right, node * 2 + 1))
    return max_range[node]


def min_query(left, right, node, node_left, node_right):
    if left > node_right or right < node_left:
        return 2000000000
    if left <= node_left and node_right <= right:
        return min_range[node]

    mid = (node_left + node_right) // 2
    return min(min_query(left, right, node * 2, node_left, mid), min_query(left, right, node * 2 + 1, mid + 1, node_right))


def max_query(left, right, node, node_left, node_right):
    if left > node_right or right < node_left:
        return 0
    if left <= node_left and node_right <= right:
        return max_range[node]

    mid = (node_left + node_right) // 2
    return max(max_query(left, right, node * 2, node_left, mid), max_query(left, right, node * 2 + 1, mid + 1, node_right))


N, Q = map(int, input().split())
arr = []
min_range = [0] * (N * 4)
max_range = [0] * (N * 4)
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
init_min(0, N-1, 1)
init_max(0, N-1, 1)
for _ in range(Q):
    a, b = map(int, sys.stdin.readline().split())
    print(min_query(a-1, b-1, 1, 0, N-1), max_query(a-1, b-1, 1, 0, N-1))
