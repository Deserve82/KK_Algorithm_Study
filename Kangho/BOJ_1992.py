answer = ''


def quad(start_row, start_col, size):
    global answer
    pivot = board[start_row][start_col]
    end_row, end_col = start_row + size, start_col + size
    is_all_same = True
    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            if board[i][j] != pivot:
                is_all_same = False
                break
        if not is_all_same:
            break
    if is_all_same:
        answer += str(pivot)
    else:
        answer += '('
        s = int(size / 2)
        quad(start_row, start_col, s)
        quad(start_row, start_col + s, s)
        quad(start_row + s, start_col, s)
        quad(start_row + s, start_col + s, s)
        answer += ')'


n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, list(input()))))
quad(0, 0, n)
print(answer)
