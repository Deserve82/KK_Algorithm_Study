directions = [[0, 1],[1, 0],[-1, 0],[0, -1]]
sen = ""
R, C = map(int, input().split())
check = [[False]*C for _ in range(R)]
mv = 0


def dfs(row, col):
    global sen, mv
    mv = max(len(sen), mv)
    if mv >= 26:
        print(mv)
        exit(0)

    for i in range(4):
        mr = row + directions[i][0]
        mc = col + directions[i][1]
        if 0 <= mr < R and 0 <= mc < C and board[mr][mc] not in sen and not check[mr][mc]:
            sen += board[mr][mc]
            check[mr][mc] = True
            dfs(mr, mc)
            sen = sen[:-1]
            check[mr][mc] = False


board = []
for _ in range(R):
    board.append(list(input()))
sen = board[0][0]
check[0][0] = True
dfs(0, 0)
print(mv)
