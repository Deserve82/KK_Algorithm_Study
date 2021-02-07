import sys
def init(left, right, node):
    if left == right:
        segment_tree[node] = movie_loc[left]
        return segment_tree[node]

    mid = (left + right) // 2
    segment_tree[node] = init(left, mid, node * 2) + init(mid + 1, right, node * 2 + 1)
    return segment_tree[node]


def query(left, right, node, node_left, node_right):
    if left > node_right or right < node_left:
        return 0
    if left <= node_left and node_right <= right:
        return segment_tree[node]
    mid = (node_left + node_right) // 2
    return query(left, right, node * 2, node_left, mid) + query(left, right, node * 2 + 1, mid + 1, node_right)


def update(idx, value, node, node_left, node_right):
    if idx < node_left or idx > node_right:
        return segment_tree[node]
    if node_left == node_right:
        segment_tree[node] = value
        return segment_tree[node]
    mid = (node_left + node_right) // 2
    segment_tree[node] = update(idx, value, node * 2, node_left, mid) + update(idx, value, node * 2 + 1, mid+1, node_right)
    return segment_tree[node]


for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    movies = list(map(int, sys.stdin.readline().split()))
    movie_idx = {}
    for i in range(1, N + 1):
        movie_idx[i] = N-i
    movie_loc = [1] * N
    movie_loc.extend([0] * M)
    loc_idx = N
    segment_tree = [0] * ((N + M) * 4)
    init(0, N + M - 1, 1)
    answer = []
    for movie in movies:
        answer.append(str(query(movie_idx[movie]+1, N+M-1, 1, 0, N+M-1)))
        update(movie_idx[movie], 0, 1, 0, N+M-1)
        update(loc_idx, 1, 1, 0, N+M-1)
        movie_idx[movie] = loc_idx
        loc_idx += 1
    print(" ".join(answer))
