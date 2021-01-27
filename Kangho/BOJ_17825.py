def check(row, col):
    if col >= len(board[row]):
        return False
    if [row, col] in mal:
        return False
    elif board[row][col] == 10:
        if [0, 5] in mal or [1, 0] in mal:
            return False
    elif board[row][col] == 20:
        if [0, 10] in mal or [2, 0] in mal:
            return False
    elif board[row][col] == 25:
        if [4, 0] in mal or [1, 4] in mal or [2, 3] in mal or [3, 4] in mal:
            return False
    elif board[row][col] == 30 and row == 0:
        if [0, 15] in mal or [3, 0] in mal:
            return False
    elif board[row][col] == 40:
        if [0, 20] in mal or [4, 3] in mal:
            return False
    return True


def move_mal(dice_idx, mal_idx):
    global sums, answer
    if dice_idx == 10:
        answer = max(answer, sums)
        return
    if mal_idx >= 4 or mal_idx < 0:
        return

    ori_row, ori_col = mal[mal_idx]
    if ori_row == 0 and ori_col == 5:
        row, col = 1, 0
    elif ori_row == 0 and ori_col == 10:
        row, col = 2, 0
    elif ori_row == 0 and ori_col == 15:
        row, col = 3, 0
    elif ori_row == 0 and ori_col == 20:
        row, col = 4, 3
    elif (ori_row == 1 and ori_col == 4) or (ori_row == 2 and ori_col == 3) or (ori_row == 3 and ori_col == 4):
        row, col = 4, 0
    else:
        row, col = ori_row, ori_col
    if row == -1 and col == -1:
        return
    moved_col = col + dice[dice_idx]
    if (row == 1 or row == 3) and moved_col >= 4:
        row, moved_col = 4, moved_col - 4
    elif row == 2 and moved_col >= 3:
        row, moved_col = 4, moved_col - 3
    if moved_col >= len(board[row]):
        mal[mal_idx] = [-1, -1]
        move_mal(dice_idx+1, mal_idx + 1)
        move_mal(dice_idx+1, mal_idx - 1)
        mal[mal_idx] = [ori_row, ori_col]
    else:
        if check(row, moved_col):
            mal[mal_idx] = [row, moved_col]
            sums += board[row][moved_col]
            move_mal(dice_idx+1, mal_idx)
            move_mal(dice_idx+1, mal_idx+1)
            move_mal(dice_idx+1, mal_idx-1)
            move_mal(dice_idx+1, mal_idx-2)
            move_mal(dice_idx+1, mal_idx+2)
            mal[mal_idx] = [ori_row, ori_col]
            sums -= board[row][moved_col]
        else:
            return
    return


sums = 0
answer = 0
dice = list(map(int, input().split()))
board = [
    [i for i in range(0, 42, 2)],
    [10, 13, 16, 19, 25],
    [20, 22, 24, 25],
    [30, 28, 27, 26, 25],
    [25, 30, 35, 40]
]
mal = [[0, 0] for _ in range(4)]
move_mal(0, 0)
print(answer)
