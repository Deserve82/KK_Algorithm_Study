def solution(n):
    answer = [[0] * num for num in range(1, n+1)]
    state = 0
    row, col = 0, 0
    idx = 0
    for i in range(n, 0, -1):
        for j in range(i):
            idx += 1
            if state == 0:
                answer[row][col] = idx
                row += 1
            elif state == 1:
                answer[row][col] = idx
                col += 1
            else:
                answer[row][col] = idx
                row -= 1
                col -= 1
        if state == 0:
            state = 1
            col += 1
            row -= 1
        elif state == 1:
            state = 2
            col -= 2
            row -= 1
        else:
            state = 0
            row += 2
            col += 1
    ans = []
    for a in answer:
        ans.extend(a)
    return ans
