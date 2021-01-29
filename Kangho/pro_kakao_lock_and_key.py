from copy import deepcopy


def add_key(row, col, K, nb, key):
    for i in range(K):
        for j in range(K):
            nb[i + row][j + col] += key[i][j]


def deduct_key(row, col, K, nb, key):
    for i in range(K):
        for j in range(K):
            nb[i + row][j + col] -= key[i][j]


def check(K, L, board):
    for i in range(K - 1, K - 1 + L):
        for j in range(K - 1, K - 1 + L):
            if board[i][j] != 1:
                return False
    return True


def solution(key, lock):
    answer = False
    K, L = len(key), len(lock)
    new_board = [[0] * ((2 * K + L) - 1) for _ in range((2 * K + L) - 1)]
    NL = len(new_board)
    for i in range(L):
        for j in range(L):
            new_board[K - 1 + i][K - 1 + j] = lock[i][j]
    keys = [deepcopy(key)]
    for k in range(1, 4):
        a = [[0] * K for _ in range(K)]
        for i in range(K):
            for j in range(K):
                a[j][K - 1 - i] = keys[k - 1][i][j]
        keys.append(deepcopy(a))
    for rek in keys:
        for i in range(NL-K):
            for j in range(NL-K):
                add_key(i, j, K, new_board, rek)
                if check(K, L, new_board):
                    answer = True
                    break
                deduct_key(i, j, K, new_board, rek)
            if answer:
                break
    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
