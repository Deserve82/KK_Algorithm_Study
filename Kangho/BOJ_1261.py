import heapq as hq

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def dijkstra():
    global mv
    q = [[0, 0, 0]]
    while q:
        cost, row, col = hq.heappop(q)
        if row == R - 1 and col == C - 1:
            print(cost)
            break
        for i in range(4):
            mr = row + directions[i][0]
            mc = col + directions[i][1]
            if 0 <= mr < R and 0 <= mc < C:
                if not check[mr][mc]:
                    check[mr][mc] = True
                    hq.heappush(q, [cost + board[mr][mc], mr, mc])


C, R = map(int, input().split())
check = [[False] * C for _ in range(R)]
check[0][0] = True
board = []
for _ in range(R):
    board.append(list(map(int, list(input()))))
dijkstra()
