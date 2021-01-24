move = [(0, 1), (1, 0)]


def put(y, x, val):
    for i in range(2):
        known[hint[y][x][i]] += (1 << val)
    value[y][x] = val


def remove(y, x, val):
    for j in range(2):
        known[hint[y][x][j]] -= (1 << val)
    value[y][x] = 0


def get_cand_hint(h):
    return candidates[length[h]][sums[h]][known[h]]


def get_cand_coord(y, x):
    return get_cand_hint(hint[y][x][0]) & get_cand_hint(hint[y][x][1])


def get_size(mask):
    num, compare = 0, 1
    for i in range(1, 10):
        compare = compare << 1
        if compare & mask:
            num += 1
    return num


def get_sum(mask):
    s, compare = 0, 1
    for i in range(1, 10):
        compare = compare << 1
        if compare & mask:
            s += i
    return s


def generate_candidates():
    for s in range(0, 1024, 2):
        ll = get_size(s)
        ss = get_sum(s)
        subset = s
        while True:
            candidates[ll][ss][subset] |= (s & ~subset)
            if subset == 0:
                break
            subset = (subset - 1) & s


def print_solution():
    for i in range(N):
        print(" ".join(map(str, value[i])))


def search():
    y, x, min_candidates = -1, -1, 1023
    for i in range(N):
        for j in range(N):
            if color[i][j] == 1 and value[i][j] == 0:
                candidate = get_cand_coord(i, j)
                if get_size(min_candidates) > get_size(candidate):
                    min_candidates = candidate
                    y, x = i, j
    if min_candidates == 0:
        return False
    if y == -1:
        print_solution()
        return True

    for val in range(1, 10):
        if min_candidates & (1 << val):
            put(y, x, val)
            if search():
                return True
            remove(y, x, val)
    return False


for _ in range(int(input())):
    candidates = [[[0] * 1024 for _ in range(46)] for _ in range(10)]
    generate_candidates()
    N = int(input())
    color = []
    value = [[0] * N for _ in range(N)]
    hint = [[[0] * 2 for _ in range(N)] for _ in range(N)]
    sums = [0] * (N * N)
    length = [0] * (N * N)
    known = [0] * (N * N)
    for _ in range(N):
        color.append(list(map(int, input().split())))
    hint_num = int(input())
    for j in range(hint_num):
        y, x, d, total = map(int, input().split())
        hint[y - 1][x - 1][d] = j
        sums[hint[y - 1][x - 1][d]] = total
        move_y, move_x = move[d]
        l = 0
        next_y, next_x = y - 1 + move_y, x - 1 + move_x
        while next_y < N and next_x < N:
            if not color[next_y][next_x]:
                break
            hint[next_y][next_x][d] = j
            l += 1
            next_y += move_y
            next_x += move_x
        length[hint[y - 1][x - 1][d]] = l
    search()
