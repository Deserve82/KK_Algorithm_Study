INF = float('inf')


def TSP(last, check):
    if check == (1 << N) - 1:
        if board[last][start] != 0:
            return board[last][start]
        else:
            return INF

    if cache[last][check] != -1:
        return cache[last][check]

    ret = INF
    for i in range(N):
        if board[last][i] != 0 and (check & (1 << i)) == 0:
            ret = min(ret, TSP(i, check | (1 << i)) + board[last][i])
    cache[last][check] = ret
    return ret


board = []
N = int(input())
for _ in range(N):
    board.append(list(map(int, input().split())))
cache = [[-1] * (1 << N + 1) for _ in range(16)]
start = 0
ans = TSP(0, (1 << 0))
print(ans)
