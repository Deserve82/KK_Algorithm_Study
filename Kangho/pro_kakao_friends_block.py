def solution(m, n, board):
    answer = 0
    ls_board = []
    for sen in board:
        ls_sen = list(sen)
        ls_board.append(ls_sen)

    while True:
        explode = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if ls_board[i][j] != "#" and ls_board[i][j] == ls_board[i + 1][j] == ls_board[i][j + 1] == \
                        ls_board[i + 1][j + 1]:
                    explode.add((i, j))
                    explode.add((i + 1, j))
                    explode.add((i, j + 1))
                    explode.add((i + 1, j + 1))

        answer += len(explode)

        pop_number = [0] * n
        start_number = [0] * n
        for e in explode:
            pop_number[e[1]] += 1
            if e[0] > start_number[e[1]]:
                start_number[e[1]] = e[0]

        for i in range(n):
            for j in range(start_number[i], -1, -1):
                if j - pop_number[i] < 0:
                    ls_board[j][i] = "#"
                else:
                    ls_board[j][i] = ls_board[j - pop_number[i]][i]

        if len(explode) == 0:
            break

        for z in ls_board:
            print(z)
        print("----------------------")

    return answer


print(solution(4, 4, ["AAAC", "AAAA", "AAAA", "AAAA"]))
