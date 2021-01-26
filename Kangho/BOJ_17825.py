def move_mal(dice_idx, mal_idx):
    global sums, answer
    if dice_idx == 10:
        answer = max(answer, sums)
        return
    if mal_idx >= 4 or mal_idx < 0:
        return

    row, col = mal[mal_idx]
    if row == 0 and col == 5:
        row, col = 1, 0
    elif row == 0 and col == 10:
        row, col = 2, 0
    elif row == 0 and col == 15:
        row, col = 3, 0
    elif row == -1 and col == -1:
        return
    for i in range(dice_idx, 10):
        moved_col = col + dice[dice_idx]
        if moved_col >= len(board[row]):
            mal[mal_idx] = [-1, -1]
            move_mal(i+1, mal_idx + 1)
            move_mal(i+1, mal_idx - 1)
            mal[mal_idx] = [row, col]
        elif [row, moved_col] in mal or \
                (board[row][moved_col] == 25 and ([1, 4] in mal) or (([2, 3] in mal) or ([3, 4] in mal))) or \
                (((row != 0) and board[row][moved_col] == 30) and (
                        ([1, 5] in mal) or ([2, 4] in mal) or ([3, 5] in mal))) or \
                (board[row][moved_col] == 35 and (([1, 6] in mal) or ([2, 5] in mal) or ([3, 6] in mal))) or \
                (board[row][moved_col] == 40 and (([0, 20] in mal) or ([1, 7] in mal) or ([2, 6] in mal) or ([3, 7] in mal))):
            return
        else:
            mal[mal_idx] = [row, moved_col]
            sums += board[row][moved_col]
            move_mal(i+1, mal_idx-1)
            move_mal(i+1, mal_idx)
            move_mal(i+1, mal_idx+1)
            mal[mal_idx] = [row, col]
            sums -= board[row][moved_col]
    return


sums = 0
answer = 0
dice = list(map(int, input().split()))
board = [
    [i for i in range(0, 42, 2)],
    [10, 13, 16, 19, 25, 30, 35, 40],
    [20, 22, 24, 25, 30, 35, 40],
    [30, 28, 27, 26, 25, 30, 35, 40]
]
mal = [[0, 0] for _ in range(4)]
move_mal(0, 0)
print(answer)
