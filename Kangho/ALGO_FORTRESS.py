class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.depth = 0


def sq(num):
    return num * num


def get_max_root(root):
    ret = []
    if len(root.children) == 1:
        return root.depth
    elif not root.children:
        return 0

    for c in root.children:
        ret.append(c.depth)
    ret.sort()
    return ret[-1] + ret[-2] + 2


for _ in range(int(input())):
    N = int(input())
    board = []
    for _ in range(N):
        x, y, r = map(int, input().split())
        board.append(Node((x, y, r)))
    board.sort(key=lambda x: x.data[2])
    for i in range(N):
        for j in range(i + 1, N):
            if sq(board[j].data[0] - board[i].data[0]) + sq(board[j].data[1] - board[i].data[1]) \
                    < sq(board[j].data[2] - board[i].data[2]):
                board[j].depth = max(board[j].depth, board[i].depth + 1)
                board[j].children.append(board[i])
                break
    print(get_max_root(board[-1]))
