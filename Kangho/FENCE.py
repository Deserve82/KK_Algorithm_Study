import sys
sys.setrecursionlimit(1000000)
count = 0

def rec(pivot, pivot_index, index):
    global m, count
    count += 1
    if index >= m or pivot_index >= m:
        return 0
    if board_len[index] < pivot:
        if pivot_index == index:
            rec(board_len[index+1], index + 1, index + 1)
    else:
        index_value[pivot_index] += pivot
        rec(pivot, pivot_index, index + 1)
        if pivot_index == index:
            rec(board_len[index+1], index + 1, index + 1)


n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    index_value = [0] * (m + 1)
    board_len = list(map(int, sys.stdin.readline().split()))
    board_len.append(0)
    rec(board_len[0], 0, 0)
    answer = max(index_value)
    board_len.reverse()
    index_value = [0] * (m + 1)
    rec(board_len[0], 0, 0)
    is_answer = max(index_value)
    if is_answer > answer:
        answer = is_answer
    print(answer, count)
